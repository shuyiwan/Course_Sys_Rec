from search import models

from django.db.models import QuerySet

import re # the package for regular expression

def search_from_backend(subcode: str, quarter: str, keyword: str, selected: list) -> None:
    # get class data by querying from backend DB
    query = query_from_DB(quarter, subcode)

    # We use regular expression to match keywords in descriptions
    # \b is a word boundary char in regular expressions, adding these two 
    # characters will avoid partial matching. e.g. match "search" to "research"
    # \s match the whitespace character. 
    keyword = re.escape(keyword.lower())
    keyword = r'\b' + '\\s*'.join(keyword) + r'\b' # may be modified

    # compile the regular expression above to a re object
    # re,IGNORECASE is to make the matching process case-insensitive
    regex_keyword = re.compile(keyword, re.IGNORECASE)

    # filter the query
    filter_query(query, regex_keyword, selected)

def filter_query(query: QuerySet, regex_keyword: re.Pattern, selected: list) -> None:
    """ 
    Narrows down the search query from all the classes in a department
    to courses that fit the keyword
    """
    for i in query:
        # if the course descriptions contain the keyword, we will add this course to the
        # list.
        # We add the information of this course into the dict, and then add this
        # dict to "selected"
        if regex_keyword.search(i["data"]["description"]):
            each_class = dict()
            each_class["ID"] = len(selected) # this is the index of the course
            each_class = extract_from_data(orig_dict=each_class, cached_course=i)
            selected.append(each_class)

def query_from_DB(UCSB_quarter: str, subjectCode: str) -> dict:
    """
    Query all results from the database that fit the subject code and quarter
    """
    # UCSB_quarter follows YYYYQ format; Q is an integer [W = 1, S = 2, M = 3, F = 4]
    assert UCSB_quarter
    assert len(UCSB_quarter) == 5
    assert UCSB_quarter.isdigit()
    assert int(UCSB_quarter[-1]) >= 1 and int(UCSB_quarter[-1]) <= 4

    quarter = int(UCSB_quarter[-1])
    year = int(UCSB_quarter[:-1])
    db_query = models.CachedCourses.objects.filter(quarter=quarter, year=year, department=subjectCode).values()
    return db_query

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
    orig_dict["description"] = data["description"]
    if not data["classSections"]:
        orig_dict["instructor"] = "TBD"
    elif not data["classSections"][0]["instructors"]:
        orig_dict["instructor"] = "TBD"
    else:
        orig_dict["instructor"] = data["classSections"][0]["instructors"][0]["instructor"]

    return orig_dict