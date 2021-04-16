#!/usr/bin/python env

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import argparse

# adding parsing arguments
parser = argparse.ArgumentParser(description='Splits rgb into red, green and blue channel')
parser.add_argument("--image", type=str, help="path to image file")
args = vars(parser.parse_args())

# read this file
imgToLoad = args["image"]
fig, axes = plt.subplots(1, 4)
fig.tight_layout()
fig.suptitle("Splitting Image into Red, Green & Blue")

# img to load
imgRgb = cv.cvtColor(cv.imread(imgToLoad), cv.COLOR_BGR2RGB)

# split channel using cv.split
(r, g, b) = cv.split(imgRgb)

imgs = [imgRgb, r, g, b]
headings = ["Orignal Image", "Red Channel", "Green Channel", "Blue Channel"]

for i in range(0, len(imgs)):
    axes[i].axis("off")
    axes[i].set_title(headings[i])
    axes[i].imshow(imgs[i], cmap='gray')
    # uncomment if wanna save the indivvual files 
    # cv.imwrite(f"dataset/{headings[i]}.jpg", imgs[i] )

plt.show()






