#!/usr/bin/python env

import cv2 as cv
import numpy as np
import preProcessing as pre
from matplotlib import pyplot as plt
import argparse

# adding parsing arguments
parser = argparse.ArgumentParser(description='Convert a gray Scale image into binary image and inverting them')
parser.add_argument('-i',"--image", type=str,help="path to the input image")
parser.add_argument('-o',"--output", help="Output image file path", default="")
args = vars(parser.parse_args())

# img to be read
imgToLoad = args["image"]
# output file name
output = args["output"]

# init suplots
rows, cols = 1, 3
fig, axes = plt.subplots(rows, cols)
fig.tight_layout()
fig.suptitle("Binarization & Inverting Image")

# reading an img in a grayscale mode
img = cv.cvtColor(cv.imread(imgToLoad, 0), cv.COLOR_BGR2RGB)

# convert the img to binary
rev, binaryImg = cv.threshold(img, 127, 255, cv.THRESH_BINARY)

# inverting
# or use this method invert = 1 - I
rev, invert = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)

imgs = [img, binaryImg, invert]
headings = ["Original Image", "Binary Image", "Invert Binary Image"]

# plotting using for loop
for i in range(0, len(imgs)):
    axes[i].axis("off")
    axes[i].set_title(headings[i])
    axes[i].imshow(imgs[i])

# saving file using --output argument
if not output == "":
    cv.imwrite(output, binaryImg)
    print(f"Saved: {output}")

plt.show()
