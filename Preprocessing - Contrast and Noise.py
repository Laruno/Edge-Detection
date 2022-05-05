import cv2
from cv2 import GaussianBlur
from matplotlib.pyplot import yticks
import numpy as np
import matplotlib.pyplot as plt
import SaltPepperNoise as noise

Samp1 = cv2.imread("Degraded Images/Sample One Blurr.jpeg")
Samp2 = cv2.imread("Greyscaled/SampleThree.png")

Resultx = noise.add_noise(Samp1)
Resulty = cv2.addWeighted(Samp2,0.2,np.zeros(Samp2.shape, Samp2.dtype), 0, 0)
cv2.imwrite("Contrast 0.2.jpg", Resulty)
titles = ["Gaussian Image","Original 3", "Gaussian + Noise Image","Contrast Degradation"]

images = [Samp1,Samp2,Resultx, Resulty]
for i in range(3):
    plt.subplot(2,2,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()

cv2.waitKey()
cv2.destroyAllWindows