import React, {useState} from "react";
import '../Styles/SearchPageResult.css';

export default function RMPresult({RMPinfo}) {
    const [showRate, setShowRate] = useState(false);
    console.log(RMPinfo)

    function showRMP() {
        console.log(showRate)
        if(showRate == false)
         setShowRate(true)
        else 
         setShowRate(false)
    }
    
    if(RMPinfo === "could not find this professor"){
        return <div>Professor not found</div>
    }

    else{
        return (
            <div>
                {/* need someone to work one the css for RMF button */}
                <button onClick={showRMP}>Rate My Professor</button>
                    
                <div className = {showRate ? "RMP_show" : "RMP_notshow"}>
                    {RMPinfo.map((prof, id) => (
                        <div key={id}>
                            <h2>{prof.fullname}</h2>
                            <p>Department: {prof.department}</p>
                            <p>Diffculty: {prof.difficulty}</p>
                            <p>Number of ratings: {prof.num_ratings}</p>
                            <p>Rating: {prof.rating}</p>
                            <p>Would take again: {prof.would_take_again}</p>
                        </div>
                    ))} 
                </div> 
    
            </div> 
        );
    }
   
}


