% apply any filter on a picture

clc;
rows  = 1; 
cols = 2;
% reading an image from ../dataset/
I = imread("../dataset/moon.tif");

% generating an empty filter of 3, 3 size
filter = zeros(3,3);
% input filter values
for i=1:3
    for j=1:3
        i,j
        filter(i, j) = input("Enter Filter Value: ");
    end
end

% applying filter
filteredImg = imfilter(I, filter);

% plotting both images and
subplot(rows, cols, 1), imshow(I);
title('Original');

% suplotting the filtered image
subplot(rows, cols, 2), imshow(filteredImg);
title('Filtered Image');