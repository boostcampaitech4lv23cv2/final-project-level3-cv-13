import SideBar from "./sidebar";
import Appbar from "./appbar";

import { Box, Toolbar } from "@mui/material";
const drawerWidth = 180;
export default function BasicBar({ children }) {
  return (
    <Box sx={{ display: "flex" }}>
      <SideBar></SideBar>
      <Appbar></Appbar>
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
