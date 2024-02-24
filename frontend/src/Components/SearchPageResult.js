import React from "react";
import { Link } from 'react-router-dom';
import '../Styles/SearchPageResult.css';

export default function SearchPageResult({ result }) {
    // console.log(localStorage.getItem("email"))

    // retrieve the user's email from localStorage + store here
    const userEmail = localStorage.getItem("email");

    async function addToCart() {
        const postData = [{
            email: userEmail, 
            courseID: result.courseID 
        }];
        
        async function getCsrfToken() {
                let _csrfToken = null;

                if (_csrfToken === null) {
                const response = await fetch(`http://127.0.0.1:8000/shoppingCart/crsfToken/`, {
                    credentials: 'include',
                });
                const data = await response.json();
                _csrfToken = data.csrfToken;
            }
            console.log(_csrfToken)
            return _csrfToken;
        }

        try {
            
            const response = await fetch('http://127.0.0.1:8000/shoppingCart/add/', {
                method: 'POST',
                headers: {
                    'Accept': 'application/json, text/plain, */*',
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCsrfToken(),
                },
                credentials: 'include',
                body: JSON.stringify(postData),
            });

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            console.log("Item added to cart successfully");
        } 
        
        catch (error) {
            console.error("Failed to add item to cart:", error);
        }
    }

    return (
        <div>
            <Link to="/" className="ReturnButton"> </Link>

            <div className="SearchPageResult">
                <p>{result.courseID}</p>
                <br />
                <p>{result.title}</p>
                <br />
                <p>Description: {result.description}</p>
                <br />
                <p>Instructor: {result.instructor}</p>
                <button className="AddToCartButton" onClick={addToCart}>+</button>
            </div>
        </div>
    );
}
