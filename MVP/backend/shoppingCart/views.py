import json
import requests
from django.shortcuts import render
from shoppingCart import models
from django.http import JsonResponse
from django.db import IntegrityError
from django.views.decorators.http import require_http_methods

# Create your views here.

### The function to handle the request of save courses to cart.
@require_http_methods(["GET"])  # Make sure it only handles the GET request, We will change
                                # it to POST after MVP
def add_classes(request):

    # This is a basic version of adding classes. We just get the email and the 
    # courseId of the class the user what to save to cart

    # For this version, we only add one class to db per request.

    # get the email from url. 
    # For example http://127.0.0.1:8000/shoppingCart/?email=test@ucsb.edu&courseID=CS154
    # if it cannot find parameters is not in url, set them to ''
    email = request.GET.get('email', '')
    courseID = request.GET.get('courseID', '')

    # return error if any of the keywords is empty
    if not email:
        return JsonResponse({'error': 'No email provided.'}, status=400)
    if not courseID:
        return JsonResponse({'error': 'No courseID quarter provided.'}, status=400)
    
    # check if the user name is in User table, if not we need create a user
    # and add it to the table
    if not models.User.objects.filter(email=email).exists():
        new_user = models.User(email = email) # create a user object
        new_user.save() # This will add one row for this user into the User table

    # add class to db
    # To link the class with the user, we need to fetch the user from db first
    user = models.User.objects.get(email = email)

    # Check if this class is already added for this user
    if models.SavedCourses.objects.filter(courseID = courseID, user_id = user.id).exists():
        return JsonResponse({'Failure': f'{courseID} is already added for {email}'})
    
    new_class = models.SavedCourses(courseID = courseID, user = user) # create the course
                    # object and link the user to this course
    new_class.save() # add one row to for this class to the SavedCourses table
    

    # if everything works well, return a json response indicating that the class is saved
    return JsonResponse({'Success': f'{courseID} is added for user {email}'})







