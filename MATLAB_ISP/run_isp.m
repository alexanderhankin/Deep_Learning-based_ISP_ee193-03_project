% Alex Hankin
% NOTE: I think there is a problem with my estimation of the illuminant.
% All my images look too bright or the lighting is not natural..

% Top-level script which runs the ISP
clear;

datapath = '';
imgname = 'newyear';

% Load the image
img = imread([datapath imgname '.tif']);
img_jpg = imread([datapath imgname '.jpg']);

figure(1)
imshow(img_jpg)

% Load metadata provided by the camera
metafile = [datapath imgname '.csv'];
metadata = load_metadata(metafile);

result = isp(img, metadata);

figure(15)
imshow(result)

imwrite(result,[imgname '.png'])