## api 구성
from fastapi import FastAPI, UploadFile, File
from app.inference import Inference
from PIL import Image
import io
import numpy as np
import albumentations
import pandas as pd
import gcsfs
from fastapi.middleware.cors import CORSMiddleware


RESIZE=(384,384)

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
    log_user_input(image,label.argmax(0).item())
    return label.argmax(0)

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
##User data save for user data input
def log_user_input(image: Image,label:int):
    bucket=model.storage_client.bucket("user-data-cv13")
    fs = gcsfs.GCSFileSystem(project='helloworld-374304')
    with fs.open('user-data-cv13/user_input.csv') as f:
        df = pd.read_csv(f)
    #df = pd.read_csv('gs://user-data-cv13/user_input.csv')
    cnt=len(df)
    file_name= f"images/{cnt:05d}.jpg"
    new_row=pd.DataFrame({"img_path":file_name,"categories_id":label},index=[0])
    df=pd.concat([df,new_row])
    data=df.to_csv(index=False)
    bucket.blob("user_input.csv").upload_from_string(data,"text/csv")
    with io.BytesIO() as output:
        image.save(output,format="JPEG")
        bucket.blob(file_name).upload_from_string(output.getvalue(),"image/jpeg")