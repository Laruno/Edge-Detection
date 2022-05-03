import cv2
from cv2 import GaussianBlur
from matplotlib.pyplot import yticks
import numpy as np
import matplotlib.pyplot as plt



Samp1 = cv2.imread("Greyscaled/SampleOne.png")
Samp2 = cv2.imread("Greyscaled/SampleTwo.png")
#cv2.imshow("Sample One Original", Samp1)
#cv2.imshow("Sample Two Original", Samp2)
gaussianx = GaussianBlur(Samp1, (25,25), 0)
gaussiany = GaussianBlur(Samp2, (25,25), 0)
cv2.imwrite("Degraded Images/Sample One Blurred.jpeg", gaussianx)
cv2.imwrite("Degraded Images/Sample Two Blurred.jpeg", gaussiany)

titles = ["Original 1","Original 2", "Gaussan Output 1","Gaussan Output 2"]
images = [Samp1,Samp2,gaussianx,gaussiany]
for i in range(4):
    plt.subplot(2,2,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()

cv2.waitKey()
cv2.destroyAllWindows