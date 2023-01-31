import * as React from "react";
import Card from "@mui/material/Card";
import CardActions from "@mui/material/CardActions";
import CardContent from "@mui/material/CardContent";
import CardMedia from "@mui/material/CardMedia";
import Button from "@mui/material/Button";
import Typography from "@mui/material/Typography";
import { Paper } from "@mui/material";
import { useNavigate } from "react-router-dom";
export default function Service({ img_src, desc_title, desc, link}) {
  const movePage = useNavigate();
  return (
    <Paper elevation={6} sx={{ maxWidth: 345 }}>
      <Card sx={{ maxWidth: 345 }}>
        <CardMedia
          sx={{ height: 345}}
          image={img_src}
          alt="Cannot load image"
          title="Fish Classification Service"

        />
        <CardContent>
          <Typography gutterBottom variant="h5" component="div">
            {desc_title}
          </Typography>
          <Typography variant="body2" color="text.secondary">
            {desc}
          </Typography>
        </CardContent>
        <CardActions>
          <Button size="small" onClick={(e)=> movePage(link)}>Get Started</Button>
        </CardActions>
      </Card>
    </Paper>
  );
}
