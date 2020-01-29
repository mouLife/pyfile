import cv2
import numpy as np
from matplotlib import pyplot as plt
image = cv2.imread('test.jpg',0)
plt.hist(image.ravel(),256,[0,256])
plt.show()
