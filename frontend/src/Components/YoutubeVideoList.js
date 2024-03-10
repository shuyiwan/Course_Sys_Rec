import "../Styles/YoutubeVideo.css";

export default function YoutubeVideoList( {videos, currentCourse}) {
    return (
      <div className="container">
        <p>Recommended Videos for {currentCourse}</p>
        {videos.map((video) => (
        <div key={video.id.videoId} className="item">
          <a href={`https://www.youtube.com/watch?v=${video.id.videoId}`} target="_blank" rel="noopener noreferrer">
            <img src={video.snippet.thumbnails.high.url} alt={video.snippet.title} title={video.snippet.title}/>
          </a>
        </div>
        ))}
      </div>
    );
}
