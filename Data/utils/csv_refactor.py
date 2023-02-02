import pandas as pd
import os
import os.path as osp

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

def csv_refactor(path, category):
    """여러개의 csv를 하나로 합쳐줍니다.

    Args:
        path (_type_): dataset folder들의 상위 path
    """
    folder_list = os.listdir(path)
    new_data = pd.DataFrame(columns=('img_path', 'categories_id'))
    category_name = fish_category if category == 'fish' else sashimi_category
    
    for folder in folder_list:
        
        if folder[-4:] == '.csv':
            continue

        csv_path = osp.join(path, folder, 'label.csv')
        data = pd.read_csv(csv_path)
        for idx in enumerate(data):
            data['img_name'][0] = folder + '/' + data['img_name'][0]
            data['label'][1] = category_name[folder]
            
        new_data = pd.concat(new_data, data)
    new_data.to_csv(osp.join(path,f'{category}1.csv'))

if __name__ == "__main__":
    fish_path = '/opt/ml/data/fish'
    sashimi_path = '/opt/ml/data/sashimi'
    csv_refactor(fish_path, 'fish')
    csv_refactor(sashimi_path, 'sashimi')
