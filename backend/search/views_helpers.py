from search import models
from django.forms.models import model_to_dict
from django.db.models import QuerySet
from search.keyword_gen import keyword_generation
from search import rmf_api
import json
import re 

def search_from_backend(subcode: str, quarter: str, keywords: list, selected: list) -> None:
    # Get class data by querying from the backend DB
    query = query_from_DB(quarter, subcode)

    # Prepare the regex pattern for each keyword
    regex_patterns = []
    for keyword in keywords:
        # remove spaces in the keyword so that it accepts phrases like "computer science"
        keyword = keyword.replace(" ", "")
        escaped_keyword = re.escape(keyword.lower())
        pattern = r'\b' + '\\s*'.join(escaped_keyword) + r'\b'  # May be modified
        regex_patterns.append(re.compile(pattern, re.IGNORECASE))

    # Filter the query using the prepared regex patterns
    filter_query(query, regex_patterns, selected)


def filter_query(query: QuerySet, regex_patterns: list[re.Pattern], selected: list) -> None:
    """ 
    Narrows down the search query from all the classes in a department
    to courses that fit the keywords.
    """
    for course in query:
        # if the course descriptions contain the keyword, we will add this course to the
        # list.
        # We add the information of this course into the dict, and then add this
        # dict to "selected"
        if any(regex.search(course["data"]["description"]) for regex in regex_patterns):
            each_class = dict()
            each_class["ID"] = len(selected) # this is the index of the course
            each_class = extract_from_cached_course(orig_dict=each_class, cached_course=course)
            selected.append(each_class)

def query_from_DB(UCSB_quarter: str, subjectCode: str) -> list:
    """
    Query all results from the database that fit the subject code and quarter.
    """
    assert UCSB_quarter and len(UCSB_quarter) == 5 and UCSB_quarter.isdigit()
    assert 1 <= int(UCSB_quarter[-1]) <= 4

    quarter = int(UCSB_quarter[-1])
    year = int(UCSB_quarter[:-1])

    query = None
    if subjectCode:
        query = models.CachedCourses.objects.filter(quarter=quarter, year=year, department=subjectCode)
    else:
        query = models.CachedCourses.objects.filter(quarter=quarter, year=year)
    return list(query.values())

def retrieve_prof(prof_name: str) -> list:
    """
    Query all professor from the database that match this name(the name returned by school api)
    """
    # if the name is "TBD", we will return a dict of "TBD"
    if prof_name == "TBD":
        tbd_prof = dict()
        tbd_prof["id"] = "TBD"
        tbd_prof["fullname"] = "TBD"
        tbd_prof["name"] = "TBD"
        tbd_prof["department"] = "TBD"
        tbd_prof["rating"] = "TBD"
        tbd_prof["num_ratings"] = "TBD"
        tbd_prof["difficulty"] = "TBD"
        tbd_prof["would_take_again"] = "TBD"
        tbd_prof["tags"] = ["TBD"]
        return [tbd_prof]
    
    # retrieve the professor from the database when name is not "TBD"
    # remove the initial of middle name if it exists
    split_name = prof_name.split(" ")

    if prof_name.count(" ") >= 1:
        prof_name = split_name[0] + " " + split_name[1]

    # use regex pattern to match partial name returned by school api with 
    # the full name in the database
    if  len(split_name) == 1:
        name_pattern = re.compile(split_name[0], re.IGNORECASE)
    else:
        name_pattern = re.compile(split_name[1] + '\\w*' + '\\s*' + split_name[0] + '\\b', re.IGNORECASE)
    result = []
    db_query = models.Professor.objects.filter(name=prof_name)
    for each_prof in db_query:
        if not name_pattern.match(each_prof.fullname):
            continue
        # convert the tags from json to list
        tags_list = json.loads(each_prof.tags)
        prof_dict = model_to_dict(each_prof)
        prof_dict["tags"] = tags_list
        result.append(prof_dict)
    return result

def extract_from_cached_course(orig_dict: dict, cached_course: dict) -> dict:
    """
    Adds the information of this course's data into the original dictionary
    """
    # add non data info
    orig_dict["sql_id"] = cached_course["id"]
    orig_dict["courseID"] = cached_course["courseID"]

    # add all info located in data
    data = cached_course["data"]
    orig_dict["title"] = data["title"]
    orig_dict["subject_code"] = data["subjectArea"].replace(" ", "")
    orig_dict["description"] = data["description"]

    # get instructors
    if not data["classSections"]:
        orig_dict["instructor"] = "TBD"
    elif not data["classSections"][0]["instructors"]:
        orig_dict["instructor"] = "TBD"
    else:
        orig_dict["instructor"] = data["classSections"][0]["instructors"][0]["instructor"]
    
    # get time locations
    if not data["classSections"]:
        orig_dict["timeLocations"] = "TBD"
    else:
        orig_dict["timeLocations"] = data["classSections"][0]["timeLocations"]

    # add ratings to the class
    orig_dict["rmf"] = retrieve_prof(orig_dict["instructor"])
    if not orig_dict["rmf"]:
        orig_dict["rmf"] = "could not find this professor"

    return orig_dict

def get_tags(name: str) -> list:
    """
    Given a name, get the tags of a professor
    """
    list_id = rmf_api.query_rmfapi_for_rmfid(name)
    if list_id:
        # the first id corresponds to the best result that match this name 
        return rmf_api.query_rmfapi_for_hottest_tags(list_id[0]) 
    else:
        return []
    

def search_professor_from_backend(name: str, quarter: str, selected: list) -> None:
    """
    Search for all the professors that match to this name from the backend 
    and find there classes
    """
    # Prepare the regex pattern for searching name
    name_pattern = re.compile(name, re.IGNORECASE)

    db_query = models.Professor.objects.all()
    for prof_object in db_query:
        if not name_pattern.search(prof_object.fullname):
            continue
        # convert the tags from json to list
        prof_dict = dict()
        sql_id = prof_object.id
        tags_list = json.loads(prof_object.tags)
        prof_dict["ID"] = len(selected)
        prof_dict["sql_id"] = sql_id
        prof_dict["fullname"] = prof_object.fullname
        prof_dict["name"] = prof_object.name
        prof_dict["department"] = prof_object.department
        prof_dict["rating"] = prof_object.rating
        prof_dict["num_ratings"] = prof_object.num_ratings
        prof_dict["difficulty"] = prof_object.difficulty
        prof_dict["would_take_again"] = prof_object.would_take_again
        prof_dict["tags"] = tags_list
        classes = search_classes_for_prof(prof_object, quarter)
        if not classes:
            prof_dict["classes"] = [f"There is no classes for this profess in {quarter}."]
        else:
            prof_dict["classes"] = search_classes_for_prof(prof_object, quarter)
        
        selected.append(prof_dict)

def get_regex_for_professor_name(name: str) -> re.Pattern:
    """
    get the regex pattern for the returned name in the school api
    """
    split_name = name.split(" ")

    # remove the initial of the middle name is there is one
    if name.count(" ") >= 1:
        name = split_name[0] + " " + split_name[1]

    # use regex pattern to match partial name returned by school api with 
    # the full name in the database
    if  len(split_name) == 1:
        return re.compile(split_name[0], re.IGNORECASE)
    else:
        return re.compile(split_name[1] + '\\w*' + '\\s*' + split_name[0] + '\\b', re.IGNORECASE)

def search_classes_for_prof(prof_object: models.Professor, UCSB_quarter: str) -> list: 
    """
    Search classes for a professor object
    """
    # get all the classes from this quarter in every dept
    db_query = query_from_DB(UCSB_quarter, '')
    result = []

    for class_dict in db_query:
        data = class_dict["data"]
        if not (data["classSections"] and data["classSections"][0]["instructors"]):
            continue
        
        name_pattern = get_regex_for_professor_name(data["classSections"][0]["instructors"][0]["instructor"])
        if name_pattern.search(prof_object.fullname):
            each_class = dict()
            each_class["ID"] = len(result)
            each_class = extract_from_cached_course(orig_dict=each_class, cached_course=class_dict)
            result.append(each_class)
    return result

