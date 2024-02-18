from django.test import TestCase

# Create your tests here.

from django.urls import reverse

class addTests(TestCase):

    def test_adding_to_sameusers(self):
        
        # This test will add CS 8 and CS 9 to test5@ucsb.edu. 
        # It will test if the return message is correct.
        
        url_add = reverse("add_classes")      
        classes = [{'email': 'test5@ucsb.edu', 'courseID': 'CS 8'}, {'email': 'test5@ucsb.edu', 'courseID': 'CS 9'}]       
        response_add_classes = self.client.post(url_add, classes, content_type='application/json')
        correct_response = {'Success': 'All of the courses are saved.'}
        self.assertEqual(response_add_classes.json(), correct_response)
    
    def test_adding_mix_to_sameusers(self):

        # This test will add CS 8, CS 9, and CS 16 to test5@ucsb.edu.
        # Then it will add CS 8, CS 9, and CS 16 to test5@ucsb.edu.
        # It will test if the return message is correct.

        url_add = reverse("add_classes")
        classes = [{'email': 'test5@ucsb.edu', 'courseID': 'CS 8'}, {'email': 'test5@ucsb.edu', 'courseID': 'CS 9'}]       
        response_add_classes = self.client.post(url_add, classes, content_type='application/json')

        classes2 = [{'email': 'test5@ucsb.edu', 'courseID': 'CS 8'}, {'email': 'test5@ucsb.edu', 'courseID': 'CS 9'},
                    {'email': 'test5@ucsb.edu', 'courseID': 'CS 16'}]
        response_add_classes2 = self.client.post(url_add, classes2, content_type='application/json')
        correct_response = {'Success': 'CS 8, CS 9 are already in' +
                              ' the cart, and the new courses are saved'}
        self.assertEqual(correct_response, response_add_classes2.json())

    def test_adding_same_to_sameusers(self):

        # This test will add CS 8 and CS 8 to test5@ucsb.edu.
        # Then it will add them again.
        # It will test if the return message is correct.

        url_add = reverse("add_classes")
        classes = [{'email': 'test5@ucsb.edu', 'courseID': 'CS 8'}, {'email': 'test5@ucsb.edu', 'courseID': 'CS 8'}]
        response_add_classes = self.client.post(url_add, classes, content_type='application/json')
        
        response_add_classes2 = self.client.post(url_add, classes, content_type='application/json')
        correct_response = {'Failure': 'All of the courses are already in the cart'}
        self.assertEqual(correct_response, response_add_classes2.json())

    def test_adding_to_diffusers(self):

        # This test will add CS 8 to test5@ucsb.edu, and CS 9 to test6@ucsb.edu.
        # It will test if the return message is correct.

        url_add = reverse("add_classes")
        classes = [{'email': 'test5@ucsb.edu', 'courseID': 'CS 8'}, {'email': 'test6@ucsb.edu', 'courseID': 'CS 9'}]
        response_add_classes = self.client.post(url_add, classes, content_type='application/json')
        correct_response = {'Success': 'All of the courses are saved.'}
        self.assertEqual(response_add_classes.json(), correct_response)

    def test_adding_mix_to_diffusers(self):

        # This test will add CS 8 to test5@ucsb.edu, and CS 9 to test6@ucsb.edu.
        # Then it will add CS 8 to test5@ucsb.edu, and CS 9, CS 16 to test6@ucsb.edu.
        # It will test if the return message is correct.

        url_add = reverse("add_classes")
        classes = [{'email': 'test5@ucsb.edu', 'courseID': 'CS 8'}, {'email': 'test6@ucsb.edu', 'courseID': 'CS 9'}]
        response_add_classes = self.client.post(url_add, classes, content_type='application/json')

        classes2 = [{'email': 'test5@ucsb.edu', 'courseID': 'CS 8'}, {'email': 'test6@ucsb.edu', 'courseID': 'CS 9'}
                    , {'email': 'test6@ucsb.edu', 'courseID': 'CS 16'}]
        response_add_classes2 = self.client.post(url_add, classes2, content_type='application/json')
        correct_response = {'Success': 'CS 8, CS 9 are already in' +
                              ' the cart, and the new courses are saved'}
        self.assertEqual(correct_response, response_add_classes2.json())

    def test_adding_same_to_diffusers(self):

        # This test will add CS 8 to test5@ucsb.edu, and CS 9 to test6@ucsb.edu.
        # Then it will add the same courses to the users again.
        # It will test if the return message is correct.

        url_add = reverse("add_classes")
        classes = [{'email': 'test5@ucsb.edu', 'courseID': 'CS 8'}, {'email': 'test6@ucsb.edu', 'courseID': 'CS 9'}]
        response_add_classes = self.client.post(url_add, classes, content_type='application/json')

        response_add_classes2 = self.client.post(url_add, classes, content_type='application/json')
        correct_response = {'Failure': 'All of the courses are already in the cart'}
        self.assertEqual(correct_response, response_add_classes2.json())

        