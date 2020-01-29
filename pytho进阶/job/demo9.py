# using skimage compute gray scale histogram to make a comparison
import numpy as np
from skimage import exposure, io, data
import matplotlib.pyplot as plt
image = io.imread('test.jpg')
arr = image.flatten()
print(arr)
hists, bin_centers = exposure.histogram(arr)
print(bin_centers)
print(hists)
# hists = list(filter(lambda x:x!=0,list(hists)))
# print(hists)
plt.hist(hists,256,[0,256],normed=1, edgecolor='None', facecolor='red')
plt.show()