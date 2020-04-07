img = imread('a15_bottle_image.jpg');

img_size = size(img);
disp(img_size);

% mirroring the image
mirrored = img(:, end:-1:1, :);
imshow(mirrored);
% imshow(img);