import UploadImageButton from "./components/uploadImageButton";
import { green, grey } from "@mui/material/colors";
import { createTheme, ThemeProvider } from "@mui/material/styles";
import Image from "./components/displayImage";
import { useState } from "react";
import React from "react";
import MainDesc from "./components/main_desc";
import Service from "./components/service";
import fish_service from "./images/fish_classification_icon.png";
import sashimi_service from "./images/sashimi_classification_icon.png";
import { Stack } from "@mui/system";
import { Divider, Box, Toolbar ,Typography} from "@mui/material";
import SideBar from "./components/sidebar";
import Appbar from "./components/appbar";
import BigTitle from "components/title";

const drawerWidth = 180;

export default function App() {
  const [selectedImage, setSelectedImage] = useState(new Blob());
  const [label, setlabel] = useState(null)
  const theme = createTheme({
    Typography: {
      h1: {
        color: green[500],
      },
    },
    palette: {
      text: {
        primary: "#173A5E",
        secondary: grey[400],
      },
    },
  });

  return (
    <Box sx={{ display: "flex" }}>
      <SideBar></SideBar>
      <Appbar></Appbar>
      <ThemeProvider theme={theme}>
        <Box
          component="main"
          sx={{
            flexGrow: 1,
            p: 3,
            width: { sm: `calc(100% - ${drawerWidth}px)` },
          }}
        >
          <Toolbar/>
          <BigTitle>FICV</BigTitle>
          <MainDesc>This part is description of project!</MainDesc>
          <Image>{selectedImage}</Image>
          <UploadImageButton onChange={setSelectedImage} inference= {setlabel}></UploadImageButton>
          <Typography display="flex" justifyContent="center" alignItems="center" variant="h5">{"Label: " + label}</Typography>
          <Stack
            direction="row"
            divider={<Divider orientation="vertical" flexItem />}
            style={{
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
            }}
            spacing={4}
          >
            <Service img_src={fish_service} desc_title = "What is this fish?"></Service>
            <Service img_src={sashimi_service} desc_title = "What is this Sashimi?"></Service>
          </Stack>
        </Box>
      </ThemeProvider>
    </Box>
  );
}
