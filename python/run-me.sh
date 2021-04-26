#!/bin/bash

python3 filters/laplacian.py --image input/input.tif --output output/laplacian.jpg --variant ori
python3 filters/sobel.py --image output/laplacian.jpg --output output/sobel.jpg
python3 contrast-level/power-law.py --image output/sobel.jpg --output output/power.jpg
