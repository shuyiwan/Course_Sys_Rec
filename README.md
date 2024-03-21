# Course Organization and Recommendation System https://platinum-plus.netlify.app/

This system is a website application which aims to help student to pick the right course and succeed later in the class.

## Team Members: ##
| Name             | Github ID           |
| ---------------- | ------------------- |
| Shuyi Wan        | shuyiwan            |
| Yicong Yan	     | YicongYan           |
| Kevin Nguyen     | knguy22             |
| Claire Pemberton | cmpem               |
| Mariana Rosillo	 | rosillo-m           |
| Ivan Hernandez	 | ivan512az           |
| Leo Guo	         | HououinKyouma-2036  |
| Katz Yan	       | jyan840             |

## Descriptions: ##
**Tech Stack**: We use React for the frontend, and the backend is implemented with Django. MySQL for database.

This is a course recommendation website that integrates GPT, YouTube, and other features to provide users with better experiences in looking up the classes compared to GOLD. Students can get recommended classes from all the departments by entering the topics they like. They can see the class information,  the ratings for their instructors, and the grade distribution of this professor in the previous quarter. Students can also search for the names of the professors they like and see if they teach any classes this quarter. By adding their interested courses to the cart, users can get previews by checking the recommended videos. Users can add their notes and tips in the course cart. Our product provides a space where users can broaden their exploration of different courses across all departments in UCSB and improve their learning experience by personalizing selected courses and taking recommended information generated with assistance of AI.

## APIs ##
* UCSB API: acquire courses information in UCSB
* OpenAI GPT: text generation and keywords extraction
* Youtube Search API: get recommended videos
* Daliy Nexus's Grade Distribution
* Rate My Professor


 ## User Roles:

* **Students** that consider which courses to take in the next quarter and need help managing their courses.
* **Maintainers** that need to modify the courses& courses' descriptions and other information listed on the website.


## Setup:

The instructions to get the backend setup can be located [here](backend/README.md#setting-up-the-backend). <br>
Here are the instructions to get the [frontend-setup](frontend/README.md) and here is the [documentation](frontend/Frontend_Documentation.md) for frontend.

## Deployment:
https://platinum-plus.netlify.app/
