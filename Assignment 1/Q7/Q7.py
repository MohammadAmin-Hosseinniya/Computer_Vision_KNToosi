import cv2
import numpy as np
import matplotlib.pyplot as plt

# --------------- Data initialization ---------------
# original = cv2.imread(r'E:\Term8\Computer Vision\Assignment1\M.Amin.Hosseinniya_9726123_Assignment1\Q7\xray.jpg')
original = cv2.imread('xray.jpg')

# Linear filters:
blur = cv2.blur(original, (5,5))
gaussian = cv2.GaussianBlur(original, (5,5), 0)
bilateral = cv2.bilateralFilter(original,9, 75, 75)

# Nonlinear filter:
median = cv2.medianBlur(original, 5)

# Showing results:
img = [original, blur, gaussian, bilateral, median]
title = ['Original Image', 'Blurred Image', 'Gaussian Blurred Image', 'Bilateral Image', 'Median blurred Image']

for i in range(5):
    plt.subplot(2,3,i+1)
    plt.imshow(img[i]), plt.title(title[i])
    plt.xticks([]), plt.yticks([])
plt.show()