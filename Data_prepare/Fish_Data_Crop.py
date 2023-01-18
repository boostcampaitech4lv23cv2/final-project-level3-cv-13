import csv
import os
from Function.annotaion_part import make_annotation
from Function.image_part import crop_image

###########Setting Part ###########
dataset_path  = "./Fish_dataset" #Fish_dataset 폴더가 있는 파일의 절대 경로를 적어주자
train_image_filename = "Training/dtset" #dtset들의 상위폴더의 폴더명을 적어주자
train_label_filename = "Training/gbt_fish_dtset" #json파일 (label)이 담겨 있는 폴더명을 적어주자

val_image_filename = "Validation/dtset" #images의 상위폴더의 폴더명을 적어주자
val_label_filename = "Validation/gbt_fish_dtset" #json파일 (label)이 담겨 있는 폴더명을 적어주자

csv_folder_path = './Fish_dataset/output/analysis_csv/'


try:
    if not os.path.exists(csv_folder_path):
        os.makedirs(csv_folder_path)
except OSError:
    print("Error: Failed to create the directory.")

###########annotation Part ###########
print("\n\n######################################")
print("## start to running annotation part ##")
print("######################################\n")

category_list = make_annotation(dataset_path, train_image_filename, train_label_filename, "train")
#추후 category 번호에 따른 name을 확인하기 위해 return으로 구현
valid_category_list = make_annotation(dataset_path, val_image_filename, val_label_filename, "val")


print("\n\n")


###########image Part ###########
print("\n######################################")
print("##    start to running image part   ##")
print("######################################\n")

train_images_size_list, train_csv = crop_image(dataset_path, train_image_filename)
valid_images_size_list, valid_csv = crop_image(dataset_path, val_image_filename)



print("\n#######################################")
print("##########     train.csv      ###########")
print("#######################################\n")



with open(csv_folder_path +'train.csv','w',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["img_path","categories_id"])
    for idx in range (len(train_csv)):
        writer.writerow(train_csv[idx])

print("\n train.csv  sucessfully making \n")



print("\n#######################################")
print("##########     valid.csv      ###########")
print("#######################################\n")



with open(csv_folder_path +'valid.csv','w',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["img_path","categories_id"])
    for idx in range (len(valid_csv)):
        writer.writerow(valid_csv[idx])

print("\n valid.csv  sucessfully making \n")


print("\n#######################################")
print("##     making category_list.csv      ##")
print("#######################################\n")


with open(csv_folder_path +'category_list.csv','w',newline='') as f:
    fieldnames = list(category_list[0].keys())
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    for idx in range (len(category_list)):
        writer.writeheader() #첫번째 행에 항목 이름들을 넣어줄 것인지
        writer.writerows(category_list)

print("\n category_list.csv  sucessfully making \n")


print("\n#######################################")
print("##   making valid_category_list.csv    ##")
print("#######################################\n")

with open(csv_folder_path +'valid_category_list.csv','w',newline='') as f:
    fieldnames = list(valid_category_list[0].keys())
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    for idx in range (len(valid_category_list)):
        writer.writeheader() #첫번째 행에 항목 이름들을 넣어줄 것인지
        writer.writerows(valid_category_list)


print("\n valid_category_list.csv sucessfully making \n")


print("\n#######################################")
print("## making train_images_size_list.csv ##")
print("#######################################\n")

with open(csv_folder_path +'train_images_size_list.csv','w',newline='') as f:
    writer = csv.writer(f)
    for idx in range (len(train_images_size_list)):
        writer.writerow(train_images_size_list[idx])

print("\n train_images_size_list.csv sucessfully making \n")

print("#######################################")
print("## making valid_images_size_list.csv ##")
print("#######################################\n")

with open(csv_folder_path +'valid_images_size_list.csv','w',newline='') as f:
    writer = csv.writer(f)
    for idx in range (len(valid_images_size_list)):
        writer.writerow(valid_images_size_list[idx])

print("\n valid_images_size_list.csv sucessfully making \n")
