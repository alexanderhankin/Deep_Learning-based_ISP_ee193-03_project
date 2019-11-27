clear;

datapath = '';
% newly denoised and demosaiced image:
A = zeros(57, 1, 3);
for i = 1:57 
imgname = num2str(i);

% Load the image
%datapath1 = '/Users/Olive/Documents/MATLAB/final193/Dataset_LINEAR_with_noise/bayer_panasonic/input';
%datapath2 = '/Users/Olive/Documents/MATLAB/final193/results_from_MSR_panasonic';
%datapath2 = '/Users/Olive/Documents/MATLAB/final193/Dataset_LINEAR_with_noise/bayer_panasonic/groundtruth';

% reads image from computed final results:
cd results_from_MSR_canon;
img_A = imread([datapath imgname '.png']);
img_A = rescale(img_A);
cd ..

cd Dataset_LINEAR_with_noise
cd bayer_canon
cd groundtruth
img_B = imread([datapath imgname '.png']);
img_B = rescale(img_B);

cd ..
cd ..
cd ..

A(i,:,:) = PSNR(img_A,img_B);
end
save('PSNR_Between_groundTruth_and_MSR_canon');
