import React from "react"
import "../Styles/SearchPageList.css"
import SearchPageResult from "./SearchPageResult.js"

export default function SearchPageList({results}){
    
    return (
        <div className="SearchPageList">
        {results.map((result, id) => {
          return <SearchPageResult result={result} key={id} />;
        })}
        </div>
    )
}