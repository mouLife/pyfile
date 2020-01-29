from skimage import data,exposure,io
import matplotlib.pyplot as plt


def Gen(image): # plot original image histogram
    img = [0 for i in range(256)]
    wide = image.shape[0]
    hight = image.shape[1]
    for i in range(wide):
        for j in range(hight):
            gray = image[i, j]
            img[gray] += 1  # statistics all data
    y = img
    x = [i for i in range(256)]
    plt.figure()
    plt.title("histogram")
    plt.xlabel("Bins")  # different bins
    plt.plot(x, y)
    plt.xlim([0, 256])
    plt.show()




def Plot():

    img=io.imread('test.jpg')
    plt.figure("hist",figsize=(8,8))
    arr=img.flatten()
    #



    plt.subplot(221)
    plt.imshow(img,plt.cm.gray) #原始图像
    plt.subplot(222)
    plt.hist(arr, bins=256, normed=1,edgecolor='None',facecolor='red') #原始图像直方图

    img1=exposure.equalize_hist(img) #进行直方图均衡化
    arr1=img1.flatten() #返回数组折叠成一维的副本
    plt.subplot(223)
    plt.imshow(img1,plt.cm.gray) #均衡化图像
    plt.subplot(224)
    plt.hist(arr1, bins=256, normed=1,edgecolor='None',facecolor='red') #均衡化直方图
    plt.show()