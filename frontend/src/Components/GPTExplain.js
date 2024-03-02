import OpenAI from "openai";
import React, { useState } from 'react';
import Chatbox from "./Chatbox.js";
import '../Styles/Chatbox.css';

const GPTExplain = ( input ) => async () =>{
    const openai = new OpenAI({ apiKey: process.env.REACT_APP_OPENAI_API_KEY, 
                                dangerouslyAllowBrowser: true }); 

    const chatCompletion = await openai.chat.completions.create({
        model: "gpt-3.5-turbo",
        messages: [{"role": "system", "content": "You are an assistant to explain given description."},
        {"role": "user", "content": "I want to know more about this course." + input}],
        max_tokens: 10,
    });


    // const message = chatCompletion.choices[0].message.content;
    // Chatbox(message);
    console.log(chatCompletion.choices[0].message.content);
    
};

export default GPTExplain;