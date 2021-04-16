#!/usr/bin/python env

import preProcessing
import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np
import argparse

# adding parsing arguments
parser = argparse.ArgumentParser( description='Performs Power Law Transformation Method')
parser.add_argument("--image", type=str, help="path to image file")
parser.add_argument("--output", help="Output File name and path", default="")
args = vars(parser.parse_args())

imgToLoad = args["image"]
output = args["output"]

# init figures
rows, cols = 2, 2 
fig, axes = plt.subplots(rows, cols)
fig.suptitle("Power Law Transformation")
# increasing the hspace between subplots 
fig.tight_layout()

# perform rotation on the given image
img = cv.imread(imgToLoad, 0)

gamma = float(input("Enter Value for gamma: "))

# perform the s = r^(gamma) of light information
imgEnhanced = np.array(255 * (img / 255) ** gamma, dtype='uint8')

#plotting using for loop
imgs = [img, imgEnhanced]
headings = ["Grayscale", "Histogram (Grayscale)","Gray Scale (Improved Constrast)", "Histogram (Image Constrast)"]

counter = 0
for i in range(0, len(imgs)):
    axes[i, 0].axis("off")
    for j in range(0, len(imgs)):
        axes[i, j].set_title(headings[counter])
        counter += 1
    axes[i, 0].imshow(imgs[i], cmap='gray')
    axes[i, 1].hist(imgs[i].ravel(), 256, [0, 255])

if not output == "":
    print("Saving Power Transformated Image!")
    cv.imwrite(output, imgEnhanced)
    print(f"Saved: {output}")

plt.show()


