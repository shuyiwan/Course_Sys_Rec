import React from "react";
import '../Styles/SearchPageResult.css';

export default function SearchPageResult({ result, addToCart }) {
    const handleAddToCart = (e) => {
        e.stopPropagation();
        addToCart(result);
    };

    return (
        <div className="SearchPageResult" onClick={(e) => alert('Click on ' + result.title)}>
            {result.title}
            <button onClick={handleAddToCart} className="AddToCartButton">+</button>
        </div>
    );
}
