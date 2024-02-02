# The Backend

## Setting up the backend

### Setting up MySQL

1. Install MySQL to your device.
2. Start up the MySQL shell:
    ```
    # Mac
    > /usr/local/mysql/bin/mysql -u root -p

    # Linux
    > sudo mysql -u root -p

    # Windows
    Not tested yet
    ```
    **Important:** Your machine may require you to activate MySQL before you can use the shell. You must do this first if this happens.
3. From inside the MySQL shell, create the database, username, and password as defined in `MVP/backend/backend/settings.py`
    ```
    # create the database
    > CREATE DATABASE saved_courses_db;

    # create the username and password
    > CREATE USER ‘team4’@’localhost’ IDENTIFIED BY 'cs148winter';

    # grant the username and password required privileges
    > USE saved_courses_db;
    > GRANT ALL PRIVILEGES ON saved_courses_db TO team4'@'localhost;
    > FLUSH PRIVILEGES;

    # exit the shell
    > exit;
    ```

#### Other Useful Commands:

    ```
    # Show current databases
    > SHOW DATABASES;

    # Show users
    > SELECT User FROM mysql.user;
    ```

For more information about MySQL, please refer to the MySQL documentation.

### Setting up Python

1. Install Python. Only `Python 3.9` and above have been shown to work with this project.

2. Create the Python virtual environment. These commands may vary depending on your machine/setup, but it generally goes like this:
    ```
    # head to the correct folder
    > cd MVP/backend

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

    ```
    # from requirements.txt
    > python -m pip install -r requirements.txt

    # from Pipfile
    > pipenv shell
    > pipenv install
    ```

### Setting up Django
Once both the Python environment and MySQL is setup, it is finally time to get the Django app set up:

```
# Make sure that you've activated your virtual environment



```

## The Backend API

### Querying the UCSB API

### Querying the shopping cart (WIP)