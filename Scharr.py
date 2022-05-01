import matplotlib
import cv2
import numpy
import sympy
import pandas as pd

img = cv2.imread("Image Processing Reference/SampleFour.jpg",0)
cv2.imwrite("Greyscaled/SampleFour.png",img)

cv2.waitKey(0)
cv2.destroyAllWindows