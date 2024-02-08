
## Components Documentation

#### `App.js`

`App.js` serves as the main component in a React application, orchestrating the overall layout and routing. It typically includes application-wide components like navigation bars, footers, and route definitions. This file is crucial for defining the structure and navigation flow of the application.

---

#### `index.js`

`index.js` is the entry point for a React application. It sets up the root React component and renders it to the DOM. This file includes important configurations such as wrapping the app with browser router for navigation and setting up providers for global contexts like authentication. It's essential for bootstrapping the application and applying global CSS styles.

---

#### `Navbar.js`

The `Navbar.js` file defines a navigation bar component for a React application using React Router for navigation. The main `Navbar` function component renders a navigation bar with links to different pages of the application. It includes a `siteTitle` link that navigates to the home page and a list of `CustomLink` components for other navigation links like Search, CourseCart, and About.

The `CustomLink` component, defined within the same file, is a customized link component that uses `useResolvedPath` and `useMatch` hooks from React Router to determine if the link's destination matches the current location. This is used to apply active styling to the link that corresponds to the current page. The component takes `to` as a prop for the destination path and `children` to render the link's text or content. Additional props can be passed through to the underlying `Link` component from React Router.

---

#### `LoginButton.js`

This component is responsible for handling user login functionality. It uses the `react-oauth` library to facilitate Google login. It also imports styles from `App.css` and uses `axios` for HTTP requests.

It implements a React component for a login button that integrates Google OAuth for authentication. It manages user login state, displays user profile information upon successful login, and offers a logout functionality. The component uses React hooks for state management and side effects, and Axios for API requests to fetch user profile information from Google's OAuth2 userinfo endpoint. It conditionally renders either the login button or user information and a logout button based on the authentication state. This component is designed to be easily integrated into React applications requiring Google authentication.


---

#### `SearchBar.js`

The `SearchBar.js` file defines a React component that provides a search input field for users. It incorporates a search icon from `react-icons/fa`, utilizes React hooks for state management, and performs a simulated API call to fetch user data based on the search input. The component updates its parent's state with the search results, enabling dynamic search functionality within the application. The file also includes a custom CSS import for styling the search bar. This component is designed to be integrated into web applications that require a user-friendly search feature with real-time filtering capabilities. It also imports styles from `SearchBar.css`.

---

#### `SearchPageResult.js`

The `SearchPageResult.js` file defines a React component that displays an individual search result. It imports a CSS file for styling and expects a `result` object as a prop, which contains the title of the search result. The component renders a `div` with a class `SearchPageResult`, and an `onClick` event handler that triggers an alert displaying the result title when clicked. This component is designed to be used as part of a search results page, where each instance represents a clickable search result item.

---

#### `SearchPageList.js`

`SearchPageList.js` is the component that renders a list of search results. It imports a `SearchPageResult` component for each individual result. The component takes a `results` prop, which is an array of result objects, and maps over this array to render a `SearchPageResult` component for each result, passing the result object and a unique key to each. The component is styled with an imported CSS file. It's designed for use in applications where search functionality returns multiple results that need to be displayed to the user.

---

#### `SearchResult.js`

`SearchResult.js` is a React component designed to display an individual search result. It is structured to show the title of a result, encapsulated within a `div` element, styled with a corresponding CSS file. The component is interactive, featuring an `onClick` handler that triggers an alert with the result's title, enhancing user engagement. This component is essential for applications displaying clickable search results, allowing for a modular and reusable design.

---

#### `SearchResultList.js`

`SearchResultList.js` is a React component that renders a list of search results, leveraging the `SearchResult` component to display each item. It accepts a `results` array prop, iterating over it to render a `SearchResult` for each entry, providing a unique `key` for React's rendering optimization. The component is styled with a dedicated CSS file, ensuring a consistent and visually appealing presentation of the results list. Ideal for search functionality, it efficiently aggregates and displays multiple results in a structured format.

## Pages Documentation

#### `About.js`

`About.js` is a straightforward React functional component that renders a simple message indicating that the About Page is not yet implemented. This component is used to represent the About section of the application and can be expanded in the future to include detailed information about the application or organization.

---

### `CourseCart.js`

`CourseCart.js` is a React component designed to display the course selection cart for users. It typically involves listing selected courses, managing course quantities, and providing options to remove courses or proceed to checkout. The component might also integrate state management to handle the dynamic nature of user interactions with the cart.

---

### `Home.js`

`Home.js` is the React component representing the landing or home page of the application. It serves as the initial view users encounter, often showcasing key features, benefits, and call-to-action elements. The Home component may include sections like a welcome message, overview of services or products, testimonials, and links to other parts of the application.

--- 

### `Search.js`

`Search.js` is a React component dedicated to providing search functionality within the application. It usually includes a search input field, possibly with advanced filtering options, and displays the results in a user-friendly format. This component handles user queries, search result processing, and may involve state management to track user input and search results.

## Styles Documentation

#### `App.css`
This CSS file contains global styles for the main layout of the React application, defining the look and feel of common elements and the overall structure. It typically includes styles for the main container, header, footer, and other layout components.

---

#### `Pages.css`
This stylesheet is dedicated to styling the individual page components within the `Pages` directory, such as `Home`, `About`, `Search`, and `CourseCart`. It ensures that each page has a consistent design language while allowing for page-specific customizations.

---

#### `CourseCart.css` (First Upload)
This CSS file is specifically tailored for styling the `CourseCart` component, detailing the presentation of course listings, cart items, buttons, and other elements related to the course selection and checkout process.

---

Other css file has similar logic and structure (there is too many to write, so I'm just documenting 3 of them)
