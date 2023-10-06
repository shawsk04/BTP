import cv2
from matplotlib import pyplot as plt

# reading image
img = cv2.imread("2.jpeg")

# converting image in RGB format
color = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# converting image in grayscale format
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


mean_thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 51, 25)        #Better
gaussian_thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 51, 25)

# Original image in gray scale
# plt.figure("Gray Image")
# plt.imshow(gray, cmap="gray")


#---------------------------------------------------------------------------------------------------------#
plt.figure("Mean Thresholding")

# calculation of crack area
crackArea_Mean = 0
for i in mean_thresh:
    for j in i:
        if(j == 0):  
            crackArea_Mean+=1

percentCrack_Mean = (crackArea_Mean / (len(mean_thresh) * len(mean_thresh[0]))) * 100

print("Percentage crack = ", 100 - percentCrack_Mean)

plt.imshow(mean_thresh, cmap="gray")


#----------------------------------------------------------------------------------------------------------#
plt.figure("Gaussian Thresholding")

# calculation of crack area
crackArea_Gaussian = 0
for i in gaussian_thresh:
    for j in i:
        if(j == 0):  
            crackArea_Gaussian+=1

percentCrack_Gaussian = (crackArea_Gaussian / (len(gaussian_thresh) * len(gaussian_thresh[0]))) * 100

print("Percentage crack = ", 100 - percentCrack_Gaussian)

plt.imshow(gaussian_thresh, cmap="gray")

plt.show()
