from bs4 import BeautifulSoup
import requests
import re

def query_rmfapi_for_rmfid(professor_name: str) -> str:
    """
    This function scrapes a list of RMF id of the professor given a professor name
    We need the RMF id of that professor before scraping his page.
    """
    url: str = (
        f'https://www.ratemyprofessors.com/search/professors/1077?' # 1077 is the code of UCSB
        f'q={professor_name}'
    )
    # Wrote this function with references to the code inside RateMyProfessorAPI package
    page = requests.get(url)
    data = re.findall(r'"legacyId":(\d+)', page.text)
    id_list = []

    for professor_data in data:
        try:
            id_list.append(int(professor_data))
        except ValueError:
            pass
    return id_list

def query_rmfapi_for_hottest_tags(rmf_id: str) -> list:
    """
    The main scraper function for professor webpage.
    This function returns the list of hottest tags for the professor if there are any.
    We can change this later to scrape more stuff.
    """
    url: str = (
            f'https://www.ratemyprofessors.com/ShowRatings.jsp?'
            f'tid={rmf_id}'
    )
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    # search the corresponding div elements
    tags_container = soup.find('div', class_='TeacherTags__TagsContainer-sc-16vmh1y-0 dbxJaW')

    tags_text = []
    # if we can find the div element that corresponds to tags, we extract them
    if tags_container:
        # Find all the span elements with the class "Tag-bs9vf4-0 hHOVKF" which contain the tags
        raw_tags = tags_container.find_all('span', class_='Tag-bs9vf4-0 hHOVKF')
        # Extract the text from each tag
        tags_text = [each_tag.get_text().strip() for each_tag in raw_tags]
        return tags_text
    # If we can not find that div element, there is no tags for this prof and we return an empty list
    return tags_text
