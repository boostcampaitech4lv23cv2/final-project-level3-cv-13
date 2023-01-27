import UploadImageButton from "./components/uploadImageButton";
import { useState } from "react";
import React from "react";
import BigTitle from "./components/title";
import { green,grey } from "@mui/material/colors";
import { createTheme, ThemeProvider } from "@mui/material/styles";
import Image from "./components/displayImage";

export default function App() {
  const [selectedImage, setSelectedImage] = useState(new Blob());

  const theme = createTheme({
    typography: {
      h1: {
        color: green[500]
      },
    },
    palette: {
      text: {
        primary: '#173A5E',
        secondary: grey[400],
      },
    },
  });

  return (
    <>
      <ThemeProvider theme={theme}>
        <BigTitle>FICV</BigTitle>
        <Image>{selectedImage}</Image>
        <UploadImageButton onChange={setSelectedImage}></UploadImageButton>
      </ThemeProvider>
    </>
  );
}
