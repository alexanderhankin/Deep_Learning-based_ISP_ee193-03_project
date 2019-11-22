% Alex Hankin
% NOTE: I think there is a problem with my estimation of the illuminant.
% All my images look too bright or the lighting is not natural..

% Top-level script which runs the ISP
clear;

datapath = '/Users/Olive/Documents/MATLAB/final193/'; %Specify folder where .dng images are saved
imgname = 'medium_exposure';

% Load the image
img = imread([datapath imgname '.dng']);
%img_jpg = imread([datapath imgname '.jpg']);

%figure(1)
%imshow(img_jpg)
%{
% Load metadata provided by the camera
metafile = [datapath imgname '.csv'];
metadata = load_metadata(metafile);
%}
result = isp(img);
figure(15)
imshow(result)
folder = ' '; %Specify folder where you want to save the new .png image
imwrite(result,fullfile(folder,[imgname '.png']))