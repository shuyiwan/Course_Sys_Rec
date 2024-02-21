"""
Internal scraper used to query course information from the UCSB API
"""

from django.conf import settings
from search import models

import json
import requests
import time

"""
Information about the API can be found here: 
<https://developer.ucsb.edu/content/academic-curriculums#/>
"""
def query_UCSB_classes(quarter: str, subjectCode: str = "", pageNumber: int = 1, pageSize: int = 30) -> dict:
    # quarter is required to query the UCSB api
    # quarter follows YYYYQ format; Q is an integer [W = 1, S = 2, M = 3, F = 4]
    assert quarter
    assert len(quarter) == 5
    assert quarter.isdigit()
    assert int(quarter[-1]) >= 1 and int(quarter[-1]) <= 4

    # *** Query Parameters ***
    minUnits: int = 1
    maxUnits: int = 12
    includeClassSections: bool = True

    # all of the valid parameters found on the api should be input into the url
    url: str = (
        f"https://api.ucsb.edu/academics/curriculums/v3/classes/search?"
        f"quarter={quarter}"
        f"&minUnits={minUnits}"
        f"&maxUnits={maxUnits}"
        f"&pageNumber={pageNumber}"
        f"&pageSize={pageSize}"
        f"&includeClassSections={includeClassSections}"
        f"&subjectCode={subjectCode}"
    )

    # let the UCSB api know what this application is
    headers: dict = {
        "accept": "application/json",
        "ucsb-api-version": "3.0",
        "ucsb-api-key": settings.USCB_API_CONSUMER_KEY
    }

    # send our request and receive the payload
    response: requests.Response = requests.get(url, headers=headers)
    data: dict = response.json()
    return data

def query_from_DB(UCSB_quarter: str, subjectCode: str) -> dict:
    """
    Query from the database
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

def fetch_all_courses() -> None:
    """
    This function should only be run once during startup to get required courses 
    in your DB. This function will take a while to complete. Once run, you don't
    need to run this again unless you want to get more classes from different quarters.
    """

    # parameters, change if needed
    # make sure to be considerate of the UCSB API
    YEARS = ['2024']
    QUARTERS = ['1', '2']
    SUBJECT_CODES =  ["ANTH", "ART", "ARTHI", "ARTST", "AS AM", "ASTRO", "BIOE", "BIOL",
    "BMSE", "BL ST", "CH E", "CHEM", "CH ST", "CHIN", "CLASS", "COMM", "C LIT", "CMPSC",
    "CMPTG", "CNCSP", "DANCE", "DYNS", "EARTH", "EACS", "EEMB", "ECON", "ED", "ECE", "ENGR",
    "ENGL", "EDS", "ESM", "ENV S", "ESS", "ES", "FEMST", "FAMST", "FR", "GEN S", "GEOG",
    "GER", "GPS", "GLOBL", "GRAD", "GREEK", "HEB", "HIST", "INT", "ITAL", "JAPAN", "KOR",
    "LATIN", "LAIS", "LING", "LIT", "MARSC", "MARIN", "MATRL", "MATH", "ME", "MAT", "ME ST",
    "MES", "MS", "MCDB", "MUS", "MUS A", "PHIL", "PHYS", "POL S", "PORT", "PSY", "RG ST",
    "RENST", "RUSS", "SLAV", "SOC", "SPAN", "SHS", "PSTAT", "TMP", "THTR", "WRIT", "W&L",]

    for year in YEARS:
        for quarter in QUARTERS:
            for code in SUBJECT_CODES:
                fetch_department(year, quarter, code)
    print("Success! Finished querying")

def fetch_department(year: str, quarter: str, code: str) -> None:
    """
    If the department isn't already fetched, this function will 
    fetch all of the courses for a given department.
    """
    # config, change if needed
    MAX_PAGES = 5

    # convert the quarter to UCSB format
    UCSB_quarter = f"{year}{quarter}"
    queried_courses = 0
    total_courses = get_total_courses(UCSB_quarter, code)

    if already_stored_department(year, quarter, code, total_courses):
        print(f"Skipped Department: {UCSB_quarter} {code}")
        return
    print(f"Querying Department: {UCSB_quarter} {code} {total_courses}")

    # UCSB API stores its courses in multiple pages, meaning we need to loop through each page
    for page_number in range(1, MAX_PAGES):

        # fetch the page
        query = query_UCSB_classes(UCSB_quarter, code, page_number, pageSize=total_courses)

        # sleep for 2 seconds to avoid overloading the api
        time.sleep(2)

        # keep track of page statistics
        assert query["pageNumber"] == page_number
        queried_courses += query["pageSize"]

        store_courses(query, year, quarter, code)

        # check if we have reached the total number of courses
        if (queried_courses >= total_courses):
            break

def get_total_courses(UCSB_quarter: str, code: str) -> int:
    """
    Returns the total number of courses for a given quarter and subject code
    while keeping network load low
    """
    # sleep less because the network load is smaller
    time.sleep(0.5)
    query = query_UCSB_classes(UCSB_quarter, code, pageNumber=1, pageSize=1)
    return query["total"]

def store_courses(query: dict, year: str, quarter: str, code: str) -> None:
    """
    Stores the courses in the database
    """
    for i in query["classes"]:
        # if we have already stored this class, skip
        if models.CachedCourses.objects.filter(quarter=int(quarter), year=int(year), department=code, courseID=i["courseId"]).count() > 0:
            print(f"Skipping: {i['courseId']}")
            continue
        
        # otherwise store
        course = models.CachedCourses(
            courseID = i["courseId"],
            department = code,
            year = int(year),
            quarter = int(quarter),
            data = i
        )
        course.save()
        print(f"Stored: {i['courseId']}")

def already_stored_department(year: str, quarter: str, code: str, total_courses: int) -> bool:
    """
    Returns true if the entire department has already been stored
    """
    return models.CachedCourses.objects.filter(quarter=int(quarter), year=int(year), department=code).count() >= total_courses


if __name__ == "__main__":
    # Example way to query; this should return a list of courses and descriptions
    query = query_UCSB_classes("20241", "CMPSC")
    for i in query["classes"]:
        print(i["courseId"])
        print(i["description"])
    pass 