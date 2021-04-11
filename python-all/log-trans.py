#!/usr/bin/python env


# performs log transformation

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import math
import argparse

# adding parsing arguments
parser = argparse.ArgumentParser(
    description='Performs Log transformation on an image')
parser.add_argument("--image", type=str,
                    help="path to the input image")
args = vars(parser.parse_args())

# img to be read
imgToLoad = args["image"]

# init fig, axes and subplots
rows, cols = 3, 2
fig, axes = plt.subplots(rows, cols)
fig.tight_layout()
fig.suptitle("Log Transformation")

# read the already rotated image, convert open cv bgr to rgb
img = cv.cvtColor(cv.imread(imgToLoad), cv.COLOR_BGR2RGB )
# plot the color img and its histogram
axes[0, 0].axis("off")
axes[0, 0].set_title('Original Image')
axes[0, 0].imshow(img)

# plotting histogram
axes[0, 1].set_title('Histogram (Original Image)')
axes[0, 1].hist(img.ravel(), 256, [0, 255])

# convert to grayscale
grayScale = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
# plot gray scale img
axes[1, 0].axis("off")
axes[1, 0].set_title('Gray Scale')
axes[1, 0].imshow(grayScale, cmap='gray')

# plotting histogram
axes[1, 1].set_title('Histogram (Gray Scale Image)')
axes[1, 1].hist(grayScale.ravel(), 256, [0, 255])

# applying log transformation
# S = Clog(1+r), C (opacity) = 1

# creating a lambda function
logTransformation = lambda i: math.log2(1 + i)
# vectorize the above lambda function
vectorLogTransformation = np.vectorize(logTransformation)
# apply the function on gray scale img
improvedConstrast = vectorLogTransformation(grayScale)

# plot log transformed img
axes[2, 0].axis("off")
axes[2, 0].set_title('Gray Scale (Improved Constrast)')
axes[2, 0].imshow(improvedConstrast, cmap='gray')

# plotting histogram
axes[2, 1].set_title('Histogram (Image Constrast)')
axes[2, 1].hist(improvedConstrast.ravel(), 256, [0, 255])

plt.show()
