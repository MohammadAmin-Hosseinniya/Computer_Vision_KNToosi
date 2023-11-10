import cv2
import numpy as np
import matplotlib.pyplot as plt

# --------------- Data initialization ---------------
# img1 = cv2.imread('E:\Term8\Computer Vision\Assignment1\M.Amin.Hosseinniya_9726123_Assignment1\Q1\Image1.jpg')
img1 = cv2.imread('Image1.jpg')
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
height1, width1, _ = img1.shape

# img2 = cv2.imread('E:\Term8\Computer Vision\Assignment1\M.Amin.Hosseinniya_9726123_Assignment1\Q1\Image2.jpg')
img2 = cv2.imread('Image2.jpg')
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
height2, width2, _ = img2.shape

# img3 = cv2.imread('E:\Term8\Computer Vision\Assignment1\M.Amin.Hosseinniya_9726123_Assignment1\Q1\Image3.jpg')
img3 = cv2.imread('Image3.jpg')
img3 = cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)
height3, width3, _ = img3.shape

# img4 = cv2.imread('E:\Term8\Computer Vision\Assignment1\M.Amin.Hosseinniya_9726123_Assignment1\Q1\Image4.jpg')
img4 = cv2.imread('Image4.jpg')
img4 = cv2.cvtColor(img4, cv2.COLOR_BGR2RGB)
height4, width4, _ = img4.shape

# --------------- Source Points ---------------
p_src1 = np.array([[138, 220],
                   [370, 280],
                   [43, 463],
                   [292, 536]])

p_src2 = np.array([[318, 328],
                   [378, 456],
                   [114, 397],
                   [180, 540]])

p_src3 = np.array([[114, 155],
                   [436, 172],
                   [146, 698],
                   [500, 658]])

p_src4 = np.array([[259, 286],
                   [412, 385],
                   
                   [91, 515],
                   [265, 630]])

# --------------- Destination Points ---------------
p_dst1 = np.array([[0,0],
                   [width1, 0],
                   [0, height1],
                   [width1, height1]])

p_dst2 = np.array([[0,0],
                   [width2, 0],
                   [0, height2],
                   [width2, height2]])

p_dst3 = np.array([[0,0],
                   [width3, 0],
                   [0, height3],
                   [width3, height3]])

p_dst4 = np.array([[0,0],
                   [width4, 0],
                   [0, height4],
                   [width4, height4]])

# --------------- Warping Images ---------------
H, _ = cv2.findHomography(p_src1, p_dst1, method=0)
img1Warped = cv2.warpPerspective(img1, H, (width1, height1))

H, _ = cv2.findHomography(p_src2, p_dst2, method=0)
img2Warped = cv2.warpPerspective(img2, H, (width2, height2))

H, _ = cv2.findHomography(p_src3, p_dst3, method=0)
img3Warped = cv2.warpPerspective(img3, H, (width3, height3))

H, _ = cv2.findHomography(p_src4, p_dst4, method=0)
img4Warped = cv2.warpPerspective(img4, H, (width4, height4))

# --------------- Showing Results ---------------
images = [img1, img1Warped, img2, img2Warped, img3, img3Warped, img4, img4Warped]
titles = ['Image1', 'Image1 warped', 'Image2', 'Image2 warped', 'Image3', 'Image3 warped', 'Image4', 'Image4 warped']

for i in range(4):
    plt.subplot(1,2,1), plt.imshow(images[2*i])
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
    plt.subplot(1,2,2), plt.imshow(images[2*i+1])
    plt.title(titles[2*i+1])
    plt.xticks([]), plt.yticks([])
    plt.show()
