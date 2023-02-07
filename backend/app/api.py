## api 구성
from fastapi import FastAPI, UploadFile, File, Form 
from app.inference import Inference, Inference_Sashimi,Logger                               
from PIL import Image
import io
import numpy as np
import albumentations
import secrets
from typing import List
import os
from fastapi.middleware.cors import CORSMiddleware
# from fastapi_cprofile.profiler import CProfileMiddleware

RESIZE=(384,384)

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# app.add_middleware(CProfileMiddleware, enable=True, print_each_request = True, strip_dirs = False, sort_by='time')

@app.on_event("startup") 
def init():
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="google_key.json"
    global model_fish, model_sashimi,logger
    logger=Logger()
    model_fish=Inference(logger.get_logger())
    model_sashimi = Inference_Sashimi(logger.get_logger())

@app.get("/blob_name")
def get_blob_name() -> str:
    return model_fish.blob_name

@app.get("/blob_name_sashimi")
def get_blob_name() -> str:
    return model_sashimi.blob_name

@app.get("/refresh")
def refresh():
    global model_fish, model_sashimi,logger
    model_fish=Inference(logger.get_logger())
    model_sashimi = Inference_Sashimi(logger.get_logger())
    return "Sucess!"

@app.post("/inference")
async def inference(files:UploadFile = File()) -> List[int]:
    image= await files.read()
    image = Image.open(io.BytesIO(image))
    image = image.convert("RGB")
    data = transform(image)
    label= model_fish.run(data)
    softmax_label = softmax(label.tolist())
    model_fish.logger.info(softmax_label)
    label=label.argmax(0)
    prob=int(softmax_label[label]*100)
    log_user_input_fish(image,label,prob)
    return [label, prob]

@app.post("/inference_sashimi")
async def inference_sashimi(files: UploadFile=File()) -> List[int]:
    image= await files.read()
    image = Image.open(io.BytesIO(image))
    image = image.convert("RGB")
    data = transform(image)
    label= model_sashimi.run(data)
    softmax_label = softmax(label.tolist())
    model_sashimi.logger.info(softmax_label)
    label=label.argmax(0)
    prob=int(softmax_label[label]*100)
    log_user_input_sashimi(image,label,prob)
    return [label, prob]

def transform(image):
    aug = albumentations.Compose([
            albumentations.Resize(height=RESIZE[0], width=RESIZE[1]),
            albumentations.Normalize()
        ])
    image=np.array(image)
    image=aug(image=image)['image']
    image=np.transpose(image,axes=[2,0,1])/255
    image=np.expand_dims(image,0)
    image=image.astype(np.float32)
    return image
##User data save for user data input
def log_user_input_fish(image: Image,label:int,probability:int):
    bucket=model_fish.storage_client.bucket("user-data-cv13")
    file_name= f"fish/{secrets.token_hex(30)}_{label}_{probability}.jpg"
    with io.BytesIO() as output:
        image.save(output,format="JPEG")
        bucket.blob(file_name).upload_from_string(output.getvalue(),"image/jpeg")
        
##User data save for user data input
def log_user_input_sashimi(image: Image,label:int,probability:int):
    bucket=model_fish.storage_client.bucket("user-data-cv13")
    file_name= f"sashimi/{secrets.token_hex(30)}_{label}_{probability}.jpg"
    with io.BytesIO() as output:
        image.save(output,format="JPEG")
        bucket.blob(file_name).upload_from_string(output.getvalue(),"image/jpeg")
        
def softmax(x):
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum(axis=0)