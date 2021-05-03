#!/usr/bin/python env

# this file creates all commands neccessary for applying image processing
# command create can be used to create commands for following image processing techniques
# laplacian (image sharpening filter)
# apply sobel (filters/)
# apply prewitt (filters/)
# apply power law or log transformation (constrast-level/)

#TODO: 1) add canny filter support
# 2) add mean blur support
# 3) find a way to make commands for any file name given
# 4) any combination of the above

import argparse
from shutil import copyfile
import sys

# adding cmd parser
parser = argparse.ArgumentParser(description='Create Image Processing Commands')
parser.add_argument('-i', '--image', help='Path to input image.')
parser.add_argument('-t', "--tech", help="enter technique to apply on image")
parser.add_argument('-v', "--verbose", help="enable verbose output", action='store_true')
parser.add_argument('-p', '--print', help="print all techniques supported!", action="store_true")
args = vars(parser.parse_args())


# if -p or --print is given then print
if args['print']: 
    print("Supported Techniques")
    print("1. Laplacian [l]")
    print('2. Power Law Transformation [po]')
    print('3. Log Transformation [lo]')
    print('4. Sobel Edge Detection [s]')
    print('5. Prewitt Edge Detection [p]')
    print()
    print("Prints this message and exits!")
    # exit from the program
    sys.exit(0)

# splitting technique on basis of comma
# if more than one techniques are given
techniques = args['tech'].split(',')
image = args["image"]
verbose = args['verbose']

# if no image is given then print this message 
if not image:
    print("Please input a image file path using --image or -i tag!")
    sys.exit(0)

# splitting file from the '.' in the file name
img = image.split('.')
# copy original image from image to this location input/
dst = f"input/input.{img[-1]}"
# if image src and dst are both same
if image == dst:
    if verbose:
        print("No file move required, files are in the same directory!")
# if image and destination are not same
elif not image == dst:
    copyfile(image, dst)
    if verbose:
        print(f"File Moved to {dst}")
        print(f"Original File Path: {image}")
# change the pointer to the input/input.(ext)
image = dst

commands = []

# output file for laplacian function
outputLaplacian = "output/laplacian.jpg"
# applying laplacian sharpening filter only
if 'l' in techniques:
    # creating laplacian command
    laplacian = f"python3 filters/laplacian.py -i {image} -o {outputLaplacian} -v v1"
    
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
        applyEdgeDetection = f"python3 filters/sobel.py -i {outputLaplacian} -o {outputEdgeDetection}"
    else:  # applying prewitt filter
        if verbose:
            print("Creating Command for Prewitt Technique")
        outputEdgeDetection = "output/prewitt.jpg"
        applyEdgeDetection = f"python3 filters/prewitt.py -i {outputLaplacian} -o {outputEdgeDetection}"
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
        contrastLevel = f"python3 contrast-level/power-law.py -i {outputEdgeDetection} -o {outputFinal}"
    else:  # applying log transformation
        if verbose:
            print("Creating Command for Log Transformation")
        outputFinal = "output/log.jpg"
        contrastLevel = f"python3 contrast-level/log-trans.py -i {outputEdgeDetection} -o {outputFinal}"
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
