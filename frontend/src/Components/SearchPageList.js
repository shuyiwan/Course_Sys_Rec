import React, {useEffect, useState} from "react";
import "../Styles/SearchPageList.css"
import SearchPageResult from "./SearchPageResult.js"
import Filter from "./Filter.js";

export default function SearchPageList({results}){
    //console.log(results)
    const [subjectCodes, setSubjectCodes] = useState([...new Set(results.map((courses) => courses.subject_code))]);
    const [searchResult, setSearchResult] = useState(results);
    useEffect(()=> {
      // console.log(searchResult)
      // console.log(subjectCodes)
    },[])
    return (
        <div className="SearchPageList">
        <Filter subjectCodes = {subjectCodes} setSubjectCodes = {setSubjectCodes} 
                courses={searchResult} setCourses={setSearchResult}/>

        {searchResult.map((result, ID) => {
          return <SearchPageResult result={result} key={ID} />;
        })}
        </div>
    )
}