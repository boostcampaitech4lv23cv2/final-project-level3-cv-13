
def confusion_matrix(labels, preds, class_items, CLASSES):

    # 0으로 채워진 class_items에서 label과 pred을 받아 confusion matrix 작성
    class_items[CLASSES.index(preds)][CLASSES.index(labels)] += 1
    
    return class_items


def accuracy(class_items, CLASSES):
    
    # confusion matrix에서 tp 부분인 대각성분을 받아서 전체 개수로 나눠서 accuracy 계산
    return sum([class_items[i][i] for i in range(len(CLASSES))])/sum(sum(class_items))


def macro_f1(class_items, CLASSES):
    
    # class별 macro_f1을 담기 위한 dict 생성
    macro_f1_items = dict()
    
    for i in len(CLASSES):
        
        # tp, fp, fn 등 f1 계산에 필요한 요소 계산
        tp = class_items[i][i]
        fp = sum(class_items[:][i]-tp)
        fn = sum(class_items[i][:]-tp)
        
        # precision & recall 계산
        precision = (tp/(tp+fp))
        recall = (tp/(tp+fn))
        f1_score = 2*precision*recall/(precision + recall)
    
        macro_f1_items[CLASSES[i]] = f1_score
        
    return sum(macro_f1_items.values())/len(macro_f1_items)