  
function img = isp(raw);

%iso = metadata_value(metadata, 'ISO')

img = blacklevel(raw);
%img = demosaic(uint8(img), 'grbg');
% img = demosaic(uint8(img), 'grbg'); right one for babushka dolls
img = isp_demosaic(img);
img = colorcorrection(img);
img = denoise(img);
img = cameracurve(img);