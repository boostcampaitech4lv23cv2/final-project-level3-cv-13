import { Card, CardMedia, Typography, Box } from "@mui/material";

export default function Image({ children }) {
  return (
    <Box display="flex" justifyContent="center" alignItems="center">
      <Card sx={{ maxWidth: 500 }}>
        <CardMedia sx={{ height: 300, width: 200 }} image={URL.createObjectURL(children)}></CardMedia>
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
