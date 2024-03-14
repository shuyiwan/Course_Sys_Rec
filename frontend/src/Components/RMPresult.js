import React, {useState} from "react";
import '../Styles/SearchPageResult.css';
import ProfTag from "./ProfTag";
import Button from '@mui/material/Button';
import PsychologyAltIcon from '@mui/icons-material/PsychologyAlt';

export default function RMPresult({RMPinfo}) {
    const [showRate, setShowRate] = useState(false);
    
    //console.log(RMPinfo)

    function showRMP() {
        if(showRate === false)
         setShowRate(true)
        else 
         setShowRate(false)
    }
    
    if(RMPinfo === "could not find this professor"){
        return (
            <div>
                {/* need someone to work one the css for RMF button */}
                <Button variant="outlined" onClick={showRMP} endIcon={<PsychologyAltIcon fontSize="small"/>}size="small" color="inherit" style={{color: 'black'}}>
                    Rate My Professor
                </Button>
                    
                <div className = {showRate ? "RMP_show" : "RMP_notshow"}>
                    Professor Not Found
                </div> 
            </div> 
        );
    }
    
    else{
        return (
            <div>
                {/* need someone to work one the css for RMF button */}
                <Button variant="outlined" onClick={showRMP} endIcon={<PsychologyAltIcon fontSize="small"/>}size="small" color="inherit" style={{color: 'black'}}>
                    Rate My Professor
                </Button>
                    
                <div className = {showRate ? "RMP_show" : "RMP_notshow"}>
                    {RMPinfo.map((prof, id) => (
                        <div key={id}>
                            <h2>{prof.fullname}</h2>
                            <p>Department: {prof.department}</p>
                            <p>Diffculty: {prof.difficulty}</p>
                            <p>Number of ratings: {prof.num_ratings}</p>
                            <p>Rating: {prof.rating}</p>
                            <p>Would take again: {prof.would_take_again}</p>
                            <br/>
                            <p>Professor tags:</p>
                            <ProfTag Tags = {prof.tags}/>
                        </div>
                    ))} 
                    
                    
                </div> 
            </div> 
        );
    }
   
}


