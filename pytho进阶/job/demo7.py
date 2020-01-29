import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np
# 画直方图
def zhifangtu(image):
    print(type(image))
    print("-------------")
    a = [0] * 256  # 创建储存像素数的一维数组
    w = image.shape[0]  # 得到图像宽高
    h = image.shape[1]
    # 计算灰度像素数
    for i in range(w):
        for j in range(h):
            gray = image[i, j]
            a[gray] += 1
    # 以灰度为x轴像素数为y轴画直方图
    y = a
    x = [i for i in range(256)]
    plt.figure()
    plt.title("zhifangtu")
    plt.xlabel("Bins")
    plt.ylabel("Pixels")
    plt.plot(x, y)
    plt.xlim([0, 256])
    return a  # 返回灰度像素数


# 将图像均衡化



image = cv.imread("test.jpg",0)  # 读取灰度图像
cv.imshow("base", image)
print(image)
a = zhifangtu(image)  # 画原始图像直方图并得到灰度像素数

plt.show()
