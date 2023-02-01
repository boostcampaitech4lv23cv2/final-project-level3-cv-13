import { Card, Typography, Box, CardContent } from "@mui/material";
import { useDropzone } from "react-dropzone";
import React from "react";
import dnd from "../images/drag-and-drop.png";
export default function Image({ image, setImage }) {
  const { getRootProps, getInputProps } = useDropzone({
    onDrop: (files) => setImage(files[0]),
  });
  return (
    <Box display="flex" justifyContent="center" alignItems="center">
      <Card
        {...getRootProps({ className: "dropzone" })}
        sx={{ minWidth: 600, maxWidth: 1000, minHeight: 400 , display: "flex",
        alignItems: "center",
        justifyContent: "center"}}
      >
        <CardContent >
          <input {...getInputProps()} />
          {image != null ? (
            <Box display="flex" justifyContent="center" alignItems="center">
              <img src={URL.createObjectURL(image)} alt="" width={500}></img>
            </Box>
          ) : (
            <>
              <Box display="flex" justifyContent="center" alignItems="center">
                <img src={dnd} alt="" width={256} />
              </Box>
              <br/>
              <Typography
                variant="subtitle1"
                color="text.secondary"
                style={{
                  display: "flex",
                  alignItems: "center",
                  justifyContent: "center",
                }}
              >
                해당 영역을 눌러 예측하고 싶은 파일을 선택하거나 끌어서
                넣어주세요!
              </Typography>
            </>
          )}
        </CardContent>
      </Card>
    </Box>
  );
}
