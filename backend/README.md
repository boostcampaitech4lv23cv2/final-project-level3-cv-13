## 서버 환경 구성(Requirements)
```
# Server Environment set-ups
-f https://download.pytorch.org/whl/torch_stable.html
pip install fast-api
pip install uvicorn

#for server torch environments
pip install torch==1.13.1+cpu
pip install torchaudio==0.13.1+cpu
pip install torchvision==0.14.1+cpu
pip install python-multipart

# for code integrity test
pip install pytest==7.2.0
pip install httpx==0.23.3

# Convert models to resolve dependency issues
pip install onnxruntime
pip install onnx

# for image preprocessing
pip install albumentations

```
## 구현 목록
- 프론트 구성
    - Streamlit으로 구현 ✅
- 백엔드 구성(fast api base)
    - Onnx 변환 코드(자동화 예정)
    - Onnx로 변환된 모델로 inference(완성) ✅
    - GCP 설정
        - Google Docker에 image push ✅
        - Container Registry에 등록 ✅
        - push된 이미지를 Cloud run으로 실행 ✅
    - 서비스 요청에 따른 Inference 결과 저장 -> DB에 저장해서 분석하기
- Pytest 구성
    - 인퍼런스 시간 측정 ✅
        - localhost
            - Resnet50 : 0.3XX
            - Efficient b0 : 0.1XX
        -Google Cloud PlatForm
            - Resnet50 : 0.4XX
    - ...

## 참고자료
### ONNX 모델 변환 및 추론
[PyTorch models to onnx models](https://pytorch.org/docs/stable/onnx.html)  
[Get Started with ONNX Runtime in Python](https://onnxruntime.ai/docs/get-started/with-python.html)  
[ONNX Runtime API](https://onnxruntime.ai/docs/api/python/api_summary.html)  
[ONNX Runtime inference examples- Microsoft](https://github.com/microsoft/onnxruntime-inference-examples/blob/main/python/api/onnxruntime-python-api.py)  

### PyTest 설정
[FastAPI 및 pytest를 이용한 API 서버 테스트 코드 작성하기](https://sehoi.github.io/etc/fastapi-pytest/)  

### GCP Docker 설정
[Docker Credential gcr](https://github.com/GoogleCloudPlatform/docker-credential-gcr)

### GCP Docker 설정
[Docker Credential gcr](https://github.com/GoogleCloudPlatform/docker-credential-gcr)  
### Serverless 모델 자료
[Google Cloud Run](https://cloud.google.com/run?hl=ko)  
[Google Cloud Deploy](https://cloud.google.com/sdk/gcloud/reference/run/deploy)   
[Heroku](https://www.heroku.com/)  
[Cold Start Optimizing](https://www.youtube.com/watch?v=rWw90N2gVPk)

### Data Logging 설정 자료
[Stream Handler Attribute Error](https://stackoverflow.com/questions/34319521/python-logging-module-having-a-formatter-causes-attributeerror) 
[Python Logging 설명](https://data-newbie.tistory.com/248)  
[GCP Bitbucket 객체 다운로드](https://cloud.google.com/storage/docs/downloading-objects#client-libraries-download-object-portion)  
[GCP Bitbucket 파일 업로드](https://cloud.google.com/storage/docs/uploading-objects?hl=ko#storage-upload-object-python)  
[GCP Bitbucket 파일 Read & Write](https://github.com/googleapis/python-storage/blob/HEAD/samples/snippets/storage_fileio_write_read.py)  

### Travis CI
[Travis CI Docker](https://docs.travis-ci.com/user/docker/)  
[Travis Client](https://github.com/travis-ci/travis.rb)  
[Travis Environment Variables](https://docs.travis-ci.com/user/environment-variables/)  
[Building a Python Project](https://docs.travis-ci.com/user/languages/python/)  
[Conditional Builds, Stages, Jobs](https://docs.travis-ci.com/user/conditional-builds-stages-jobs/)  
[Customize Builds](https://docs.travis-ci.com/user/customizing-the-build/)  
[Script Deployment](https://docs.travis-ci.com/user/deployment/script/)  
[Build Stages](https://docs.travis-ci.com/user/build-stages/)  

### Docker
[Parent Directory](https://velog.io/@skynet/Dockerfile%EC%97%90-%EB%B6%80%EB%AA%A8-%EB%94%94%EB%A0%89%ED%86%A0%EB%A6%AC%EC%9D%98-%ED%8C%8C%EC%9D%BC%EC%9D%84-%EB%B3%B5%EC%82%AC-%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95)

## Annotation Tools
[ipyannotatoins](https://ipyannotations.readthedocs.io/en/latest/)  
[pigeon](https://github.com/agermanidis/pigeon)  