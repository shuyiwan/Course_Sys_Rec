from search import models, ucsb_api, views_helpers

from django.test import TestCase
from unittest.mock import patch, call # for testing print statements

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
            call(f"Stored: CMPSC8"),
            call(f"Stored: CMPSC16"),
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
            call(f"Stored: CMPSC8"),
            call(f"Skipping: CMPSC8"),
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

class ExtractFromData(TestCase):
    '''
    This class tests whether the extract_from_cached_course function extracts the correct information
    given from the UCSB api
    '''

    def test_extract_no_sections(self):
        cached_course = {
            'id': 1,
            'courseID': 'CMPSC8',
            'data': {
                'title': 'Intro to CMPSC',
                'description': 'Python',
                'classSections': [],
            },
        }

        result = views_helpers.extract_from_cached_course(orig_dict={}, cached_course=cached_course)
        self.assertEqual(result["sql_id"], 1)
        self.assertEqual(result["courseID"], "CMPSC8")
        self.assertEqual(result["title"], "Intro to CMPSC")
        self.assertEqual(result["instructor"], "TBD")
        self.assertEqual(result["description"], "Python")

    def test_extract_from_data_no_instructor(self):
        cached_course = {
            'id': 1,
            'courseID': 'CMPSC8',
            'data': {
                'title': 'Intro to CMPSC',
                'description': 'Python',
                'classSections': [{
                    'instructors': [],
                }],
            },
        }

        result = views_helpers.extract_from_cached_course(orig_dict={}, cached_course=cached_course)
        self.assertEqual(result["sql_id"], 1)
        self.assertEqual(result["courseID"], "CMPSC8")
        self.assertEqual(result["title"], "Intro to CMPSC")
        self.assertEqual(result["instructor"], "TBD")
        self.assertEqual(result["description"], "Python")

    def test_extract_from_data_has_instructors(self):
        cached_course = {
            'id': 1,
            'courseID': 'CMPSC8',
            'data': {
                'title': 'Intro to CMPSC',
                'description': 'Python',
                'classSections': [{
                    'instructors': [{
                        'instructor': 'John Doe',
                    }],
                }],
            },
        }

        result = views_helpers.extract_from_cached_course(orig_dict={}, cached_course=cached_course)
        self.assertEqual(result["sql_id"], 1)
        self.assertEqual(result["courseID"], "CMPSC8")
        self.assertEqual(result["title"], "Intro to CMPSC")
        self.assertEqual(result["instructor"], "John Doe")
        self.assertEqual(result["description"], "Python")
