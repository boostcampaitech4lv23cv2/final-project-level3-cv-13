import { useState } from "react";
import Button from "@mui/material/Button";
import React from 'react';
import ImageIcon from '@mui/icons-material/Image';

export default function UploadImageButton({ onChange }) {
    const [label, setlabel] = useState(null);
    return (
      <>
        <Button variant="contained" component="label">
          <ImageIcon></ImageIcon>
            Upload File
          <input
            accept=".jpg, .jpeg, .png"
            type="file"
            onChange={async (event) => {
              onChange(event.target.files[0]);
              const formData = new FormData();
              formData.append("files", event.target.files[0]);
              try {
                const response = await fetch("https://fast-api-backend-nzhkc6v44a-du.a.run.app/inference", {
                  method: "POST",
                  cache: "no-cache",
                  body: formData,
                });
                setlabel(await response.json());
              } catch (err) {
                console.log("Error >>", err);
              }
            }}
            hidden
          />
        </Button>
        <h3  style={{"textAlign":"center"}}>{label}</h3>
      </>
    );
  }