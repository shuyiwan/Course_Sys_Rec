from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from search import models
from search.ucsb_api import query_UCSB_classes
import json
import time

class Command(BaseCommand):
    help = "Fetches all course information from the UCSB API"

    def handle(self, *args, **options):
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
                        # print query as a formatted dictionary like a json
                        print(json.dumps(query, indent=4))


                        # sleep for 2 seconds to avoid overloading the api
                        time.sleep(2)

                        # keep track of page statistics
                        assert query["pageNumber"] == page_number
                        queried_courses += query["pageSize"]
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
        self.stdout.write("Success!")
