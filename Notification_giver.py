import time
from plyer import *
import cv2
import numpy as np
from matplotlib import pyplot as plt

if __name__ == "__main__":
    print("Started")
    notification.notify(
        title = "Drink Water!",
        message = "1. Drinking Water Helps Maintain the Balance of "
                  "Body Fluids. Your body is composed of about 60% water. ",
        app_icon = "Glass.ico",
        timeout = 10
    )
print("Hello World")
print("Hey there")
img = cv2.imread('watch.jpg',cv2.IMREAD_GRAYSCALE)

plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.plot([200,300,400],[100,200,300],'c', linewidth=5)
plt.show()
