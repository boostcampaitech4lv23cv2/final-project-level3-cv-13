import React from "react";
import {MainDesc}from "./components/main_desc";
import {Desc} from "./components/main_desc";
import Service from "./components/service";
import fish_service from "./images/fish.png";
import sashimi_service from "./images/sashimi.png";
import { Stack } from "@mui/system";
import { Divider,Typography,Box} from "@mui/material";

import {BigTitle} from "./components/title";
import BasicBar from "./components/bars";


export default function App() {
  return (
    <BasicBar>
      <BigTitle>FICV</BigTitle>
      <br/>
      <br/>

      <MainDesc>저희들이 제공하는 서비스는 다음과 같은 분들이 사용하면 좋습니다!</MainDesc>
      <Desc>1. 구입한 물고기가 명시된 이름과 같은 종인지 궁금한 경우</Desc>
      <Desc>2. 구입한 회가 명시된 이름과 같은 종인지 궁금한 경우</Desc>
      <br/>
      <br/>
      <br/>
      
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
        <Service
          img_src={fish_service}
          desc_title="물고기 분류 서비스"
          desc = "물고기 분류 서비스는 12종의 어종 구별이 가능합니다."
          link = "/fish"
        ></Service>
        <Service
          img_src={sashimi_service}
          desc_title="회 분류 서비스"
          desc = "회 분류 서비스는 현재 8 종류의 회 구별이 가능합니다."
          link = "/sashimi"
        ></Service>
      </Stack>
      <Box>

      <Typography
        display="flex"
        justifyContent="center"
        alignItems="center"
        paddingTop={30}
        color="text.secondary"
      >
       💡 We collect your submission data to ensure you have the best browsing experience on our website and to improve our classification model. <br/>      By using our site, you acknowledge that you have read and understood our Privacy Policy.
      </Typography>
  
      </Box>
    </BasicBar>
  );
}
