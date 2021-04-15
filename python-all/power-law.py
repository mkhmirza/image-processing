#!/usr/bin/python env

# performs power law transformation

import preProcessing
import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np
import argparse

# adding parsing arguments
parser = argparse.ArgumentParser(
    description='Performs Power Law Transformation Method')
parser.add_argument("--image", type=str, help="path to image file")

args = vars(parser.parse_args())

imgToLoad = args["image"]

# init figures 
fig, axes = plt.subplots(3, 2)
fig.suptitle("Power Law Transformation")
# increasing the hspace between subplots 
fig.tight_layout()

# perform rotation on the given image
img = cv.imread(imgToLoad)

# # rotating the image to 90 degree counter clockwise
# if you wann rotate uncomment this line
# imgRotated = preProcessing.rotateImage(img, rotationType=cv.ROTATE_90_COUNTERCLOCKWISE)
# # rgb2gray()
# imgRotatedRgb = cv.cvtColor(imgRotated, cv.COLOR_BGR2RGB)

# # save rotated img  
# cv.imwrite("img_dark-rotated90.jpg", imgRotated)

# to not change every instance of this 
imgRotatedRgb = img
imgRotated = img

# plotting the rotated image
axes[0, 0].axis("off")
axes[0, 0].set_title('Original Image')
axes[0, 0].imshow(imgRotatedRgb)

# plotting histogram
axes[0, 1].set_title("Histogram (Original)")
axes[0 ,1].hist(imgRotated.ravel(), 256, [0, 255])

# conver the rotated image into a gray scale
grayScale = cv.cvtColor(imgRotated, cv.COLOR_RGB2GRAY)
# plotting the gray scale image now
axes[1, 0].axis("off")
axes[1, 0].set_title("Gray Scale Image")
axes[1, 0].imshow(grayScale, cmap='gray', vmin=0, vmax=255)

# plotting histogram of the grayscale image
axes[1, 1].set_title("Histogram (Gray Scale)")
axes[1, 1].hist(grayScale.ravel(), 256, [0, 255])

gamma = float(input("Enter Value for gamma: "))

# perform the s = r^(gamma) of light information
imgEnhanced = np.array(255 * (grayScale / 255) ** gamma, dtype='uint8')

# plotting the new grayscale
axes[2, 0].axis("off")
axes[2, 0].set_title("Gray Scale (Improved Contrast)")
axes[2, 0].imshow(imgEnhanced, cmap='gray', vmin=0, vmax=255)

# plotting the histogram for new enhanced version of the grayscale image
axes[2, 1].set_title("Histogram (Improved Contrast)")
axes[2, 1].hist(imgEnhanced.ravel(), 256, [0, 255])

plt.show()


