import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np
from skimage import exposure
def zhifangtu(image):
    a = [0] * 256
    w = image.shape[0]
    h = image.shape[1]
    # 计算灰度像素数
    for i in range(w):
        for j in range(h):
            gray = image[i, j]
            a[gray] += 1
    return a
def Bhattacharyya(image1,image2):
    lens = len(image1)
    image1=list(image1)
    image2 = list(image2)
    BhattacharyyaCoefficient = 0.0
    for i in range(lens):
        BhattacharyyaCoefficient += np.sqrt(image1[i]*image2[i])
    print("The value of Bhattacharyya Coefficient is:",BhattacharyyaCoefficient)
    return BhattacharyyaCoefficient
image1 = cv.imread("day.png",0)
b = image1.shape[0] * image1.shape[1]
a = np.array(zhifangtu(image1))
gailvA = a/b
image2 = cv.imread("night.png",0)
c = image2.shape[0] * image2.shape[1]
d = np.array(zhifangtu(image2))
gailvB = d/c
getBhattacharyyaCoefficient = Bhattacharyya(gailvA,gailvB)

plt.figure("images", figsize=(8, 8))
plt.subplot(221)
plt.imshow(image1,cmap=plt.cm.gray)
cent1,histogramDay = exposure.histogram(image1,nbins=256)
print(cent1)
plt.subplot(222)
plt.hist(cent1,256)
plt.subplot(223)
plt.imshow(image2,cmap=plt.cm.gray)
cent2,histogramNight = exposure.histogram(image2,nbins=256)
plt.subplot(224)
plt.hist(cent2,256)
plt.suptitle("The value of Bhattacharyya Coefficient is:"+str(getBhattacharyyaCoefficient))
plt.show()
