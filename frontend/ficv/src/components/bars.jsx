import SideBar from "./sidebar";
import Appbar from "./appbar";
import React from "react";

import { Box, Toolbar } from "@mui/material";
const drawerWidth = 180;
export default function BasicBar({ children }) {
  const [mobileOpen, setMobileOpen] = React.useState(false);
  return (
    <Box sx={{ display: "flex" }}>
      <SideBar mobileOpen={mobileOpen} setMobileOpen={setMobileOpen}></SideBar>
      <Appbar mobileOpen={mobileOpen} setMobileOpen={setMobileOpen}></Appbar>
      <Box
        component="main"
        sx={{
          flexGrow: 1,
          p: 3,
          width: { sm: `calc(100% - ${drawerWidth}px)` },
        }}
      >
        <Toolbar />
        {children}
      </Box>
    </Box>
  );
}
