# How To prepare Sashimi Data
Please rename the Dirctories like bottom Structure

## Before running code
# 

### Notice : 반드시 gbt_fish_dtset3.json 과 dtset3 와 같이 <br/> 이미지를 담은 파일명이 해당 json앞에 이름이 있어야 한다
<br/> 

#### (Ex) json : gbt_fish_dtset_val_images.json ==>  image folder : val_images


#
📂Fish

┣ 📂Fish_dataset

┃ ┣ 📂Training

┃ ┃ ┣ 📂dtset

┃ ┃ ┃ ┣ 📂dtset1

┃ ┃ ┃ ┣ 📂dtset2

┃ ┃ ┃ ┣ 📂dtset3

┃ ┃ ┃ ┗ 📂dtset4

┃ ┃ ┗ 📂gbt_fish_dtset

┃ ┃ ┃ ┗ 📜gbt_fish_dtset1.json

┃ ┃ ┃ ┗ 📜gbt_fish_dtset2.json

┃ ┃ ┃ ┗ 📜gbt_fish_dtset3.json

┃ ┃ ┃ ┗ 📜gbt_fish_dtset4.json

┃ ┗ 📂Validation

┃ ┃ ┣ 📂dtset

┃ ┃ ┃ ┗ 📂val_images

┃ ┃ ┣ 📂gbt_fish_dtset

┃ ┃ ┃ ┗ 📜gbt_fish_dtset_val_images.json

┃ ┣ 📂Function

┃ ┃ ┣ 📜annotation_part.py

┃ ┃ ┗ 📜image_part.py

┃ ┣ 📂utils

┃ ┃ ┗ 📜json_refactor.py

┃ ┗ 📜Fish_Data_Crop.py (main)

┗ 📂Sashimi
<br/> 
<br/> 
<br/> 


### 다음과 같은 세팅을 마친 후

#### Fish_Data_Crop.py를 실행 시켜준다 (경로 등을 설정)
<br/> 
<br/> 


## After running code
# 

📂Fish

📂Sashimi

┣ 📂Sashimi_dataset

┃ ┗ 📜Sashimi_Data_Crop.py (main)