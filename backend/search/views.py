from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from search import views_helpers

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
    views_helpers.search_from_backend(subcode, quarter, keyword, selected)
    views_helpers.search_from_backend(subcode_W, quarter, keyword, selected)
        
    # return a json, "safe = False" so that it can handle the data that 
    # are not dict, "json_dumps_params={'indent': 4}" is for adding indentation
    # so that it looks better than all the course cluster together.
    return JsonResponse(selected, safe = False, json_dumps_params={'indent': 4})
