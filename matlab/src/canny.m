% applying canny filter (edge detection)

clc;
rows  = 1; 
cols = 2;
% reading an image from ../dataset/
I = imread("../dataset/moon.tif");

% plotting both images and
subplot(rows, cols, 1), imshow(I);
title('Original');

% this can also be defined as below:
filterCanny = edge(I,'canny');

% plotting laplacian edge detection
subplot(rows, cols, 2), imshow(filterCanny);
title('Canny Filter (Edge Detection)');
