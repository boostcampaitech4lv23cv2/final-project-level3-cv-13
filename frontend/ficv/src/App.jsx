import React from "react";
import MainDesc from "./components/main_desc";
import Service from "./components/service";
import fish_service from "./images/fish_classification_icon.png";
import sashimi_service from "./images/sashimi_classification_icon.png";
import { Stack } from "@mui/system";
import { Divider} from "@mui/material";

import BigTitle from "./components/title";
import BasicBar from "./components/bars";

export default function App() {
  return (
    <BasicBar>
      <BigTitle>FICV</BigTitle>
      <MainDesc>This part is description of project!</MainDesc>
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
          desc_title="What is this fish?"
          link = "/fish"
        ></Service>
        <Service
          img_src={sashimi_service}
          desc_title="What is this Sashimi?"
          link = "/sashimi"
        ></Service>
      </Stack>
    </BasicBar>
  );
}
