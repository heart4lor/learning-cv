import cv2
import numpy as np

img = cv2.imread('in/len_std.jpg')

res = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation = cv2.INTER_CUBIC)

cv2.imwrite('out/resize.jpg', res)