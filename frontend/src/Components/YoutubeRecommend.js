import React, { useState, useEffect } from 'react';
import axios from 'axios';
import OpenAI from "openai";
import YoutubeData from './YoutubeTest.json';

export default function YoutubeRecommend(props) {

    async function GPTKeyword(GPTinput) {
        console.log(GPTinput);
        const openai = new OpenAI({ apiKey: process.env.REACT_APP_OPENAI_API_KEY, 
            dangerouslyAllowBrowser: true }); 

        const chatCompletion = await openai.chat.completions.create({
        model: "gpt-3.5-turbo",
        messages: [{"role": "system", "content": 
        "You are an assistant to recommend a youtube video for the given course description."},
        {"role": "user", "content": 
        "Give me one phrase if I want to preview for the course of given course description" + GPTinput}],
        max_tokens: 15,
        });

        searchYouTubeVideos(chatCompletion.choices[0].message.content); 
    }
   

    const searchYouTubeVideos = async (keywords) => {
        try {
          const response = await axios.get('https://www.googleapis.com/youtube/v3/search', {
            params: {
              part: 'snippet',
              q: keywords,
              type: 'video',
              key: process.env.REACT_APP_YOUTUBE_API_KEY,
            },
          });
          
            props.updateVideoData(response.data.items, props.courseID, true);
        } catch (error) {
          console.error('Error searching YouTube videos:', error);
          props.updateVideoData([], '', false);
        }
      };

    return (
        <div>
            <button onClick={() => GPTKeyword(props.description)}>Youtube</button>
        </div>
    );
    
   
}