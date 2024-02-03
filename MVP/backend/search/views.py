import json
import re # the package for regular expression
import requests
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from search import ucsb_api 

@require_http_methods(["GET"])  # Make sure it only handles the GET request
def search_keywords(request):
    # get the keyword from url. 
    # For example http://www.random.com/search/?keyword=calculus
    # if keyword is not in url, set 'keyword' to ''
    keyword = request.GET.get('keyword', '')
    quarter = request.GET.get('quarter', '')
    subcode = request.GET.get('subject_code', '')

    # return error if any of the keywords is empty
    if not keyword:
        return JsonResponse({'error': 'No search keyword provided.'}, status=400)
    if not quarter:
        return JsonResponse({'error': 'No search quarter provided.'}, status=400)
    if not subcode:
        return JsonResponse({'error': 'No search subject code provided.'}, status=400)
    
    # return error if the subject_code end with "W" since we will handle the online 
    # courses together with regular courses.
    if subcode[-1] == "W":
        return JsonResponse({'error': 'Invalid subject code.'}, status=400)
    
    # get the subject code for online course e.g. "CMPSCW"
    subcode_W = subcode + "W" 

    # pre-process the keyword to remove all whitespace
    keyword = keyword.replace(" ", "")

    # get the python dictionary return by calling ucsb-api
    # Since the online courses have different subject_code, we need to
    # call api two times
    query = ucsb_api.query_UCSB_classes(quarter, subcode)
    query_W = ucsb_api.query_UCSB_classes(quarter, subcode_W)

    # We use regular expression to match keywords in descriptions
    # \b is a word boundary char in regular expressions, adding these two 
    # characters will avoid partial matching. e.g. match "search" to "research"
    # \s match the whitespace character. 
    keyword = re.escape(keyword.lower())
    keyword = r'\b' + '\\s*'.join(keyword) + r'\b' # may be modified

    # compile the regular expression above to a re object
    # re,IGNORECASE is to make the matching process case-insensitive
    regex = re.compile(keyword, re.IGNORECASE)

    # search classes that contain keywords
    selected = [] # will contain all the matched classes. This list will be converted 
                  # to json and returned to frontend after searching.
    
    course_index = 1 # used in React
    for i in query["classes"]:

        # if the course descriptions contain the keyword, we will add this course to the
        # list.
        # We add the information of this course into the dict, and then add this
        # dict to "selected"
        if regex.search(i["description"]):
            each_class = dict()
            each_class["ID"] = course_index
            each_class["courseID"] = i["courseId"]
            each_class["title"] = i["title"]
            each_class["instructor"] = i["classSections"][0]["instructors"][0]["instructor"]
            each_class["description"] = i["description"]

            selected.append(each_class)
            course_index += 1

    # search the online classes
    for i in query_W["classes"]:
        
        if regex.search(i["description"]):
            each_class = dict()
            each_class["ID"] = course_index
            each_class["courseID"] = i["courseId"]
            each_class["title"] = i["title"]
            each_class["instructor"] = i["classSections"][0]["instructors"][0]["instructor"]
            each_class["description"] = i["description"]
        
            selected.append(each_class)
            course_index += 1
        
    # return a json, "safe = False" so that it can handle the data that 
    # are not dict, "json_dumps_params={'indent': 4}" is for adding indentation
    # so that it looks better than all the course cluster together.
    return JsonResponse(selected, safe = False, json_dumps_params={'indent': 4})