#!/usr/bin/python env

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import math
import argparse

# adding parsing arguments
parser = argparse.ArgumentParser( description='Performs Log transformation on an image')
parser.add_argument("-i","--image", type=str, help="path to the input image")
parser.add_argument("-o","--output", help="Output File name and path", default="")
args = vars(parser.parse_args())

# img to be read
imgToLoad = args["image"]
# output image to be saved 
output = args["output"]

# init fig, axes and subplots
rows, cols = 2, 2
fig, axes = plt.subplots(rows, cols)
fig.tight_layout()
fig.suptitle("Log Transformation")

# read the already rotated image grayscale image
img = cv.cvtColor(cv.imread(imgToLoad, 0), cv.COLOR_BGR2RGB )

# applying log transformation
# S = Clog(1+r), C (opacity) = 1

# creating a lambda function
logTransformation = lambda i: math.log2(1 + i)
# vectorize the above lambda function
vectorLogTransformation = np.vectorize(logTransformation)
# apply the function on gray scale img
improvedConstrast = vectorLogTransformation(img)

#plotting using for loop
imgs = [img, improvedConstrast]
headings = ["Grayscale","Histogram (Grayscale)", "Gray Scale (Improved Constrast)", "Histogram (Image Constrast)"]

counter = 0
for i in range(0, len(imgs)):
    axes[i, 0].axis("off")
    for j in range(0, len(imgs)):
        axes[i, j].set_title(headings[counter])
        counter += 1
    axes[i, 0].imshow(imgs[i])
    axes[i, 1].hist(imgs[i].ravel(), 256, [0, 255])

if not output == "":
    cv.imwrite(output, improvedConstrast)
    print(f"Saved: {output}")



plt.show()
