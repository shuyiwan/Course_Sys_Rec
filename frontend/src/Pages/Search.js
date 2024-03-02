import SearchPageList from '../Components/SearchPageList.js'
import React, {useEffect, useState} from "react"
import { useLocation } from 'react-router-dom';
import "../Styles/Pages.css"

export default function Course(){
    let location = useLocation();
    let keyword = " "
    //if()
    const [results, setResults] = useState({name: 'downloading'})
   
    useEffect(()=> {
        const fetchData = async (value) =>{
            let url = 'https://intermittence.pythonanywhere.com/search/?keyword=' + value +'&quarter=20241&subject_code=CMPSC';
            await fetch(url)
            .then((response) => response.json())
            .then((jsonFile) => {
                setResults(jsonFile)
                console.log(jsonFile)
            })
        }
        if(location.state && location.state.value){
            keyword = location.state.value
            localStorage.setItem("savedKeyword", keyword)
        }  
        else{
            keyword = localStorage.getItem("savedKeyword")
        } 
        fetchData(keyword)
    },[])

    const isJsonEmpty = Object.keys(results).length === 0;

    if(isJsonEmpty){
        return (
            <div className='loadingMessage'>
               Course not found
            </div> 
        )
    }

    else{
        if (results.name === "downloading"){
            return (
                <div className='loadingMessage'>
                   Loading.....
                </div> 
            )
        }
        return (
            // render the results
            <SearchPageList results={results}/>  
        )
    }

    

    
}