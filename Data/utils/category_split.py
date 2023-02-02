import os
import os.path as osp
from tqdm import tqdm
import pandas as pd
import shutil

category = {
    0 : "Olive flounder",
    1 : "Korea rockfish",
    2 : "Red seabream",
    3 : "Black porgy",
    4 : "Rock bream"
}

def category_split(data_root, csv_root, out_root):
    """split dataset with each category

    Args:
        data_root (str): 원본 이미지의 경로
        csv_root (str): 원본 csv의 경로
        out_root (str): 만들어진 image와 csv가 저장될 경로
    """
    # make image folder
    for idx in range(5):
        try:
            if not osp.exists(osp.join(out_root, category[idx])):
                os.makedirs(osp.join(out_root, category[idx]))
        except OSError:
            print("Error: Failed to create the directory.")

    data = pd.read_csv(csv_root)

    # make empty dataframe
    data_list = []
    for i in range(5):
        df = pd.DataFrame(columns=['img_path', 'categories_id'])
        data_list.append(df)
    
    # categories_id에 맞는 데이터 프레임에 넣고 파일 옮기기
    for idx in tqdm(range(len(data))):
        
        new_data_path = category[data['categories_id'][idx]] + data['img_path'][idx][10:]
        new_data_id = data['categories_id'][idx]
        row = {'img_path': new_data_path, 'categories_id': new_data_id}

        if data['categories_id'][idx] == 0:
            data_list[0] = data_list[0].append(row, ignore_index=True)
        elif data['categories_id'][idx] == 1:
            data_list[1] = data_list[1].append(row, ignore_index=True)
        elif data['categories_id'][idx] == 2:
            data_list[2] = data_list[2].append(row, ignore_index=True)
        elif data['categories_id'][idx] == 3:
            data_list[3] = data_list[3].append(row, ignore_index=True)
        else:
            data_list[4] = data_list[4].append(row, ignore_index=True)

        shutil.move(osp.join(data_root, data['img_path'][idx]), osp.join(out_root, new_data_path))
    
    # dataframe to csv
    for idx in range(5):
        data_list[idx].to_csv(osp.join(out_root, category[idx])+"/label.csv", index=False)

if __name__ == "__main__":
    data_root = './Validation/crop_image'
    csv_root = './Validation/csv/train.csv'
    out_root = './images'
    category_split(data_root, csv_root, out_root)