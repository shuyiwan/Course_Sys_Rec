import React, {useEffect, useState} from "react";
import '../Styles/SearchPageResult.css';
import Button from '@mui/material/Button';
import ReactEcharts from "echarts-for-react"
import BarChartOutlinedIcon from '@mui/icons-material/BarChartOutlined';

export default function GradeDistribution({grades}) {

    const [showGrade, setShowGrade] = useState(false);
    const [allGrades, setAllGrades] = useState(grades);
    const [option, setOption] = useState({});
    
    //this might be buggy due to the return info from backend
    useEffect(()=> {
        if(grades !== "not found"){
            setAllGrades(grades)
            const newList = allGrades.filter((grade) => {
                return grade.quarter === grades[0].quarter; 
            });
            
            // console.log(newList);
            let chartOption = {
                title:{
                    text: grades[0].quarter,
                },
                
                xAxis: {
                    type: 'category',
                    data: newList.map(function (item) {
                        return item.grade;}),
                },

                yAxis: {
                },

                series: [{
                    type: 'bar',
                    data:newList.map(function (item) {
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
                 <Button variant="outlined" onClick={handleClick} endIcon={<BarChartOutlinedIcon fontSize="small"/>}size="small" color="inherit" style={{color: 'black'}}>Grade Distribution</Button>
                    
                <div className = {showGrade ? "Grade_show" : "Grade_notshow"}>
                    Grades Not Found
                </div> 
            </div> 
        );
    }
    
    else{
        return (
            <div>
                <Button variant="outlined" onClick={handleClick} endIcon={<BarChartOutlinedIcon fontSize="small"/>}size="small" color="inherit" style={{color: 'black'}}>Grade Distribution</Button>
                    
                <div className = {showGrade ? "Grade_show" : "Grade_notshow"}>
                    <ReactEcharts option={option} className="chart"/>
                </div> 
            </div> 
        );
    }
   
}


