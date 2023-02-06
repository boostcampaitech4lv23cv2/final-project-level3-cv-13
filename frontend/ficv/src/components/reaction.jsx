import Button from "@mui/material/Button";
import React from "react";
import SentimentVeryDissatisfiedIcon from "@mui/icons-material/SentimentVeryDissatisfied";
import SentimentVerySatisfiedIcon from "@mui/icons-material/SentimentVerySatisfied";
import { Box, Typography } from "@mui/material";

export default function ReactionButton({label, answered, setanswered}) {

  if (answered === false && label!=null) {
    return (
      <>
        <Box
          display="flex"
          justifyContent="center"
          alignItems="center"
          marginBottom={2}
        >
          <Typography>결과에 만족하시나요?</Typography>
        </Box>
        <Box display="flex" justifyContent="center" alignItems="center">
          <Button
            sx={{
              maxWidth: "40px",
              maxHeight: "40px",
              minWidth: "40px",
              minHeight: "40px",
              borderRadius: 30,
              marginLeft: 1,
            }}
            onClick={(event) => {
              try {
                fetch(
                  `https://fast-api-backend-nzhkc6v44a-du.a.run.app/reaction/?q=${encodeURIComponent(label[2])}&q=0`,
                  {
                    method: "GET",
                  }
                ); 
                setanswered(true);
              } catch (err) {
                console.log("Error >>", err);
              }
            }}
          >
            <SentimentVerySatisfiedIcon
              fontSize="large"
              color="error"
            ></SentimentVerySatisfiedIcon>
          </Button>
          <Button
            sx={{
              maxWidth: "40px",
              maxHeight: "40px",
              minWidth: "40px",
              minHeight: "40px",
              borderRadius: 30,
              marginLeft: 1,
            }}
            onClick={(event) => {
              try {
                fetch(
                  `https://fast-api-backend-nzhkc6v44a-du.a.run.app/reaction/?q=${encodeURIComponent(label[2])}&q=2`,
                  {
                    method: "GET",
                  }
                )
                setanswered(true);
              } catch (err) {
                console.log("Error >>", err);
              }
            }}
          >
            <SentimentVeryDissatisfiedIcon
              fontSize="large"
              color="success"
            ></SentimentVeryDissatisfiedIcon>
          </Button>
        </Box>
      </>
    );
  } else if (answered === true) {
    return (
      <Box display="flex" justifyContent="center" alignItems="center">
        <Typography>대답해 주셔서 감사합니다!</Typography>
      </Box>
    );
  }
  return <Box></Box>;
}
