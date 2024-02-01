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
    
    # get the subject code for online course e.g. "CMPSCW"
    assert subcode[-1] != "W"
    subcode_W = subcode + "W" 

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
    selected = dict()
    for i in query["classes"]:
        
        # if the course descriptions contain the keyword, we add this course to 
        # the dictionary 'selected'
        # with key = courseID and value = description
        if regex.search(i["description"]):
            selected[i["courseId"]] = i["description"]
    
    for i in query_W["classes"]:
        
        if regex.search(i["description"]):
            selected[i["courseId"]] = i["description"]
        
    # return a json
    return JsonResponse(selected)