from search import models

from django.test import TestCase
from django.urls import reverse

class addTests(TestCase):

    def test_adding_to_sameusers(self):
        
        # This test will add CS 8 and CS 9 to test5@ucsb.edu. 
        # It will test if the return message is correct.
        
        url_add = reverse("add_classes")      
        classes = [{'email': 'test5@ucsb.edu', 'courseID': 'CS 8', 'sql_id': 1}, {'email': 'test5@ucsb.edu', 'courseID': 'CS 9', 'sql_id': 2}]       
        response_add_classes = self.client.post(url_add, classes, content_type='application/json')
        correct_response = {'Success': 'All of the courses are saved.'}
        self.assertEqual(response_add_classes.json(), correct_response)
    
    def test_adding_mix_to_sameusers(self):

        # This test will add CS 8, CS 9, and CS 16 to test5@ucsb.edu.
        # Then it will add CS 8, CS 9, and CS 16 to test5@ucsb.edu.
        # It will test if the return message is correct.

        url_add = reverse("add_classes")
        classes = [{'email': 'test5@ucsb.edu', 'courseID': 'CS 8', 'sql_id': 1}, {'email': 'test5@ucsb.edu', 'courseID': 'CS 9', 'sql_id': 2}]       
        response_add_classes = self.client.post(url_add, classes, content_type='application/json')

        classes2 = [{'email': 'test5@ucsb.edu', 'courseID': 'CS 8', 'sql_id': 1}, {'email': 'test5@ucsb.edu', 'courseID': 'CS 9', 'sql_id': 2},
                    {'email': 'test5@ucsb.edu', 'courseID': 'CS 16', 'sql_id': 3}]
        response_add_classes2 = self.client.post(url_add, classes2, content_type='application/json')
        correct_response = {'Success': 'CS8, CS9 are already in' +
                              ' the cart, and the new courses are saved'}
        self.assertEqual(correct_response, response_add_classes2.json())

    def test_adding_same_to_sameusers(self):

        # This test will add CS 8 and CS 8 to test5@ucsb.edu.
        # Then it will add them again.
        # It will test if the return message is correct.

        url_add = reverse("add_classes")
        classes = [{'email': 'test5@ucsb.edu', 'courseID': 'CS 8', 'sql_id': 1}, {'email': 'test5@ucsb.edu', 'courseID': 'CS 8', 'sql_id': 2}]
        response_add_classes = self.client.post(url_add, classes, content_type='application/json')
        
        response_add_classes2 = self.client.post(url_add, classes, content_type='application/json')
        correct_response = {'Failure': 'All of the courses are already in the cart'}
        self.assertEqual(correct_response, response_add_classes2.json())

    def test_adding_to_diffusers(self):

        # This test will add CS 8 to test5@ucsb.edu, and CS 9 to test6@ucsb.edu.
        # It will test if the return message is correct.

        url_add = reverse("add_classes")
        classes = [{'email': 'test5@ucsb.edu', 'courseID': 'CS 8', 'sql_id': 1}, {'email': 'test6@ucsb.edu', 'courseID': 'CS 9', 'sql_id': 2}]
        response_add_classes = self.client.post(url_add, classes, content_type='application/json')
        correct_response = {'Success': 'All of the courses are saved.'}
        self.assertEqual(response_add_classes.json(), correct_response)

    def test_adding_mix_to_diffusers(self):

        # This test will add CS 8 to test5@ucsb.edu, and CS 9 to test6@ucsb.edu.
        # Then it will add CS 8 to test5@ucsb.edu, and CS 9, CS 16 to test6@ucsb.edu.
        # It will test if the return message is correct.

        url_add = reverse("add_classes")
        classes = [{'email': 'test5@ucsb.edu', 'courseID': 'CS 8', 'sql_id': 1}, {'email': 'test6@ucsb.edu', 'courseID': 'CS 9', 'sql_id': 2}]
        response_add_classes = self.client.post(url_add, classes, content_type='application/json')

        classes2 = [{'email': 'test5@ucsb.edu', 'courseID': 'CS 8', 'sql_id': 1}, {'email': 'test6@ucsb.edu', 'courseID': 'CS 9', 'sql_id': 2},
                    {'email': 'test6@ucsb.edu', 'courseID': 'CS 16', 'sql_id': 3}]
        response_add_classes2 = self.client.post(url_add, classes2, content_type='application/json')
        correct_response = {'Success': 'CS8, CS9 are already in' +
                              ' the cart, and the new courses are saved'}
        self.assertEqual(correct_response, response_add_classes2.json())

    def test_adding_same_to_diffusers(self):

        # This test will add CS 8 to test5@ucsb.edu, and CS 9 to test6@ucsb.edu.
        # Then it will add the same courses to the users again.
        # It will test if the return message is correct.

        url_add = reverse("add_classes")
        classes = [{'email': 'test5@ucsb.edu', 'courseID': 'CS 8', 'sql_id': 1}, {'email': 'test6@ucsb.edu', 'courseID': 'CS 9', 'sql_id': 2}]
        response_add_classes = self.client.post(url_add, classes, content_type='application/json')

        response_add_classes2 = self.client.post(url_add, classes, content_type='application/json')
        correct_response = {'Failure': 'All of the courses are already in the cart'}
        self.assertEqual(correct_response, response_add_classes2.json())

class retrieveTests(TestCase):

    def test_retrieve(self):
        # make sure that CachedCourses has the correct data
        models.CachedCourses.objects.create(id = 1, courseID = "CS8", quarter = 1, year=2024, data = {'description': 'test'})

        # test if the retrieve_classes works, and also if add_classes removes all the whitespaces
        url_add = reverse("add_classes")
        classes = [{'email': 'test5@ucsb.edu', 'courseID': 'CS 8  ', 'sql_id': 1}]
        response_add_classes = self.client.post(url_add, classes, content_type='application/json')
        correct_response = {'Success': 'All of the courses are saved.'}
        self.assertEqual(response_add_classes.json(), correct_response)

        url_retrieve = reverse("retrieve_classes")
        response_retrieve = self.client.get(url_retrieve, {'email': 'test5@ucsb.edu'})
        response_retrieve = response_retrieve.json()

        self.assertEqual(response_retrieve[0]['courseID'], 'CS8')

class deleteTests(TestCase):

    def test_delete(self):
        
        # test if the delete_classes can delete the course with whitespaces in courseID

        url_add = reverse("add_classes")
        classes = [{'email': 'test5@ucsb.edu', 'courseID': 'CS 8  ', 'sql_id': 1}]
        response_add_classes = self.client.post(url_add, classes, content_type='application/json')
        correct_response = {'Success': 'All of the courses are saved.'}
        self.assertEqual(response_add_classes.json(), correct_response)

        response_delete = self.client.get(reverse("delete_class"), {'email': 'test5@ucsb.edu', 'courseID': 'CS   8   ', 'sql_id': 1})
        self.assertEqual(response_delete.json(), {'Success': 'CS8 is already deleted for test5@ucsb.edu'})

        response_retrieve = self.client.get(reverse("retrieve_classes"), {'email': 'test5@ucsb.edu'})
        self.assertEqual(response_retrieve.json(), {'Empty': 'User test5@ucsb.edu has not added any classes.'})




        