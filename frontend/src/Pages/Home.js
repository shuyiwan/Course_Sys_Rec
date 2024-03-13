//import React, {useEffect,useState} from "react"
import React, { useState } from "react"
// import { saveAs } from 'file-saver';
import SearchBar from '../Components/SearchBar';
import SearchResultList from '../Components/SearchResultList';
import "../Styles/Pages.css";

export default function Home() {

    // useEffect(()=> {

    //     const jsonData = [{ email: '123@123', courseID: 'COMSC 156' }];
    //     const jsonString = JSON.stringify(jsonData, null, 2);
    //     const blob = new Blob([jsonString], { type: 'application/json' });
    //     saveAs(blob, 'yourData.json');

    // },[])

    const [results, setResult] = useState([]);
    return (
        <div className='searchBarWrapper'>
            <div>
                <h1>Welcome to Platinum</h1>
                <SearchBar setResult={setResult} />
                <div className="rectangle-blocks-container">
                    <div className="rectangle-block">
                        <p>Search: Linear Algebra</p>
                    </div>
                    <div className="rectangle-block">
                        <p>Try: Software Engineer</p>
                    </div>
                    <div className="rectangle-block">
                        <p>Try: Computer Science Teaching</p>
                    </div>
                    <div className="rectangle-block">
                        <p>Try: Nietzsche</p>
                    </div>
                </div>

                <SearchResultList results={results} />
            </div>
        </div>
    );
}
