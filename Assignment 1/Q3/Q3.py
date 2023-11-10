import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# --------------- Data initialization ---------------
# cat1 = cv.imread(r'E:\Term8\Computer Vision\Assignment1\M.Amin.Hosseinniya_9726123_Assignment1\Q3\cat1.png')
cat1 = cv.imread('cat1.png')
cat1 = cv.resize(cat1, (128,128))

# cat2 = cv.imread(r'E:\Term8\Computer Vision\Assignment1\M.Amin.Hosseinniya_9726123_Assignment1\Q3\cat2.jpg')
cat2 = cv.imread('cat2.jpg')
cat2 = cv.resize(cat2, (128,128))

# dog  = cv.imread(r'E:\Term8\Computer Vision\Assignment1\M.Amin.Hosseinniya_9726123_Assignment1\Q3\dog.jfif')
dog  = cv.imread('dog.jfif')
dog  = cv.resize(dog, (128,128))

# --------------- Extracting HOG Features ---------------
winSize     = (32,32)
blockSize   = (16,16)
blockStride = (16,16)
cellSize    = (8,8)
nbins       = 9
hog         = cv.HOGDescriptor(winSize,
                                blockSize,
                                blockStride,
                                cellSize,
                                nbins)
winStride  = (32,32)

hist1       = hog.compute(cat1,winStride)
hist2       = hog.compute(cat2,winStride)
histDog     = hog.compute(dog, winStride)

# --------------- Calculating L2 Distance ---------------
L2_cat1_dog     = np.sqrt(np.sum((hist1-histDog)**2))
L2_cat1_cat2    = np.sqrt(np.sum((hist1-hist2)**2))
L2_cat2_dog     = np.sqrt(np.sum((hist2-histDog)**2))

print('L2_cat1_dog is: ', L2_cat1_dog)
print('L2_cat1_cat2 is: ', L2_cat1_cat2)
print('L2_cat2_dog is: ', L2_cat2_dog)