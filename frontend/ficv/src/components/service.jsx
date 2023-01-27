import * as React from 'react';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
export default function Service({img_src}) {
  console.log(typeof img_src)
  return (
    <Card sx={{ maxWidth: 345 }}>
      <CardMedia
        sx = {{ height: 225 }}
        image= {img_src}
        alt = "Cannot load image"
        title="Fish Classification Service"
      />
      <CardContent>
        <Typography gutterBottom variant="h5" component="div">
          What is this fish?
        </Typography>
        <Typography variant="body2" color="text.secondary">
          Our fish classification service ....
        </Typography>
      </CardContent>
      <CardActions>
        <Button size="small">Get Started</Button>
      </CardActions>
    </Card>
  );
}