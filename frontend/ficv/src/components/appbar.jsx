import { AppBar, Toolbar, IconButton, Typography } from "@mui/material";
import MenuIcon from "@mui/icons-material/Menu";
import React from "react";
import { ReactComponent as Fishicon} from "../images/fish.svg"
import { useTheme } from '@mui/material/styles';
export default function Appbar(props) {
  const theme = useTheme();
  const handleDrawerToggle = () => {
    props.setMobileOpen(!props.mobileOpen);
  };
  return (
    <AppBar position="fixed" sx={{ zIndex: 4000 }} style={{ "background-image": `linear-gradient(to right, ${theme.palette.primary.main}, ${theme.palette.secondary.main})`}}>
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
        <Fishicon></Fishicon>
        <Typography variant="h6" noWrap component="div">
            FICV
        </Typography>
      </Toolbar>
    </AppBar>
  );
}
