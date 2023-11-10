import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# --------------- Data initialization ---------------
img_noGoal1  = cv.imread('No_Goal_1.jpg')
img_noGoal2  = cv.imread('No_Goal_2.jpg')
img_Goal1    = cv.imread('Goal_1.jpg')
img_Goal2    = cv.imread('Goal_2.jpg')

img_noGoal1 = cv.cvtColor(img_noGoal1, cv.COLOR_BGR2RGB)
img_noGoal1_gray = cv.cvtColor(img_noGoal1, cv.COLOR_RGB2GRAY)

img_noGoal2 = cv.cvtColor(img_noGoal2, cv.COLOR_BGR2RGB)
img_noGoal2_gray = cv.cvtColor(img_noGoal2, cv.COLOR_RGB2GRAY)

img_Goal1 = cv.cvtColor(img_Goal1, cv.COLOR_BGR2RGB)
img_Goal1_gray = cv.cvtColor(img_Goal1, cv.COLOR_RGB2GRAY)

img_Goal2 = cv.cvtColor(img_Goal2, cv.COLOR_BGR2RGB)
img_Goal2_gray = cv.cvtColor(img_Goal2, cv.COLOR_RGB2GRAY)


images = [img_noGoal1, img_noGoal2, img_Goal1, img_Goal2]
images_gray = [img_noGoal1_gray, img_noGoal2_gray, img_Goal1_gray, img_Goal2_gray]

# --------------- Detecting Circles and lines ---------------
minRadius = 70
maxRadius = 80

# img_noGoal1:
img_noGoal1_gray_gaussian = cv.GaussianBlur(img_noGoal1_gray, ksize=(13,13), sigmaX=1.6)
img_noGoal1_gray = cv.blur(img_noGoal1_gray, (17,17), 0)
# edge = cv.Canny(image_gray, 120, 60)
circles = cv.HoughCircles(img_noGoal1_gray, cv.HOUGH_GRADIENT, 1, 2,
        param1=60,
        param2=10,
        minRadius=minRadius,
        maxRadius=maxRadius)

circles = np.uint16(np.around(circles))
i = 0
center_col = circles[0][i][0]
center_row = circles[0][i][1]
radius = circles[0][i][2]

cv.circle(img_noGoal1,(center_col,center_row),radius,(0,0,255))

edges = cv.Canny(img_noGoal1_gray_gaussian, 150, 100)
minLineLength = 750
maxLineGap = 50
lines = cv.HoughLinesP(edges,
                        rho=1,
                        theta=np.pi/36,
                        threshold=200,
                        minLineLength=minLineLength,
                        maxLineGap=maxLineGap)
for line in lines:
    for x1,y1,x2,y2 in line:
        cv.line(img_noGoal1,(x1,y1),(x2,y2),(0,255,0),2)

if center_row+radius < np.min(lines[...,1]):
    cv.putText(img_noGoal1, text='Goal!', org=(10, 560), fontFace=cv.FONT_HERSHEY_TRIPLEX, fontScale=3, color=(0, 0, 0),thickness=3)
    print('Goaaaaalll!!!')
else:
    print('No Goal...')
    cv.putText(img_noGoal1, text='No Goal...', org=(10, 560), fontFace=cv.FONT_HERSHEY_TRIPLEX, fontScale=3, color=(0, 0, 0),thickness=3)
plt.imshow(img_noGoal1)
plt.show()




# img_noGoal2:
img_noGoal2_gray_gaussian = cv.GaussianBlur(img_noGoal2_gray, ksize=(13,13), sigmaX=1.6)
img_noGoal2_gray = cv.blur(img_noGoal2_gray, (17,17), 0)
# edge = cv.Canny(image_gray, 120, 60)
circles = cv.HoughCircles(img_noGoal2_gray, cv.HOUGH_GRADIENT, 1, 2,
        param1=70,
        param2=10,
        minRadius=minRadius,
        maxRadius=maxRadius)

circles = np.uint16(np.around(circles))
i = 0
center_col = circles[0][i][0]
center_row = circles[0][i][1]
radius = circles[0][i][2]

cv.circle(img_noGoal2,(center_col,center_row),radius,(0,0,255))

edges = cv.Canny(img_noGoal2_gray_gaussian, 150, 100)
minLineLength = 750
maxLineGap = 50
lines = cv.HoughLinesP(edges,
                        rho=1,
                        theta=np.pi/36,
                        threshold=200,
                        minLineLength=minLineLength,
                        maxLineGap=maxLineGap)
for line in lines:
    for x1,y1,x2,y2 in line:
        cv.line(img_noGoal2,(x1,y1),(x2,y2),(0,255,0),2)

if center_row+radius < np.min(lines[...,1]):
    cv.putText(img_noGoal2, text='Goal!', org=(10, 560), fontFace=cv.FONT_HERSHEY_TRIPLEX, fontScale=3, color=(0, 0, 0),thickness=3)
    print('Goaaaaalll!!!')
else:
    print('No Goal...')
    cv.putText(img_noGoal2, text='No Goal...', org=(10, 560), fontFace=cv.FONT_HERSHEY_TRIPLEX, fontScale=3, color=(0, 0, 0),thickness=3)
plt.imshow(img_noGoal2)
plt.show()




# img_Goal1:
img_Goal1_gray_gaussian = cv.GaussianBlur(img_Goal1_gray, ksize=(13,13), sigmaX=1.6)
img_Goal1_gray = cv.blur(img_Goal1_gray, (17,17), 0)
# edge = cv.Canny(image_gray, 120, 60)
circles = cv.HoughCircles(img_Goal1_gray, cv.HOUGH_GRADIENT, 1, 2,
        param1=60,
        param2=10,
        minRadius=minRadius,
        maxRadius=maxRadius)

circles = np.uint16(np.around(circles))
i = 0
center_col = circles[0][i][0]
center_row = circles[0][i][1]
radius = circles[0][i][2]

cv.circle(img_Goal1,(center_col,center_row),radius,(0,0,255))

edges = cv.Canny(img_Goal1_gray_gaussian, 150, 100)
minLineLength = 750
maxLineGap = 50
lines = cv.HoughLinesP(edges,
                        rho=1,
                        theta=np.pi/36,
                        threshold=200,
                        minLineLength=minLineLength,
                        maxLineGap=maxLineGap)
for line in lines:
    for x1,y1,x2,y2 in line:
        cv.line(img_Goal1,(x1,y1),(x2,y2),(0,255,0),2)

if center_row+radius < np.min(lines[...,1]):
    cv.putText(img_Goal1, text='Goal!', org=(10, 560), fontFace=cv.FONT_HERSHEY_TRIPLEX, fontScale=3, color=(0, 0, 0),thickness=3)
    print('Goaaaaalll!!!')
else:
    print('No Goal...')
    cv.putText(img_Goal1, text='No Goal...', org=(10, 560), fontFace=cv.FONT_HERSHEY_TRIPLEX, fontScale=3, color=(0, 0, 0),thickness=3)
plt.imshow(img_Goal1)
plt.show()




# img_Goal2:
img_Goal2_gray_gaussian = cv.GaussianBlur(img_Goal2_gray, ksize=(13,13), sigmaX=1.6)
img_Goal2_gray = cv.blur(img_Goal2_gray, (17,17), 0)
# edge = cv.Canny(image_gray, 120, 60)
circles = cv.HoughCircles(img_Goal2_gray, cv.HOUGH_GRADIENT, 1, 2,
        param1=80,
        param2=10,
        minRadius=minRadius,
        maxRadius=maxRadius)

circles = np.uint16(np.around(circles))
i = 0
center_col = circles[0][i][0]
center_row = circles[0][i][1]
radius = circles[0][i][2]

cv.circle(img_Goal2,(center_col,center_row),radius,(0,0,255))


edges = cv.Canny(img_Goal2_gray_gaussian, 150, 100)
minLineLength = 750
maxLineGap = 50
lines = cv.HoughLinesP(edges,
                        rho=1,
                        theta=np.pi/36,
                        threshold=200,
                        minLineLength=minLineLength,
                        maxLineGap=maxLineGap)
for line in lines:
    for x1,y1,x2,y2 in line:
        cv.line(img_Goal2,(x1,y1),(x2,y2),(0,255,0),2)

if center_row+radius < np.min(lines[...,1]):
    cv.putText(img_Goal2, text='Goal!', org=(10, 560), fontFace=cv.FONT_HERSHEY_TRIPLEX, fontScale=3, color=(0, 0, 0),thickness=3)
    print('Goaaaaalll!!!')
else:
    print('No Goal...')
    cv.putText(img_Goal2, text='No Goal...', org=(10, 560), fontFace=cv.FONT_HERSHEY_TRIPLEX, fontScale=3, color=(0, 0, 0),thickness=3)
plt.imshow(img_Goal2)
plt.show()
