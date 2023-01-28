import React from "react";
import "@fontsource/roboto/500.css";
import { Typography , Box} from "@mui/material";

export default function BigTitle({ children }) {
  return (
    <Box display="flex" justifyContent="center" alignItems="center">
          <Typography
      variant="h1"
      color={"text.primary"}
      
    >
      {children}
    </Typography>
    </Box>

  );
}
