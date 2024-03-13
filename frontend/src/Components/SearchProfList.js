import React, {useEffect, useState} from "react";
import "../Styles/SearchPageList.css"
import SearchProfResult from "./SearchProfResult.js"
import Filter from "./Filter.js";

export default function SearchProfList({results}){
    //console.log(results)
    const [subjectCodes, setSubjectCodes] = useState([...new Set(results.map((courses) => courses.subject_code))]);
    const [searchResult, setSearchResult] = useState(results);
    //console.log(searchResult)

    return (
        <div>
            <div className="SearchPageList">
            {/* <Filter
            subjectCodes = {subjectCodes} setSubjectCodes = {setSubjectCodes} 
            courses={searchResult} setCourses={setSearchResult}
            /> */}
                            
            {searchResult.map((result) => {
                return <SearchProfResult result={result}/>;
            })}
            </div>
        </div>    
    )   
    
}