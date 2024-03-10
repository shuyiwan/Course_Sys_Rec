import React from 'react';
import pencil_icon from "../assets/NoBkgrndPencilIcon.png";
import '../Styles/CourseCart.css'; 
import RMPresult from './RMPresult';

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
    console.log(props.course)
    return (
        <div className="cart-item" key={props.id}>
            <button className="remove-item" onClick={() => props.removeItem(props.id)}>Remove</button>
            <h2>{props.course.courseID}</h2>
            <p>{props.course.description}</p>
            <RMPresult RMPinfo={props.course.rmf}></RMPresult>
            <div className="cart-note">
                <textarea className="hidden" name="Notes" id={"note_" + props.id}></textarea>
                <div className="cart-note-button" onClick={() => getNote("note_" + props.id)}>
                    <p>Note</p>
                    <img src={pencil_icon} alt="notes" />
                </div>
            </div>
        </div>
    );
}