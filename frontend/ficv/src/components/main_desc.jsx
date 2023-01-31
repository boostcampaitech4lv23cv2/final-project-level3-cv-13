import Typography from "@mui/material/Typography";
import React from "react";

export default function MainDesc({ children }) {
  return (
    <>
      <Typography
        variant="h5"
        style={{
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
        }}
      >
        {children}
      </Typography>
      <br />
    </>
  );
}

export function Desc({ children }) {
  return (
    <>
      <Typography
        variant="body1"
        style={{
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
        }}
      >
        {children}
      </Typography>
      <br />
    </>
  );
}
export function MainDescWhite({ children }) {
  return (
    <>
      <Typography
        variant="h5"
        style={{
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
        }}
        color="white"
      >
        {children}
      </Typography>
      <br />
    </>
  );
}

export function DescWhite({ children }) {
  return (
    <>
      <Typography
        variant="body1"
        style={{
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
        }}
        color="white"
      >
        {children}
      </Typography>
      <br />
    </>
  );
}
