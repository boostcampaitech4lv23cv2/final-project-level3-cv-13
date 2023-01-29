import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import reportWebVitals from "./reportWebVitals";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { green, grey } from "@mui/material/colors";
import { createTheme, ThemeProvider } from "@mui/material/styles";
import Fish from "./Fish";
import Sashimi from "./Sashimi";
import AboutUs from "./AboutUs";

const root = ReactDOM.createRoot(document.getElementById("root"));

const theme = createTheme({
  Typography: {
    h1: {
      color: green[500],
    },
  },
  palette: {
    text: {
      primary: "#173A5E",
      secondary: grey[400],
    },
  },
});

root.render(
  <React.StrictMode>
    <ThemeProvider theme={theme}>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<App />} />
          <Route path="/fish" element={<Fish />} />
          <Route path="/sashimi" element={<Sashimi />} />
          <Route path="/about_us" element={<AboutUs />} />
        </Routes>
      </BrowserRouter>
    </ThemeProvider>
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
