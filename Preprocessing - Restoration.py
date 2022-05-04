import cv2
from cv2 import GaussianBlur
from cv2 import medianBlur
from matplotlib.pyplot import yticks
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread("Degraded Images/SingContrast 0.5.jpg")
img2 = cv2.imread("Degraded Images/salt-and-pepper.jpg")

equ = cv2.equalizeHist(img1)
histr = cv2.calcHist([equ],[0],None,[256],[0,256])
filtered1 = medianBlur(img2,7)
kernel = np.array([[0,-1,0], [-1,5,-1], [0,-1,0]])
image_sharp = cv2.filter2D(filtered1,-1, kernel)

titles = ["Contrast 0.2","Salt and Pepper image", "Equalized Histogram","Median Filtered"]

images = [img2,filtered1]
for i in range(2):
    plt.subplot(2,2,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()

cv2.waitKey()
cv2.destroyAllWindows()