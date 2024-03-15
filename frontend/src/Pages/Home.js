//import React, {useEffect,useState} from "react"
import React, { useState } from "react"
// import { saveAs } from 'file-saver';
import SearchBar from '../Components/SearchBar';
import ProcessSteps from '../Components/ProcessSteps';
import "../Styles/Pages.css";


export default function Home() {

    // useEffect(()=> {

    //     const jsonData = [{ email: '123@123', courseID: 'COMSC 156' }];
    //     const jsonString = JSON.stringify(jsonData, null, 2);
    //     const blob = new Blob([jsonString], { type: 'application/json' });
    //     saveAs(blob, 'yourData.json');

    // },[])

    return (
        <div className='searchBarWrapper'>
            <div>
                <h1>Welcome to Platinum</h1>
                <SearchBar/>
                <div className="rectangle-blocks-container">
                    <div className="rectangle-block">
                        <p>Try: Linear Algebra</p>
                    </div>
                    <div className="rectangle-block">
                        <p>Try: Software Engineer</p>
                    </div>
                    <div className="rectangle-block">
                        <p>Try: Tobias Hollerer</p>
                    </div>
                    <div className="rectangle-block">
                        <p>Try: Nietzsche</p>
                    </div>
                </div>
                <ProcessSteps />
            </div>
        </div>
    );
}
