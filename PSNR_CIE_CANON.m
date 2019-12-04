% Computes the S-CIELAB and PSNR values between two images.
% PLEASE NOTE: S-CIELAB computation heavily reference and use code from hte
% following github repo: https://github.com/wandell/SCIELAB-1996

% clears workspace
clear;

% set datapath to current directoru
datapath = '';

% sets a whitepoint 
whitepoint = [1 1 1];

% initializes image format to take in XYZ 
imageformat = 'xyz';

% initializes final data structure for SCIELAB results
CIE_canon = zeros(57, 2, 1);
PSNR_canon = zeros(57, 2, 1);

% iterates through the values for panasonic images: (there are 500)
for i = 40:40
% note that input and ground truth images are labelled with numbers 1 - 500
imgname = num2str(i);

% grabs and reads the input image 
cd Dataset_LINEAR_with_noise;
cd bayer_canon;
cd input; 
img = imread([datapath imgname '.png']);
cd ..
cd ..
cd ..

% grabs and reads groundtruth image
cd Dataset_LINEAR_with_noise;
cd bayer_canon;
cd groundtruth;
imgGTruth = imread([datapath imgname '.png']);
cd ..
cd ..
cd ..

% joint denoising and demoisaicing the input images
img = demosaic(img, 'rggb'); % right demosaic for the MSR dataset
img = denoise(img);

figure
imshow(img);

% converts to XYZ 
imgGTXYZ = rgb2xyz(imgGTruth);
imgXYZ   = rgb2xyz(img);

% computes and returns SCIELAB values (the different between the color
% values in the two provided images). 23 here is the samples per deg. A
% commented example on github (https://github.com/wandell/SCIELAB-1996) is
% used here: 
errorImage = scielab(23, imgGTXYZ, imgXYZ, whitepoint, imageformat);
avrgSCIELAB = mean(errorImage(:));

% saves image number and the computed average SCIELAB value in matrix
CIE_canon(i,1,:) = i;
CIE_canon(i,2,:) = avrgSCIELAB;

% computes PSNR values 
resultPSNR = PSNR(rescale(imgGTruth),rescale(img));

% stores the value of the dB from PSNR calculation in a matrix (along with
% image number)
PSNR_canon(i,1,:) = i;
PSNR_canon(i,2,:) = resultPSNR(:,:,1);

% displays histogram of errorImage (SCIELAB returns)
% figure(50)
% hist(errorImage(:))

end