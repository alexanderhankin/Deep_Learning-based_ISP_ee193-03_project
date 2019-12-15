function denoised = denoise(img)

% For psnr are we using a special matlab function, or the normal psnr
% function??

 % DeepNetwork Denoise
% % Took 30 min, but it worked!
% [noisyR,noisyG,noisyB] = imsplit(img);
% 
% net = denoisingNetwork('DnCNN');
% r_denoised = denoiseImage(noisyR,net);
% g_denoised = denoiseImage(noisyG,net);
% b_denoised =  denoiseImage(noisyB,net);
% 
% denoised = cat(3,r_denoised,g_denoised,b_denoised);

%rggb, panasonic #15,
%cannon #29

 



% % Normal Denoise
% [x, y] = meshgrid(-1:1); % Build square matrices with the specified range
% 
% % Standard deviation of the blur;
% sigma = 2;
% blur = exp(-(x.^2 + y.^2)/(2*sigma^2)); % Gaussian blur -- ran out of time!
% blur = blur / sum(blur(:)); % Normalize to 1
% 
% img_cc_denoise = zeros(size(img, 1),size(img, 2),3,'double');
% img_cc_denoise(:,:,1) = filter2(blur, img(:,:,1));
% img_cc_denoise(:,:,2) = filter2(blur, img(:,:,2));
% img_cc_denoise(:,:,3) = filter2(blur, img(:,:,3));
% 
% %img_cc_denoise = sigdenoise(img_cc_denoise);
% 
% denoised = imsharpen(rescale(img_cc_denoise));


% Wavelate denoise, it works too!
  denoised = wdenoise2(img);


