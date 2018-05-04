import cv2
import numpy
import os

# make an array of 120000 bytes
randomByteArray = bytearray(os.urandom(120000))
# 使用 os.urandom() 函数生成原始字节
flatNumpyArray = numpy.array(randomByteArray)
# 转化成 numpt.array
# 也可以使用 numpy.random.randint(0, 256, 120000).reshape(300, 400) 来高效生成 numpy 数组

# reshape and convert array to gray image
grayImage = flatNumpyArray.reshape(300, 400)
cv2.imwrite('random_gray.png', grayImage)

# reshape and convert array to bgr image
bgrImage = flatNumpyArray.reshape(100, 400, 3)
cv2.imwrite('random_bgr.png', bgrImage)