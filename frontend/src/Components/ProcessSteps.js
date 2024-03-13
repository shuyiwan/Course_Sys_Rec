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
                        <p className="cs-title"> <strong>Get Started</strong></p>
                            <p className="cs-item-text">
                            Type keywords of courses, carrers, or professors in search bar.
                        </p>
                    </div>
                    <div className="cs-item">
                        <span className="cs-number">02</span>
                        <p className="cs-title"> <strong>Discover</strong></p>
                        <p className="cs-item-text">
                            Get relvant courses across all departments with a single search.
                        </p>
                    </div>
                    <div className="cs-item">
                        <span className="cs-number">03</span>
                        <p className="cs-title"> <strong>DIY Course Cart</strong></p>
                        <p className="cs-item-text">
                            Add courses your personalized cart.
                        </p>
                    </div>
                    <div className="cs-item">
                        <span className="cs-number">04</span>
                        <p className="cs-title"> <strong>Start Learning Ahead</strong></p>
                        <p className="cs-item-text">
                            Click on recommended videos and here we go!
                        </p>
                    </div>
                </div>
            </div>
        </section>
    );
}

export default ProcessSteps;
