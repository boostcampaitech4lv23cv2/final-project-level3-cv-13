# How To prepare Fish Data <br/>
Please rename the Dirctories like bottom Structure <br/><br/><br/>

# Before running code

### Notice : 반드시 gbt_fish_dtset3.json 과 dtset3 와 같이 <br/> 이미지를 담은 파일명이 해당 json앞에 이름이 있어야 한다
<br/> 

#### (Ex) json : gbt_fish_dtset_val_images.json ==>  image folder : val_images <br/><br/><br/>


# Data File Rename Convention

## 1. 어류 개체 촬영 영상 --> Fish_dataset

<br/>

폴더 이름을 Fish _dataset으로 바꿔 주기

<br/>


## 2. Training 폴더에 들어 가기

<br/>

>### 2-1 앞에 라벨이라는 단어 제거해주기 <br/>  
>>~~[라벨]gbt_fish_dtset~~ -> **gbt_fish_dtset**

<br/>

>### 2-2 [원천]dtset/dtset을 다음 dtset과 같이 속의 폴더를 꺼내주기 <br/> 
>>~~[원천]dtset1/dtset1~~ -> **dtset1** <br/> 
>>~~[원천]dtset2/dtset2~~ -> **dtset2** <br/> 
>>~~[원천]dtset3/dtset3~~ -> **dtset3** <br/> 
>>~~[원천]dtset4/dtset4~~ -> **dtset4** <br/>

<br/>

## 3. Validation 폴더에 들어 가기

<br/>

>### 3-1 <br/>  
>>~~[라벨]gbt_fish_dtset~~ -> **gbt_fish_dtset**

<br/>

>### 3-2 <br/> 
>>~~[라벨]gbt_fish_dtset.json~~ -> **gbt_fish_dtset_val_images.json** <br/>
>>~~[원천]images~~ -> **val_images** <br/> 



<br/> 

## 4. 다음과 같은 구조가 만들어졌는지 확인하기
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

┣ 📂Function

┃ ┣ 📜annotation_part.py

┃ ┗ 📜image_part.py

┣ 📂utils

┃ ┗ 📜json_refactor.py

┗ 📜Fish_Data_Crop.py (main)

📂Sashimi
<br/> 
<br/> 


### 다음과 같은 세팅을 마친 후
<br/> 

## 5. gbt_fish_dtset_val_images.json를 열어 

<br/> 
"categories":[]
<br/> <br/> 
를

<br/>


"categories":[{"name":"Olive flounder","supercategory":"fish","id":1},{"name":"Korea rockfish","supercategory":"fish","id":2},{"name":"Red seabream","supercategory":"fish","id":3},{"name":"Black porgy","supercategory":"fish","id":4},{"name":"Rock bream","supercategory":"fish","id":5}]

<br/> 
로  바꿔주자
<br/> <br/> 

## 6. Fish_Data_Crop.py를 실행 시켜준다 
경로 등은 설정
<br/> 
<br/> 

## 7. 실행 이후 다음과 같은 파일 구조가 만들어졌는지 확인

# 
## After running code
# 

📂Fish

┣ 📂Fish_dataset

┃ ┣ 📂output

┃ ┃ ┣ 📂analysis_csv

┃ ┃ ┃ ┣ 📗catagory_list.csv

┃ ┃ ┃ ┣ 📗train_images_size_list.csv

┃ ┃ ┃ ┣ 📗train.csv

┃ ┃ ┃ ┣ 📗valid_catagory_list.csv

┃ ┃ ┃ ┣ 📗valid_images_size_list.csv

┃ ┃ ┃ ┗ 📗valid_images_size_list.csv

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

┃ ┣ 📜annotation_part.py

┃ ┗ 📜image_part.py

┣ 📂utils

┃ ┗ 📜json_refactor.py

┗ 📜Fish_Data_Crop.py (main)

📂Sashimi


</br>

## 🎉 Congratulations 🎉