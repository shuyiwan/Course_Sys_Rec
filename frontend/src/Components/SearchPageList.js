import React from "react"
import "../Styles/SearchPageList.css"
import SearchPageResult from "./SearchPageResult.js"

export default function SearchPageList({results}){
    //console.log(results)
    return (
        <div className="SearchPageList">
        {results.map((result, ID) => {
          return <SearchPageResult result={result} key={ID} />;
        })}
        </div>
    )
}