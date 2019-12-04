% Alex Hankin
% NOTE: I think there is a problem with my estimation of the illuminant.
% All my images look too bright or the lighting is not natural..

% Top-level script which runs the ISP
%clear;

% datapath = '/Users/Olive/Documents/MATLAB/final193/'; %Specify folder where .dng images are saved

% iterates through the number of provided images in the dataset
for i = 1:110
    cd s7_dataset;
    cd(num2str(i));
    img = imread('medium_exposure.dng');
    cd ..
    cd ..
    
    final = isp(img);
    %save('DATA');
    %figure(1)
    %imshow(final);
    
    %final = final image;
    
    % writes files to final files (called 1.png etc.)
    finalName = num2str(i);
    imwrite(final, [finalName, '.png']);
end
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