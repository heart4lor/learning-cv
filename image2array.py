import cv2
import numpy as np

img = cv2.imread('len_std.jpg')
print(type(img))
print(img.shape)
print(img.dtype)

# img[0, 0] = [255, 255, 255]
print(img.item(150, 120, 0))
img.itemset((150, 120, 0), 255)
print(img.item(150, 120, 0))
# 更改单个像素值，通过 item 和 itemset 访问单个像素通道

print(img[150, 120])
img[:, :, 2] = 0
# 通过切片操作将 BGR 通道中的 Red 全部设置为 0
print(img[150, 120])

my_roi = img[0:64, 0:64]
img[100:164, 100:164] = my_roi


cv2.namedWindow('img')
cv2.imshow('img', img)
cv2.waitKey()