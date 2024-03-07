import SearchPageList from '../Components/SearchPageList.js'
import React, { useEffect, useState } from "react"
import { useLocation, useNavigate } from 'react-router-dom';
import "../Styles/Pages.css"

export default function Course() {
    let location = useLocation();
    let navigate = useNavigate(); 
    let keyword = " "
    const [results, setResults] = useState({ name: 'downloading' })

    useEffect(() => {
        const fetchData = async (value) => {
            setResults({ name: 'downloading' }); 
            navigate('/loading'); // Redirect to loading page
            let url = `https://intermittence.pythonanywhere.com/search/?keyword=${value}&quarter=20241&subject_code=CMPSC`; // Use template literal for URL
            await fetch(url)
                .then((response) => response.json())
                .then((jsonFile) => {
                    setResults(jsonFile);
                    if (jsonFile.name !== 'downloading') {
                        navigate('/search'); // Navigate back to the search page or the current page
                    }
                });
        }
        if (location.state && location.state.value) {
            keyword = location.state.value
            localStorage.setItem("savedKeyword", keyword)
        } else {
            keyword = localStorage.getItem("savedKeyword")
        }
        fetchData(keyword)
    }, [navigate, location.state]) 

    const isJsonEmpty = Object.keys(results).length === 0;

    if (isJsonEmpty) {
        return (
            <div className='loadingMessage'>
                Course not found
            </div>
        )
    } else {
        return (
            // Render the results
            <SearchPageList results={results} />
        )
    }
}
