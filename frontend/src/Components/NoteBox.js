import React, { useState } from 'react';
import '../Styles/NoteBox.css';

export default function NoteBox( props ) {
    const init_notes = (props.course.notes === null || props.course.notes === " ") ? "" : props.course.notes;
    const [noteText, setNoteText] = useState(init_notes);
    const [editMode, setEditMode] = useState(false);
    const userEmail = localStorage.getItem("email");  
    
    async function addNote(note) {
        const postData = [{
            email: userEmail, 
            courseID: props.course.courseID,
            sql_id: props.course.sql_id,
            notes: (note === "") ? " " : note,
        }];

        try {       
            const response = await fetch('https://intermittence.pythonanywhere.com/shoppingCart/add/', {
                method: 'POST',
                headers: {
                    'Accept': 'application/json, text/plain, */*',
                    'Content-Type': 'application/json',
                },
                credentials: 'include',
                body: JSON.stringify(postData),
            });

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            // console.log("Note added to cart");
        }       
        catch (error) {
            console.error("Failed to add note to cart:", error);
        }
    }

    const handleChange = (event) => {
        setNoteText(event.target.value);
    };
  
    const handleEditClick = () => {
        setEditMode(!editMode);
    };
  
    const handleSaveClick = () => {
        setEditMode(false);
        addNote(noteText);
    };

    const characterCount = noteText.length;
  
    return (
        <div className="note-box">
        {editMode ? (
          <>
            <textarea
              className="note-input"
              placeholder="Enter your note here..."
              value={noteText}
              onChange={handleChange}
              maxLength={500}
            />
            <div className="character-count">Character count: {characterCount}/500</div>
            <button className="edit-save-button" onClick={handleSaveClick}>Save</button>
          </>
        ) : (
          <>
            <p className="saved-note">{noteText}</p>
            <button className="edit-save-button" onClick={handleEditClick}>✏️ Edit Note</button>
          </>
        )}
      </div>
    );
  }
