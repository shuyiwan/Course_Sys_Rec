import React, {useEffect, useState} from "react"
import { useLocation } from 'react-router-dom';
import "../Styles/Pages.css"
import Loading from '../Pages/Loading.js'; // Import the Loading component
import noResultsIcon from '../assets/no-results.png';
import "../Styles/SearchPageList.css"
import SearchProfList from '../Components/SearchProfList.js';
import ProfTag from "../Components/ProfTag.js";
import { color } from "echarts";


export default function SearchProfessor(){
    let location = useLocation();
    let keyword = " "
    const [results, setResults] = useState({name: 'downloading'})
   
    useEffect(()=> {
        const fetchData = async (value) =>{
            let url = 'https://intermittence.pythonanywhere.com/search/professor/?name=' + value +'&quarter=20241';
            await fetch(url)
            .then((response) => response.json())
            .then((jsonFile) => {
                setResults(jsonFile)
                // console.log(results)
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
        console.log(results)
        if (results.name === "downloading"){
            return (
                <Loading />
            )
        }

        if(results[0] === "There is no professor that matches this name."){
            return(
                <div>
                    <p style={{color: "white"}}>
                        There is no professor that matches this name
                    </p>
                </div>
            )
        }

        return (
            <div>
              {results.map((prof, id) => {
                  return (
                    <div key = {id} className="SearchPageList">
                        <p> Name: {prof.name}</p>
                        <p> Fullname: {prof.fullname}</p>
                        <p> Department: {prof.department}</p>
                        <p> Rating: {prof.rating}</p>
                        <p> Difficulty: {prof.difficulty}</p>
                        <ProfTag Tags={prof.tags}/>
                        <SearchProfList results={prof.classes}/>
                    </div>
                  )
              })}
            </div>
        )
    }
}