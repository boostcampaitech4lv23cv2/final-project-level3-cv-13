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
    - ...
- 백엔드 구성(fast api base)
    - Onnx 변환 코드(자동화 예정)
    - Onnx로 변환된 모델로 inference
- Pytest 구성
    - 인퍼런스 시간 측정
    - ...

## 참고자료
### ONNX 모델 변환 및 추론
[PyTorch models to onnx models](https://pytorch.org/docs/stable/onnx.html)  
[Get Started with ONNX Runtime in Python](https://onnxruntime.ai/docs/get-started/with-python.html)  
[ONNX Runtime API](https://onnxruntime.ai/docs/api/python/api_summary.html)  
[ONNX Runtime inference examples- Microsoft](https://github.com/microsoft/onnxruntime-inference-examples/blob/main/python/api/onnxruntime-python-api.py)  

