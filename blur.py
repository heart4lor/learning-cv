import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('in/cvlogo.png')
# img[:][:][0], img[:][:][2] = img[:][:][2], img[:][:][0]

blur = cv2.medianBlur(img, 5)

plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(blur), plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()