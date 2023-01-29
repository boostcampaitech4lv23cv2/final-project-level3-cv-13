import BasicBar from "./components/bars";
import { useState } from "react";
import UploadImageButton from "./components/uploadImageButton";
import Image from "./components/displayImage";
import { Typography } from "@mui/material";
export default function Sashimi() {
  const [selectedImage, setSelectedImage] = useState(new Blob());
  const [label, setlabel] = useState(null);
  return (
    <BasicBar>
      <Image>{selectedImage}</Image>
      <UploadImageButton onChange={setSelectedImage} inference={setlabel} />
      <Typography
        display="flex"
        justifyContent="center"
        alignItems="center"
        variant="h5"
      >
        {"Label: " + label}
      </Typography>
    </BasicBar>
  );
}
