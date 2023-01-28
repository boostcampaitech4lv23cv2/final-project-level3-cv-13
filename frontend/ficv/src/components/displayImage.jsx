import { Card, CardMedia, Typography, Box,CardContent } from "@mui/material";

export default function Image({ children }) {
  return (
    <Box display="flex" justifyContent="center" alignItems="center">
      <Card sx={{minWidth:400, maxWidth: 1000 }}>
      <Box display="flex" justifyContent="center" alignItems="center">
        <CardMedia  sx={{ height: 400, width: 200 }} image={URL.createObjectURL(children)}></CardMedia>
        </Box>
        <Typography
          variant="subtitle1"
          sx={{ textAlign: "center" }}
          color="text.secondary"
        >
          Your Image
        </Typography>
      </Card>
    </Box>
  );
}
