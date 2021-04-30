#!/usr/bin/python env

import cv2 as cv
import numpy as np
import preProcessing as pre
from matplotlib import pyplot as plt
import argparse

# adding cmd parser
parser = argparse.ArgumentParser(description='Comparison Between 2 Pictures using Histogram')
parser.add_argument('-i','--image', help='Path to input image.')
parser.add_argument('-i2','--image2', help="Path to second input image")
args = vars(parser.parse_args())

imgToLoad = args["image"]
img2ToLoad = args["image2"]

# init subplots
if img2ToLoad:
    rows, cols = 2, 2
else:
    # only show 1 image with its histogram
    rows, cols = 1, 2
fig, axs = plt.subplots(rows, cols)
fig.tight_layout()
fig.suptitle("Comparsion Using Histogram")

# loading image in grayscale mode
img = cv.imread(imgToLoad, 0)

# read second image if given
if img2ToLoad:
    img2 = cv.imread(img2ToLoad, 0)
    imgs = [img, img2]
else:
    imgs = [img]
    
counter = 0
# if 2nd image is given for comparision
if img2ToLoad:
    for i in range(0, len(imgs)):
        axs[i, 0].axis("off")
        axs[i, 0].imshow(imgs[i], cmap='gray')
        axs[i, 1].hist(imgs[i].ravel(), 256, [0, 255])
else: # if only there is 1 image for histogram calc
    axs[0].axis("off")
    axs[0].imshow(img, cmap='gray')
    axs[1].hist(img.ravel(), 256, [0, 255])

plt.show()
