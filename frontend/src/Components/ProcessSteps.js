import React from 'react';
import '../Styles/ProcessSteps.css'; 

const ProcessSteps = () => {
    return (
        <section className="process-steps-container" id="steps-284">
            <div className="cs-container">
                <div className="cs-content">
                    <h3 className="cs-title">Course DIY Guide</h3>
                </div>
                
                <div className="cs-right-section">
                    <div className="cs-item">
                        <span className="cs-number">01</span>
                        <p className="cs-item-text">
                            <strong>Get Started</strong> - Type keywords of courses, carrers, or professors in search bar.
                        </p>
                    </div>
                    <div className="cs-item">
                        <span className="cs-number">02</span>
                        <p className="cs-item-text">
                            <strong>Discover</strong> - Get relvant courses across all departments with a single search.
                        </p>
                    </div>
                    <div className="cs-item">
                        <span className="cs-number">03</span>
                        <p className="cs-item-text">
                            <strong>DIY Course Cart</strong> - Add courses your personalized cart.
                        </p>
                    </div>
                    <div className="cs-item">
                        <span className="cs-number">04</span>
                        <p className="cs-item-text">
                            <strong>Start Learning Ahead</strong> - Click on recommended videos and here we go!
                        </p>
                    </div>
                </div>
            </div>
        </section>
    );
}

export default ProcessSteps;
