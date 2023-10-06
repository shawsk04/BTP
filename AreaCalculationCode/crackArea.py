# Importing required libraries
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("3.jpeg")
color_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray_img, 220, 255, cv2.THRESH_BINARY)


# inverting image values
# thus cracked area will be represented in black
# and non cracked area in white 
segmentedImage = thresh
for i in range(len(segmentedImage)):
    for j in range(len(segmentedImage[i])):
        if(segmentedImage[i][j] == 0):
            segmentedImage[i][j] = 255
        elif(segmentedImage[i][j] == 255):
            segmentedImage[i][j] = 0


# original image
plt.figure("ORIGINAL")
plt.imshow(color_img)

# segmented image
plt.figure("Segmented Image")
plt.imshow(segmentedImage, cmap = "gray")

# Calculation of cracked area in segmented image
CrackArea = 0
for i in thresh:
    for j in i:
        if(j == 0):  
            CrackArea += 1

# calculating total slab area in image
totalSlabArea = len(segmentedImage) * len(segmentedImage[0])

percentCrackArea = (CrackArea / totalSlabArea) * 100
print("Percentage Crack Area = ", percentCrackArea)

plt.show()