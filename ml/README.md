# ML

## Poetry 환경 구성(Requirements)
```
# 환경 설정은 poetry를 통해서 구성했습니다
# poetry를 설치 후 ml/ 에서
# poetry install 명령을 통해 환경을 구성합니다
# pyproject.toml

python = ">=3.8,<3.10"
matplotlib = "^3.6.3"
numpy = "^1.24.1"
pandas = "^1.5.2"
torch = { url = "https://download.pytorch.org/whl/cu110/torch-1.7.1%2Bcu110-cp38-cp38-linux_x86_64.whl"}
torchaudio = { url = "https://download.pytorch.org/whl/torchaudio-0.7.2-cp38-cp38-linux_x86_64.whl"}
torchvision = { url = "https://download.pytorch.org/whl/cu110/torchvision-0.8.2%2Bcu110-cp38-cp38-linux_x86_64.whl"}
opencv-python = "^4.7.0.68"
pillow = "^9.4.0"
sklearn = "^0.0.post1"
scipy = "^1.10.0"
tqdm = "^4.64.1"
wandb = "^0.13.8"
timm = "^0.6.12"
jupyter = "^1.0.0"
json5 = "^0.9.11"
pyyaml = "^6.0"
albumentations = "^1.3.0"
gdown = "^4.6.0"
onnx = "^1.13.0"
google-cloud-storage = "^2.7.0"
plotly = "^5.12.0"
scikit-learn = "^1.2.1"
```
## 구현 목록
- ml 구성
    - config
        - config.yaml: train parameter를 설정할 수 있습니다.
        - sweep.yaml: wandb sweep 구성시 train parameter를 설정할 수 있습니다.
    - feature map
        - CAM.ipynb: Fish 모델의 결과를 시각화할 수 있습니다.
        - Sashimi_CAM.ipynb: Sashimi 모델의 결과를 시각화할 수 있습니다.
    - pipeline
        - utils: 학습에 필요한 유용한 파일들을 작성하였습니다.
        - dataloader.py: dataset을 class 형태로 정의하였습니다.
        - inference.py: inference 결과와 소요 시간을 확인할 수 있습니다.
        - loss.py: loss를 class 형태로 정의하였습니다.
        - model.py: model을 class 형태로 정의하였습니다.
        - optimizer.py: optimizer를 함수 형태로 정의하였습니다.
        - scheduler.py: scheduler를 함수 형태로 정의하였습니다. 
        - train.py
            - wandb를 사용해 학습 기록을 로그할 수 있습니다.
            - config파일을 통해 각 pipeline에서 원하는 값을 가져올 수 있습니다.
        - transforms.py: transforms를 class 형태로 정의하였습니다.
## How to train
```bash
~/final-project-level3-cv-13/ml$ pip install poetry
~/final-project-level3-cv-13/ml$ poetry install
~/final-project-level3-cv-13/ml$ mkdir output
~/final-project-level3-cv-13/ml/pipeline$ python train.py
```