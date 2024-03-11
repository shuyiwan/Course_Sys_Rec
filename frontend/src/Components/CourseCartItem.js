import React from 'react';
import pencil_icon from "../assets/NoBkgrndPencilIcon.png";
import '../Styles/CourseCart.css'; 
import RMPresult from './RMPresult';
import YoutubeRecommend from './YoutubeRecommend.js';
import GradeDistribution from "./GradeDistribution.js";
import '../Styles/SearchPageResult.css';

export default function CourseCartItem( props ) {

    function getNote(id) {
        let _docNote = document.getElementById(id);
        console.log("I got here", _docNote);
        if (_docNote.classList.contains("show")) {
            console.log("Has show");
            _docNote.classList.remove("show");
            _docNote.classList.add("hidden");

        } else if (_docNote.classList.contains("hidden")) {
            console.log("Has hidden");
            _docNote.classList.remove("hidden");
            _docNote.classList.add("show");
        }
    }
    

    return (
        <div className="cart-item" key={props.id}>
            <button className="remove-item" onClick={() => props.removeItem(props.id)}>Remove</button>
            <h2>{props.course.courseID}</h2>
            <p>Description: {props.course.description}</p>
            <br/>
            <p>Instructor: {props.course.instructor}</p>

            {props.course.timeLocations.map((info, id) => (
                <div key={id}>
                    <div>
                        {info.days}
                        {info.beginTime + " - "}
                        {info.endTime}
                        <br/>
                        {info.building + " "}
                        {info.room}
                    </div>
                </div>
            ))}
            
            <RMPresult RMPinfo={props.course.rmf}></RMPresult>
            <GradeDistribution grades = {props.course.grades}/>
            <YoutubeRecommend description={props.course.description} updateVideoData={props.updateVideoData} courseID={props.course.courseID}></YoutubeRecommend>
            <div className="cart-note">
                <textarea className="hidden" name="Notes" id={"note_" + props.id}></textarea>
                <div className="cart-note-button" onClick={() => getNote("note_" + props.id)}>
                    <p>Note</p>
                    {/* <img src={pencil_icon} alt="notes" /> */}
                </div>
            </div>
        </div>
    );
}