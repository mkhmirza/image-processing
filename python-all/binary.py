#!/usr/bin/python env


import cv2 as cv
import numpy as np
import preProcessing as pre
from matplotlib import pyplot as plt
import argparse

# adding parsing arguments
parser = argparse.ArgumentParser(description='Convert a gray Scale image into binary image and inverting them')
parser.add_argument("--image", type=str,
                help="path to the input image")
args = vars(parser.parse_args())

# img to be read
imgToLoad = args["image"]
# init suplots
fig, axes = plt.subplots(1, 3)
fig.tight_layout()
fig.suptitle("Binarization & Inverting Image")

# reading an img in a grayscale mode
img = cv.cvtColor(cv.imread(imgToLoad, 0), cv.COLOR_BGR2RGB)
axes[0].set_title("Original Image (Grayscale)")
axes[0].imshow(img)

# convert the img to binary
rev, binaryImg = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
# or you can use the previous pixel acessing method
# see gray-level.py
axes[1].set_title("Binary Image")
axes[1].imshow(binaryImg)

# inverting
# or use this method invert = 1 - I
rev, invert = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
axes[2].set_title("Binary Image (Invert)")
axes[2].imshow(invert)

plt.show()
