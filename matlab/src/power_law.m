% power law transformation 

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

% power law: S = T(r) = Cr^gamma
gamma = input('Enter the value for gamma: ');
powerLaw = newGray.^gamma;
% subplotting img, and histogram 
subplot(2, 2, 3), imshow(powerLaw);
subplot(2, 2, 4), imhist(powerLaw);