# -*- coding: utf-8 -*-
"""HW4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Pg2fYEO4NGjgv6YQjQpwtmQkzXj3sFrV

## Global
"""

import numpy as np
import cv2
from google.colab.patches import cv2_imshow
import matplotlib.pyplot as plt

#download image
# !wget -O rice.png "https://raw.githubusercontent.com/ozgunsungar/count-rice/main/rice%20(1).png"
!wget -O rice.png https://raw.githubusercontent.com/ozgunsungar/count-rice/main/rice.png

"""## First Approach (BEST)"""

image = cv2.imread('rice.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray, (7,7), 0)

ret, thresh = cv2.threshold(gray,120,255, cv2.THRESH_BINARY)

canny = cv2.Canny(blur,50, 100)

dilated = cv2.dilate(canny, (1, 1), iterations=0)

(cnt, hierarchy) = cv2.findContours(
    dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.drawContours(rgb, cnt, -1, (0, 255, 0), 2)

imgContour = image.copy()

fig= plt.figure()
fig.set_figheight(15)
fig.set_figwidth(24)

fig.add_subplot(1,4,1)
plt.title("Input Image")
plt.imshow(image, cmap='gray')

fig.add_subplot(1,4,2)
plt.title("Output image of thresholding")
plt.imshow(thresh, cmap='gray')

fig.add_subplot(1,4,3)
plt.title("Output image of morphological operations")
plt.imshow(dilated, cmap='gray')

fig.add_subplot(1,4,4)
plt.title("Output image of number of rices : {0}".format(len(cnt)))
plt.imshow(rgb, cmap='gray')

"""## Second Approach"""

#Open the picture 
img=cv2.imread( 'rice.png',0 )
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

kernel=np.ones(( 5 , 5 ),np.uint8)
erosion=cv2.erode(img,kernel,iterations= 6 )
dilation=cv2.dilate(erosion,kernel,iterations= 4 )

#Original image minus the background to get the shape of rice grains
backImg=dilation
rice=img-backImg

#Thresholding
ret, th1 = cv2.threshold(rice,20,255, cv2.THRESH_BINARY)

#Morphological operations
kernel = np.ones((5,5), np.uint8)
opening = cv2.morphologyEx(th1, cv2.MORPH_OPEN, kernel)

kernel=np.ones(( 3 , 3 ),np.uint8)
erosion=cv2.erode(opening,kernel,iterations= 1 )
rice = opening - erosion

#Contour detection
(cnt, hierarchy) = cv2.findContours(
    rice.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.drawContours(rgb, cnt, -1, (0, 255, 0), 2)

#Display
fig= plt.figure()
fig.set_figheight(15)
fig.set_figwidth(24)

fig.add_subplot(1,4,1)
plt.title("Input Image")
plt.imshow(img, cmap='gray')

fig.add_subplot(1,4,2)
plt.title("Output image of thresholding")
plt.imshow(th1, cmap='gray')

fig.add_subplot(1,4,3)
plt.title("Output image of morphological operations")
plt.imshow(rice, cmap='gray')

fig.add_subplot(1,4,4)
plt.title("Output image of number of rices : {0}".format(len(cnt)))
plt.imshow(rgb, cmap='gray')