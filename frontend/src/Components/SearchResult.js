import React from "react"
import '../Styles/SearchResult.css'
import {Link} from "react-router-dom"

export default function SearchResult({result}){

    return (
        <div className="searchResult">
            {/* <Link to="/search" style={{ color: 'black'}}> */}
                {result.courseID}
            {/* </Link> */}
        </div>
    )
}