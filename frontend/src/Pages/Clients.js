import React from "react";
import "../Styles/Clients.css";

export default function Clients() {
    return (
        <section className="clients-container">
            <div className="client-text">
                <h2>Meet our Clients</h2>
                <p>Trusted by the best teams in the world.</p>
                <button>Contact Sales</button>
            </div>
            <div className="client-image">
                <img
                    alt="Client 1"
                    src={require("../assets/clientsNoBkgrnd.png")} // Adjusted relative path
                />
            </div>
        </section>
    );
}