import cv2
from matplotlib import pyplot as plt

img = cv2.imread("1.jpeg")
color = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
ret2, thresh2 = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)        #Best
# ret3, thresh3 = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_TRIANGLE)
 
# plt.figure("GRAY")
# plt.imshow(gray_img, cmap="gray")

plt.figure("ORIGINAL")
plt.imshow(color)

# plt.figure("BINARY")
# plt.imshow(thresh, cmap = "gray")
# print(ret)

plt.figure("OTSU")
plt.imshow(thresh2, cmap="gray")
# print(ret2)

# plt.figure("TRIANGLE")
# plt.imshow(thresh3, cmap="gray")
# print(ret3)

crack = 0
for i in thresh2:
    for j in i:
        if(j == 0):  
            crack+=1

percent_crack = (crack / (len(thresh2) * len(thresh2[0]))) * 100
print("Percentage crack = ", percent_crack)

plt.show()