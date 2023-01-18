import os
import json
import os.path as osp

def make_annotation(dataset_path, image_path, label_filename, mode, direc_root = "/opt/ml/final-project-level3-cv-13/Data/Fish/Fish_dataset/output/new_json_set"):
    ###########annotation Part ###########
    #디렉토리 없으면 만들어 주는 코드 -> 새로운 json이 담길 폴더를 만들기
    # dataset_path = ./Fish_dataset
    # image_path = Training/dtset
    # label_filename = Training/gbt_fish_dtset
    try:
        if not os.path.exists(direc_root):
            os.makedirs(direc_root)
    except OSError:
        print("Error: Failed to create the directory.")

    anns_path = dataset_path + '/' + label_filename
    anns_name_list = os.listdir(anns_path)
    
    for count ,anns_folder_name in enumerate (anns_name_list): #gbt_fish_dtset1~4.json
        print("Making anns process [",count+1,"/",len(anns_name_list),"]")
        if anns_folder_name[-5:] != ".json":
            print(anns_folder_name," is not json \n\n")
        else:
            tmp_anns_path = anns_path +'/'+ anns_folder_name
            
            with open(tmp_anns_path, 'r') as f: # Read annotations
                anns = json.loads(f.read())
            categories = anns["categories"]
            images = anns["images"]
            annotations = anns["annotations"]
            
            categories_id = []
            img_file_name = []
            img_id_list = []
            bbox = []
            if mode == 'train':
                folder_name = anns_folder_name[-11:-5]
            elif mode == 'val':
                folder_name = anns_folder_name[-15:-5]
            
            for img in images:
                # print(dataset_path + '/' + image_path + folder_name + '/' + img['file_name'])
                if osp.exists(osp.join(dataset_path, image_path, folder_name, img['file_name'][2:])):
                    img_file_name.append(img['file_name'])
                    img_id_list.append(img['id'])
                else:
                    continue
            # print(img_id_list)
            for anno in annotations:
                if anno['image_id'] in img_id_list: #### <- 요기가 문제 아닐까
                    # print(anno['category_id'], anno['bbox'])
                    categories_id.append(anno['category_id'])
                    bbox.append(anno['bbox'])
                else:
                    continue
            print("##################################")
            print("## Name of json file : " ,anns_folder_name)
            print("## Number of categories_id : ", len(categories_id))
            print("## Number of img_file_name : ", len(img_file_name))
            print("## Number of bbox : ", len(bbox))
            print("##################################")
            new_json = {}
            for idx in range (len(img_file_name)):
                new_json[idx] = {'img_file_name' : img_file_name[idx][2:], 
                                "categories_id" : categories_id[idx], 
                                "bbox" : bbox[idx]}

            with open(direc_root+'/'+'[new]_'+anns_folder_name, "w") as f:
                print("new_json file is complete to create at \n",direc_root+'/'+'[new]'+anns_folder_name,"\n\n")
                json.dump(new_json, f, indent = 4)

    return categories