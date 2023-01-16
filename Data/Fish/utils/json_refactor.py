import json
import os
import os.path as osp

file_path = "./Fish_dataset/Training/gbt_fish_dtset"
file_list = ['gbt_fish_dtset1.json', 'gbt_fish_dtset2.json', 'gbt_fish_dtset3.json', 'gbt_fish_dtset4.json']
new_file_path = ""

file_name_list = os.listdir(file_path)
#print(file_name_list)

for file_name in file_name_list:
    if file_name[-4:] != 'json':
        continue 
    new_path = osp.join(file_path, file_name)
    # path = osp.join(file_path, "new", file_name)
    # print(new_path)
    with open(new_path, "r") as f:
        new_json = json.load(f)


    with open(new_path, "w") as nf:
        json.dump(new_json, nf, indent=4)#, sort_keys=True