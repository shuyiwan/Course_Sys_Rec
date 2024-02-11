import json
import requests
from django.shortcuts import render
from shoppingCart import models
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.forms.models import model_to_dict

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


### The function to retrieved the courses
@require_http_methods(["GET"])  # Make sure it only handles the GET request。
def retrieve_classes(request):

    # get the email from url. 
    # For example http://127.0.0.1:8000/shoppingCart/retrieve/?email=test@ucsb.edu
    # if it cannot find parameters is not in url, set them to ''
    email = request.GET.get('email', '')

    # return error if any of the keywords is empty
    if not email:
        return JsonResponse({'Failure': 'No email provided.'}, status=400)

    # check if this user is in User table, if not we return an error message
    if not models.User.objects.filter(email=email).exists():
        return JsonResponse({'Failure': f'User {email} does not exist.'}, status=400)
    
    # get all the instance of the class that link to this user
    user= models.User.objects.get(email=email)
    all_classes = user.saved_courses.all()

    # if there is no class linked to this user, the return an message
    if not all_classes.exists():
        return JsonResponse({'Empty': f'User {email} has not added any classes.'})

    # all_classes is the QuerySet that contains all the class instance linked to this
    # user, we need to return these classes to correct format.
    return_classes = []
    custom_id = 1
    for i in all_classes:
        i_dict = model_to_dict(i) # change each class to a dict

        # The "id" field is originally the primery key of the SavedCourses instance. We change this 
        # id to the incremented number of each class(for the convenience of frontend). 
        # Then we store the primary key in another field "pk_id"
        pk_id = i_dict["id"]
        i_dict["id"] = custom_id
        i_dict["pk_id"] = pk_id
        custom_id += 1
        return_classes.append(i_dict)

    return JsonResponse(return_classes, safe = False, json_dumps_params={'indent': 4})

    






