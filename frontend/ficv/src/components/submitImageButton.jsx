import Button from "@mui/material/Button";
import React from "react";
import ImageIcon from "@mui/icons-material/Image";
import { Typography } from "@mui/material";
import { useTheme } from '@mui/material/styles';
export default function SubmitImageButton({image,inference,link }) {
  const theme = useTheme();
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
        style={{ "background-image": `linear-gradient(to right, ${theme.palette.primary.main}, ${theme.palette.secondary.main})`}}
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
