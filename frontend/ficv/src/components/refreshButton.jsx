import Button from "@mui/material/Button";
import React from "react";
import ReplayIcon from '@mui/icons-material/Replay';
export default function RefreshButton() {
  return (
      <Button
      sx={{maxWidth: '20px', maxHeight: '20px', minWidth: '20px', minHeight: '20px',borderRadius:30, marginLeft:1}}
        onClick={async (event) => {
          try {
            const response = await fetch(
              "https://fast-api-backend-nzhkc6v44a-du.a.run.app/refresh",
              {
                method: "GET",
              }
            );
            console.log(response.json());
          } catch (err) {
            console.log("Error >>", err);
          }
        }}
      >
        <ReplayIcon fontSize="small" color="third" ></ReplayIcon>
      </Button>
  );
}
