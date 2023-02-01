import * as React from "react";
import Box from "@mui/material/Box";
import Divider from "@mui/material/Divider";
import Drawer from "@mui/material/Drawer";
import List from "@mui/material/List";
import ListItem from "@mui/material/ListItem";
import ListItemButton from "@mui/material/ListItemButton";
import ListItemIcon from "@mui/material/ListItemIcon";
import ListItemText from "@mui/material/ListItemText";

import Toolbar from "@mui/material/Toolbar";

import home_icon from "../images/home.png";
import fish_icon from "../images/fish.png";
import sashimi_icon from "../images/sashimi.png";
import github_icon from "../images/github.png";
import { useNavigate } from "react-router-dom";

const drawerWidth = 180;

export default function SideBar(props) {
  const { window } = props;
  const movePage = useNavigate();
  const handleDrawerToggle = () => {
    props.setMobileOpen(!props.mobileOpen);
  };
  const icons = [home_icon, fish_icon, sashimi_icon, github_icon];
  const link = ["/", "/fish", "/sashimi", "/about_us"]
  const drawer = (
    <div>
      <Toolbar />
      <Divider />
      <List>
        {["Main", "물고기 분류", "회 분류", "About us"].map((text, index) => (
          <ListItem key={text} disablePadding>
            <ListItemButton onClick={(e)=> movePage(link[index])}>
              <ListItemIcon>
                <img src={icons[index]} alt="" width={24}/>
      
              </ListItemIcon>
              <ListItemText primary={text} />
            </ListItemButton>
          </ListItem>
        ))}
      </List>
    </div>
  );
  const container =
    window !== undefined ? () => window().document.body : undefined;

  return (
    <Box
      component="nav"
      sx={{ width: { sm: drawerWidth }, flexShrink: { sm: 0 } }}
      aria-label="mailbox folders"
    >
      <Drawer
        container={container}
        variant="temporary"
        open={props.mobileOpen}
        onClose={handleDrawerToggle}
        ModalProps={{
          keepMounted: true,
        }}
        sx={{
          display: { xs: "block", sm: "none" },
          "& .MuiDrawer-paper": { boxSizing: "border-box", width: drawerWidth },
        }}
      >
        {drawer}
      </Drawer>
      <Drawer
        variant="permanent"
        sx={{
          display: { xs: "none", sm: "block" },
          "& .MuiDrawer-paper": { boxSizing: "border-box", width: drawerWidth },
        }}
        open
      >
        {drawer}
      </Drawer>
    </Box>
  );
}
