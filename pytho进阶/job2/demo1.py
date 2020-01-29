from skimage import filters,io
import matplotlib.pyplot as plt
img1 = io.imread('noise1.jpg')
img2 = io.imread('noise2.png',as_grey=True)
edges1 = filters.gaussian(img1,sigma=1.5) #sigma=0.4
edges2 = filters.gaussian(img2,sigma=1.5) #sigma=5
plt.figure('gaussian',figsize=(8,8))
plt.subplot(121)
plt.imshow(edges1,plt.cm.gray)
plt.subplot(122)
plt.imshow(edges2,plt.cm.gray)
plt.show()