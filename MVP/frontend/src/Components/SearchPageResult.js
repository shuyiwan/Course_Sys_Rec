import React from "react"
import '../Styles/SearchResult.css'

export default function SearchPageResult({result}){
    return (
        <div className="searchResult" onClick={(e) => alert('Click on ' + result.title)}>{result.title}</div>
    )
}