import React, { useState } from "react";
import '../Styles/About.css';

export default function About() {
    const [activeBlock, setActiveBlock] = useState(null);

    const handleBlockClick = (blockName) => {
        setActiveBlock(activeBlock === blockName ? null : blockName);
    };

    const teamMembers = [
        "Shuyi Wan", "Kevin Nguyen", "Claire Pemberton", "Mariana Rosillo",
        "Leo Guo", "Katz Yan", "Yicong Yan", "Ivan Hernandez"
    ];

    return (
        <div className="about-container">
            {/* Title bar */}
            <div className="title-bar">
                <h1>About Platinum</h1>
            </div>

            {/* Mission Statement */}
            <div className="mission-statement">
                <h2 className="mission-title">Mission Statement</h2>
                <p className="mission-text">
                    At Platinum, our mission is to personalize the learning experience for every individual. We understand that each learner's journey is unique, and our goal is to provide course recommendations that reflect their specific interests, goals, and learning pace. By simplifying the process of finding the right courses through intelligent, keyword-driven recommendations, we strive to empower users to take charge of their learning and achieve their full potential.
                </p>
            </div>
            {/* Blocks for History, Team, Services */}
            <div className="blocks-container">
                {['Our History', 'Our Team', 'Our Services'].map((blockName) => (
                    <div 
                        key={blockName}
                        className={`block ${activeBlock === blockName ? 'active' : ''} ${blockName === 'Our Team' ? 'team-block' : ''} ${blockName === 'Our Services' ? 'service-block' : ''} ${blockName === 'Our History' ? 'history-block' : ''}`}
                        onClick={() => handleBlockClick(blockName)}
                    >
                        <h2>{blockName}</h2>
                        {activeBlock === blockName && blockName === 'Our History' && (
                            <div className="history-content">
                                <p>Lost</p>
                                <p>Inefficient</p>
                                <p>Exhausting</p>
                                <p>We are a group of students tired of using the Gold system to search for the courses we want. Starting from January 2024, we decided to build a course searching app better than Gold --- introducing Platinum.</p>
                            </div>
                        )}
                        {activeBlock === blockName && blockName === 'Our Team' && (
                            <div className="team-members-container">
                                {teamMembers.map(member => (
                                    <div key={member} className="team-member">{member}</div>
                                ))}
                            </div>
                        )}
                        {activeBlock === blockName && blockName === 'Our Services' && (
                            <div className="service-details">
                                <ul>
                                    <li><span className="custom-bullet"></span> Discover courses that align with your academic goals and passion - easy search!</li>
                                    <li><span className="custom-bullet"></span> Create personalized course plans according to your interests - we all love DIY!</li>
                                    <li><span className="custom-bullet"></span> Boost your learning efficiency with our AI-Bot - cyberpunk!</li>
                                </ul>
                            </div>
                        )}
                        {activeBlock === blockName && (
                            <div className="close-button" onClick={() => setActiveBlock(null)}>&times;</div>
                        )}
                    </div>
                ))}
            </div>
        </div>
    );
}
