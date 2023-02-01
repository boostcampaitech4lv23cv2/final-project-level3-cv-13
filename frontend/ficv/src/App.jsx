import React from "react";
import MainDesc from "./components/main_desc";
import {Desc} from "./components/main_desc";
import Service from "./components/service";
import fish_service from "./images/fish.png";
import sashimi_service from "./images/sashimi.png";
import { Stack } from "@mui/system";
import { Divider} from "@mui/material";

import {BigTitle} from "./components/title";
import BasicBar from "./components/bars";

export default function App() {
  return (
    <BasicBar>
      <BigTitle>FICV</BigTitle>
      <MainDesc>저희들이 제공하는 서비스는 다음과 같은 분들이 사용하면 좋습니다!</MainDesc>
      <Desc>1. 구입한 물고기가 명시된 이름과 같은 종인지 궁금한 경우</Desc>
      <Desc>2. 구입한 회가 명시된 이름과 같은 종인지 궁금한 경우</Desc>
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
          desc = "Our fish classification service provides up to 11 species fish classification"
          link = "/fish"
        ></Service>
        <Service
          img_src={sashimi_service}
          desc_title="회 분류 서비스"
          desc = "Our Sashimi classification service provides up to 8 species fish classification"
          link = "/sashimi"
        ></Service>
      </Stack>
    </BasicBar>
  );
}