# Implementing Jest for Frontend Testing

[Jest](https://jestjs.io/) is a delightful JavaScript testing framework with a focus on simplicity. It works seamlessly with frontend using React in our project. This guide will walk you through the process of seting up Jest for testing frontend.

## Prerequisites

Before getting started, ensure that you have the following installed:

- [Node.js](https://nodejs.org/) (version 10.0.0 or higher)
- NPM (Node Package Manager), simply install NPM if Node is installed using command:
    ```npm install```

## Installation

To add Jest to your project, follow these steps: 

1. Navigate to your project directory to "frontend" in the terminal.

2. Run following command:

    ```
    # Using npm
    npm install --save-dev jest
    ```

3. Jest is now installed as a development dependency in your project.

## Testing File

All the frontend testing files are in frontend/src/Tests

## Testing

1. Make sure current project directory is "frontend" in the terminal.

2. Run following command:

    ```npm test```

# Testing for Backend

There are no additional libraries required to run the corresponding unit tests. They use Django's and Python's native testing libraries. Thus, to run tests, call the following command from `backend`:

`python manage.py test`

Each submodule testing file is located within the different submodule folders in the `backend` folder 
such as `backend/search/tests.py` or `backend/shoppingCart/tests.py`. To learn how to create Django tests, please see the [official Django documentation](https://docs.djangoproject.com/en/5.0/topics/testing/overview/).