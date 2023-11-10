import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# --------------- Data initialization ---------------
# img1 = cv.imread(r'E:\Term8\Computer Vision\Assignment1\M.Amin.Hosseinniya_9726123_Assignment1\Q6\mech.jpg')
img1 = cv.imread('mech.jpg')
img1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)

# img2 = cv.imread(r'E:\Term8\Computer Vision\Assignment1\M.Amin.Hosseinniya_9726123_Assignment1\Q6\mech2.jpg')
img2 = cv.imread('mech2.jpg')
img2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

# --------------- Applying SIFT ---------------
nfeatures         = 0
nOctaveLayers     = 3
edgeThreshold     = 10
sigma             = 1.6

sift              = cv.SIFT_create(nfeatures=nfeatures,
                                    nOctaveLayers=nOctaveLayers,
                                    edgeThreshold=edgeThreshold,
                                    sigma=sigma)

kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)
bf        = cv.BFMatcher()
matches   = bf.knnMatch(des1,des2,k=2)

good = []
for m,n in matches:
    if m.distance < 0.75*n.distance:
        good.append([m])

# Showing results:
img3 = cv.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
plt.imshow(img3)
plt.xticks([]), plt.yticks([])
plt.show()