import torch.optim
import wandb

def SGD(model):    
    return torch.optim.SGD(params= model.parameters(),lr= wandb.config.lr)

def Momentum(model):
    try:
        momentum = wandb.config.momentum        
    except:
        momentum = 0.01
        
    return torch.optim.SGD(params= model.parameters(),lr= wandb.config.lr, momentum=momentum)

def Adam(model):
    try:
        weight_decay = wandb.config.weight_decay
    except:
        weight_decay = 5e-4
    
    return torch.optim.Adam(params= filter(lambda p: p.requires_grad, model.parameters()),lr= wandb.config.lr, weight_decay=weight_decay)

def AdamW(model):
    try:
        weight_decay = wandb.config.weight_decay
    except:
        weight_decay = 5e-4
    return torch.optim.AdamW(params= model.parameters(),lr= wandb.config.lr, weight_decay=weight_decay)

def Adagrad(model):
    try:
        weight_decay = wandb.config.weight_decay
    except:
        weight_decay = 5e-4
    return torch.optim.Adagrad(params= model.parameters(),lr= wandb.config.lr, weight_decay=weight_decay)

