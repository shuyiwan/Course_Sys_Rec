import React from "react";
import Button from '@mui/material/Button';

export default function ProfTag({Tags}) {
    
    
    return (
        <div style={{ display: 'flex', flexWrap: 'wrap', gap: '10px', marginTop: '4px'}}>
            {Tags.map((tag, tagId) => (
                <Button key={tagId} size = 'small' variant="contained" color="inherit" style={{ marginBottom: '10px', backgroundColor: 'lightgrey', color: 'black'}}>
                    {tag}
                </Button>
            ))}
        </div>
    );
    
   
}


