#!/usr/bin/python env

import cv2 as cv
import numpy as np


# rotate image 90, 180, 270 degrees only, [clockwise counter clockwise]
def rotateImage(source, rotationType=cv.ROTATE_90_CLOCKWISE):
    return cv.rotate(source, rotationType)

# rotate a image using different degree
def rotateImageDegree(source, angle=90, scale=1):
    # unpack rows, cols information
    rows, cols, _ = source.shape

    # get 2x3 matrix for rotation
    M = cv.getRotationMatrix2D((cols/2, rows/2), angle, scale)
    # apply the rotation on the source matrix
    dst = cv.warpAffine(source, M, (cols, rows))
    return dst

# resizing img based on another img dimensions 
def resizeImage(source, fx=1, fy=1, interpolation=cv.INTER_CUBIC):    
    res = cv.resize(source, None, fx=fx, fy=fy, interpolation=interpolation)
    return res


def resizeImageDimension(source, width=None, height=None, interpolation=cv.INTER_CUBIC):
    if width == None or height==None:
        return source
    dim = (width, height)
    res = cv.resize(source, dim, interpolation=interpolation)
    return res
