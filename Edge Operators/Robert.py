import cv2
from cv2 import GaussianBlur
from cv2 import medianBlur
from matplotlib.pyplot import yticks
import numpy as np
import matplotlib.pyplot as plt

img0 = cv2.imread("Greyscaled/SampleThree.png")
img1 = cv2.imread("Histogram Equalized.jpg")
img2 = cv2.imread("SingContrast 0.2.jpg")
img3 = cv2.imread("Degraded Images/Sample One Blurr.jpeg")
Robertx = np.array([[0,1],[-1,0]])

Roberty = np.array([[1, 0],[0,-1]])

edge_p1 = cv2.filter2D(img1,-1, Robertx)+ cv2.filter2D(img1,-1, Roberty)
edge_p2 = cv2.filter2D(img2,-1, Robertx) + cv2.filter2D(img2,-1, Roberty)
edge_p3 = cv2.filter2D(img3,-1, Robertx)+ cv2.filter2D(img3,-1, Roberty)
edge_p4 = cv2.filter2D(img0,-1, Robertx)+ cv2.filter2D(img0,-1, Roberty)

titles = ["Original","Histogram Equalized","Contrast Dark","Median Filtered"]

images = [edge_p4,edge_p1,edge_p2, edge_p3]
for i in range(4):
    plt.subplot(2,2,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()

cv2.waitKey()
cv2.destroyAllWindows()