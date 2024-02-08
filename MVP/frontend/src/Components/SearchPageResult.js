import React from "react"
import '../Styles/SearchPageResult.css'

export default function SearchPageResult({result}){

    return (
        <div className="SearchPageResult">
            
            <p>{result.courseID}</p>
            <br />
            <p>{result.title}</p>
            <br />
            <p>Description: {result.description}</p>
            <br />
            <p>Instructor: {result.instructor}</p>
        </div>
    )
}