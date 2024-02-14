import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom'; // Import Link from React Router
import '../Styles/CourseCart.css'; // Import the CSS file
import testData from '../Components/DataTest.json';

export default function CourseCart() {
    const [cartItems, setCartItems] = useState(testData);
    useEffect(() => {
        setCartItems(testData);   
    },[])

    function removeItem(index) {
        const updatedCart = [...cartItems];
        updatedCart.splice(index, 1);
        setCartItems(updatedCart);
    }

    return (
        <div>

            <div id="shopping-cart">
                {cartItems.map((course, id) => (
                    <div className="cart-item" key={id}>
                        <button className="remove-item" onClick={() => removeItem(id)}>Remove</button>
                        <h2>{course.title}</h2>
                        <p>{course.description}</p>
                    </div>
                ))}
            </div>

            <Link to="/search">Back to Search</Link>

            <button id="checkout-button">Download PDF</button>
        </div>
    );
}
