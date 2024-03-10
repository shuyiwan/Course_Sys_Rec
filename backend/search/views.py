from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from search import views_helpers
from search.keyword_gen import keyword_generation  # Import the keyword_generation function





### The function to handle the search request
@require_http_methods(["GET"])  # Make sure it only handles the GET request
def search_keywords(request):
    # get the keyword from url. 
    # For example http://127.0.0.1:8000/search/?keyword=project&quarter=20241&subject_code=CMPSC
    # if it cannot find parameters is not in url, set them to ''
    keyword = request.GET.get('keyword', '')
    quarter = request.GET.get('quarter', '')
    subcode = request.GET.get('subject_code', '')

    # Return error if any parameter is missing
    if not (keyword and quarter):
        return JsonResponse({'error': 'Missing required search parameters.'}, status=400)
    
    # return error if the subject_code end with "W" since we will handle the online 
    # courses together with regular courses.
    # Return error for invalid subject code

    # get the subject code for online course e.g. "CMPSCW" if there is a subject code
    if subcode and subcode[-1] == "W":
        return JsonResponse({'error': 'Invalid subject code.'}, status=400)
    
    # Generate keywords once for the search request
    generated_keywords = keyword_generation(keyword)

    # Initialize the list to hold selected courses
    selected = []

    # Search for courses matching the generated keywords, for both regular and online courses
    views_helpers.search_from_backend(subcode, quarter, generated_keywords, selected)
    
    # get the subject code for online course e.g. "CMPSCW"
    # note that this only applies if there is a subject code in the first place
    if subcode:
        views_helpers.search_from_backend(subcode + "W", quarter, generated_keywords, selected)
        
    # return a json, "safe = False" so that it can handle the data that 
    # are not dict, "json_dumps_params={'indent': 4}" is for adding indentation
    # so that it looks better than all the course cluster together.
    return JsonResponse(selected, safe = False, json_dumps_params={'indent': 4})

@require_http_methods(["GET"])  # Make sure it only handles the GET request
def search_professor(requests):
    name = requests.GET.get('name', '')
    quarter = requests.GET.get('quarter', '')

    # Return error if any parameter is missing
    if not (name and quarter):
        return JsonResponse({'error': 'Missing required search parameters.'}, status=400)
    
    selected = []
    views_helpers.search_professor_from_backend(name, quarter, selected)
    if not selected:
        selected = ["There is no professor that match to this name."]
    return JsonResponse(selected, safe = False, json_dumps_params={'indent': 4})