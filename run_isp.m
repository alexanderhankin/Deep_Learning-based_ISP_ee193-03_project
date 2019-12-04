% Alex Hankin
% NOTE: I think there is a problem with my estimation of the illuminant.
% All my images look too bright or the lighting is not natural..

% Top-level script which runs the ISP
%clear;

% datapath = '/Users/Olive/Documents/MATLAB/final193/'; %Specify folder where .dng images are saved
imgname = 'short_exposure1.dng';

i = 1;
%for i = 1:57
    cd Dataset_LINEAR_with_noise;
    cd bayer_canon;
    cd input;
    imgName = sprintf('%d.png', i);
   % imgNameCat = imgName, imgName2;
    img = imread(imgName);
    
    cd /Users/Olive/Documents/MATLAB/final193/;
    final = isp(img);
    save('DATA');
    figure(1)
    imshow(final);
    
    %final = final image;
    
    % writes files to final files (called 1.png etc.)
    finalName = num2str(i);
    imwrite(img, [finalName, '.png']);

%end
% 
% loadData();
% hello = load('Hello.mat');
% 
% for i = 1:5
% 
%     img = imread('54.png');
%     %img(:,:) = squeeze(hello.imgArray(i));
% 
%     % Load the image
%     %img = imread([datapath imgname '.dng']);
%     %img_jpg = imread([datapath imgname '.jpg']);
% 
%     result = isp(img);
%     figure(15)
%     imshow(result)
%     folder = ' '; %Specify folder where you want to save the new .png image
%     imwrite(result,[imgname '.png']);
% 
% end