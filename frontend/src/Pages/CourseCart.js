import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom'; // Import Link from React Router
import '../Styles/CourseCart.css'; // Import the CSS file
import testData from '../Components/DataTest.json';

export default function CourseCart() {

    const [cartItems, setCartItems] = useState([]);
    
    async function getCourseList() {
        const response = await fetch(`http://127.0.0.1:8000/shoppingCart/retrieve/?email=`+localStorage.getItem("email"), {
            credentials: 'include',
        });
        const data = await response.json();
        console.log(data)
        setCartItems(data); 
    }

    useEffect(() => {
         //http://127.0.0.1:8000/shoppingCart/retrieve/?email=test@ucsb.edu
        //setCartItems(testData);
        getCourseList();
    },[])

    async function removeItem(index) {
        const updatedCart = [...cartItems];
        updatedCart.splice(index, 1);
        setCartItems(updatedCart);
        let ID = cartItems[index].courseID
        // ID = ID.replace(/\s/g, '')
        console.log(ID)
        //http://127.0.0.1:8000/shoppingCart/delete/?email=test@ucsb.edu&courseID=CS148
        const response = await fetch('http://127.0.0.1:8000/shoppingCart/delete/?email='
        +localStorage.getItem("email") + '&courseID=' + ID, {
            method: 'GET',
        });
        const data = await response.json();
        console.log(data)
        //getCourseList();
    }

    return (
        <div>

            <div id="shopping-cart">
                {cartItems.map((course, id) => (
                    <div className="cart-item" key={id}>
                        <button className="remove-item" onClick={() => removeItem(id)}>Remove</button>
                        <h2>{course.courseID}</h2>
                        <p>{course.description}</p>
                    </div>
                ))}
            </div>

            <Link to="/search">Back to Search</Link>

            <button id="checkout-button">Download PDF</button>
        </div>
    );
}
