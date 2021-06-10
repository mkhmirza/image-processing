% convert image to binary img and invert the img

clc;
rows  = 1; 
cols = 3;
% reading an image from ../dataset/
I = imread("../dataset/apple-red.jpg");

% converting the img into a binary img
bw = im2bw(I, 0.7);
% inverting the image
invert = 1 - bw;

subplot(rows, cols, 1), imshow(I);
title('Original Image');
subplot(rows, cols, 2), imshow(bw);
title('Binary Image');
subplot(rows, cols, 3), imshow(invert);
title('Invert Binary Image');

