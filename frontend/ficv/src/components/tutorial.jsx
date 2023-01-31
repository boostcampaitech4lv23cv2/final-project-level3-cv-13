import { Modal, Box, Typography, Button } from "@mui/material";
import { useState } from "react";
import InfoOutlinedIcon from '@mui/icons-material/InfoOutlined';
import { grey} from "@mui/material/colors";
const drawerWidth = 180;
export default function Tutorial() {
  const [open, setOpen] = useState(false);
  const style = {
    maxWidth: 400,
    bgcolor: 'background.paper',
    border: '1px solid #000',
    boxShadow: 24,
    p: 4,
    flexGrow: 1,
  };
  function handleOpen() {
    setOpen(!open);
  }
  return (
    <>
    <Button onClick={handleOpen} sx={{maxWidth: '30px', maxHeight: '30px', minWidth: '30px', minHeight: '30px',borderRadius:15,marginBottom:1}}>
        <InfoOutlinedIcon></InfoOutlinedIcon>
    </Button>
    <Modal open={open} onClose={handleOpen} sx={{display:"flex", justifyContent:"center", alignItems:"center" }}>
      <Box sx={style} borderRadius={5}>
        <Box>
        <Typography id="modal-modal-title" variant="h4" color="text.primary">
          서비스 사용법
        </Typography>
        <Typography id="modal-modal-description" sx={{ mt: 2 }} variant="h6">
          1. 파일을 업로드 하는 경우
        </Typography>
        <Typography id="modal-modal-description" sx={{ mt: 2 }} color={grey[700]}>
          결과를 얻고 싶은 사물이 이미지 영역의 대부분을 차지하는 이미지를 선택하여 업로드합니다.
        </Typography>
        <Typography id="modal-modal-description" sx={{ mt: 2 }} variant="h6">
          2. 사진을 촬영하는 경우
        </Typography>
        <Typography id="modal-modal-description" sx={{ mt: 2 }}  color={grey[700]}>
          분류할 한 종류의 사물이 사진 영역을 최대한 꽉 채울 수 있도록 촬영한 뒤 업로드합니다.
        </Typography>
        </Box>
      </Box>
    </Modal>
    </>
  );
}
