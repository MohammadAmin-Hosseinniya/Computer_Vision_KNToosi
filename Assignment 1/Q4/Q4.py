import cv2
import numpy as np
import matplotlib.pyplot as plt

# --------------- Data initialization ---------------
truss1 = cv2.imread(r'E:\Term8\Computer Vision\Assignment1\M.Amin.Hosseinniya_9726123_Assignment1\Q4\truss1.jpg')
# truss1 = cv2.imread('truss1.jpg')
truss2 = cv2.imread(r'E:\Term8\Computer Vision\Assignment1\M.Amin.Hosseinniya_9726123_Assignment1\Q4\truss2.jpg')
# truss2 = cv2.imread('truss2.jpg')

# Sobel_x and Sobel_y:
SobelX1 = cv2.Sobel(truss1,-1,dx=1,dy=0,ksize=5)
SobelX2 = cv2.Sobel(truss2,-1,dx=1,dy=0,ksize=5)

SobelY1 = cv2.Sobel(truss1,-1,dx=0,dy=1,ksize=5)
SobelY2 = cv2.Sobel(truss2,-1,dx=0,dy=1,ksize=5)

# Laplacian:
Laplacian1 = cv2.Laplacian(truss1, -1, ksize=5)
Laplacian2 = cv2.Laplacian(truss2, -1, ksize=5)

# LoG (Lapplacian of Gaussian):
kernel = np.array([[0, -1, 0],
                   [-1, 4, -1],
                   [0, -1, 0]])
LoG1 = cv2.filter2D(truss1, -1, kernel)
LoG2 = cv2.filter2D(truss2, -1, kernel)

# DoG (Difference of Gaussian): 
blur1_1 = cv2.GaussianBlur(truss1, (21,21), sigmaX=1.6, sigmaY=1.6)
blur1_2 = cv2.GaussianBlur(truss1, (3,3), sigmaX=1.6, sigmaY=1.6)

DoG1 = cv2.subtract(blur1_1, blur1_2)


blur2_1 = cv2.GaussianBlur(truss2, (21,21), sigmaX=1.6, sigmaY=1.6)
blur2_2 = cv2.GaussianBlur(truss2, (3,3), sigmaX=1.6, sigmaY=1.6)

DoG2 = cv2.subtract(blur2_1, blur2_2)

# canny:
canny1 = cv2.Canny(truss1, 80, 150)
canny2 = cv2.Canny(truss2, 250, 320)

# Showing results:
img1 = [truss1, SobelX1, SobelY1, Laplacian1, LoG1, DoG1, canny1]
img2 = [truss2, SobelX2, SobelY2, Laplacian2, LoG2, DoG2, canny2] # LoG1, LoG2, DoG1, DoG2
titles1 = ['Truss1 Original', 'SobelX truss1', 'SobelY truss1', 'Laplacian truss1', 'LoG truss1', 'Dog1', 'canny truss1']
titles2 = ['Truss2 Original', 'SobelX truss2', 'SobelY truss2', 'Laplacian truss2', 'LoG truss2', 'Dog2', 'canny truss2']

for i in range(7):
    plt.subplot(4,2,i+1)
    plt.imshow(img1[i]), plt.title(titles1[i])
    plt.xticks([]), plt.yticks([])
plt.show()

for i in range(7):
    plt.subplot(4,2,i+1)
    plt.imshow(img2[i]), plt.title(titles2[i])
    plt.xticks([]), plt.yticks([])
plt.show()