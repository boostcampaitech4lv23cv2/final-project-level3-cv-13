## api 구성
from fastapi import FastAPI, UploadFile, File
from fastapi.param_functions import Depends
from pydantic import BaseModel, Field
from typing import List, Union, Optional, Dict, Any
from app.inference import Inference
from PIL import Image
import io
import numpy as np
import albumentations
import time

RESIZE=(512,512)

app=FastAPI()

@app.on_event("startup") 
def init():
    global model
    model=Inference()

@app.post("/inference")
async def inference(files: UploadFile=File(...)) -> int:
    image= await files.read()
    data = transform(image)
    label= model.run(data)
    return label

def transform(image):
    aug = albumentations.Compose([
            albumentations.Resize(height=RESIZE[0], width=RESIZE[1])
        ])
    image = Image.open(io.BytesIO(image))
    image=np.array(image)
    image=aug(image=image)['image']
    image=np.transpose(image,axes=[2,0,1])/255
    image=np.expand_dims(image,0)
    image=image.astype(np.float32)
    return image