import numpy as np
from skimage import exposure, io, data
import matplotlib.pyplot as plt

def histdemo():
    image = io.imread('test.jpg')
    arr = image.flatten()
    print
    plt.subplot(221)
    plt.imshow(image)
    plt.subplot(222)
    plt.hist(arr, bins=256, normed=1, edgecolor='None', facecolor='red')  # 原始图像直方图

    img1 = exposure.equalize_hist(image)
    arr1 = img1.flatten()
    plt.subplot(223)
    plt.imshow(img1, plt.cm.gray)  # 均衡化图像
    plt.subplot(224)
    plt.hist(arr1, bins=256, normed=1, edgecolor='None', facecolor='red')  # 均衡化直方图

    plt.show()


histdemo()