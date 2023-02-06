import { AppBar, Toolbar, IconButton, Typography } from "@mui/material";
import MenuIcon from "@mui/icons-material/Menu";
import React from "react";
import { ReactComponent as Fishicon} from "../images/fish.svg"
import { useTheme } from '@mui/material/styles';
import { useNavigate } from "react-router-dom";
export default function Appbar(props) {
  const theme = useTheme();
  const handleDrawerToggle = () => {
    props.setMobileOpen(!props.mobileOpen);
  };
  const movePage = useNavigate();
  return (
    <AppBar position="fixed"  sx={{zIndex: 1300, "backgroundImage": `linear-gradient(to right, ${theme.palette.primary.main}, ${theme.palette.secondary.main})`}}>
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
        <Fishicon onClick={(e) => movePage("/")}></Fishicon>
        <Typography variant="h6" noWrap component="div" onClick={(e) => movePage("/")}>
            FICV
        </Typography>
      </Toolbar>
    </AppBar>
  );
}
