% difference between two pictures

clc;
rows  = 1; 
cols = 3;
% reading an image from ../dataset/
I = imread("../dataset/pcbCroppedTranslated.png");
I2 = imread('../dataset/pcbCroppedTranslatedDefected.png');

% plotting both images and
subplot(rows, cols, 1), imshow(I);
title('Original');
subplot(rows, cols, 2), imshow(I2);
title('Image Defected');

% calculating difference of both images
diff = abs(I - I2);

% subplotting difference image
subplot(rows, cols, 3), imshow(diff);
title("Difference")