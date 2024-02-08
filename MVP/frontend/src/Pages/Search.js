import SearchPageList from '../Components/SearchPageList.js'
import React, {useEffect, useState} from "react"
import { useLocation } from 'react-router-dom';
import "../Styles/Pages.css"

export default function Course(){
    let location = useLocation();
    let keyword = location.state.value
    const [results, setResults] = useState({})

    useEffect(()=> {
        const fetchData = async (value) =>{
            let url = 'https://intermittence.pythonanywhere.com/search/?keyword=' + value +'&quarter=20241&subject_code=CMPSC';
            await fetch(url)
            .then((response) => response.json())
            .then((jsonFile) => {
                setResults(jsonFile)
            })
        }
        fetchData(keyword)
    },[])

    console.log(results)

    const isJsonEmpty = Object.keys(results).length === 0;

    if(isJsonEmpty){
        return (
            <div className='loadingMessage'>
               Loading.....
            </div> 
        )
    }

    else{
        return (
            <SearchPageList results={results}/> 
        )
    }

    

    
}