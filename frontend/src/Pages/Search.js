import SearchPageList from '../Components/SearchPageList.js'
import React, {useEffect, useState} from "react"
import { useLocation } from 'react-router-dom';
import "../Styles/Pages.css"
import Loading from '../Pages/Loading.js'; // Import the Loading component
import noResultsIcon from '../assets/no-results.png';


export default function Course(){
    let location = useLocation();
    let keyword = " "
    const [results, setResults] = useState({name: 'downloading'})
   
    useEffect(()=> {
        const fetchData = async (value) =>{
            let url = 'https://intermittence.pythonanywhere.com/search/?keyword=' + value +'&quarter=20241';
            await fetch(url)
            .then((response) => response.json())
            .then((jsonFile) => {
                setResults(jsonFile)
                //console.log(jsonFile)
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
            <div className='noResultsIconContainer'>
                <img src={noResultsIcon} alt="No Results Found" style={{ maxWidth: '120px' }}/>
                <p className="courseNotFound">Course Not Found</p>
                <p className="tryDifferent">Try again with different words or phrases</p>
            </div>
        )
    }

    else{
        if (results.name === "downloading"){
            return (
            <Loading />
            )
        }
        
        return (
            <div>
                <SearchPageList results={results}/> 
            </div> 
        )
    }
}