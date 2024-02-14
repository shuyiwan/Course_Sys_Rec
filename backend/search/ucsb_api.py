"""
Internal scraper used to query course information from the UCSB API
"""

import requests
import os
from dotenv import load_dotenv
from search import models
import time

# .env file containing UCSB api keys should be located in the root folder of backend
load_dotenv() # uses absolute path
uscb_api_consumer_key = os.getenv('uscb_api_consumer_key') # ask Kevin for the key

"""
Information about the API can be found here: 
<https://developer.ucsb.edu/content/academic-curriculums#/>
"""
def query_UCSB_classes(quarter: str, subjectCode: str = "", pageNumber: int = 1) -> dict:
    # quarter is required to query the UCSB api
    # quarter follows YYYYQ format; Q is an integer [W = 1, S = 2, M = 3, F = 4]
    assert quarter
    assert len(quarter) == 5
    assert quarter.isdigit()
    assert int(quarter[-1]) >= 1 and int(quarter[-1]) <= 4

    # *** Query Parameters ***
    minUnits: int = 1
    maxUnits: int = 12
    pageSize: int = 30 # to be modified
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

    print(url)

    # let the UCSB api know what this application is
    headers: dict = {
        "accept": "application/json",
        "ucsb-api-version": "3.0",
        "ucsb-api-key": uscb_api_consumer_key
    }

    # send our request and receive the payload
    response: requests.Response = requests.get(url, headers=headers)
    data: dict = response.json()
    return data

def populate_courses_db():
    """
    This function should only be run once during startup to get required courses in your DB
    This function will take a while to complete
    Once run, it will not run again, even for future restarts of the server as long as the DB doesn't erase data
    """

    max_pages = 5
    years = ['2024']
    quarters = ['1', '2', '3', '4']
    subject_codes =  ["ANTH", "ART", "ARTHI", "ARTST", "AS AM", "ASTRO", "BIOE", "BIOL", 
    "BMSE", "BL ST", "CH E", "CHEM", "CH ST", "CHIN", "CLASS", "COMM", "C LIT", "CMPSC", 
    "CMPTG", "CNCSP", "DANCE", "DYNS", "EARTH", "EACS", "EEMB", "ECON", "ED", "ECE", "ENGR", 
    "ENGL", "EDS", "ESM", "ENV S", "ESS", "ES", "FEMST", "FAMST", "FR", "GEN S", "GEOG", 
    "GER", "GPS", "GLOBL", "GRAD", "GREEK", "HEB", "HIST", "INT", "ITAL", "JAPAN", "KOR", 
    "LATIN", "LAIS", "LING", "LIT", "MARSC", "MARIN", "MATRL", "MATH", "ME", "MAT", "ME ST", 
    "MES", "MS", "MCDB", "MUS", "MUS A", "PHIL", "PHYS", "POL S", "PORT", "PSY", "RG ST", 
    "RENST", "RUSS", "SLAV", "SOC", "SPAN", "SHS", "PSTAT", "TMP", "THTR", "WRIT", "W&L",]

    for year in years:
        for quarter in quarters:
            for code in subject_codes:
                # convert the quarter to UCSB format
                UCSB_quarter = f"{year}{quarter}"
                queried_courses = 0
                total_courses = 1000000

                # UCSB API stores its courses in multiple pages, meaning we need to loop through each page
                for page_number in range(1, max_pages):

                    # fetch the page
                    query = query_UCSB_classes(UCSB_quarter, code, page_number)

                    # sleep for 2 seconds to avoid overloading the api
                    time.sleep(2)

                    # keep track of page statistics
                    assert query["pageNumber"] == str(page_number)
                    queried_courses += int(query["pageSize"])
                    total_courses = query["total"]

                    # store the classes in the query
                    for i in query["classes"]:
                        course = models.Cached_Courses(
                            courseID = i["courseId"],
                            year = int(year),
                            quarter = int(quarter),
                            data = i
                        )
                        course.save()
                    
                    # check if we have reached the total number of courses
                    if (queried_courses >= total_courses):
                        break

if __name__ == "__main__":
    # Example way to query; this should return a list of courses and descriptions
    query = query_UCSB_classes("20241", "CMPSC")
    for i in query["classes"]:
        print(i["courseId"])
        print(i["description"])
    pass 