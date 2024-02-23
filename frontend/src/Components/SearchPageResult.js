import React from "react";
import { Link } from 'react-router-dom';
import '../Styles/SearchPageResult.css';

export default function SearchPageResult({ result }) {
    // console.log(localStorage.getItem("email"))

    // retrieve the user's email from localStorage + store here
    const userEmail = localStorage.getItem("email");

    async function addToCart() {
        const postData = {
            email: userEmail, 
            courseID: result.courseID 
        };

        try {
            const response = await fetch('https://intermittence.pythonanywhere.com/shoppingCart/add/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(postData),
            });

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            console.log("Item added to cart successfully");
        } catch (error) {
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
