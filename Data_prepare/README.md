# How To prepare Fish Data
Please rename the Dirctories like bottom Structure

## Before running code
# 

### Notice : 반드시 gbt_fish_dtset3.json 과 dtset3 와 같이 <br/> 이미지를 담은 파일명이 해당 json앞에 이름이 있어야 한다
<br/> 

#### (Ex) json : gbt_fish_dtset_val_images.json ==>  image folder : val_images


#
📂Data_prepare

┣ 📂Fish_dataset

┃ ┣ 📂Training

┃ ┃ ┣ 📂gbt_fish_dtset

┃ ┃ ┃ ┗ 📜gbt_fish_dtset1.json

┃ ┃ ┃ ┗ 📜gbt_fish_dtset2.json

┃ ┃ ┃ ┗ 📜gbt_fish_dtset3.json

┃ ┃ ┃ ┗ 📜gbt_fish_dtset4.json

┃ ┃ ┃ ┗ 📂dtset

┃ ┃ ┃ ┃ ┣ 📂dtset1

┃ ┃ ┃ ┃ ┣ 📂dtset2

┃ ┃ ┃ ┃ ┣ 📂dtset3

┃ ┃ ┃ ┃ ┗ 📂dtset4

┃ ┗ 📂Validation

┃ ┃ ┣ 📜gbt_fish_dtset_val_images.json

┃ ┃ ┗ 📂val_images

┣ 📂Function

┃ ┃ ┣ 📜annotation_part.py

┃ ┃ ┗ 📜image_part.py

┗ 📜Fish_Data_Crop.py (main)
<br/> 
<br/> 
<br/> 


### 다음과 같은 세팅을 마친 후

#### Fish_Data_Crop.py를 실행 시켜준다 (경로 등을 설정)
<br/> 
<br/> 


## After running code
# 

📂Data_prepare

┣ 📂Fish_dataset

┃ ┣ 📂output

┃ ┃ ┣ 📂analysis_csv

┃ ┃ ┃ ┣ 📜catagory_list.csv

┃ ┃ ┃ ┣ 📜valid_catagory_list.csv

┃ ┃ ┃ ┣ 📜train_images_size_list.csv

┃ ┃ ┃ ┗ 📜valid_images_size_list.csv

┃ ┃ ┣ 📂crop_image

┃ ┃ ┃ ┣ 📂dtset1

┃ ┃ ┃ ┣ 📂dtset2

┃ ┃ ┃ ┣ 📂dtset3

┃ ┃ ┃ ┣ 📂dtset4

┃ ┃ ┃ ┗ 📂val_images

┃ ┃ ┗ 📂new_json_set

┃ ┃ ┃ ┣ 📜[new]_gbt_fish_dtset_val_images.json

┃ ┃ ┃ ┣ 📜[new]_gbt_fish_dtset1.json

┃ ┃ ┃ ┣ 📜[new]_gbt_fish_dtset2.json

┃ ┃ ┃ ┣ 📜[new]_gbt_fish_dtset3.json

┃ ┃ ┃ ┣ 📜[new]_gbt_fish_dtset4.json

┃ ┣ 📂Training

┃ ┗ 📂Validation

┣ 📂Function

┃ ┃ ┣ 📜annotation_part.py

┃ ┃ ┗ 📜image_part.py

┗ 📜Fish_Data_Crop.py (main)
