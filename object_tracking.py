import cv2
import numpy as np

cap = cv2.VideoCapture(0)

lower_img = cv2.imread('in/r.png')
upper_img = cv2.imread('in/upper_red.png')

lower_img = cv2.cvtColor(lower_img, cv2.COLOR_BGR2HSV)
upper_img = cv2.cvtColor(upper_img, cv2.COLOR_BGR2HSV)

print([int(lower_img.shape[0]/2), int(lower_img.shape[1]/2)])

lower_hsv = np.array(lower_img[int(lower_img.shape[0]/2), int(lower_img.shape[1]/2)])
upper_hsv = np.array(upper_img[int(upper_img.shape[0]/2), int(upper_img.shape[1]/2)])

print(lower_hsv, upper_hsv)

while(1):

    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # lower_red = np.array(lower_hsv-[5, 60, 30])
    # upper_red = np.array(lower_hsv+[5, 60, 30])
    lower_red = np.array([0, 0, 0])
    upper_red = np.array([10, 255, 130])

    mask = cv2.inRange(hsv, lower_red, upper_red)

    res = cv2.bitwise_and(frame, frame, mask = mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    k = cv2.waitKey(5)
    if k == 27:
        break

cv2.destroyAllWindows()
