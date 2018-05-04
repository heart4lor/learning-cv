import cv2

grayImage = cv2.imread('len_std.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imwrite('len_gray.png', grayImage)
cv2.namedWindow('lenna')
cv2.imshow('lenna', grayImage)
cv2.waitKey()