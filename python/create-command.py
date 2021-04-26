#!/usr/bin/python env

# this file creates all commands neccessary for applying image processing
# command create can be used to create commands for following image processing techniques
# laplacian (image sharpening filter)
# apply sobel (filters/)
# apply prewitt (filters/)
# apply power law or log transformation (constrast-level/)
# apply smoothing filter (filters/)
# any combination of the above

import argparse
from shutil import copyfile

# adding cmd parser
parser = argparse.ArgumentParser(description='Create Image Processing Commands')
parser.add_argument('-i', '--image', help='Path to input image.')
parser.add_argument('-t', "--tech", help="enter technique to apply on image")
parser.add_argument('-v', "--verbose", help="enable verbose output", action='store_true')
args = vars(parser.parse_args())

techniques = args['tech'].split(',')
image = args["image"]
verbose = args['verbose']

# splitting file from the '.' in the file name
img = image.split('.')
# copy original image from image to this location input/
dst = f"input/input.{img[-1]}"
if not image == dst : # if image and destination are not same
    copyfile(image, dst)
# change the pointer to the input/input.(ext)
image = dst

commands = []

# output file for laplacian function
outputLaplacian = "output/laplacian.jpg"
# applying laplacian sharpening filter only
if 'l' in techniques:
    # creating laplacian command
    laplacian = f"python3 filters/laplacian.py --image {image} --output {outputLaplacian} --variant ori"
    
    if verbose:
        print("Creating Command for Laplacian Technique")
        print(f"laplacian: {laplacian}")
    
    commands.append(laplacian)

outputEdgeDetection = ""
applyEdgeDetection = ""
if 's' in techniques or 'p' in techniques:
    
    # applying sobel filter
    if 's' in techniques:

        if verbose:
            print("Creating Command for Sobel Technique")

        outputEdgeDetection = "output/sobel.jpg"
        applyEdgeDetection = f"python3 filters/sobel.py --image {outputLaplacian} --output {outputEdgeDetection}"
    else:  # applying prewitt filter
        if verbose:
            print("Creating Command for Prewitt Technique")
        outputEdgeDetection = "output/prewitt.jpg"
        applyEdgeDetection = f"python3 filters/prewitt.py --image {outputLaplacian} --output {outputEdgeDetection}"
    if verbose:
        print(f"Sobel/Prewitt: {applyEdgeDetection}")
    commands.append(applyEdgeDetection)

outputFinal = ""
contrastLevel = ""
if 'po' in techniques or 'lo' in techniques:
    # applying power law 
    if 'po' in techniques:
        if verbose:
            print("Creating Command for Power Law Transformation")
        outputFinal = "output/power.jpg"
        contrastLevel = f"python3 contrast-level/power-law.py --image {outputEdgeDetection} --output {outputFinal}"
    else:  # applying log transformation
        if verbose:
            print("Creating Command for Log Transformation")
        outputFinal = "output/log.jpg"
        contrastLevel = f"python3 contrast-level/log-trans.py --image {outputEdgeDetection} --output {outputFinal}"
    if verbose:
        print(f"PowerLaw/Log: {contrastLevel}")
    commands.append(contrastLevel)

# create a new bash file for running
with open("run-me.sh", "w") as f:
    f.writelines("#!/bin/bash\n\n")
    if verbose:
        print("Writing Commands to a bash file!")
        print("Make sure the commands created are correct then run the bash file!")
    for i in commands:
        f.writelines(f"{i}\n")
