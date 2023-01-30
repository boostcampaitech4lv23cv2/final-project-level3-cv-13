import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from dataloader import CLASSES


# 52번째 줄 print 제거 필요
# cm_image 함수 table 이름 잘 보이게 정리 필요
# accuracy, macro_f1 정확한지 확인 필요
# 카테고리 이미지가 없을 때 NaN으로 표시 되는 오류 해결 필요

def confusion_matrix(labels, preds, class_items, CLASSES):

    # val_batch size만큼 받아온 preds, labels를 묶어서 표로 만들어준다
    for pred, label in zip(preds, labels):

        # 0으로 채워진 class_items에서 label과 pred을 받아 confusion matrix 작성
        class_items[CLASSES.index(int(pred))][CLASSES.index(int(label))] += 1
    
    return class_items


def accuracy(class_items, CLASSES):
    
    # confusion matrix에서 tp 부분인 대각성분을 받아서 전체 개수로 나눠서 accuracy 계산
    return sum([class_items[i][i] for i in range(len(CLASSES))])/sum(sum(class_items))


def macro_f1(class_items, CLASSES):
    tp = 0
    fp = 0
    fn = 0
    # class별 macro_f1을 담기 위한 dict 생성
    macro_f1_items = dict()
    
    for i in range(len(CLASSES)):
        
        # tp, fp, fn 등 f1 계산에 필요한 요소 계산
        tp = class_items[i][i]
        fp = sum(class_items[:][i])-tp
        fn = sum(class_items[i][:])-tp

        # precision & recall 계산
        if tp == 0 and fp == 0:
            precision = 0
        else:     
            precision = (tp/(tp+fp))
            
        if tp == 0 and fn == 0:
            recall = 0 
        else:
            recall = (tp/(tp+fn))

        if precision == 0 and recall == 0:
            f1_score = 0
        else:
            f1_score = 2*precision*recall/(precision + recall)
    
        macro_f1_items[CLASSES[i]] = f1_score
        
    print(macro_f1_items)       
    return sum(macro_f1_items.values())/len(macro_f1_items)

def cm_image(confusion_matrix):
    cm_figure = plt.figure(figsize=(24, 20))
    fig, ax =plt.subplots(1,1)
    data= confusion_matrix

    column_labels = CLASSES
    row_labels =CLASSES

    ax.axis('off')

    axtable = ax.table(cellText=data, rowLabels=row_labels, colLabels=column_labels, cellLoc='center', loc="center", cellColours=plt.cm.RdYlGn(data/100))
    axtable.scale(1,3)

    plt.show()

    return fig