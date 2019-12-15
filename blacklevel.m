
% This function 
% Inputs: img - a .tif file from camera sensors
% Outputs: a matrix of .tif pixels. 

function result = blacklevel(img)

% J = filter2(fspecial('sobel'),img);
 result = mat2gray(img);

%     % converts image to type double 
%     y = double(img);
% 
%     % shifts the image to the left by minimum value (so that the histogram
%     % data starts at 0)
%     ynew = y - (min(y(:)));
%     
%     % rescales image
%     ynew = rescale(ynew);
%     
%     % stretches the image by a certain factor. I played around with the
%     % stretching of the image and it seemed to create the most natural
%     % black level correction when scaled not to 0 to 1 but keeping with the
%     % image's original values. This way, if the inputted .tif file goes
%     % from true black to true white (0 to 1 after scaling), then the ynew
%     % scaled stays as 0-1. However, this increases contrast for all images.
%     ynew = ynew .* (2 - (max(ynew(:))));
% 
%     % rescaling data to range from 0 to 1
%     ynew = rescale(ynew);
%     
%     % brightens image in case the original is too dark. This is a built in
%     % matlab function that adds 0.5 to all intensity values. 
%     ynew = brighten(ynew, 0.5);
%     
%     % output results
%     result = ynew;
% % function result = blacklevel(img)
% % 
% % figure(2)
% % histogram(img);
% % img=rescale(img, 0, 255);
% % 
% % % Histogram equalization to improve gray level contrast
% % h = size(img,1);
% % w = size(img,2);
% % [counts,binLocations] = imhist(uint8(img));
% % 
% % cdf=zeros(256,1);
% % 
% % for i=1:256
% %     p_c = round((counts(i)/(h*w))*255);
% %     if i==1
% %         cdf(i)=p_c;
% %     else
% %         cdf(i)=p_c+cdf(i-1);
% %     end
% % end
% % 
% % for i=1:h
% %     for j=1:w
% %         img(i,j)=cdf(uint8(img(i,j))+1);
% %     end
% % end
% % 
% % result=double(img);
% % figure(100)
% % imshow(rescale(result));
% % %
% % % histogram(result)