#!/usr/bin/python env

import cv2 as cv
import numpy as np
import preProcessing as pre
from matplotlib import pyplot as plt
import argparse

# adding cmd parser
parser = argparse.ArgumentParser(description='Applying Histogram Equalization')
parser.add_argument('--image', help='Path to input image.')
args = vars(parser.parse_args())

imgToLoad = args["image"]

# init subplots
rows, cols = 2, 2
fig, axs = plt.subplots(rows, cols)
fig.tight_layout()
fig.suptitle("Applying Histogram Equalization")

# loading image in grayscale mode
img = cv.imread(imgToLoad, 0)

# histogram equalization on img source
histEqualized = cv.equalizeHist(img)

imgs = [img, histEqualized]

counter = 0
for i in range(0, len(imgs)):
    axs[i, 0].axis("off")
    axs[i, 0].imshow(imgs[i], cmap='gray')
    axs[i, 1].hist(imgs[i].ravel(), 256, [0, 255])


plt.show()
