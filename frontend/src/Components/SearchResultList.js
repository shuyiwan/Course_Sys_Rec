import React from "react"
import "../Styles/SearchResultList.css"
import SearchResult from "./SearchResult.js"
import Chatbox from "./Chatbox.js"

export default function SearchResultList({results}){
    
    return (
        <div className="resultList">
        {results.map((result, ID) => {
          return <SearchResult result={result} key={ID} />;
        })}
        {/* <Chatbox /> */}
        </div>
    )
}