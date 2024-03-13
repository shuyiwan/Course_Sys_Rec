import {FaSearch} from "react-icons/fa"
import React, {useState} from "react"
import { useNavigate } from 'react-router-dom';
import "../Styles/SearchBar.css"

export default function SearchBar(){
    const [userInput, setUserInput] = useState("")
    const navigate = useNavigate();
    //backend API call for search page
    const handleChange = (value) =>{
        setUserInput(value);
    }

    const handleEnter = (value, event) =>{
        if (event.key === 'Enter') {
            if (value.length === 0) {
                ;
            }
            else{
                navigate('/search',{state: {value}})
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