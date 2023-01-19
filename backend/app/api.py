## api 구성
from fastapi import FastAPI, UploadFile, File
from app.inference import Inference
from PIL import Image
import io
import numpy as np
import albumentations

RESIZE=(384,384)

app=FastAPI()

@app.on_event("startup") 
def init():
    global model
    model=Inference()

@app.get("/blob_name")
def get_blob_name() -> str:
    return model.blob_name

@app.post("/inference")
async def inference(files: UploadFile=File(...)) -> int:
    image= await files.read()
    image = Image.open(io.BytesIO(image))
    image = image.convert("RGB")
    data = transform(image)
    label= model.run(data)
    log_user_input(image,label)
    return label.argmax()

def transform(image):
    aug = albumentations.Compose([
            albumentations.Resize(height=RESIZE[0], width=RESIZE[1]),
        ])
    image=np.array(image)
    image=aug(image=image)['image']
    image=np.transpose(image,axes=[2,0,1])/255
    image=np.expand_dims(image,0)
    image=image.astype(np.float32)
    return image

def log_user_input(image: Image,label:int):
    pass