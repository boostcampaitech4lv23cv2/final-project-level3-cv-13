import pandas as pd
import argparse
import glob
import os
from datetime import datetime

def make_csv(data: str, path: str, date: str):
    """maek csv function

    Args:
        data (str): dataset
        path (str): folder path to make csv
        date (str): today date
    """
    today_path = os.path.join(path, date)
    files = os.listdir(today_path)
    csv_path = os.path.join(path, data+'.csv')
    df = pd.read_csv(csv_path)

    for file in files:
        file = file[:-4].split('_')
        print(file)
        if (int(file[3]) == 2 and int(file[2]) >= 70) or (int(file[3]) == 1 and int(file[2]) >= 80):
            new_row = {'img_path': f"{date}/"+file[0]+'.jpg', 'categories_id': file[1]}
            df = df.append(new_row, ignore_index=True)
    
    df.to_csv(os.path.join(path, data+'.csv'), columns = ['img_path', 'categories_id'], index = False)

def rename_file(path: str, date: str):
    """rename file

    Args:
        path (str): folder path to make csv
        date (str): today date
    """
    today_path = os.path.join(path, date)
    files = os.listdir(today_path)
    for file in files:
        f_split = file[:-4].split('_')
        os.rename(os.path.join(today_path, file), os.path.join(today_path, f_split[0]+".jpg"))

if __name__ == "__main__":
    today = datetime.today().strftime('%Y%m%d')
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--fpath', type=str, default='/opt/ml/data2/fish', help='rename folder path')
    parser.add_argument('--spath', type=str, default='/opt/ml/data2/sashimi', help='rename folder path')
    parser.add_argument('--date', type=str, default=today, help='today date')

    args = parser.parse_args()

    make_csv('fish', args.fpath, args.date)
    make_csv('sashimi', args.spath, args.date)
    
    rename_file(args.fpath, args.date)
    rename_file(args.spath, args.date)