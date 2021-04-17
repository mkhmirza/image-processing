#!/usr/bin/python env

import cv2 as cv
import numpy as np
import preProcessing as pre
from matplotlib import pyplot as plt
import argparse

# adding cmd parser
parser = argparse.ArgumentParser(description='Prewitt Edge Detection')
parser.add_argument('--image', help='Path to input image.',default='dataset/original.jpg')
parser.add_argument("--output", help="Output File name and path", default="")
args = vars(parser.parse_args())

imgToLoad = args["image"]
output = args["output"]

# init subpot
row, cols = 1, 2
fig, axs = plt.subplots(row, cols)
fig.tight_layout()
fig.suptitle(f"Applying Prewitt Filter (Edge Detection)")

# loading image in grayscale mode
img = cv.imread(imgToLoad, 0)
# changing img 2 double
out = cv.normalize(img.astype('float'), None, 0.0, 1.0, cv.NORM_MINMAX)
print(img.shape[0], img.shape[1])

# apply x and y filter using convolution
x = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
y = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])

# calculating, gx = x * I, gy = y * I
gx = cv.filter2D(out, -1, kernel=x)
gy = cv.filter2D(out, -1, kernel=y)

# squaring
gXsquare = np.square(gx)
gYsquare = np.square(gy)

# calulating g = (gx^2 + gy^2)^1/2
g = cv.sqrt(cv.add(gXsquare, gYsquare))

imgs = [out, g]
headings = ["Original Image", "Edge Detection"]

for i in range(0, len(imgs)):
    axs[i].axis("off")
    axs[i].imshow(imgs[i], cmap='gray')
    axs[i].set_title(headings[i])

if not output == "":
    cv.imwrite(output, g)
    print(f"Saved: {output}")

plt.show()
