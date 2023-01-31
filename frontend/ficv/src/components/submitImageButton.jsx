import Button from "@mui/material/Button";
import React from "react";
import ImageIcon from "@mui/icons-material/Image";
import { Typography } from "@mui/material";

export default function SubmitImageButton({image,inference,link }) {
  return (
    <div
      style={{
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        padding: 20,
      }}
    >
      <Button
        variant="contained"
        component="label"
        
        onClick={async (event) => {
          const formData = new FormData();
          formData.append("files", image);
          try {
            const response = await fetch(
              link,
              {
                method: "POST",
                cache: "no-cache",
                body: formData,
              }
            );
            inference(await response.json());
          } catch (err) {
            console.log("Error >>", err);
          }
        }}
      >
        <ImageIcon></ImageIcon>
        <Typography sx={{marginTop:0.4}}>  Submit Image!</Typography>
      </Button>
    </div>
  );
}
