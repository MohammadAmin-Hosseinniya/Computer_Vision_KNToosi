import cv2
import numpy as np
import matplotlib.pyplot as plt

# --------------- Data initialization ---------------
img = cv2.imread('E:\Term8\Computer Vision\Assignment1\M.Amin.Hosseinniya_9726123_Assignment1\Q2\quarter_circle.png')
# img = cv2.imread('quarter_circle.png')
b,g,r = cv2.split(img)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
ret, imgBinary = cv2.threshold(b, 195, 255, cv2.THRESH_BINARY_INV)
row, column = imgBinary.shape
imgBinary = imgBinary.astype(int)

# --------------- Calculating area of circle ---------------
x = np.zeros((1, column))
y = np.zeros((row,1))

toBeDeleted = []
for i in range(column):
    x[0][i] = np.count_nonzero(imgBinary[:,i])

    if x[0][i] == 0 or x[0][i] == 2:
        toBeDeleted = np.append(toBeDeleted, i)

toBeDeleted = toBeDeleted.astype(int)
x = np.delete(x, toBeDeleted, axis=1)
x = np.delete(x, [0,1,-1], axis=1)
x = x.astype(int)

toBeDeleted = []
for i in range(row):
    y[i] = np.count_nonzero(imgBinary[i,:])

    if y[i][0] == 0 or y[i][0] == 2:
        toBeDeleted = np.append(toBeDeleted, i)

toBeDeleted = toBeDeleted.astype(int)
y = np.delete(y, toBeDeleted, axis=0)
y = y.astype(int)
y = np.delete(y, [0,-1,-2], axis=0)

A = np.sum(x)

# --------------- Calculating coordinates of centroid of the circle in image space ---------------
sumY = 0

for i in range(len(y)):
    sumY += (len(y)-i)*y[i][0]
Y = int(sumY/A)

sumX = 0

for i in range(len(x[0])):
    sumX += i*x[0][i]
X = int(sumX/A)

print('X is: ', X)
print('Y is: ', Y)
print('')

# --------------- Calculating coordinates of centroid of the circle in real world coordinates ---------------
offsetX = 0
stop = False
while not stop:
    if np.count_nonzero(imgBinary[:,offsetX]) == x[0][0]:
        stop = True
    offsetX += 1
# print('offsetX is: ',offsetX)

offsetY = 0
stop = False
while not stop:
    if np.count_nonzero(imgBinary[offsetY,:]) == y[-1][0]:
        stop = True
    offsetY += 1
# print('offsetY is: ',offsetY)

realX = X + offsetX
realY = offsetY - Y
print('realX is: ', realX)
print('realY is: ', realY)
print('')

# --------------- Analytical solution ---------------
print('radius (according to rows) is: ', np.max(x))
print('radius (according to columns) is: ', np.max(y))
print('')
radius = np.max(x)
X_Analytical = (4*radius)/(3*np.pi)
Y_Analytical = (4*radius)/(3*np.pi)

print('X_Analytical is: ', X_Analytical)
print('Y_Analytical is: ', Y_Analytical)

# --------------- Showing Result ---------------
img = cv2.circle(img, (realY, realX), 0, (255,0,0), 10)
plt.imshow(img)
plt.show()