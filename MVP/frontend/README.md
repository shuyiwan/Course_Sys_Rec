# Read Me First
Here is the instruction for viewing the frontend documentation:
1. cd into MVP/frontend via terminal
2. type `npm install`
3. type `npm start`
4. Then you will be redirected to your broswer (your localhost)
5. Then you can check the frontend part! Have fun :-D




# Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

<strong>deployment</strong>: https://github.com/shuyiwan/DEPLOY/deployments/github-pages
## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can't go back!**

If you aren't satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you're on your own.

You don't have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn't feel obligated to use this feature. However we understand that this tool wouldn't be useful if you couldn't customize it when you are ready for it.

## Install node.js
node.js is a package that can be used to make web applications that run JavaScript on the server side.

Installing node also provides a JavaScript CLI (REPL) on Unix/Windows/Mac systems, as well as a way to use JavaScript as a basic scripting language (separated from any web browser.)

Installation
You can download installers here for Windows, Mac and Linux: https://nodejs.org/en/download/

Additional installation advice for specific platforms can be found here:

#### `MacOS`
You can install node (which installs npm and npx along with it) either by
- Directly obtaining an installer from: https://nodejs.org/en/download/
- With the <strong>brew</strong> package manager (see below).

<strong>Installing brew</strong>
To install brew, visit https://brew.sh and follow the instructions
Before installing anything with brew, it’s good practice to run brew update first.
If your brew install is messed up, brew doctor can help restore a proper install.

<strong>Using brew to install node</strong>
This command will install node using brew: `brew install node`

To test if it worked, you can try: `npm --version`


#### `Windows via Command Prompt`

This method is the simplest to setup, but restricts you to using Node in the Windows Command Prompt.

To install Node for the Windows Command Prompt, download an installer from https://nodejs.org/en/download/.

After installing Node, open Command Prompt and run `node -v` and `npm -v` to verify that the version numbers for Node and npm match the installer that you downloaded.

You should now be able to open a Command Prompt window and run node and npm commands as usual.

Keep in mind that Command Prompt does not support most UNIX commands. As a result, Node scripts that utilize system commands will not run properly. Because of this, we strongly discourage this method and recommend one of the other methods.


#### `Windows via Git Bash`

This method requires you to install one additional program, but gives you the ability to use Node in a UNIX-like environment with access to a limited number of UNIX commands.

First, install Node using the same method as above (by downloading and running the installer).

Then, download and install Git for Windows from https://git-scm.com/downloads.

When running the installer, we recommend the following options:

- When prompted for a default editor, select the code editor that you use on your machine. The course staff recommends Visual Studio Code, but you are free to select the editor that you are most comfortable with, given that it is already installed on your machine. The default option is Vim, but we don’t recommend it unless you know how to use it well.
- You can leave the other options to their default values, but you are welcome to change them if your project requires it and you know what you’re doing.
After installing both Node and Git, open Git Bash and run `node -v` and `npm -v` to verify that the version numbers for Node and npm match the installer that you downloaded.

You should now be able to open a Git Bash window and run node, npm, and basic UNIX commands as usual.

## Install `npm` (After installing `node`)
`npm` is the Node Package Manager. It differs from nvm in the following ways:
- `nvm` is used to determine which version of `node` we are using
- once we’ve settled on a version of `node`, `npm` uses the information in our `package.json` to load the dependencies for our specific project.
- once `npm` is installed, we can update our `npm` version by typing the following:`npm install -g npm`

## Deployment
`npm` run build creates a build directory with a production build of your app. Set up your favorite HTTP server so that a visitor to your site is served `index.html`, and requests to static paths like `/static/js/main.<hash>.js` are served with the contents of the `/static/js/main.<hash>.js` file. 

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `npm run build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)
