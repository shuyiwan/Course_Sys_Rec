import React, { useState } from 'react';
import './CourseCart.css'; // Import the CSS file

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
        // Implement logic to remove the corresponding item from the cart
        const updatedCart = [...cartItems];
        updatedCart.splice(index, 1);
        setCartItems(updatedCart);
    }

    return (
        <div>
            <h1>Shopping Cart</h1>

            {/* Shopping Cart Content */}
            <div id="shopping-cart">
                {/* Mapping through cart items */}
                {cartItems.map((item, index) => (
                    <div className="cart-item" key={index}>
                        <h2>{item.name}</h2>
                        <p>{item.description}</p>
                        <button className="remove-item" onClick={() => removeItem(index)}>Remove</button>
                    </div>
                ))}
            </div>

            {/* Continue Shopping Link */}
            <a href="searchpage.html">Continue Shopping</a>

            {/* Checkout Button */}
            <button id="checkout-button">Checkout</button>

            {/* Add your JavaScript files here for dynamic behavior */}
            <script>
                {`
                    function removeItem(index) {
                        // Implement logic to remove the corresponding item from the cart
                        var cartItem = document.getElementsByClassName('cart-item')[index];
                        cartItem.parentNode.removeChild(cartItem);
                    }
                `}
            </script>
        </div>
    );
}
