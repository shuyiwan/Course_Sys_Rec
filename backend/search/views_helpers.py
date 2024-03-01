from search import models
from django.db.models import QuerySet
from search.keyword_gen import keyword_generation
import re # the package for regular expression

def search_from_backend(subcode: str, quarter: str, keywords: list, selected: list) -> None:
    # Get class data by querying from the backend DB
    query = query_from_DB(quarter, subcode)

    # Prepare the regex pattern for each keyword
    regex_patterns = []
    for keyword in keywords:
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
    db_query = list(models.CachedCourses.objects.filter(quarter=quarter, year=year, department=subjectCode).values())
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