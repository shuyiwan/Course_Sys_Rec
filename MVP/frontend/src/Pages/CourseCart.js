import React, { useState } from 'react';
import '../Styles/CourseCart.css'; // Import the CSS file

export default function CourseCart() {
    const [cartItems, setCartItems] = useState([
        {
            name: "Course Name 1",
            description: "Course Description 1",
        },
        {
            name: "Course Name 2",
            description: "Course Description 2",
        },
    ]);

    function removeItem(index) {
        const updatedCart = [...cartItems];
        updatedCart.splice(index, 1);
        setCartItems(updatedCart);
    }

    return (
        <div>
            <h1>Shopping Cart</h1>

            <div id="shopping-cart">
                {cartItems.map((item, index) => (
                    <div className="cart-item" key={index}>
                        <button className="remove-item" onClick={() => removeItem(index)}>Remove</button>
                        <h2>{item.name}</h2>
                        <p>{item.description}</p>
                    </div>
                ))}
            </div>

            <a href="searchpage.html">Continue Shopping</a>

            <button id="checkout-button">Checkout</button>
        </div>
    );
}
