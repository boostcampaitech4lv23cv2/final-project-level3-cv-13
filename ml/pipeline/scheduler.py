import torch.optim.lr_scheduler as lr_scheduler
import wandb

def step_lr(optimizer):
    try: 
        step_size = wandb.config.step_size
        gamma = wandb.config.gamma
    except:
        step_size = 50
        gamma = 0.5
    return lr_scheduler.StepLR(optimizer, step_size, gamma)

def lambda_lr(optimizer):
    try:
        lr_lambda = wandb.config.lr_lambda
    except AttributeError:
        lr_lambda = lambda epoch: 0.95 ** epoch
    return lr_scheduler.LambdaLR(optimizer, lr_lambda)

def multistep_lr(optimizer):
    try:
        milestone = wandb.config.milestone
        gamma = wandb.config.gamma
    except:
        milestone = [30, 80]
        gamma = 0.5
    return lr_scheduler.MultiStepLR(optimizer, milestone, gamma)

def exponential_lr(optimizer):
    try:
        gamma = wandb.config.gamma
    except:
        gamma = 0.5
    return lr_scheduler.ExponentialLR(optimizer, gamma)

def cosine_annealing_lr(optimizer):
    try:
        T_max = wandb.config.T_max
    except:
        T_max = 20
    return lr_scheduler.CosineAnnealingLR(optimizer, T_max)

def cosine_annealing_warm_restarts_lr(optimizer):
    try:
        T_0 = wandb.config.T_0
    except:
        T_0 = 20
    return lr_scheduler.CosineAnnealingWarmRestarts(optimizer, T_0)

def reduce_on_plateau_lr(optimizer):
    try:
        mode = wandb.config.mode
    except:
        mode = "min"
    return lr_scheduler.ReduceLROnPlateau(optimizer, mode)

def cyclic_lr(optimizer):
    try:
        base_lr = wandb.config.base_lr
        max_lr = wandb.config.max_lr
    except:
        base_lr = 0.0001
        max_lr = 0.001
    return lr_scheduler.CyclicLR(optimizer, base_lr, max_lr)