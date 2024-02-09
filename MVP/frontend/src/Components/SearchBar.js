import {FaSearch} from "react-icons/fa"
import React, {useState} from "react"
import { useNavigate } from 'react-router-dom';
import "../Styles/SearchBar.css"

export default function SearchBar({setResult}){
    const [userInput, setUserInput] = useState("")
    const navigate = useNavigate();

    //backend API call
    const fetchData = (value) =>{
        let url = 'https://intermittence.pythonanywhere.com/search/?keyword=' + value +'&quarter=20241&subject_code=CMPSC';
        fetch(url)
        .then((response) => response.json())
        .then((jsonFile) => {
            setResult(jsonFile)
        })

    }
    //backend API call for search page
    const handleChange = (value) =>{
        setUserInput(value);
        if(value.trim() === ''){
            setResult([]);
        }
        else{
            if (value.length === 0) {
                console.log(value);
                setResult([]);
            }
            else{
                fetchData(value);
            }
        }    
    }

    const handleEnter = (value, event) =>{
        if (event.key === 'Enter') {
            if(value.trim() === ''){
                setResult([]);
            }
            else{
                if (value.length === 0) {
                    setResult([]);
                }
                else{
                    navigate('/search',{state: {value}})
                }
            }
        }
    }

    return (
        <div className="inputWrapper">
            <FaSearch id="searchIcon"/>
            <input placeholder="Search for courses" 
                value={userInput}
                onChange={(e) => handleChange(e.target.value)}
                onKeyDown={(e) => handleEnter(userInput, e)}>
            </input>
        </div>
    )
}