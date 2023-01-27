import { Card, CardMedia, Typography } from "@mui/material";


export default function Image({children}) {
  return (
    <>
      <Card sx={{maxWidth:800}}>
        <CardMedia sx={{height:500,maxWidth:800}} image={URL.createObjectURL(children)}>

        </CardMedia>
        <Typography variant="subtitle1" sx={{"textAlign":'center'}} color="text.secondary">Your Image</Typography> 
      </Card>
      <br/>
    </>
  );
}
