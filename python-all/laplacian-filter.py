#!/usr/bin/python env

# applys laplacian filter (Edge Detection)

import cv2 as cv
import numpy as np
import preProcessing as pre
from matplotlib import pyplot as plt
import argparse

# adding cmd parser
parser = argparse.ArgumentParser(
    description='Applying Laplacian Filter for Sharpening images')
parser.add_argument('--image', help='Path to input image.')
args = vars(parser.parse_args())

imgToLoad = args["image"]

fig, axs = plt.subplots(1, 3)
fig.tight_layout()
fig.suptitle("Applying Laplacian Filter (Edge Detection)")

# loading image in grayscale mode
img = cv.imread(imgToLoad, 0)

# applying laplacian matrix 
kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
laplacian = cv.filter2D(img, -1, kernel=kernel)

# sharpened image
sharpenImg = cv.absdiff(img, laplacian)


imgs = [img, laplacian, sharpenImg]
headings = ["Original Image", "Edge Detection", "Sharpened Image"]


for i in range(0, len(imgs)):
    axs[i].axis("off")
    axs[i].imshow(imgs[i], cmap='gray')
    axs[i].set_title(headings[i])

plt.show()




