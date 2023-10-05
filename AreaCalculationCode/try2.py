import cv2
from matplotlib import pyplot as plt

img = cv2.imread("crack6.jpg")
color = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

mean_thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 1001, 25)        #Better
gaussian_thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 1001, 25)

plt.figure("Gray Image")
plt.imshow(gray, cmap="gray")

plt.figure("Mean Thresholding")
plt.imshow(mean_thresh, cmap="gray")

plt.figure("Gaussian Thresholding")
plt.imshow(gaussian_thresh, cmap="gray")
plt.show()
