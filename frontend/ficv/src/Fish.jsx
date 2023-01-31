import BasicBar from "./components/bars";
import { useState } from "react";
import SubmitImageButton from "./components/submitImageButton";
import { Typography } from "@mui/material";
import Image from "./components/displayImage";
import  {SmallTitle} from "./components/title";

export default function Fish() {
  const [selectedImage, setSelectedImage] = useState(null);
  const [label, setlabel] = useState(null);
  const num2str = ["광어", "우럭", "참돔", "감성돔", "돌돔","민어", "큰민어", "강도다리", "자바리", "능성어", "방어", "부시리"]
  return (
    <BasicBar>
      <SmallTitle>물고기 분류 서비스</SmallTitle>
      <br/>
      <Image image={selectedImage} setImage={setSelectedImage}></Image>
      <SubmitImageButton image={selectedImage} inference={setlabel} link="https://fast-api-backend-nzhkc6v44a-du.a.run.app/inference"/>
      <Typography
        display="flex"
        justifyContent="center"
        alignItems="center"
        variant="h5"
      >
      { label != null ? <p>예측결과: {num2str[label]}</p> : <p></p>}
      </Typography>
    </BasicBar>
  );
}
