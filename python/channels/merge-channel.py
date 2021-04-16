#!/usr/bin/python env

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import argparse

# adding parsing arguments
parser = argparse.ArgumentParser(description='Merges red, green and blue channel into the original image')
parser.add_argument("--red", type=str, help="path to red channel")
parser.add_argument("--green", type=str,help="path to green channel")
parser.add_argument("--blue", type=str,help="path to blue channel")
args = vars(parser.parse_args())

# read 3 images, red channel, green and blue channel
r = args["red"]
g = args["green"]
b = args["blue"]

fig, axes = plt.subplots(1, 4)
fig.tight_layout()
fig.suptitle("Merging Image into Red, Green & Blue")

# img to load in grayscale mode
red = cv.imread(r, 0)
green = cv.imread(g, 0)
blue = cv.imread(b, 0)

original = cv.merge([red, green, blue])

imgs = [red, green, blue, original]
headings = ["Red Channel", "Green Channel", "Blue Channel","Orignal Image"]

for i in range(0, len(imgs)):
    axes[i].axis("off")
    axes[i].set_title(headings[i])
    axes[i].imshow(imgs[i], cmap='gray')
    
plt.show()
