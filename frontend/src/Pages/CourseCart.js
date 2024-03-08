import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom'; 
import '../Styles/CourseCart.css'; 
import testData from '../Components/DataTest.json';
import CourseCartItem from '../Components/CourseCartItem';


export default function CourseCart() {

    const [cartItems, setCartItems] = useState([]);

    async function getCourseList() {
        const response = await fetch(`https://intermittence.pythonanywhere.com/shoppingCart/retrieve/?email=` + localStorage.getItem("email"), {
            credentials: 'include',
        });
        const data = await response.json();
        // console.log(data);
        setCartItems(data);
    }

    useEffect(() => {
        //http://127.0.0.1:8000/shoppingCart/retrieve/?email=test@ucsb.edu
        //setCartItems(testData);
        getCourseList();
       
    }, [localStorage.getItem("loginStatus")])

    async function removeItem(index) {
        const updatedCart = [...cartItems];
        updatedCart.splice(index, 1);
        setCartItems(updatedCart);
        let ID = cartItems[index].courseID
        let sqlID = cartItems[index].sql_id
        // ID = ID.replace(/\s/g, '')
        console.log(ID)
        //http://127.0.0.1:8000/shoppingCart/delete/?email=test@ucsb.edu&courseID=CS148
        const response = await fetch('https://intermittence.pythonanywhere.com/shoppingCart/delete/?email='
            + localStorage.getItem("email") + '&courseID=' + ID + '&sql_id=' + sqlID, {
            method: 'GET',
        });
        const data = await response.json();
        //console.log(data)
        //getCourseList();
    }

    if (localStorage.getItem("loginStatus") === "false" || localStorage.getItem("loginStatus") === null){
        return (
            <div>
                <div>
                    <h1>Please log in to view your cart</h1>
                </div>
            </div>
        )
    }
    else {
        if (cartItems.hasOwnProperty("Empty")) {
            return (
                // need someone to work on the css for this message
                <div>
                    Nothing in the cart....
                    <div className="searchButtonContainer">
                        <Link to="/" className="searchButton">Back to Search</Link>
                    </div>
                </div>
                
            )
        }
        else{ 
            return (
                <div>
                    <div id="shopping-cart">
                        {cartItems.map((course, id) => (
                            <CourseCartItem course={course} id={id} removeItem={removeItem} />
                        ))}
                    </div> 
    
                    <div className="searchButtonContainer">
                        <Link to="/" className="searchButton">Back to Search</Link>
                    </div>
                </div>
            );
        }        
    }
}
