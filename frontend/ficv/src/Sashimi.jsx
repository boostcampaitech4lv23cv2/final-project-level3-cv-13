import BasicBar from "./components/bars";
import { useState } from "react";
import SubmitImageButton from "./components/submitImageButton";
import { Typography } from "@mui/material";
import Image from "./components/displayImage";
import  {SmallTitle} from "./components/title";
import { DescWhite,MainDescWhite } from "./components/main_desc";
import Box from "@mui/material/Box";
import { useTheme } from "@mui/material/styles";
export default function Fish() {
  const theme = useTheme();
  const [selectedImage, setSelectedImage] = useState(null);
  const [label, setlabel] = useState(null);
  const num2str = ["광어", "우럭", "참돔", "민어", "점성어","틸라피아", "연어", "참치", "방어"]
  return (
    <BasicBar>
      <SmallTitle>회 분류 서비스</SmallTitle>
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
      <Box display="flex" justifyContent="center" alignItems="center">
        <Box
          padding={5}
          style={{
            "background-image": `linear-gradient(to bottom right, ${theme.palette.primary.main}, ${theme.palette.secondary.main})`,
            borderRadius: '20px',
          }}
        >
          <MainDescWhite>분류 가능한 회 종류</MainDescWhite>
          <DescWhite>광어, 우럭, 참돔, 민어, 점성어, 탈라피아, 연어, 참치, 방어</DescWhite>
        </Box>
      </Box>
      
    </BasicBar>
  );
}
