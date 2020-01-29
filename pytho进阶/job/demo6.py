import numpy as np
from skimage import exposure, io, data
import matplotlib.pyplot as plt


image = io.imread('test.jpg')
arr = image.flatten()
print(arr)
hist, bin_centers = exposure.histogram(arr)
hist = list(hist)
hist.insert(0,0)
hist.append(0)
bin_centers = list(bin_centers)
bin_centers.insert(0,0)
bin_centers.append(255)
plt.plot(bin_centers,hist,c='red')
plt.xlim([0, 256])
plt.show()