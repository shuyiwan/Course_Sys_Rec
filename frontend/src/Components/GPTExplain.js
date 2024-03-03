import OpenAI from "openai";
import React, { useState } from 'react';
import '../Styles/SearchPageResult.css';
import '../Styles/GPTExplain.css';

export default function GPTExplanation ( {input} ){
    const [courseExp, setCourseExp] = useState('');
    const [active, setActive] = useState(false);

    const GPTExplain = ( GPTinput ) => async () =>{
        const openai = new OpenAI({ apiKey: process.env.REACT_APP_OPENAI_API_KEY, 
                                    dangerouslyAllowBrowser: true }); 
        
        const chatCompletion = await openai.chat.completions.create({
            model: "gpt-3.5-turbo",
            messages: [{"role": "system", "content": "You are an assistant to explain given description in 100 tokens."},
            {"role": "user", "content": 
            "what would be prerequisite and takeaway of the course by the given description: " + GPTinput}],
            max_tokens: 100,
        });
    
        // console.log(chatCompletion.choices[0].message.content);
        setCourseExp(chatCompletion.choices[0].message.content);
    };

    const handleClick = (value) =>{
        GPTExplain(value)();
        setActive(true);
    };

    const handleClose = () => {
        setActive(false);
        setCourseExp('');
    };

    return (active && (!!courseExp)) ? 
    (            
        <div>
            <button className="GPTExplainButton" onClick={(e) => handleClick(input)}>Explain More</button>
            <div className='chat-bubble-show'>
                <button className='closeButton' onClick={handleClose}>✖️</button>
                <div>👽:{courseExp}</div>
            </div>      
        </div>
    ):( 
       <div>
            <button className="GPTExplainButton" onClick={(e) => handleClick(input)}>Explain More</button>      
        </div>     
    );
}
