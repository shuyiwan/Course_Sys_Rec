import React, { useState } from "react";
import '../Styles/About.css';
import Container from '@mui/material/Container';
import Typography from '@mui/material/Typography';
import Features from '../Components/Features'; 
import Testimonials from '../Components/Testimonials';


export default function About() {
    const [activeBlock, setActiveBlock] = useState(null);

    const handleBlockClick = (blockName) => {
        setActiveBlock(activeBlock === blockName ? null : blockName);
    };


    return (
        <div className="about-container">
            {/* Title bar */}
            <div className="title-bar">
                <h1>About Platinum</h1>
            </div>
            <Features />
            <Testimonials />
        </div>


    );
}
