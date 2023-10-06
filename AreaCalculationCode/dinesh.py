import cv2
import numpy as np


def segment_image(image_path):
    
    image = cv2.imread(image_path)


    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    
    _, binary_image = cv2.threshold(gray_image, 70, 300, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    
    mask = cv2.cvtColor(binary_image, cv2.COLOR_GRAY2BGR)

    total = mask.shape[0] * mask.shape[1]
    black= np.sum(mask[:, :, 0] == 0)  
    percentage = (black / total) * 100

    print("Percentage of Crack: {:.2f}%".format(percentage))


    cv2.imshow('Original Image', image)
    cv2.imshow('Segmented Image', mask)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

image_path = '1.jpeg'
segment_image(image_path)