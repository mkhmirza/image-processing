% applying prewitt filter (edge detection)

clc;
rows  = 1; 
cols = 2;
% reading an image from ../dataset/
I = imread("../dataset/moon.tif");

% plotting both images and
subplot(rows, cols, 1), imshow(I);
title('Original');

% this can also be defined as below:
% filterPrewitt = edge(I,'prewitt');
filterPrewitt = fspecial('prewitt');

% apply filter on the image 
prewittFilter = imfilter(I, filterPrewitt);

% plotting laplacian edge detection
subplot(rows, cols, 2), imshow(prewittFilter);
title('Prewitt Filter (Edge Detection)');

