import React from "react";

export default function TimeLocation({timeLocations}){
  
    if (timeLocations === "TBD" || Object.keys(timeLocations).length === 0){
        return <div>Time and Location: TBD</div>
    }
    else{
        return(
            timeLocations.map((info, id) => (
                <div key={id}>
                    <div>
                        {info.days}
                        {info.beginTime + " - "}
                        {info.endTime}
                        <br/>
                        {info.building + " "}
                        {info.room}
                    </div>
                </div>)
            )
        )
    }  
}

