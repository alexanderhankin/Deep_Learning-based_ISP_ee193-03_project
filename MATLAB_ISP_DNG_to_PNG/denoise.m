function denoised = denoise(img)

[x, y] = meshgrid(-10:10); % Build square matrices with the specified range

% Standard deviation of the blur;
sigma = 2;
blur = exp(-(x.^2 + y.^2)/(2*sigma^2)); % Gaussian blur -- ran out of time!
blur = blur / sum(blur(:)); % Normalize to 1

img_cc_denoise = zeros(size(img, 1),size(img, 2),3,'double');
img_cc_denoise(:,:,1) = filter2(blur, img(:,:,1));
img_cc_denoise(:,:,2) = filter2(blur, img(:,:,2));
img_cc_denoise(:,:,3) = filter2(blur, img(:,:,3));
denoised = img_cc_denoise;
