import Typography from '@mui/material/Typography'
import React from 'react';

export default function MainDesc({children}) {
    return (
        <>
            <div>
            <Typography variant='h3' align='center'>{children}</Typography>
            </div>
        </>
        
    );
  }