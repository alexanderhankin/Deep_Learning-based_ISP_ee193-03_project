clear;

datapath = '';
imgname_A = 'newyear';
imgname_B = 'newyear';

% Load the image
img_A = imread([datapath imgname '.tif']);
img_B = imread([datapath imgname '.tif']);
PSNR(img_A,img_B);
