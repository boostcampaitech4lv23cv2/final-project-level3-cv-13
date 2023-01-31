import * as React from "react";
import Card from "@mui/material/Card";
import CardActions from "@mui/material/CardActions";
import CardContent from "@mui/material/CardContent";
import CardMedia from "@mui/material/CardMedia";
import Button from "@mui/material/Button";
import Typography from "@mui/material/Typography";
import { Paper } from "@mui/material";

export default function OutService({ img_src, desc_title, desc, link}) {
  return (
    <Paper elevation={12} sx={{ width: 330 }}>
      <Card sx={{ width: 330 }}>
        <CardMedia
          sx={{ height: 330}}
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
          <Button size="small" onClick={(e)=>{window.open(link)}}>Link</Button>
        </CardActions>
      </Card>
    </Paper>
  );
}
