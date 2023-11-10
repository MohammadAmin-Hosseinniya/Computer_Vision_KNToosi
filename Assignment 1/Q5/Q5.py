import cv2
import numpy as np
import matplotlib.pyplot as plt

# --------------- Data initialization ---------------
logo = cv2.imread('E:\Term8\Computer Vision\Assignment1\M.Amin.Hosseinniya_9726123_Assignment1\Q5\kntu.jpg')
# logo = cv2.imread('kntu.jpg')
logo = cv2.cvtColor(logo, cv2.COLOR_BGR2RGB)
logo = cv2.resize(logo, (int(logo.shape[1]/2), int(logo.shape[0]/2)))

back = cv2.imread('E:\Term8\Computer Vision\Assignment1\M.Amin.Hosseinniya_9726123_Assignment1\Q5\mech.jpg')
# back = cv2.imread('mech.jpg')
back = cv2.cvtColor(back, cv2.COLOR_BGR2RGB)

# --------------- Preparing logo ---------------
# b,g,r = cv2.split(logo)
logoGray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
ret, maskForLogo = cv2.threshold(logoGray, 180, 255, cv2.THRESH_BINARY_INV)
maskedLogo = cv2.bitwise_and(logo, logo, mask=maskForLogo)

# --------------- Preparing background ---------------
# print(logo.shape)
roi = back[int((back.shape[0]/2)-(logo.shape[0]/2)):int((back.shape[0]/2)+(logo.shape[0]/2)), int((back.shape[1]/2)-(logo.shape[1]/2)):int((back.shape[1]/2)+(logo.shape[1]/2))]
# ret, maskForRoi = cv2.threshold(logoGray, 180, 255, cv2.THRESH_BINARY)
maskForRoi = cv2.bitwise_not(maskForLogo)
maskedRoi = cv2.bitwise_and(roi, roi, mask=maskForRoi)
roi = cv2.add(maskedRoi, maskedLogo)

# --------------- Adding logo to background ---------------
back[int((back.shape[0]/2)-(logo.shape[0]/2)):int((back.shape[0]/2)+(logo.shape[0]/2)), int((back.shape[1]/2)-(logo.shape[1]/2)):int((back.shape[1]/2)+(logo.shape[1]/2))] = roi

# Showing results:
plt.imshow(back)
plt.xticks([]), plt.yticks([])
plt.show()