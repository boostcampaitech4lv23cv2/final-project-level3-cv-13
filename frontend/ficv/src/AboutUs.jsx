import React from "react";
import MainDesc from "./components/main_desc";
import OutService from "./components/out_service";
import { Stack } from "@mui/system";
import { Divider} from "@mui/material";
import notion from "./images/instagram_profile_image.png"
import github from "./images/github3.png"
import {SmallTitle} from "./components/title";
import BasicBar from "./components/bars";


export default function AboutUs(){
    return <BasicBar>
        <SmallTitle>부스트캠프 AI Tech 4기 최종프로젝트</SmallTitle>
        <br/>
      <MainDesc>CV-13조 📞031</MainDesc>
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
        <OutService
          img_src={notion}
          desc_title="Notion page"
          desc = "진행과정 및 진행방식에 대해 정리되어있습니다."
          link = "https://github.com/boostcampaitech4lv23cv2/final-project-level3-cv-13"
        ></OutService>
        <OutService
          img_src={github}
          desc_title="Git Repository"
          desc = "개발 프로세스에 대한 모든 기록이 담겨 있습니다."
          link = "https://github.com/boostcampaitech4lv23cv2/final-project-level3-cv-13"
        ></OutService>
      </Stack>
        </BasicBar>
}