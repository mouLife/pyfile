import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np
def Gen(image):   #  plot original image histogram
    img = [0 for i in range(256)]
    wide = image.shape[0]
    hight = image.shape[1]
    for i in range(wide):
        for j in range(hight):
            gray = image[i, j]
            img[gray] += 1  # statistics all data
    y = img
    x = [i for i in range(256)]
    return x,y
def Equalize(a,image):
    b = [0 for i in range(256)]
    c = [0 for i in range(256)]
    w = image.shape[0]
    h = image.shape[1]
    mn = w * h * 1.0
    img = np.zeros([w, h], np.uint8)
    for i in range(len(a)):
        b[i] = a[i] / mn
    for i in range(len(c)):
        if i == 1:
            c[i] = b[i]
        else:
            c[i] = c[i - 1] + b[i]
            a[i] = int(255 * c[i])
    for i in range(w):
        for j in range(h):
            img[i, j] = a[image[i, j]]
    return img
def Plot():
    # plot original
    img = cv.imread('test.jpg',0)
    originalImgX,originalImgY = Gen(img)
    plt.figure("image", figsize=(8, 8))
    plt.subplot(221)
    plt.imshow(img, plt.cm.gray)  # 原始图像

    plt.title('Original')
    plt.subplot(222)
    plt.bar(originalImgX, originalImgY)
    plt.title('Original')
    # plot histogram equalize
    img_equ = Equalize(originalImgY,img)
    equ_x,equ_y = Gen(img_equ)

    plt.subplot(223)
    plt.imshow(np.array(img_equ),plt.cm.gray)
    plt.title("Equalize")
    plt.subplot(224)
    plt.bar(equ_x,equ_y, width=1)
    plt.title('Equalize')
    plt.show()
Plot()