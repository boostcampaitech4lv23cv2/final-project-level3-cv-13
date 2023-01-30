import os
from PIL import Image
import json


def crop_image(dataset_path,image_filename,anns_path):

    #parameter
    save_path = dataset_path +"/crop_image"

    #디렉토리 없으면 만들어 주는 코드
    try:
        if not os.path.exists(save_path):
            os.makedirs(save_path)
    except OSError:
        print("Error: Failed to create the directory.")


    image_path = dataset_path + '/' + image_filename
    image_name_list = os.listdir(image_path)
    #dataset_path  = "/opt/ml/jzone_workspace/Data_prepare/Fish_dataset" #Fish_dataset 폴더가 있는 파일의 절대 경로를 적어주자
    #train_image_filename = "Training/dtset" #dtset들의 상위폴더의 폴더명을 적어주자
    images_size = [] #Model 부분에서 추후 EDA할 때 사용하기 위함
    results = []

    for count, image_folder_name in enumerate (image_name_list): #dtset 1~4
        print("Making Crop image [",count+1,"/",len(image_name_list),"]")
        if(image_folder_name[0] == "."):
            continue
        # print(image_folder_name)
        if image_folder_name[-5:] == ".json":
            print(image_folder_name,"is not image folder \n\n")
        else:
            #print(image_folder_name)
            #"bbox": [x,y,width,height],
            

            tmp_save_path = save_path+'/'+image_folder_name
            try:
                if not os.path.exists(tmp_save_path):
                    os.makedirs(tmp_save_path)
            except OSError:
                print("Error: Failed to create the directory.")


            # Read annotations
            anns_name_list = os.listdir(anns_path)
            for anns_name in anns_name_list:
                if image_folder_name == anns_name[-5-len(image_folder_name):-5]: #.json앞이 image폴더이름과 일치하면    
                    #anns_path = dataset_path +'/'+"output/new_json_set"
                    with open(anns_path+'/'+anns_name, 'r') as f:
                        anns = json.loads(f.read())
            # print(len(anns))
            #try-except문은 real data로 돌릴 때는 빼도 된다(sample data여서 사용)
            print(image_folder_name," is now processing ")
            for idx in anns.keys():
                try:
                    file_name = anns[idx]["img_file_name"]
                    category = anns[idx]["categories_id"]-1
                    tmp_img_path =image_path+ '/'+image_folder_name +'/' + file_name
                    bbox = anns[idx]["bbox"]
                    tmp_img = Image.open(tmp_img_path)
                    croppedImage=tmp_img.crop(tuple([bbox[0],bbox[1],bbox[0]+bbox[2],bbox[1]+bbox[3]]))
                    result = tuple([image_folder_name + '/' + file_name, int(category)])
                    results.append(result)
                    images_size.append(croppedImage.size)
                    croppedImage.save(tmp_save_path +"/"+file_name)

                except FileNotFoundError as e:
                    pass
        print("complete to making Crop image please check bottom path")
        print(save_path, "\n")
    return images_size, results
