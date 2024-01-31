import {FaSearch} from "react-icons/fa"
import React, {useeffect, useState} from "react"
import "../Styles/SearchBar.css"

export default function SearchBar({setResult}){
    const [userInput, setUserInput] = useState("")

    //fake API call
    const fetchData = (value) =>{   
        fetch("https://jsonplaceholder.typicode.com/users")
        .then((response) => response.json())
        .then((jsonFile) => {
            const results = jsonFile.filter((user) => {
                return value && user && user.name && user.name.toLowerCase().includes(value.toLowerCase())
            })
            setResult(results)
        })
    }
 
    const handleChange = (value) =>{
        setUserInput(value);
        fetchData(value);
    }

    return (
        <div className="inputWrapper">
            <FaSearch id="searchIcon"/>
            <input placeholder="Search for courses" value={userInput} onChange={(e) => handleChange(e.target.value)}></input>
        </div>
    )
}