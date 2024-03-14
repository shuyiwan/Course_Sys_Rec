import React, {useEffect, useState} from "react";
import { Link } from 'react-router-dom';
import '../Styles/SearchPageResult.css';
import GPTExplanation from './GPTExplain.js';
import RMPresult from "./RMPresult.js"
import GradeDistribution from "./GradeDistribution.js";
import returnIcon from '../assets/return.png';
import allAddedIcon from '../assets/addcart.png'; // Adjust the path according to your project structure


export default function SearchProfResult({ result}) {
    // retrieve the user's email from localStorage + store here
    //console.log(result)
    const userEmail = localStorage.getItem("email");  
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

    console.log(result)
    if(result === "There is no classes for this professor in quarter 20241."){
        return(
            <div>
                <div>
                    No classes for this professor in this quarter
                </div>
            </div>
        )
    }

    else{
        return (
            <div>
                <Link to="/" style={{ backgroundImage: `url(${returnIcon})` }} className="ReturnButton"></Link>
                {addedToCart ? ( // Conditionally render based on addedToCart state
                    showMessage && <div className="confirmationMessage">Course added to cart!</div>
                ) : (
                    <div className="SearchPageResult">
                        <p>{result.courseID}</p>
                        <br />
                        <p>{result.title}</p>
                        <br />
                        <p>Description: {result.description}</p>
                        <br />
                        <p>Instructor: {result.instructor}</p>
                        {/* time location should change into a component to handle null cases */}
                        {result.timeLocations.map((info, id) => (
                            <div key={id}>
                                <div>
                                    {info.days}
                                    {info.beginTime + " - "}
                                    {info.endTime}
                                    <br/>
                                    {info.building + " "}
                                    {info.room}
                                </div>
                            </div>
                        ))}
                        <button className="AddToCartButton" onClick={addToCart}>+</button>
                        <RMPresult RMPinfo={result.rmf} />
                        <GPTExplanation input={result.description} />
                        <GradeDistribution grades = {result.grades}/>
                    </div>
                )}
            </div>
        );
    }

}