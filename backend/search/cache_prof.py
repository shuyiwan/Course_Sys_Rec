"""
A collection of functions to cache the professors into the database
"""
from django.db import models
from search import models
from search import rmf_api
from django.db.models import QuerySet
import ratemyprofessor
import time
import json

"""
Information about the API can be found here: 
<https://pypi.org/project/RateMyProfessorAPI/>
"""

def read_missprof_file() -> set:
    """
    Read the missing professor list from the text file, and change it into a set
    """
    with open("search/missing_prof.txt", "r") as f:
        result = f.read().splitlines()
    return set(result)

def write_missprof_file(new_name: str) -> None:
    """
    Append new professor name to the missing_prof.txt 
    """
    print("Writing to missing_prof.txt")
    with open("search/missing_prof.txt", "a") as f:
        f.write(new_name + "\n")
    return

def process_raw_profname(raw_profname: str) -> str:
    """
    get rid of the inital of the middle name if it exists
    """
    if raw_profname.count(" ") >= 1:
        return raw_profname.split(" ")[0] + " " + raw_profname.split(" ")[1]
    return raw_profname

def fetch_all_professors() -> None:
    """
    Query all classes from the database, and store all professor from each class
    """

    # get all classes that don't have not linked to its professor object
    db_query = models.CachedCourses.objects.filter(instructor=None)
    num_classes = db_query.count()
    if num_classes == models.CachedCourses.objects.all().count():
        print("Starting to populate the professor table from scratch...")
        # create a dummy professor object in the database, so that if a class has no 
        # instructor & cannot find a instructor, it will be linked to this object
        # we need to distinguish them from the classes that are not processed yet
        dummy_prof = models.Professor(fullname = "no professor")
        dummy_prof.save()    

    elif num_classes != 0:
        print("Continuing to populate the professor table...")
        dummy_prof = models.Professor.objects.filter(fullname = "no professor")
        if dummy_prof.exists() and dummy_prof.count() == 1:
            dummy_prof = models.Professor.objects.get(fullname = "no professor")
        else:
            print("Error: There is an error when trying to find dummy professor. " +
                   "There are bugs in the code.")
            return
        
    else:
        print("Finished: Already populated the professor table.")
        return
    
    start_time = time.time()
    # get the set of professors that are not on Ratemyprofessor, so the api
    # don't need to be queried for these names
    miss_set = read_missprof_file()

    for class_object in db_query:
        fetch_professor_from_class(class_object, dummy_prof, miss_set)

    print("Success! Finished querying")
    finish_time = time.time()
    total_time = (finish_time - start_time) / 60
    print(f"Total time for this run: {total_time} minutes")

def fetch_professor_from_class(class_object: models.CachedCourses,
                               dummy_prof: models.Professor,
                               miss_set: set) -> None:
    """
    Process each class in the databse to find the professor
    """
    each_class = class_object.data
    print("CourseID: " + class_object.courseID + ", " + str(class_object.year) + str(class_object.quarter))

    if each_class["classSections"] and each_class["classSections"][0]["instructors"]:
            raw_profname = each_class["classSections"][0]["instructors"][0]["instructor"]
    else:
        print("Skipped: " + "no instructor for " + each_class["courseId"])
        # set the foreign key field to be 1 to distinguish it from the classes that
        # haven't been went over
        class_object.instructor = dummy_prof
        class_object.save()
        return

    print("Instructor: " + raw_profname)
    # get rid of the inital of the middle name, otherwise ratemyprofessor api could fail
    profname = process_raw_profname(raw_profname)
    if profname in miss_set:
        print("Skipped: " + raw_profname + 
                " is in missing_prof.txt (cannot be found on ratemyprofessor at UCSB)")
        class_object.instructor = dummy_prof
        class_object.save()
        return

    # if we already have professors with this name, we need to link the class to them
    existing_prof = models.Professor.objects.filter(name=profname)
    if existing_prof.exists():
        link_prof_to_class(existing_prof, class_object)

        print("Skipped: " + 
                f"{raw_profname} is already stored, and {class_object.courseID} is linked to {raw_profname}" )
        return
    
    # otherwise, we need to create new professors
    query_ratemyprofessor_api(class_object, raw_profname, profname, dummy_prof)
    # sleep for 1 seconds to avoid overloading the api
    time.sleep(1)

def query_ratemyprofessor_api(each_class: models.CachedCourses, 
                                raw_prof_name: str,
                                prof_name: str,
                                dummy_prof: models.Professor) -> None:
    """
    Query the professor from ratemyprofessor api, and store the professor in the database
    """
    SCHOOL = ratemyprofessor.get_school_by_name("University of California Santa Barbara")
    prof_list = ratemyprofessor.get_professors_by_school_and_name(SCHOOL, prof_name)

    # handle the case that it is not on Ratemyprofessor but also not in missing_prof.txt
    if not prof_list:
        print(f"Skipped: {raw_prof_name} not found in Ratemyprofessor for any school")
        each_class.instructor = dummy_prof
        each_class.save()
        write_missprof_file(prof_name)
        return
    
    if prof_list[0].school.name != "University of California Santa Barbara":
        print(f"Skipped: there is no professor with name {raw_prof_name} found in UCSB")
        each_class.instructor = dummy_prof
        each_class.save()
        write_missprof_file(prof_name)
        return
 
    for prof_object in prof_list:
        create_prof_object(prof_object, each_class, prof_name)

    print(f"Stored: {raw_prof_name} for {each_class.courseID}")

def link_prof_to_class(existing_profs: QuerySet, 
                       class_object: models.CachedCourses) -> None:
    """
    link the class to the existing professors objects in the database without creating new ones
    """
    for each_prof in existing_profs:
        class_object.instructor = each_prof
        class_object.save()

def create_prof_object(prof: ratemyprofessor.Professor, 
                       each_class: models.CachedCourses,
                       prof_name: str) -> None:
    """
    Create a new professor object, and link it to this class
    """
    if (prof.would_take_again is not None) and (prof.would_take_again != -1):
        would_take_again = str(round(prof.would_take_again)) + "%"
    else:
        would_take_again = "N/A"
    new_prof = models.Professor(fullname = prof.name, # the full name in ratemyprofessor
                                 name = prof_name,     # the processed name with no initial of middle name
                                 department = prof.department,
                                 rating = prof.rating,
                                 difficulty = prof.difficulty,
                                 num_ratings = prof.num_ratings,
                                 would_take_again = would_take_again)
    new_prof.save()
    each_class.instructor = new_prof
    each_class.save()

def fetch_all_tags() -> None:
    """
    Use scraper in search/rmf_api.py to get the professor tags and add them to the database
    """
    start_time = time.time()
    db_query = models.Professor.objects.filter(tags__isnull=True)

    if db_query.count() == models.Professor.objects.all().count():
        print("Starting to populate the tags column from scratch...")
    else:
        print("Continuing to populate the tags column...")

    # go thorough each professor and query api to get their tags
    for each_prof in db_query:
        fullname = each_prof.fullname
        print("Professor: " + fullname + ", " + "Department: " + each_prof.department)
        tags = get_tags(fullname)
        if not tags:
            tags = ["could not find tags for this professor"]
        elif tags[0] == "could not find rmf id":
            tags = ["no tags: failed to find rmf id for this professor"]

        # store the tags
        tags_json = json.dumps(tags)
        each_prof.tags = tags_json
        each_prof.save()
        if tags[0] == "could not find tags for this professor":
            print("Skipped: "  + "could not find tags for " + fullname)
        elif tags[0] == "no tags: failed to find rmf id for this professor":
            print("Skipped: "  + "failed to find rmf id for " + fullname)
        else:
            print("Stored: " + fullname)

    print("Success! Finished querying")
    finish_time = time.time()
    total_time = (finish_time - start_time) / 60
    print(f"Total time for this run: {total_time} minutes")

def get_tags(name: str) -> list:
    """
    Given a name, get the tags of a professor
    """
    list_id = rmf_api.query_rmfapi_for_rmfid(name)
    if list_id: # the first id corresponds to the best result that match this name 
        return rmf_api.query_rmfapi_for_hottest_tags(list_id[0]) # this may return an empty list if no tags found
    else:
        # normally this should not happen since every professor name in db have a record in rmf
        return ["could not find rmf id"]