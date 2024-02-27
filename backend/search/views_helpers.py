from search import models
import ratemyprofessor

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

def fetch_all_professors() -> dict:
    """
    Query all classes from the database, and store all professor from each class
    """
    db_query = models.CachedCourses.objects.all()

    for class_object in db_query:
        each_class = class_object.data
        print("CourseID: " + each_class["courseId"])
        print("Title: " + each_class["title"]) 

        if each_class["classSections"] and each_class["classSections"][0]["instructors"]:
                raw_profname = each_class["classSections"][0]["instructors"][0]["instructor"]
        else:
            print("Skipped: " + "no instructor for " + each_class["courseId"])
            continue
        
        # get rid of the inital of the middle name, otherwise ratemyprofessor api could fail
        if raw_profname.count(" ") >= 1:
            profname = raw_profname.split(" ")[0] + " " + raw_profname.split(" ")[1]
        else:
            profname = raw_profname

        # if we already have professors with this name, we need to link the class to them
        existing_prof = models.Professor.objects.filter(name=profname)
        if existing_prof.exists():
            for each_prof in existing_prof:
                class_object.instructor = each_prof
                class_object.save()
            print("Skipped: " + f"{profname} is already stored" )
            continue
        
        # otherwise, we need to create a new professor
        fetch_professor_for_classes(class_object, profname)

def fetch_professor_for_classes(each_class: models.CachedCourses, prof_name: str) -> None:
    SCHOOL = ratemyprofessor.get_school_by_name("University of California Santa Barbara")
    prof_list = ratemyprofessor.get_professors_by_school_and_name(SCHOOL, prof_name)

    if not prof_list:
        print(f"Skipped: {prof_name} not found in ratemyprofessor")
        with open('missing_prof.txt', 'a') as f:
            f.write(prof_name + '\n')
        return
    if prof_list[0].school.name != "University of California Santa Barbara":
        print(f"Skipped: there is no professor with name {prof_name} found in UCSB")
        with open('missing_prof.txt', 'a') as f:
            f.write(prof_name + '\n')
        return

    
    for prof_object in prof_list:
        if (prof_object.would_take_again is not None) and (prof_object.would_take_again != -1):
            would_take_again = str(round(prof_object.would_take_again))
        else:
            would_take_again = "N/A"
        new_prof = models.Professor(fullname = prof_object.name,
                                     name = prof_name,
                                     department = prof_object.department,
                                     rating = prof_object.rating,
                                     difficulty = prof_object.difficulty,
                                     num_ratings = prof_object.num_ratings,
                                     would_take_again = would_take_again)
        new_prof.save()
        each_class.instructor = new_prof
        each_class.save()
    print(f"Stored: {prof_name} for {each_class.courseID}")
            
            
        
        
                


        

        


    