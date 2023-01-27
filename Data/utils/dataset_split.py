import pandas as pd
import numpy as np
import os.path as osp
import os
from sklearn.model_selection import StratifiedKFold
from tqdm import tqdm


def dataset_split(path, name):
    """통합된 csv파일을 train, valid로 나눔

    Args:
        path (_type_): 입력으로 들어올 csv파일의 경로
    """
    data = pd.read_csv(path + f'{name}.csv')

    target = data.loc[:,'categories_id']

    cv = StratifiedKFold(n_splits=5)

    k = 1
    for train_idx, valid_idx in cv.split(data, target):
        
        train = data.loc[train_idx, ['img_path', 'categories_id']]
        valid = data.loc[valid_idx, ['img_path', 'categories_id']]
        train.to_csv(path + f'train_{k}.csv', index=False)
        valid.to_csv(path + f'valid_{k}.csv', index=False)

        k+=1


if __name__ == "__main__":
    fish_path = '../fish/'
    sashimi_path = '../sashimi/'
    dataset_split(fish_path, 'fish')
    dataset_split(sashimi_path, 'sashimi')