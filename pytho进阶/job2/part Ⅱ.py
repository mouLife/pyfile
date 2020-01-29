from skimage import filters,io,morphology
import matplotlib.pyplot as plt
def median_filter(image):
    a = filters.median(image,morphology.disk(1))
    return a
def gaussian_filter(image):
    a = filters.gaussian(image,sigma=1.5)
    return a
img1 = io.imread('noise1.jpg',as_grey=True)

# median_filter
img1_med = median_filter(img1)

#gaussian_filter
img1_gau = gaussian_filter(img1)

plt.figure('median',figsize=(8,8))
plt.subplot(221)
plt.imshow(img1,plt.cm.gray)
plt.title('origin')
plt.subplot(222)
plt.imshow(img1_med,plt.cm.gray)
plt.title('median_filter to cope salt&pepper noise(disk=1)')

plt.subplot(223)
plt.imshow(img1,plt.cm.gray)
plt.title('origin')
plt.subplot(224)
plt.imshow(img1_gau,plt.cm.gray)
plt.title('gaussian_filter to cope salt&pepper noise(sigma=1.5)')

plt.suptitle('gaussian sigma = 1.5 and median disk = 1  (can change)')
plt.show()