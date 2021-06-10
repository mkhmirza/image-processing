% applying sharpening filter (laplacian)

clc;
rows  = 1; 
cols = 3;
% reading an image from ../dataset/
I = imread("../dataset/moon.tif");

% plotting both images and
subplot(rows, cols, 1), imshow(I);
title('Original');

% applying laplacian
filterLaplacian = [0 1 0; 1 -4 1; 0 1 0];
% this can also be defined as below:
%filterLaplacian = fspecial('laplacian',alpha)

% apply filter on the image 
laplacianFilter = imfilter(I, filterLaplacian);

% plotting laplacian edge detection
subplot(rows, cols, 2), imshow(laplacianFilter);
title('Laplacian Filter');

% for sharpening of the image f = I - laplacianFilter
% this can be replaced by [0 -1 0; -1 5 -1; 0 -1 0]
sharpenedImage = I - laplacianFilter;

% plotting difference, sharpened image
subplot(rows, cols, 3), imshow(sharpenedImage);
title('Sharpened Image');

