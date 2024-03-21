[Link to document:](https://docs.google.com/document/d/10ZYk4dn_uY_zG9XWjFFz8PnQh_Z0nV4vykgIHrLIrwY/edit?usp=sharing)
## Kevin:
### Backend
- Created functions to gather course data from the UCSB api
- Wrote Django command to populate database using the UCSB api course data
- Helped maintain Django views (tests + code readability + returning course data from backend)
- Maintains the backend deployment with PythonAnywhere
- Helped the development of other backend related features


## Katz:
### Backend
- Wrote the initial version of search functions(using Kevin’s API functions)(also with the help from Kevin)
- Wrote the initial version of course carts functionalities in the backend(with Mariana and Ivan)
- Wrote Django commands to populate the professor database using RateMyProfessorAPI and add the ratings to search results.
- Wrote a small scraper to add professors’ tags to database+ add tags to search
- Implement the search professor functionality
- Worked with frontend developers to test some of these functionalities.

## Shuyi:
### Frontend
- Implemented Google Oauth and login component (Login.js) that help retrieve user’s information
- Testing the POST function in Search List
- Wrote the frontend testing for home page routing.
- Implemented GPT (GPTExplain.js) in Search list to get more detailed course description.
- Restructured code of CourseCart and created coursecartItem.js
- Implement youtube video recommendation festure that integrated GPT keywords extracting.
- Implement adding note feature in CourseCart that connecting with backend.
  
### Deployment
- Deploy the website and finish the documentation.

## Yicong:
### Frontend
- Design the structure of frontend
- Create and write Home.js, Search.js, and App.js, and write components for those pages
- Create and write the router and navbar
- Write the add and delete function in the course cart
- Implemented the search function on the search page
- Write CSS for some pages and component
- Implement the rate my professor in the frontend
- Implement the filter in the frontend
- Implement SearchByProfessor.js in the frontend

## Leo:
### Backend
- Wrote keyword_gen.py & wrote prompt, allowing the app to generate keyword lists that are relevant to user input and parsing the keyword to support better keyword function
- Revised the filters in original view.py & view_helper.py (created by Kevin and Katz) to accommodate the GPT-supported course searching
Setup OpenAI & Key (under Kevin’s guidance)

### Frontend
- Wrote POST (add to cart) functionality & message
- Designed SearchPage return functionality & button
- Created and implemented the About.js 
- Wrote SearchPageResult.js (except CSRF)
- Engineered, restructured & refined frontend components of the major functionalities, including Home.js, Navbar.js, App.js, Search.js, CourseCart.js (originally created by Claire) , by adding more functionalities and buttons (working together with Yicong & Sherry)
- Designed Loading.js
- Wrote frontend documentation
  
### UI-Design
- Designed the UI for the whole app, frontend components and frontend objects, including landing page, search result, about us, and course cart, etc.
- Designed animation for loading
- Designed & restructured all icons & layout & message for frontend buttons and user actions

## Mariana:
### Backend
- Set up a database with mySQL for saving courses in the course cart.
- Wrote initial version of course cart functionalities in the backend (with Katz and Ivan)
- Set up YouTube API key for access to videos in course cart

### Frontend
- Contributed with frontend of setting up the YouTube API for course video recommendations in the course cart as a component
- Maintenance:
- Helped maintain the team folder [and the documents contained in it]
- Kept track of leadership roles of the team
- Helped maintain records of our meetings
- Helped design the DESIGN.md document

## Ivan:
- Wrote initial version of course cart functionalities in the backend (with Katz and Mariana)
- Helped set up saved courses database
- Helped implement the YouTube API
- Wrote important documents needed such as MVP_FOLLOWUP.md and USER_FEEDBACK_NEEDS.md, among others
- Helped maintain track of meeting notes and contributed on a big scale to the design of the DESIGN.md document

## Claire:
### Frontend
- Styled the web app to match Leo’s original design
- Created the original shopping cart for the MVP (courseCart.js and courseCart.css) and fixed linking issues
- Added a notes feature to the shopping cart so that users can enter short notes about the courses they are interested in taking in the future

### Backend
- Database for the notes feature so that users’ notes won’t be lost (will be finished soon)
- Database for the grade distributions (will be finished soon)



