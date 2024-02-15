from django.test import TestCase

# Create your tests here.

from django.urls import reverse

class addTests(TestCase):
    def test_post_request1(self):

        print()
        print("Executing Test 1:")
        print()
        print("Add CS 8 and CS 9 to test5@ucsb.edu ")
        url_add = reverse("add_classes")
        
        classes_1 = [{'email': 'test5@ucsb.edu', 'courseID': 'CS 8'}, {'email': 'test5@ucsb.edu', 'courseID': 'CS 9'}]
        
        print()  
        print("Adding classes")
        response_add_data_1 = self.client.post(url_add, classes_1, content_type='application/json')

        print()
        print("The backend response to the Add request:")
        print(response_add_data_1.json())

        print()
        print("Retrieving the courses for test5@ucsb.edu")
        response_retri_1 = self.client.get("/shoppingCart/retrieve/?email=test5@ucsb.edu")

        print()
        print("The backend response to the Retrieve request:")
        print(response_retri_1.json())

        print()
        print("Given that CS 8, CS 9 are already saved for test5, add them one more time together with CS 16")

        classes2 = [{'email': 'test5@ucsb.edu', 'courseID': 'CS 8'}, {'email': 'test5@ucsb.edu', 'courseID': 'CS 9'},
                    {'email': 'test5@ucsb.edu', 'courseID': 'CS 16'}]
        
        print()
        print("Adding classes")
        response_add_data2 = self.client.post(url_add, classes2, content_type='application/json')

        print()
        print("The backend response to the Add request:")
        print(response_add_data2.json())

        print()
        print("Retrieving the courses for test5@ucsb.edu")
        response_retri_2 = self.client.get("/shoppingCart/retrieve/?email=test5@ucsb.edu")

        print()
        print("The backend response to the Retrieve request:")
        print(response_retri_2.json())

        print()
        print("Add these three classes again")

        print()
        print("Adding classes")
        response_add_data3 = self.client.post(url_add, classes2, safe = False, content_type='application/json')

        print()
        print("The backend response to the Add request:")
        print(response_add_data3.json())

        print()
        print("Retrieving the courses for test5@ucsb.edu")
        response_retri_3 = self.client.get("/shoppingCart/retrieve/?email=test5@ucsb.edu")
        
        print()
        print("The backend response to the Retrieve request:")
        print(response_retri_3.json())

    def test_post_request2(self):

        print()
        print("Execute Test 2:")

        print()
        print("Add CS 8 for test6@ucsb.edu, and add CS 9 for test5@ucsb.edu")
        classes_1 = [{'email': 'test6@ucsb.edu', 'courseID': 'CS 8'}, {'email': 'test5@ucsb.edu', 'courseID': 'CS 9'}]
        url_add = reverse("add_classes")

        print()
        print("Adding classes")
        response_add_data_1 = self.client.post(url_add, classes_1, content_type='application/json')

        print()
        print("The backend response to the Add request:")
        print(response_add_data_1.json())

        print()
        print("Retrieving the courses for test5@ucsb.edu")
        response_retri_1 = self.client.get("/shoppingCart/retrieve/?email=test5@ucsb.edu")

        print()
        print("The backend response to the Retrieve request:")
        print(response_retri_1.json())

        print()
        print("Retrieving the courses for test6@ucsb.edu")
        response_retri_2 = self.client.get("/shoppingCart/retrieve/?email=test6@ucsb.edu")

        print()
        print("The backend response to the Retrieve request:")
        print(response_retri_2.json())

        print()
        print("Given that CS 8 and CS 9 are already added, add them again along with add CS 16 for test5@ucsb.edu")

        classes3 = [{'email': 'test6@ucsb.edu', 'courseID': 'CS 8'}, 
                   {'email': 'test5@ucsb.edu', 'courseID': 'CS 9'},
                   {'email': 'test5@ucsb.edu', 'courseID': 'CS 16'}]
        
        print()
        print("Adding classes")
        
        response_add_data_3 = self.client.post(url_add, classes3, content_type='application/json')

        print()
        print("The backend response to Add request:")
        print(response_add_data_3.json())

        print()
        print("Retrieving the courses for test5@ucsb.edu")

        response_retri_3 = self.client.get("/shoppingCart/retrieve/?email=test5@ucsb.edu")

        print()
        print("The backend response to the Retrieve request:")
        print(response_retri_3.json())

        
        print()
        print("Retrieving the courses for test6@ucsb.edu")
        response_retri_4 = self.client.get("/shoppingCart/retrieve/?email=test6@ucsb.edu")

        print()
        print("The backend response to the Retrieve request:")
        print(response_retri_4.json())

        print()
        print("Adding the same classes again")
        
        response_add_data_3 = self.client.post(url_add, classes3, content_type='application/json')

        print()
        print("The backend response to Add request:")
        print(response_add_data_3.json())

        print()
        print("Retrieving the courses for test5@ucsb.edu")

        response_retri_3 = self.client.get("/shoppingCart/retrieve/?email=test5@ucsb.edu")

        print()
        print("The backend response to the Retrieve request:")
        print(response_retri_3.json())

        print()
        print("Retrieving the courses for test5@ucsb.edu")
        response_retri_4 = self.client.get("/shoppingCart/retrieve/?email=test6@ucsb.edu")

        print()
        print("The backend response to the Retrieve request:")
        print(response_retri_4.json())

        print()
        print("Finish")

                

        
