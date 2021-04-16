#!/usr/bin/python env

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import preProcessing as pre
import argparse

# adding parsing arguments
parser = argparse.ArgumentParser(description='Difference Between 2 similar images')
parser.add_argument("--image", type=str, help="path to the first input image")
parser.add_argument("--image2", type=str, help="path to second input image")
parser.add_argument("--output", help="Output image file path", default="")
args = vars(parser.parse_args())

# read 2 images
# both pictures should be of same res (number of pixels)
imgToLoad = args["image"]
img2ToLoad = args["image2"]
# output file name
output = args["output"]

# init subplots
rows, cols = 1, 3
fig, axes = plt.subplots(1, 3)
fig.tight_layout()
fig.suptitle("Difference Between 2 Images")

# read the img using grayscale mode
img = cv.cvtColor(cv.imread(imgToLoad, 0), cv.COLOR_BGR2RGB)
# second img with a difference
img2 = cv.cvtColor(cv.imread(img2ToLoad, 0), cv.COLOR_BGR2RGB)

print(f"Shape of First Image: {img.shape}")
print(f"Shape of Second Image: {img2.shape}")
print(f"Aspect Ratio: {img.shape[0]/ img.shape[1]}")

resizedImg = img2
# shape of img & img2 is not equal
if not img.shape == img2.shape:
    print("Since the shape of 'img' and 'img2' is not equal, resizing the second img")
    (width, height) = (img.shape[1], img.shape[0])
    # resizing img based on the first image 
    resizedImg = pre.resizeImageDimension(source=img2, width=width, height=height)
    print(f"Shape of First Image: {img.shape}")
    print(f"Shape After 'Resizing' of Second Image: {resizedImg.shape}")

if img.shape == resizedImg.shape:
    print("Shape of Both Imgs is Same")


    # calculate the difference between img
    # can also be done accessing the img pixel
    # diff (i, j) = abs( img(i, j) - img2(i, j) )
    diff = cv.absdiff(img, resizedImg)

    imgs = [img, img2, diff]
    headings = ["Image 1", "Image 2", "Difference"]

    for i in range(0, len(imgs)):
    
        axes[i].axis("off")
        axes[i].set_title(headings[i])
        axes[i].imshow(imgs[i])

    # saving file using --output argument
    if not output == "":
        print("Saving Difference Image File!")
        cv.imwrite(output, diff)
        print(f"Saved: {output}")

    plt.show()
else:
    print("There was an error in resizing please try again.")
