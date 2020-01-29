import matplotlib.pyplot as plt
from skimage import io
import numpy as np
import math
def gausskernel(size):
    sigma=1.0
    gausskernel=np.zeros((size,size),np.float32)
    for i in range (size):
        for j in range (size):
            norm=math.pow(i-1,2)+pow(j-1,2)
            gausskernel[i,j]=math.exp(-norm/(2*math.pow(sigma,2)))
    sum=np.sum(gausskernel)
    kernel=gausskernel/sum
    return kernel
def gauss(i, j, da):
    kernel=gausskernel(3)
    for i in range (i-3,i+3):
        for j in range (j-3,j+3):
            sum=0
            for k in range(-1,2):
                for l in range(-1,2):
                        sum=sum+da[i+k,j+l]*kernel[k+1,l+1]
            da[i, j] = sum
    return da
if __name__ == '__main__':
    mask = io.imread('mask.png', as_gray=True)
    da = io.imread('damage_camerman.PNG', as_gray=True)
    da_copy = da.copy()
    a,b = da.shape
    for k in range(10): #这里更改迭代次数，题目要求使用高斯平滑滤波器来迭代修复图像，所以不能修复的很完美
        # 不同迭代次数会有不同的修复结果，我试过最好应该是5-8次左右，你可以自己试试
        for i in range(a):
            for j in range(b):
                if mask[i][j]<255 and i<250 and j<250:
                    da = gauss(i,j,da)
        if k==0:
            da1 = da.copy()
        if k == 1:
            da5 = da.copy()
        if k==3:
            da2 = da.copy()
        if k==6:
            da3 = da.copy()
        if k==9:
            da4 = da.copy()
    plt.figure('guass', figsize=(16,16))
    plt.subplot(231)
    plt.imshow(da_copy, plt.cm.gray)
    plt.title('Origin')
    plt.subplot(232)
    plt.imshow(da1, plt.cm.gray)
    plt.title('Number of iterations = 1')
    plt.subplot(233)
    plt.imshow(da5, plt.cm.gray)
    plt.title('Number of iterations = 2')
    plt.subplot(234)
    plt.imshow(da2, plt.cm.gray)
    plt.title('Number of iterations = 4')
    plt.subplot(235)
    plt.imshow(da3, plt.cm.gray)
    plt.title('Number of iterations = 6')
    plt.subplot(236)
    plt.imshow(da4, plt.cm.gray)
    plt.title('Number of iterations = 10')
    plt.suptitle('Degree of image repair at different iterations')
    plt.show()
