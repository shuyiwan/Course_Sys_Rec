import React from "react"
import '../Styles/SearchPageResult.css'

export default function SearchPageResult({result}){
    return (
        <div className="SearchPageResult" onClick={(e) => alert('Click on ' + result.title)}>{result.title}</div>
    )
}