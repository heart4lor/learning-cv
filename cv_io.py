import cv2

grayImage = cv2.imread('in/len_std.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imwrite('out/len_gray.png', grayImage)
cv2.namedWindow('lenna')
cv2.imshow('lenna', grayImage)
cv2.waitKey()