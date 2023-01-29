import BasicBar from "./components/bars";
import { useState } from "react";
import UploadImageButton from "./components/uploadImageButton";
import { Typography } from "@mui/material";
import Image from "./components/displayImage";
export default function Fish() {
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
