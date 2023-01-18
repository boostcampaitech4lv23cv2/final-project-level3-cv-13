## 서버 환경 구성(Requirements)
```
# Server Environment set-ups
pip install fast-api
pip install uvicorn
pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu
pip install python-multipart
# for code integrity test
pip install pytest
pip install httpx
# Convert models to resolve dependency issues
pip install onnxruntime
pip install onnx
# for image preprocessing
pip install albumentations
```
## 구현 목록
- 프론트 구성
    - Streamlit으로 구현 상태
- 백엔드 구성(fast api base)
    - Onnx 변환 코드(자동화 예정)
    - Onnx로 변환된 모델로 inference(완성)
    - 서비스 요청에 따른 Inference 결과 저장 -> DB에 저장해서 분석하기
- Pytest 구성
    - 인퍼런스 시간 측정
    - ...

## 참고자료
### ONNX 모델 변환 및 추론
[PyTorch models to onnx models](https://pytorch.org/docs/stable/onnx.html)  
[Get Started with ONNX Runtime in Python](https://onnxruntime.ai/docs/get-started/with-python.html)  
[ONNX Runtime API](https://onnxruntime.ai/docs/api/python/api_summary.html)  
[ONNX Runtime inference examples- Microsoft](https://github.com/microsoft/onnxruntime-inference-examples/blob/main/python/api/onnxruntime-python-api.py)

### PyTest 설정
[FastAPI 및 pytest를 이용한 API 서버 테스트 코드 작성하기](https://sehoi.github.io/etc/fastapi-pytest/)

### Serverless 모델 자료
[Google Cloud Run](https://cloud.google.com/run?hl=ko)  
[Heroku](https://www.heroku.com/)

