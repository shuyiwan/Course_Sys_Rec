

export default function YoutubeVideoList( {videos} ) {
    return (
        <div>
          {videos.map((video) => (
            <div key={video.id.videoId}>
              <a href={`https://www.youtube.com/watch?v=${video.id.videoId}`} target="_blank" rel="noopener noreferrer">
                <img src={video.snippet.thumbnails.high.url} alt={video.snippet.title} title={video.snippet.title}/>
                {/* {video.snippet.title} */}
              </a>
            </div>
          ))}
        </div>
      );
}
