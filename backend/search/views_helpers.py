from search import models
from django.forms.models import model_to_dict


import re # the package for regular expression

def search_from_backend(subcode: str, quarter: str, keyword: str, selected: list) -> None:
    # get class data by querying from backend DB
    query = query_from_DB(quarter, subcode)

    # only get ["data"] from the dicts returned by query_from_DB
    query = [i["data"] for i in query]

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

def filter_query(query: dict, regex_keyword: re.Pattern, selected: list) -> None:
    """ 
    Narrows down the search query from all the classes in a department
    to courses that fit the keyword
    """
    for i in query:
        # if the course descriptions contain the keyword, we will add this course to the
        # list.
        # We add the information of this course into the dict, and then add this
        # dict to "selected"
        if regex_keyword.search(i["description"]):
            each_class = dict()
            each_class["ID"] = len(selected)
            each_class["courseID"] = i["courseId"]
            each_class["title"] = i["title"]

            # check if the "instructors" list is empty, if so then set "instructor" to "TBD"
            if not i["classSections"]:
                each_class["instructor"] = "TBD"
            else:
                if not i["classSections"][0]["instructors"]:
                    each_class["instructor"] = "TBD"
                else:
                    each_class["instructor"] = i["classSections"][0]["instructors"][0]["instructor"]
            each_class["description"] = i["description"]
            if each_class["instructor"] == "TBD":
                each_class["ratings from Ratemyprofessor"] = "TBD"
            else:
                each_class["ratings from Ratemyprofessor"] = retrieve_prof(each_class["instructor"])

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


def retrieve_prof(prof_name: str) -> list:
    """
    Query all professor from the database that match this name(the name returned by school api)
    """
    # remove the initial of middle name if it exists
    if prof_name.count(" ") >= 1:
        prof_name = prof_name.split(" ")[0] + " " + prof_name.split(" ")[1]
    result = []
    db_query = models.Professor.objects.filter(name=prof_name)
    for each_prof in db_query:
        result.append(model_to_dict(each_prof))
    return result



            
            
        
        
                


        

        


    