# The Backend

## Setting up the backend

### Setting up MySQL

1. Install MySQL to your device.
2. Start up the MySQL shell:
    ```shell
    # Mac
    > /usr/local/mysql/bin/mysql -u root -p

    # Linux
    > sudo mysql -u root -p

    # Windows
    Not tested yet
    ```
    **Important:** Your machine may require you to activate MySQL before you can use the shell. You must do this first if this happens.
3. From inside the MySQL shell, create the database, username, and password as defined in `backend/backend/settings.py`
    ```shell
    # create the database
    > CREATE DATABASE saved_courses_db;

    # create the username and password
    > CREATE USER 'team4'@'localhost' IDENTIFIED BY 'cs148winter';

    # grant the username and password required privileges
    > USE saved_courses_db;
    > GRANT ALL PRIVILEGES ON saved_courses_db TO 'team4'@'localhost';
    > FLUSH PRIVILEGES;

    # exit the shell
    > exit;
    ```

#### Other Useful Commands:

    ```shell
    # Show current databases
    > SHOW DATABASES;

    # Show users
    > SELECT User FROM mysql.user;

    # Enter the database
    > USE saved_courses_db;
    
    # Show all the tables of current database
    > SHOW TABLES;
    
    # see the structure of table
    > DESCRIBE <table_name>;

    # Show all the entries of table
    > SELECT * FROM <table_name>;

    # Empty the table
    > DELETE FROM <table_name>;
    ```

For more information about MySQL, please refer to the MySQL documentation.

### Setting up Python

1. Install Python. Only `Python 3.9` and above have been shown to work with this project.

2. Create the Python virtual environment. These commands may vary depending on your machine/setup, but it generally goes like this:
    ```shell
    # head to the correct folder from root
    > cd backend

    # create the virtual environment
    > python -m venv venv

    # activate the virtual environment (for Linux)
    > source venv/bin/activate

    # or activate the virtual environment (for Windows)
    > venv\Scripts\Activate
    ```

    **IMPORTANT:** The virtual environment should be activated whenever installing dependencies or running this project. This will help prevent dependency collisions.

    **NOTE**: To deactivate your virtual environment, simply run `deactivate`.

3. Install the dependencies. Right now, we are managing both `Pipfile` and `requirements.txt`, which can both work independently, but using `requirements.txt` is recommended.

    ```shell
    # from requirements.txt
    > python -m pip install -r requirements.txt

    # from Pipfile
    > pipenv shell
    > pipenv install
    ```

### Setting up Django

#### Setting up environmental variables
This project requires using a UCSB API key. To do so:
1. Register an account, create a UCSB API app, and get the UCSB api key from it. You can find the instructions to do so [here](https://www.developer.ucsb.edu/documentation) (mostly the `Getting Started` and `Creating your first app`).

2. Create `backend/backend/.env`

3. Register the following variable inside: `ucsb_api_key=YOUR_PUBLIC_KEY`

#### Performing migrations
After following all of the prior steps to set up your environment, it is finally time to get the Django app set up:

```shell
# Make sure that you've activated your virtual environment
python manage.py migrate
```

#### Populating local databases
The following isn't required to get the Django app running, but it's highly advised to do so to get 
some important data into your database:

```shell
python manage.py populate_course_dbs
```

#### Finally:

```shell
python manage.py runserver
```
That should be it! If everything is set up correctly, Django should be running an app at `http://127.0.0.1:8000/`.


## The Backend API

### Search (Querying the UCSB API)

URL: http://127.0.0.1:8000/search/?keyword=KEYWORD&quarter=YYYYQ&subject_code=SUBJECT_CODE #This is just a format of what the url should looks like. You need to enter the valid arguments.

The “keyword”, “quarter”, and “subject_code” are the parameters in the URL. They are all strings.

`YYYYQ` is a string that represents the year and the quarter number. The string should only contain numbers. For the last digit, 1 is winter, 2 is spring, etc. (We should probably change the format into something like quarter=Winter 2024 which makes more sense.)

Calling this URL should return a JSON object. The return JSON is converted from a python list that contains dictionaries for each class.

For example: calling the URL http://127.0.0.1:8000/search/?keyword=project&quarter=20241&subject_code=CMPSC should return all the courses offered in winter 2024 that contain “project” in its descriptions, case-insensitive:

    ```json
    [
        {
            "ID": 1,
            "courseID": "CMPSC   148  ",
            "title": "COMP SCI PROJECT",
            "instructor": "HOLLERER T",
            "description": "Team-based project development. Topics include software engineering and pro fessional development practices, interface design,         advanced library support ; techniques for team oriented design and development, testing and test dri ven development, and software reliability and            robustness. Students present and demonstrate final projects."
        },
        {
            "ID": 2,
            "courseID": "CMPSC   196B ",
            "title": "ADV UGRAD RESEARCH",
            "instructor": "TBD",
            "description": "Advanced research for undergraduate students, by petition after completing a minimum of 4 units of CMPSC 196 for a letter grade.       The student will prop ose a specific research project and make a public presentation of final res ults. Evaluation and grade will be based on feedback        from faculty advisor a nd one other faculty member."
        }
    ]
    ```

A few things to note:
* The “keyword”, “quarter”, and “subject_code” are the parameters in the URL. They cannot be set to empty for now.
* If it cannot find the courses that match this keyword, it will return an empty JSON [].
* “keyword” only accepts alphabets and white space. There should not be any other char otherwise it will return an empty JSON. However, it accepts phrases like “dynamic programming”.
* “quarter” should be formatted like YYYYQ.
* “subject_code” should be case-insensitive. However, it cannot end with “W”. All the regular subject codes do not end with “W”, but the online course has different subject codes like “CMPSCW”. We have added the online courses that match the keyword at the end of JSON when you just use the regular subject code.
* For now, each query should get at most 30 courses. We probably need to change this setting later.
* The descriptions in JSON sometimes have white space that splits the words. For example, it may have something like “rel ations”. This is the problem of ucsb-api, and we may need to deal with it later. It will not affect the search result, so when you use the keywords “relations” it should match this course.

#### Error situations:
* “keyword” is empty: `{'error': 'No search keyword provided.'}`
* “quarter” is empty:  `{'error': 'No search quarter provided.'}`
* “subject_code” is empty: `{'error': 'No search subject code provided.'}`
* “subject_code” end with “W”: `{'error': 'Invalid subject code.'}`

### Querying the shopping cart (WIP)

This feature will be documentated later after it's completed.
