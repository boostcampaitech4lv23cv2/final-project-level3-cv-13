import UploadImageButton from "./components/uploadImageButton";
import BigTitle from "./components/title";
import { green,grey } from "@mui/material/colors";
import { createTheme, ThemeProvider } from "@mui/material/styles";
import Image from "./components/displayImage";
import { Fragment, useState } from "react";
import React from 'react';
import MainDesc from "./components/main_desc"
import Service from "./components/service"
import fish_service from "./images/fish_classification_icon.png"

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
        <MainDesc>This part is description of project!</MainDesc>
        <Image>{selectedImage}</Image>
        <UploadImageButton onChange={setSelectedImage}></UploadImageButton>
        <Service img_src = {fish_service}></Service>
      </ThemeProvider>
    </>
  );
}
