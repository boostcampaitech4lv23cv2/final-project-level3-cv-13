import pandas as pd
import os
import os.path as osp
import csv
from tqdm import tqdm

fish_category = {'Olive_flounder' : 0,
                 'Korea_rockfish' : 1,
                 'Red_seabream' : 2,
                 'Black_porgy' : 3,
                 'Rock_bream' : 4,
                 'Croaker' : 5,
                 'Argyrosomus_japonicus' : 6,
                 'Starry_flounder' : 7,
                 'Longtooth_grouper' : 8,
                 'Convict_grouper' : 9,
                 'Japanese_amberjack' : 10,
                 'Yellowtail_amberjack' : 11,
                }

sashimi_category = {'Olive_flounder_sashimi' : 0,
                    'Korea_rockfish_sashimi' : 1,
                    'Red_seabream_sashimi' : 2,
                    'Brown_croaker_sashimi' : 3,
                    'Red_drum_sashimi' : 4,
                    'Tilapia_sashimi' : 4,
                    'Salmon_sashimi' : 5,
                    'Tuna_sashimi' : 6,
                    'Japanese_amberjack_sashimi' : 7
                   }

def csv_refactor(path, category, csv_folder_path):

    print("################################")
    print("## 저장경로 : ",csv_folder_path + "/" + category +'.csv ##')
    print("################################\n")


    """여러개의 csv를 하나로 합쳐줍니다.​
    Args:
        path (_type_): dataset folder들의 상위 path
    """

    flag = 0
    folder_list = os.listdir(path)
    category_name = fish_category if category == 'fish' else sashimi_category
    csv_mode = ['w','a']
    
    for folder in folder_list:
        if folder[-4:] == '.csv':
            continue

        csv_path = osp.join(path, folder, 'label.csv')
        print(csv_path)
        df = pd.read_csv(csv_path)
        if df.columns[0] == 'img_path':
            with open(csv_folder_path + "/" + category +'.csv',csv_mode[flag],newline='') as f:
                writer = csv.writer(f)
                if flag == 0:
                   writer.writerow(['img_path',"categories_id"])
                with tqdm(total = len(df)) as pbar:
                    for idx in range (len(df)):
                        title_name = df.iloc[idx][0].split("/")[0]
                        name = df.iloc[idx][0].split("/")[1]
                        writer.writerow([osp.join(remove_space(title_name),name),category_name[folder]])
                        pbar.update(1)
        
        
        elif df.columns[0] == 'img_name':
            with open(csv_folder_path + "/" + category +'.csv',csv_mode[flag],newline='') as f:
                writer = csv.writer(f)
                if flag == 0:
                   writer.writerow(['img_path',"categories_id"])
                with tqdm(total = len(df)) as pbar:
                    for idx in range (len(df)):
                        writer.writerow([osp.join(folder,df.iloc[idx][0]),category_name[folder]])
                        pbar.update(1)

        else : # 
            print("please Check columns name")

        print("")
        flag = 1
                

def remove_space(title_name):
    c_title = title_name.split(" ")
    new_title = ""
    for i in range (len(c_title)):
        new_title  += c_title[i]
        if i == len(c_title)-1:
            break
        new_title += "_"
    return new_title


if __name__ == "__main__":
    fish_path = '/opt/ml/data/fish'
    sashimi_path = '/opt/ml/data/sashimi'
    output_path = '/opt/ml/data/'


    csv_refactor(fish_path, 'fish', output_path)
    csv_refactor(sashimi_path, 'sashimi', output_path)