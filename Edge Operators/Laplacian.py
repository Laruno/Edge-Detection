import cv2
from cv2 import GaussianBlur
from cv2 import medianBlur
from cv2 import Laplacian
from matplotlib.pyplot import yticks
import numpy as np
import matplotlib.pyplot as plt

img0 = cv2.imread("Greyscaled/SampleThree.png")
img1 = cv2.imread("Histogram Equalized.jpg")
img2 = cv2.imread("SingContrast 0.2.jpg")
img3 = cv2.imread("Degraded Images/Sample One Blurr.jpeg")

blur_img0 = cv2.GaussianBlur(img0, (3,3),0)
blur_img1 = cv2.GaussianBlur(img1, (3,3),0)
blur_img2 = cv2.GaussianBlur(img2, (3,3),0)
blur_img3 = cv2.GaussianBlur(img3, (3,3),0)


Laplacian0 = cv2.Laplacian(blur_img0, cv2.CV_64F)
Laplacian1 = cv2.Laplacian(blur_img1, cv2.CV_64F)
Laplacian2 = cv2.Laplacian(blur_img2, cv2.CV_64F)
Laplacian3 = cv2.Laplacian(blur_img3, cv2.CV_64F)

titles = ["Original","Histogram Equalized","Contrast Dark","Median Filtered"]

images = [Laplacian0,Laplacian1,Laplacian2, Laplacian3]
for i in range(4):
    plt.subplot(2,2,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()

cv2.waitKey()
cv2.destroyAllWindows()