import React, {useEffect, useState} from "react";
import { Link } from 'react-router-dom';
import '../Styles/SearchPageResult.css';
import GPTExplanation from './GPTExplain.js';
import RMPresult from "./RMPresult.js"


export default function SearchPageResult({ result }) {
    // retrieve the user's email from localStorage + store here

    const userEmail = localStorage.getItem("email");  

    async function getCsrfToken() {
        let _csrfToken = null;

        if (_csrfToken === null) {
            const response = await fetch(`https://intermittence.pythonanywhere.com/shoppingCart/crsfToken/`, {
                credentials: 'include',
            });
            const data = await response.json();
            _csrfToken = data.csrfToken;
        }
        //console.log(_csrfToken)
        return _csrfToken;
    }

    async function addToCart() {
        const postData = [{
            email: userEmail, 
            courseID: result.courseID,
            sql_id: result.sql_id

        }];
        // console.log(result.courseID)

        try {
            
            const response = await fetch('https://intermittence.pythonanywhere.com/shoppingCart/add/', {
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

    //console.log(result.rmf)
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
                <RMPresult RMPinfo = {result.rmf} />
                <GPTExplanation input={result.description} />
                

            </div>
        </div>
    );
}
