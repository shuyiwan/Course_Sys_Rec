import React, {useEffect, useState} from "react";
import { Link } from 'react-router-dom';
import '../Styles/SearchPageResult.css';
import GPTExplanation from './GPTExplain.js';
import RMPresult from "./RMPresult.js"
import GradeDistribution from "./GradeDistribution.js";
import returnIcon from '../assets/return.png';
import allAddedIcon from '../assets/addcart.png';
import TimeLocation from "./TimeLocation.js";


export default function SearchPageResult({ result}) {
    // retrieve the user's email from localStorage + store here

    const userEmail = localStorage.getItem("email");
    const loginStatus = localStorage.getItem('loginStatus');
    const [addedToCart, setAddedToCart] = useState(false); // State to track if added to cart
    const [showMessage, setShowMessage] = useState(false); // State to show added message



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

            setAddedToCart(true); // Update state to indicate item is added to cart
            setShowMessage(true); // Show confirmation message
            setTimeout(() => setShowMessage(false), 1500); // Hide message after 1.5 seconds
        } 
        
        catch (error) {
            console.error("Failed to add item to cart:", error);
        }
    }

    //console.log(result.rmf)
    return (
        <div>
            <Link to="/" style={{ backgroundImage: `url(${returnIcon})` }} className="ReturnButton"></Link>
            {addedToCart ? ( // Conditionally render based on addedToCart state
                showMessage && (( loginStatus === "true" ) ? 
                <div className="confirmationMessage">Course added to cart!</div> : 
                <div className="confirmationMessage">Failed, please log in to add to cart.</div>)
            ) : (
                <div className="SearchPageResult">
                    <p>{result.courseID}</p>
                    <br />
                    <p>{result.title}</p>
                    <br />
                    <p>Description: {result.description}</p>
                    <br />
                    <p>Instructor: {result.instructor}</p>
                    <TimeLocation timeLocations={result.timeLocations} />
                    <button className="AddToCartButton" onClick={addToCart}>+</button>
                    <RMPresult RMPinfo={result.rmf} />
                    <GradeDistribution grades = {result.grades}/>
                    <GPTExplanation input={result.description} />
                </div>
            )}
        </div>
    );
}