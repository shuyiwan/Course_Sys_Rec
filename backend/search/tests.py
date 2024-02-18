from django.test import TestCase
from unittest.mock import patch, call # for testing print statements
from search import models, ucsb_api


class StoreCoursesTest(TestCase):
    '''
    This class tests that store_courses prints the correct message depending on what 
    queries are passed in to be stored in the database.
    '''

    @patch('builtins.print')
    def test_store_default(self, mock_print):
        quarter = 1
        year = 2024
        code = "CMPSC"
        UCSB_quarter = f"{year}{quarter}"
        
        query = {
            "pageNumber": 1,
            "pageSize": 30,
            "total": 30,
            "classes": [
                {
                    "quarter": int(UCSB_quarter),
                    "courseId": "CMPSC 8",
                    "description": "Intro to Computer Science",
                },

                {
                    "quarter": int(UCSB_quarter),
                    "courseId": "CMPSC 16",
                    "description": "Intro to Computer Science 2",
                }
            ]
        }

        ucsb_api.store_courses(query, year, quarter, code)
        assert mock_print.mock_calls == [
            call(f"Stored: {query['classes'][0]['courseId']}"),
            call(f"Stored: {query['classes'][1]['courseId']}"),
        ]

    @patch('builtins.print')
    def test_store_exact_duplicate(self, mock_print):
        quarter = 1
        year = 2024
        code = "CMPSC"
        UCSB_quarter = f"{year}{quarter}"
        
        query = {
            "pageNumber": 1,
            "pageSize": 30,
            "total": 30,
            "classes": [
                {
                    "quarter": int(UCSB_quarter),
                    "courseId": "CMPSC 8",
                    "description": "Intro to Computer Science",
                },

                {
                    "quarter": int(UCSB_quarter),
                    "courseId": "CMPSC 8",
                    "description": "Intro to Computer Science",
                }
            ]
        }

        ucsb_api.store_courses(query, year, quarter, code)
        assert mock_print.mock_calls == [
            call(f"Stored: {query['classes'][0]['courseId']}"),
            call(f"Skipping: {query['classes'][1]['courseId']}"),
        ]

    def test_store_department_empty(self):
        year = 2024
        quarter = 1
        code = "CMPSC"
        total_courses = 30
        self.assertFalse(ucsb_api.already_stored_department(year, quarter, code, total_courses))
    
    @patch('builtins.print')
    def test_store_department_full(self, mock_print):
        year = 2024
        quarter = 1
        code = "CMPSC"
        total_courses = 30
        UCSB_quarter = f"{year}{quarter}"
        query = {
            "pageNumber": 1,
            "pageSize": 30,
            "total": total_courses,
            "classes": []
        }

        for i in range(total_courses):
            query["classes"].append({
                "quarter": int(UCSB_quarter),
                "courseId": f"CMPSC {i}",
                "description": "TMP",
            })
        ucsb_api.store_courses(query, year, quarter, code)

        self.assertTrue(ucsb_api.already_stored_department(year, quarter, code, total_courses))

    @patch('builtins.print')
    def test_store_department_partially_full(self, mock_print):
        year = 2024
        quarter = 1
        code = "CMPSC"
        stored_courses = 15
        total_courses = 30
        UCSB_quarter = f"{year}{quarter}"
        query = {
            "pageNumber": 1,
            "pageSize": 30,
            "total": total_courses,
            "classes": []
        }

        for i in range(stored_courses):
            query["classes"].append({
                "quarter": int(UCSB_quarter),
                "courseId": f"CMPSC {i}",
                "description": "TMP",
            })
        ucsb_api.store_courses(query, year, quarter, code)

        self.assertFalse(ucsb_api.already_stored_department(year, quarter, code, total_courses))

