import React from "react";
import { Link } from 'react-router-dom';
import '../Styles/SearchPageResult.css';

export default function SearchPageResult({result}){
    console.log(localStorage.getItem("email"))
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
                <button className="AddToCartButton">+</button>
            </div>
        </div>
    );
}
