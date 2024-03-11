import React, {useEffect, useState} from "react";
import '../Styles/SearchPageResult.css';
import echarts from "echarts";
import ReactEcharts from "echarts-for-react"

export default function GradeDistribution({grades}) {

    const [showGrade, setShowGrade] = useState(false);
    const [allGrades, setAllGrades] = useState(grades);
    const [latestQuarter, setlatestQuarter] = useState("");
    const [option, setOption] = useState({});
    
    //this might be buggy due to the return info from backend
    useEffect(()=> {
        if(grades !== "not found"){
            setlatestQuarter(grades[0].quarter)
            const newList = allGrades.filter((grade) => {
                return grade.quarter === latestQuarter; 
            });
            setAllGrades(allGrades);
            console.log(allGrades);
            let chartOption = {
                title:{
                    text: latestQuarter,
                },
                xAxis: {
                    type: 'category',
                    data: allGrades.map(function (item) {
                        return item.grade;}),
                },

                yAxis: {
                },

                series: [{
                    type: 'bar',
                    data:allGrades.map(function (item) {
                        return item.student_count;})
                    }],
                    barWidth: 20,  
            };
            setOption(chartOption);
        }
    },[])

    function handleClick() {
        if(showGrade === false)
            setShowGrade(true)
        else 
            setShowGrade(false)
    }

    if(grades === "not found"){
        return (
            <div>
                <button onClick={()=>handleClick()}>Grade Distribution</button>
                    
                <div className = {showGrade ? "Grade_show" : "Grade_notshow"}>
                    Grades Not Found
                </div> 
            </div> 
        );
    }
    
    else{
        return (
            <div>
                <button onClick={()=>handleClick()}>Grade Distribution</button>
                    
                <div className = {showGrade ? "Grade_show" : "Grade_notshow"}>
                    <ReactEcharts option={option} className="chart"/>
                </div> 
            </div> 
        );
    }
   
}


