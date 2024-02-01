import React from "react"
import "../Styles/SearchBar.css"
import "../Styles/SearchResultList.css"
import SearchPageResult from "./SearchPageResult.js"

export default function SearchPageList({results}){
    
    return (
        <div className="resultList">
        {results.map((result, id) => {
          return <SearchPageResult result={result} key={id} />;
        })}
        </div>
    )
}