import json
import re # the package for regular expression
import requests
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from search import ucsb_api 


### The function to handle the search request
@require_http_methods(["GET"])  # Make sure it only handles the GET request
def search_keywords(request):
    # get the keyword from url. 
    # For example http://127.0.0.1:8000/search/?keyword=project&quarter=20241&subject_code=CMPSC
    # if it cannot find parameters is not in url, set them to ''
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

    # get the selected courses (both in person and online)
    selected = []
    search_keywords_helper(subcode, quarter, keyword, selected)
    search_keywords_helper(subcode_W, quarter, keyword, selected)
        
    # return a json, "safe = False" so that it can handle the data that 
    # are not dict, "json_dumps_params={'indent': 4}" is for adding indentation
    # so that it looks better than all the course cluster together.
    return JsonResponse(selected, safe = False, json_dumps_params={'indent': 4})

def search_keywords_helper(subcode: str, quarter: str, keyword: str, selected: list) -> None:
    # get class data by querying from backend DB
    query = ucsb_api.query_from_DB(quarter, subcode)

    # only get ["data"] from the dicts returned by query_from_DB
    query = [i["data"] for i in query]

    # We use regular expression to match keywords in descriptions
    # \b is a word boundary char in regular expressions, adding these two 
    # characters will avoid partial matching. e.g. match "search" to "research"
    # \s match the whitespace character. 
    keyword = re.escape(keyword.lower())
    keyword = r'\b' + '\\s*'.join(keyword) + r'\b' # may be modified

    # compile the regular expression above to a re object
    # re,IGNORECASE is to make the matching process case-insensitive
    regex = re.compile(keyword, re.IGNORECASE)

    for i in query:
        # if the course descriptions contain the keyword, we will add this course to the
        # list.
        # We add the information of this course into the dict, and then add this
        # dict to "selected"
        if regex.search(i["description"]):
            each_class = dict()
            each_class["ID"] = len(selected)
            each_class["courseID"] = i["courseId"]
            each_class["title"] = i["title"]

            # check if the "instructors" list is empty, if so then set "instructor" to "TBD"
            if not i["classSections"][0]["instructors"]:
                each_class["instructor"] = "TBD"
            else:
                each_class["instructor"] = i["classSections"][0]["instructors"][0]["instructor"]
            each_class["description"] = i["description"]

            selected.append(each_class)
