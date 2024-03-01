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
            {/*<div className='searchBarContainer'>*/}
            <div>
                <h1>Welcome to Platinum</h1>
                <SearchBar setResult={setResult} />
                <SearchResultList results={results} />
            </div>
        </div>
    );
}
