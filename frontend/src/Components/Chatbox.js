import React, { useState } from 'react';
import '../Styles/Chatbox.css';

function Chatbox( message ) {
  // Initialize state to store GPT message
//   const [gptMessage, setGptMessage] = useState('');

//   setGptMessage(message);
  console.log(123123);

  return (
    <div className="chat-bubble">
      <p>{message}</p>
    </div>
  );
}

export default Chatbox;
