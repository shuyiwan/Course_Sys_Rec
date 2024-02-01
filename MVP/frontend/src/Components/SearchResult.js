import React from "react"
import '../Styles/SearchResult.css'

export default function SearchResult({result}){
    return (
        <div className="searchResult" onClick={(e) => alert('Click on ' + result.name)}>{result.name}</div>
    )
}