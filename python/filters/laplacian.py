#!/usr/bin/python env

import cv2 as cv
import numpy as np
import preProcessing as pre
from matplotlib import pyplot as plt
import argparse

# adding cmd parser
parser = argparse.ArgumentParser(description='Apply Image Sharpening Filter')
parser.add_argument('--image', help='Path to input image.')
parser.add_argument('--variant', help="Enter Variant of Laplacian", default="ori")
parser.add_argument("--output", help="Output File name and path", default="")
args = vars(parser.parse_args())

imgToLoad = args["image"]
variant = args["variant"]
output = args["output"]

# init subplots
rows, cols = 1, 3
fig, axs = plt.subplots(rows, cols)
fig.tight_layout()
fig.suptitle("Applying Laplacian Filter (Edge Detection)")

# loading image in grayscale mode
img = cv.imread(imgToLoad, 0)

# if passed argument is original version 
if variant == "ori":
    laplacianMatrix = [[0, 1, 0], [1, -4, 1], [0, 1, 0]]
elif variant == "v1": # else apply variant 1
    laplacianMatrix = [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]
elif variant == "v2":
    laplacianMatrix = [[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]]
else: # if invalid option is passed 
    print("Invalid Variant! Assigning Original Laplcian Matrix")
    laplacianMatrix = [[0, 1, 0], [1, -4, 1], [0, 1, 0]]

# applying laplacian matrix 
kernel = np.array(laplacianMatrix)
laplacian = cv.filter2D(img, -1, kernel=kernel)
# laplacian = cv.Laplacian(img, -1, ksize=5)

sharpen = cv.subtract(img, laplacian)
print(sharpen)
imgs = [img, laplacian, sharpen]
headings = ["Original Image", "Laplacian Filter", "Sharpen Image"]

for i in range(0, len(imgs)):
    axs[i].axis("off")
    axs[i].imshow(imgs[i], cmap='gray')
    axs[i].set_title(headings[i])

if not output == "":
    cv.imwrite(output, sharpen)
    print(f"Saved: {output}")

plt.show()




