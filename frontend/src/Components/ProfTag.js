import React from "react";

export default function ProfTag({Tags}) {
    
    if(Tags === "could not find tags for this professor"){
        return (
            <div>   
                Tags Not Found
            </div> 
        );  
    }

    else{
        return (
            <div>
                {Tags.map((tag, id) => (
                <div key={id} style={{ margin: '5px'}}>
                    {tag}
                </div>
                ))}
            </div>
        );
    }
   
}


