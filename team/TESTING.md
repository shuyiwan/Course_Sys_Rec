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

## Testing

1. Make sure current project directory is "frontend" in the terminal.

2. Run following command:

    ```npm test```

# Testing for Backend

There are no additional libraries required to run backend tests. They use Django's and Python's native 
testing libraries. Thus, to run tests, call the following command from `backend`:

`python manage.py test`
