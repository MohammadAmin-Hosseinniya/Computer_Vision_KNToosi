import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

corrects = 0
# labels = # read a text file. red: 0; yellow: 1; green: 2;
# labels = split(labels)

img_bgr = cv2.imread(r'image5.jpg')
img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)

cv2.imshow('HSV', img_hsv)

green_mask = cv2.inRange(img_hsv, (45, 25, 25), (65, 255,255))
yellow_mask = cv2.inRange(img_hsv, (22, 93, 0), (45, 255, 255))
red_mask1 = cv2.inRange(img_hsv, (0, 120, 70), (10, 255, 255))
red_mask2 = cv2.inRange(img_hsv, (170, 120, 70), (180, 255, 255))
red_mask = red_mask1 + red_mask2

plt.subplot(131)
plt.imshow(green_mask)
plt.subplot(132)
plt.imshow(yellow_mask)
plt.subplot(133)
plt.imshow(red_mask)
plt.show()

if np.count_nonzero(red_mask) >= np.count_nonzero(green_mask) and np.count_nonzero(red_mask) >= np.count_nonzero(yellow_mask):
    color = 0    # red
elif np.count_nonzero(yellow_mask) >= np.count_nonzero(red_mask) and np.count_nonzero(yellow_mask) >= np.count_nonzero(green_mask):
    color = 1    # yellow
elif np.count_nonzero(green_mask) >= np.count_nonzero(red_mask) and np.count_nonzero(green_mask) >= np.count_nonzero(yellow_mask):
    color = 2    # green

# if color == labels[i]:
    # corrects += 1
print(color)
# plt.imshow(m)