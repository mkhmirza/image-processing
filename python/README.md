# Image Processing Using Python3 (OpenCV)
Current Folder contains the implementation of various Image processing techniques using python3's image processing library **OpenCV**.

## Folders
- binary
- channels
- contrast-level
- difference
- filters
- hist

## Usage
Create two folders, one  is *input/* and the second is *output/*
### Create Commands
Since the commands to apply some of the filters are long, *create-command.py* can be used to create commands for applying filters on an image. To create commands use the following
```
pwd  # make sure you are in the current folder as the create-command.py, it is optional but make things more easier
python3 create-command.py --image <image-path> --tech <number-of-techniques/filters>
```
When using *--tech* filter seprate the filters/techniques using a comma, for example
```
python3 create-command.py --image abc.jpg --tech/-t l,s,po --verbose
``` 
Each filter is represented as 
- `l` represents **Laplacian Filter (Sharpening)**
- `s` represents **Sobel Filter (Edge Detection)**
- `p` represents **Prewitt Filter (Edge Detection)**
- `po` represents **Power Law Transformation (Contrast Level)**
- `lo` represents **Log Transformation (Contrast Level)**

In the above example by using **--tech l,s,p**, we are applying *Laplacian Filter*, *Sobel Filter* and *Power Law Transformation*



