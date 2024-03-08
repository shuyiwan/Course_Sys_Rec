import React, { useState, useEffect } from 'react';
import { searchYouTubeVideos } from './youtube_api'; // Adjust the path accordingly

import axios from 'axios';

// Replace 'YOUR_YOUTUBE_API_KEY' with your actual YouTube Data API key
const API_KEY = process.env.youtube_api_key;

// Function to search for videos using the YouTube API
export const searchYouTubeVideos = async (query) => {
  try {
    const response = await axios.get('https://www.googleapis.com/youtube/v3/search', {
      params: {
        part: 'snippet',
        q: query,
        type: 'video',
        key: API_KEY,
      },
    });

    return response.data.items;
  } catch (error) {
    console.error('Error searching YouTube videos:', error);
    return [];
  }
};

export const YoutubeResults = ({ query }) => {
  const [youtubeResults, setYoutubeResults] = useState([]);

  useEffect(() => {
    const searchYouTube = async () => {
      const videos = await searchYouTubeVideos(query);
      setYoutubeResults(videos);
    };

    searchYouTube();
  }, [query]);

  return (
    <div>
      {youtubeResults.map((video) => (
        <div key={video.id.videoId}>
          <a href={`https://www.youtube.com/watch?v=${video.id.videoId}`} target="_blank" rel="noopener noreferrer">
            {video.snippet.title}
          </a>
        </div>
      ))}
    </div>
  );
};
