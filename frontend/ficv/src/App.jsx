import UploadImageButton  from "./components/uploadImageButton";
import { Fragment, useState } from "react";
import React from 'react';

function App() {
  const [selectedImage, setSelectedImage] = useState(new Blob());
  return (
    <>
      <div>
        <h1>FICV</h1>
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

export default App;
