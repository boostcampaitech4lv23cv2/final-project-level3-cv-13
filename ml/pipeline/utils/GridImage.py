import random
import matplotlib.pyplot as plt
import numpy as np

def grid_image(np_images, gts, preds, n=16, shuffle=False):
    """ wandb에서 n개의 validation image의 inference 결과를 보여줌

    Args:
        np_images (_type_): image to numpy
        gts (_type_): image label
        preds (_type_): model(image) output
        n (int, optional): number of image. Defaults to 16.
        shuffle (bool, optional): if you want image shuffle, set True. Defaults to False.

    Returns:
        _type_: figure on wandb
    """
    batch_size = np_images.shape[0]
    assert n <= batch_size

    choices = random.choices(range(batch_size), k=n) if shuffle else list(range(n))
    figure = plt.figure(figsize=(12, 18 + 2))  # cautions: hardcoded, 이미지 크기에 따라 figsize 를 조정해야 할 수 있습니다. T.T
    plt.subplots_adjust(top=0.8)  # cautions: hardcoded, 이미지 크기에 따라 top 를 조정해야 할 수 있습니다. T.T
    n_grid = int(np.ceil(n ** 0.5))
    tasks = ["fish"]
    for idx, choice in enumerate(choices):
        gt = gts[choice].item()
        pred = preds[choice].item()
        image = np_images[choice]
        title = "\n".join([
            f"{tasks} - gt: {gt}, pred: {pred}"
        ])

        plt.subplot(n_grid, n_grid, idx + 1, title=title)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)

        plt.imshow((image*255).astype(np.uint8))

    return figure