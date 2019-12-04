  
function img = isp(raw);

%iso = metadata_value(metadata, 'ISO')

img = blacklevel(raw);
%img = demosaic(uint8(img), 'rggb'); % right one for the MSR dataset
%img = demosaic(uint8(img), 'grbg'); %right one for the s7 dataset
% img = isp_demosaic_for_MSR(img);
img = isp_demosaic(img);
img = colorcorrection(img);
img = denoise(img);
img = cameracurve(img);