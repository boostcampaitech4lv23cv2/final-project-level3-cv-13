import UploadImageButton  from "./components/uploadImageButton";
import { Fragment, useState } from "react";
import React from 'react';
import MainDesc from "./components/main_desc"
import Service from "./components/service"
import fish_service from "./images/fish_classification_icon.png"

export default function App() {
  const [selectedImage, setSelectedImage] = useState(new Blob());
  return (
    <>
      <div>
        <h1>FICV</h1>
        <MainDesc>This part is description of project!</MainDesc>
        <Service img_src = {fish_service}></Service>
        <div>
          <img
            alt=""
            width={"500px"}
            src={URL.createObjectURL(selectedImage)}
          />
          <br />
        </div>
      </div>
      <div>
        <UploadImageButton
          onChange={setSelectedImage}
        ></UploadImageButton>
      </div>
    </>
  );
}
