import React from "react";

import { Typography , Box} from "@mui/material";

export function BigTitle({ children }) {
  return (
    <Box display="flex" justifyContent="center" alignItems="center">
          <Typography
      variant="h1"
      color={"text.primary"}
      fontSize={150}
      
    >
      {children}
    </Typography>
    </Box>

  );
}

export function SmallTitle({ children }) {
  return (
    <Box display="flex" justifyContent="center" alignItems="center">
          <Typography
      variant="h3"
      color={"text.primary"}
      
    >
      {children}
    </Typography>
    </Box>

  );
}