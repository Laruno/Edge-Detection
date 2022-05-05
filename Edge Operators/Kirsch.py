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

KirschN = np.array([[-3,-3,5],[-3,0,5], [-3,-3,5]])
KirschNW = np.array([[-3,5,5],[-3,0,5],[-3,-3,-3]])
KirschW = np.array([[5,5,5],[-3,0,-3],[3,-3,-3]])
KirschSW = np.array([[5,5,-3],[5,0,-3],[-3,-3,-3]])
KirschS = np.array([[5,-3,-3],[5,0,-3],[5,-3,-3]])
KirschSE = np.array([[-3,-3,-3],[5,0,-3],[5,5,-3]])
KirschE = np.array([[-3,-3,-3],[-3,0,-3],[5,5,5]])
KirschNE = np.array([[-3,-3,-3],[-3,0,5],[-3,5,5]])

edge_p1 = (cv2.filter2D(img1,-1, KirschN) + cv2.filter2D(img1,-1, KirschNW)+
           cv2.filter2D(img1,-1, KirschW) + cv2.filter2D(img1,-1, KirschSW)+ 
           cv2.filter2D(img1,-1, KirschS) + cv2.filter2D(img1,-1, KirschSE)+
           cv2.filter2D(img1,-1, KirschE) + cv2.filter2D(img1,-1, KirschNE))

edge_p2 = (cv2.filter2D(img2,-1, KirschN) + cv2.filter2D(img2,-1, KirschNW)+
           cv2.filter2D(img2,-1, KirschW) + cv2.filter2D(img2,-1, KirschSW)+ 
           cv2.filter2D(img2,-1, KirschS) + cv2.filter2D(img2,-1, KirschSE)+
           cv2.filter2D(img2,-1, KirschE) + cv2.filter2D(img2,-1, KirschNE))

edge_p3 = (cv2.filter2D(img3,-1, KirschN) + cv2.filter2D(img3,-1, KirschNW)+
           cv2.filter2D(img3,-1, KirschW) + cv2.filter2D(img3,-1, KirschSW)+ 
           cv2.filter2D(img3,-1, KirschS) + cv2.filter2D(img3,-1, KirschSE)+
           cv2.filter2D(img3,-1, KirschE) + cv2.filter2D(img3,-1, KirschNE))

edge_p4 = (cv2.filter2D(img0,-1, KirschN) + cv2.filter2D(img0,-1, KirschNW)+
           cv2.filter2D(img0,-1, KirschW) + cv2.filter2D(img0,-1, KirschSW)+ 
           cv2.filter2D(img0,-1, KirschS) + cv2.filter2D(img0,-1, KirschSE)+
           cv2.filter2D(img0,-1, KirschE) + cv2.filter2D(img0,-1, KirschNE))


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