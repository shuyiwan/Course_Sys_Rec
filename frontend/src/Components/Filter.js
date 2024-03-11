import React, {useState} from "react";
import "../Styles/SearchPageList.css"

export default function Filter ({ courses,setCourses,setSubjectCodes,subjectCodes}){
    const [allCourses, setAllCourses] = useState(courses);
    const [showSubjectCode, setShowSubjectCode] = useState(false);

    const filterItem = (target) => {
        const newList = allCourses.filter((course) => {
            return course.subject_code === target; 
        });
        setCourses(newList);
    };

    const showCodes = () => {
        if(showSubjectCode)
            setShowSubjectCode(false)
        else
            setShowSubjectCode(true)
    };
    
    const showAll = () => {
        setCourses(allCourses);
    };

    return (
        <div className="filter">
            <button className="filter_subjectCode" onClick={()=>showCodes()}>filter</button>

            <div className={showSubjectCode ? "filter_showCodeList" : "filter_notShowCodeList"}>
                {subjectCodes.map((code, id) => {
                    return (
                        <button className="filter_subjectCode" key={id} onClick={()=>filterItem(code)}>
                            {code}
                        </button>
                    );
                })}

                <button className="filter_allButton"onClick={()=>showAll()}>
                    All
                </button>
            </div>
        </div>
    );
};
 