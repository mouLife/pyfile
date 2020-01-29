import cv2 as cv
import matplotlib.pyplot as plt
from skimage import io
import numpy as np
import math
da = io.imread('mask.png',as_gray = True)
print(da)