import cv2
import numpy as np
from matplotlib import pyplot as plt

img_rgb = cv2.imread('in/screenshot.png')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('in/abp.png', 0);
w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)

threshold = 0.8
loc = np.where(res >= threshold)
print(*loc)
for pt in zip(*loc):
    print(pt)
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

cv2.imwrite('out/res.png', img_rgb)