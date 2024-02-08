import SearchBar from '../Components/SearchBar'
import React, {useState} from "react"
import SearchResultList from '../Components/SearchResultList'
import "../Styles/Pages.css"

export default function Home(){
      
    const [results, setResult] = useState([])
    return (
        <div>
            <div className='searchBarContainer'>
                <SearchBar setResult={setResult}/>
                <SearchResultList results={results}/> 
            </div>
        </div>

    )
}
