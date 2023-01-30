import json
import numpy as np
import os.path as osp
import os
from sklearn.model_selection import StratifiedGroupKFold
from tqdm import tqdm

def split_json(data_root, out_root):
    """stratified group kfold 사용하여 json 나누기

    Args:
        data_root (_type_): json root
        out_root (_type_): out root
    """
    def save_anns(name, images, annotations):
        sub_anns = dict()

        sub_anns['categories'] = data['categories'] # class label 10개
        sub_anns['images'] = images #이미지 너비,높이, 파일명, 라이센스, url 2개, 캡처시기,id
        sub_anns['annotations'] = annotations #image_id, category_id, area, bbox, iscrowd, id

        if not osp.isdir(out_root):
            os.mkdir(out_root)
        with open(f'{out_root}/{name}.json', "w") as f:
            json.dump(sub_anns, f, indent=4)
    

    with open(data_root) as f:
        data = json.load(f)

    var = [(ann['image_id'], ann['category_id']) for ann in data['annotations']]

    X = np.ones((len(data['annotations']),1))
    y = np.array([v[1] for v in var])
    groups = np.array([v[0] for v in var])

    cv = StratifiedGroupKFold(n_splits=5, shuffle=True, random_state=411)

    k = 0
    for train_idx, valid_idx in cv.split(X, y, groups):
        train_image, valid_image = [], []
        train_annotation, valid_annotation = [], []
        for idx in range(len(train_idx)):
            train_image.append(data['images'][idx])
            train_annotation.append(data['annotations'][idx])
        
        for i in range(len(valid_idx)):
            valid_image.append(data['images'][idx])
            valid_annotation.append(data['annotations'][idx])
        
        # save train, validation file based on percentage
        labeled_name = f'train_fold_{k+1}'
        validation_name = f'validation_fold_{k+1}'

        save_anns(labeled_name, train_image, train_annotation)
        save_anns(validation_name, valid_image, valid_annotation)
        k+=1

if __name__ == '__main__':
    data_root = './val_images/gbt_fish_dtset_val_images.json'
    out_root = './val_images/output'
    split_json(data_root, out_root)