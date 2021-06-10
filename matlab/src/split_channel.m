% split channels into rgb

clc;
rows  = 1; 
cols = 4;
% reading an image from ../dataset/
I = imread("../dataset/wall.jpg");

% subplotting original image

subplot(rows, cols, 1), imshow(I);
title("Original");

% extracting rgb channels
redChannel = I(:,:,1); 
greenChannel = I(:,:,2);
blueChannel = I(:,:,3);

% plotting red, green and blue channel
subplot(rows, cols, 2), imshow(redChannel);
title('Red Channel');
subplot(rows, cols, 3), imshow(greenChannel);
title('Green Channel');
subplot(rows, cols, 4), imshow(blueChannel);
title('Blue Channel');