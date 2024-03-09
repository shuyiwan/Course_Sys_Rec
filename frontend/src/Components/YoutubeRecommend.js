import React, { useState, useEffect } from 'react';
import axios from 'axios';
import OpenAI from "openai";
import '../Styles/YoutubeRecommend.css';
import YoutubeData from './YoutubeTest.json';
import YoutubeVideoList from './YoutubeVideoList.js';

export default function YoutubeRecommend({description}) {

    const [videos, setVideos] = useState([]);

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

        // console.log(chatCompletion.choices[0].message.content);
        // setKeywords(chatCompletion.choices[0].message.content);
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
            // console.log(keywords);
          setVideos(response.data.items);
        } catch (error) {
          console.error('Error searching YouTube videos:', error);
          setVideos([]);
        }
      };

    console.log(videos);

    return (
        <div>
            <button onClick={() => GPTKeyword(description)}>Youtube</button>
            <YoutubeVideoList videos={YoutubeData.items} />
        </div>
    );
    
   
}