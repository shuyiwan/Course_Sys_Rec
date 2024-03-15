import {FaSearch} from "react-icons/fa"
import React, {useState} from "react"
import { useNavigate } from 'react-router-dom';
import "../Styles/SearchBar.css"
import Button from '@mui/material/Button';
import AutorenewIcon from '@mui/icons-material/Autorenew';

export default function SearchBar(){
    const [userInput, setUserInput] = useState("")
    const [searchByCourse, setSearchByCourse] = useState(true)
    const [barMsg, setBarMsg] = useState("Search by course keyword")
    const navigate = useNavigate();
    //backend API call for search page
    const changeMode = () =>{
        if(searchByCourse === true){
            setSearchByCourse(false);
            setBarMsg("Search by professor")
        }
        else{
            setSearchByCourse(true);
            setBarMsg("Search by course keyword")
        }
    }

    const handleChange = (value) =>{
        setUserInput(value);
    }

    const handleEnter = (value, event) =>{
        if (event.key === 'Enter') {
            if (value.length === 0) {
                ;
            }
            else{
                if(searchByCourse === true){
                    navigate('/search',{state: {value}})
                }
                else{
                    navigate('/searchProfessor',{state: {value}})
                }
            }
        }
    }

    return (
        <div className="inputWrapper">
            <Button onClick={changeMode} variant="contained" color="primary" size="small" style={{backgroundColor: 'white', color: 'black'}}>
                <AutorenewIcon />
            </Button>
            <input placeholder={barMsg}
                value={userInput}
                onChange={(e) => handleChange(e.target.value)}
                onKeyDown={(e) => handleEnter(userInput, e)}>
            </input>
            <FaSearch id="searchIcon" />
        </div>
    )
}