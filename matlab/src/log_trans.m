% log transformation

clc;
% reading an image from ../dataset/
I = imread("../dataset/face.jpg");
% converting rgb to gray scale
gray = im2gray(I);

% subplotting new enhanced image, and histogram
subplot(2, 2, 1), imshow(gray);
subplot(2, 2, 2), imhist(gray);

% row, cols
[r, c] = size(I);

% changing image to double values
newGray = im2double(gray);

% log transformation: S = T(r) = Clog(1 + r)
addition = 1 + newGray;
logTransformation =  log2(addition);
% subplotting img, and histogram 
subplot(2, 2, 3), imshow(logTransformation);
subplot(2, 2, 4), imhist(logTransformation);