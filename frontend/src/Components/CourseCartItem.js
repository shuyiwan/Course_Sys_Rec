import React from 'react';
import '../Styles/CourseCart.css'; 
import RMPresult from './RMPresult';
import YoutubeRecommend from './YoutubeRecommend.js';
import GradeDistribution from "./GradeDistribution.js";
import '../Styles/SearchPageResult.css';
import NoteBox from './NoteBox.js';
import TimeLocation from "./TimeLocation.js";

export default function CourseCartItem( props ) {

    return (
        <div className="cart-item" key={props.id}>
            <button className="remove-item" onClick={() => props.removeItem(props.id)}>Remove</button>
            <h2>{props.course.courseID}</h2>
            <p>Description: {props.course.description}</p>
            <br/>
            <p>Instructor: {props.course.instructor}</p>

            <TimeLocation timeLocations={props.course.timeLocations} />
            <RMPresult RMPinfo={props.course.rmf}></RMPresult>
            <GradeDistribution grades = {props.course.grades}/>
            <br/>
            <NoteBox course={props.course}></NoteBox>
            <YoutubeRecommend description={props.course.description} updateVideoData={props.updateVideoData} courseID={props.course.courseID}></YoutubeRecommend>
            
        </div>
    );
}