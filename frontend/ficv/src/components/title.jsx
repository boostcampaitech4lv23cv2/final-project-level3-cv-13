import React from "react";
import "@fontsource/roboto/500.css";
import { Typography } from "@mui/material";

export default function BigTitle({ children }) {
  return (
    <Typography
      variant="h1"
      color={"text.primary"}
      
    >
      {children}
    </Typography>
  );
}
