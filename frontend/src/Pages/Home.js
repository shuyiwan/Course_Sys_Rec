import React, {useEffect,useState} from "react"
import { saveAs } from 'file-saver';
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
        <div className="homeContainer"> 
            <h1 className="welcomeMessage">Welcome to Platinum</h1>
            <div className='searchBarContainer'>
                <SearchBar setResult={setResult}/>
                <SearchResultList results={results}/> 
            </div>
        </div>
    );
}
