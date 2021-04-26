#!/usr/bin/python env

import cv2 as cv
import numpy as np
import preProcessing as pre
from matplotlib import pyplot as plt
import argparse

# adding cmd parser
parser = argparse.ArgumentParser(description='Apply Mean Smoothing Filter')
parser.add_argument('--image', help='Path to input image.')
parser.add_argument("--output", help="Output File name and path", default="")
args = vars(parser.parse_args())

imgToLoad = args["image"]
output = args["output"]

# init subplots
rows, cols = 1, 2
fig, axs = plt.subplots(rows, cols)
fig.tight_layout()
fig.suptitle("Applying Mean Smoothing Filter")

# loading image in grayscale mode
img = cv.imread(imgToLoad, 0)

meanFilter = [[1/9, 1/9, 1/9], [1/9, 1/9, 1/9], [1/9, 1/9, 1/9]]
# applying laplacian matrix
kernel = np.array(meanFilter)
# also can use cv.medianBlur(src, ksize, dst)
mean = cv.filter2D(img, -1, kernel=kernel)

imgs = [img, mean]
headings = ["Original Image",  "After Smoothing"]

for i in range(0, len(imgs)):
    axs[i].axis("off")
    axs[i].imshow(imgs[i], cmap='gray')
    axs[i].set_title(headings[i])

if not output == "":
    cv.imwrite(output, mean)
    print(f"Saved: {output}")

plt.show()
