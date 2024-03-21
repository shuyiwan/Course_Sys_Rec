# The Backend

## Setting up the Backend

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
