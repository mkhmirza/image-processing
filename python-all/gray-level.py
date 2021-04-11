#!/usr/bin/python env


import cv2 as cv
import numpy as np
import preProcessing as pre
from matplotlib import pyplot as plt
import argparse

# adding parsing arguments
parser = argparse.ArgumentParser(
    description='Change gray level of a gray scale image')
parser.add_argument("--image", type=str,
                    help="path to the input image")
args = vars(parser.parse_args())

# img to be read 
imgToLoad = args["image"]
# init suplots 
fig, axes = plt.subplots(2, 2)
fig.tight_layout()
fig.suptitle("Changing Gray Levels")

# turn off the axis of images 
for i in range(0, 2):
    axes[i, 0].axis('off')

# reading an img in a grayscale mode 
img = cv.cvtColor(cv.imread(imgToLoad, 0), cv.COLOR_BGR2RGB)

axes[0, 0].set_title("Original Image (Grayscale)")
axes[0, 0].imshow(img)
# histogram
axes[0, 1].set_title("Histogram (Grayscale)")
axes[0, 1].hist(img.ravel(), 256, [0, 255])

# changing the grayscale value with a thresold
# creating a new image consisting of zeros at the moment
newImg = np.zeros(img.shape, img.dtype)

# # here we can also use 
# rev, thres = cv.threshold(img, 127, 255, cv.THRESH_BINARY)

# changing values with accessing the pixels values
# looping the rows
for i in range(0, img.shape[0]):
    # looping the cols
    for j in range(0, img.shape[1]):
        # if the pixel value is greater than 128 
        if ((img[i, j] >= 127).any()):
            # change the pixel value to 256
            # use np.clip for setting new value
            newImg[i, j] =  np.clip(255, 0, 255)
        else:  # if the value is less than 127
            # use np.clip for setting new value
            newImg[i, j] = np.clip(1, 0, 255)


# plt the new gray level img
axes[1, 0].set_title("Edited Gray Level Image")
axes[1, 0].imshow(newImg)
# histogram
axes[1, 1].set_title("Histogram (Edited Gray Level Image)")
axes[1, 1].hist(newImg.ravel(), 256, [0, 255])

plt.show()
