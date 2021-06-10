#!/usr/bin/python env

import cv2 as cv
import numpy as np
import preProcessing as pre
from matplotlib import pyplot as plt
import argparse


def applyCannyFilter(img, thres1, thres2):
    canny = cv.Canny(img, 127, 255)
    return canny

if __name__ == "__main__":
    # adding cmd parser
    parser = argparse.ArgumentParser(description='Apply Canny Edge Detection')
    parser.add_argument("-i",'--image', help='Path to input image.')
    parser.add_argument("-o","--output", help="Output File name and path", default="")
    args = vars(parser.parse_args())

    imgToLoad = args["image"]
    output = args["output"]

    # init subplots
    rows, cols = 1, 2
    fig, axs = plt.subplots(rows, cols)
    fig.tight_layout()
    fig.suptitle("Applying Canny (Edge Detection)")

    # loading image in grayscale mode
    img = cv.imread(imgToLoad, 0)
    # applying canny filter
    canny = applyCannyFilter(img, 127, 250)

    imgs = [img, canny]
    headings = ["Original Image", "Canny Filter"]

    for i in range(0, len(imgs)):
        axs[i].axis("off")
        axs[i].imshow(imgs[i], cmap='gray')
        axs[i].set_title(headings[i])

    #cannyOuput = canny * 255
    if not output == "":
        cv.imwrite(output, canny)
        print(f"Saved: {output}")

    plt.show()
        