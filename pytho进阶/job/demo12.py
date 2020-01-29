from skimage import data,exposure,io,color
import matplotlib.pyplot as plt
import numpy as np
def Bhattacharyya(image1,image2):
    lens = len(image1)
    image1=list(image1)
    image2 = list(image2)

    BhattacharyyaCoefficient = 0.0
    for i in range(lens):
        BhattacharyyaCoefficient += np.square(image1[i]*image2[i])
    print(BhattacharyyaCoefficient)
def MaxMinNormalization(x):
    """[0,1] normaliaztion"""
    x = (x - np.min(x)) / (np.max(x) - np.min(x))
    return x

import cv2 as cv
# day picture
img1 = io.imread('day.png',as_grey=True)
print(img1)
img1 = color.rgb2gray(img1)
plt.figure("image", figsize=(8, 8))
plt.subplot(221)
plt.imshow(img1,cmap=plt.cm.gray)
cent1,histogramDay = exposure.histogram(img1,nbins=256)
plt.subplot(222)
plt.hist(cent1,256)

# img1 = img1.flatten()
# print(img1)
#night picture
img2 = io.imread('night.png',as_grey=True)
img2 = color.rgb2gray(img2)
plt.subplot(223)
plt.imshow(img2,cmap=plt.cm.gray)

# img2 = img2.flatten()
cent2,histogramNight = exposure.histogram(img2)
plt.subplot(224)
plt.hist(cent2,256)

plt.show()

Bhattacharyya(histogramDay,histogramNight)


