import { AppBar, Toolbar, IconButton, Typography } from "@mui/material";
import MenuIcon from "@mui/icons-material/Menu";
import React from "react";

export default function Appbar(props) {
  const handleDrawerToggle = () => {
    props.setMobileOpen(!props.mobileOpen);
  };
  return (
    <AppBar position="fixed" sx={{zIndex:4000}}>
      <Toolbar>
        <IconButton
          color="inherit"
          aria-label="open drawer"
          edge="start"
          onClick={handleDrawerToggle}
          sx={{ mr: 2, display: { sm: "none" } }}
        >
          <MenuIcon />
        </IconButton>
        <Typography variant="h6" noWrap component="div">
          FICV
        </Typography>
      </Toolbar>
    </AppBar>
  );
}
