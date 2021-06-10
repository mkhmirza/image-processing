#!/usr/bin/python env

import cv2 as cv
import numpy as np
import preProcessing as pre
from matplotlib import pyplot as plt
import argparse

# adding parsing arguments
parser = argparse.ArgumentParser(description='Apply any filter on the image')
parser.add_argument('-i', "--image", type=str, help="path to the input image")
parser.add_argument('-o', "--output", help="Output image file path", default="")
args = vars(parser.parse_args())

# img to be read
imgToLoad = args["image"]
# output file name
output = args["output"]

# init suplots
rows, cols = 1, 2
fig, axs = plt.subplots(rows, cols)
fig.tight_layout()
fig.suptitle("Apply Filter")

# read an image in gray mode
img = cv.imread(imgToLoad, 0)

# generating a 3,3 filter
fil = [[0 for i in range(3)] for x in range(3)]
print(fil)
# input filter values
for i in range(0, len(fil)):
    for j in range(0, len(fil)):
        fil[i][j] = float(input(f"Enter Value({i},{j}): "))

# convert filter into a numpy array
fil = np.array(fil)

# apply filter on the img
filteredImg = cv.filter2D(img, -1, kernel=fil)

imgs = [img, filteredImg]
headings = ["Original Image", "Filtered Image"]

for i in range(0, len(imgs)):
    axs[i].axis("off")
    axs[i].imshow(imgs[i], cmap='gray')
    axs[i].set_title(headings[i])
plt.show()