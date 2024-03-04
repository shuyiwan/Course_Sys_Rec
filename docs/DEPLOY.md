## Deploying the Frontend
For our team's deployment of frontend, we are using Netlify https://www.netlify.com/. The steps to deploy manully will be shown.

### Preparation

1. Open up the terminal
2. Clone the repository
  ```shell
    git clone git@github.com:ucsb-cs148-w24/project-pj04-courserecs.git
  ```
3. cd into the project-pj04-courserecs
  ```shell
    cd project-pj04-courserecs
  ```

### Deploy the Website to Acquire URL
#### Option 1: Manully Deploy

1. cd into the frontend
  ```shell
    cd frontend
  ```
2. Generate the Poduction Directory which creates the 'build' directory in frontend
  ```shell
    npm run build
  ```
3. Drag the 'build' directory to Netlify
   <img width="1089" alt="Screenshot 2024-03-02 at 11 30 01 PM" src="https://github.com/ucsb-cs148-w24/project-pj04-courserecs/assets/130107934/25c6e352-7de9-4a7a-a134-4d185ae651e2">

#### Option 2: Link the GitHub Repository to Netlify

### Setup Google OAuth

Once finishing the deployment and having the site URL. You should setup the google oauth because our project has the login feature using google oauth.

#### Option 1 (Recommended): Reach Out Our Team to Add the Website URL
In this case, you don't need to change any code in this project. We will simply add your deployment URL to our Client.

#### Option 2: Setup Your Google OAuth
1. [Create Developer Project](https://ucsb-cs156.github.io/topics/oauth/google_create_developer_project.html)
2. [OAuth Consent Screen](https://ucsb-cs156.github.io/topics/oauth/google_oauth_consent_screen.html)
3. Once you got the Google Client ID. Replace ours with yours in code in frontend/src/index.js


## Deploying the Backend

Our backend is hosted on [PythonAnywhere](https://www.pythonanywhere.com). Similar to the [steps](../backend/README.md#setting-up-the-backend) required to setup the backend environment, PythonAnywhere too must be configured for deployment.

### Getting an account

An account is required to host the server. Alongside that, a paid subscription is required in order to send HTTP requests from the server, which is required functionality to populate the local databases. In our case, we are using the $5 a month subscription.

### Setting up MySQL

PythonAnywhere supports MySQL natively, but they do need to be set up.

1. Head to the Databases page from the dashboard and specifically use MySQL, not Postgres.

2. Create a new database that this Django app will connect to. Keep track of that database name. 

3. Open a MySQL shell from the consoles section of the dashboard and connect to that database.

4. Follow step 3 of [this](../backend/README.md###-Setting-up-MySQL) in order to create a user with permissions to that database. Make sure to use a custom username and password when creating the MySQL account and save them. We will use them later.

### Local Repository

It is now time to setup the local codebase:

1. Open a new bash console from the dashboard
2. Clone the repository
    ```shell
    git clone git@github.com:ucsb-cs148-w24/project-pj04-courserecs.git
    ```
3. Set up the python virtual environment
    ```shell
    cd project-pj04-courserecs/backend
    
    # create virtual environment folder
    python -m venv venv

    # activate virtual environment
    source venv/bin/activate
    ```
4. Install dependencies
    ```shell
    python -m pip install -r requirements.txt
    ```
5. Set up environmental variables. You can see how this is done [here](../backend/README.md####Setting-up-environmental-variables)

6. Edit `./backend/backend/settings.py` for production settings:
    ```diff
    # SECURITY WARNING: don't run with debug turned on in production!
    -DEBUG = True
    +DEBUG = False
    
    -ALLOWED_HOSTS = []
    +ALLOWED_HOSTS = ["your-username.pythonanywhere.com"]
    
    
    # Application definition
    @@ -83,13 +83,13 @@ WSGI_APPLICATION = "backend.wsgi.application"
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
    -        "NAME": "saved_courses_db",
    +        "NAME": "your-username$saved_courses_db",
    +        "HOST": "your-username.mysql.pythonanywhere-services.com",
            'TEST': {
                'NAME': 'tests_saved_courses_db',
            }, # using for testing in a diff db
    -        "USER": "team4",
    -        "PASSWORD": "cs148winter",
    -        "HOST": "localhost",
    +        "USER": "your-mysql-username",
    +        "PASSWORD": "your-mysql-password",
            "PORT": "3306",
        }
    }
    ```

### Setting up the web app

1. Navigate to the Web apps section from the dashboard.

2. Change the paths of certain settings:
    * Change the source code path to: `/home/your-username/project-pj04-courserecs/backend`
    * Change the working directory path to: `/home/your-username/project-pj04-courserecs/backend`
    * Change the virtualenv path to `/home/your-username/project-pj04-courserecs/backend/venv`

3. Edit the WSGI configuration file to look something like this so that PythonAnywhere knows how to import this project:

    ```python
    import os
    import sys

    path = '/home/your-username/project-pj04-courserecs/backend'
    if path not in sys.path:
        sys.path.append(path)

    os.environ['DJANGO_SETTINGS_MODULE'] = 'backend.settings'

    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
    ```

4. Head back to the Web app page and press on the `Reload your-username.pythonanywhere.com` button. This should launch your backend, and you can check for correct behavior at `https://your-username.pythonanywhere.com/search/`

    Correct behavior is to see something like: `{"error": "No search keyword provided."}` returned.

### Populating the local database
See [these](../backend/README.md/####-Populating-local-databases) instructions to gather required data for this backend.
