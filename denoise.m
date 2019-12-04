function denoised = denoise(img)

[x, y] = meshgrid(-1:1); % Build square matrices with the specified range

% Standard deviation of the blur;
sigma = 2;
blur = exp(-(x.^2 + y.^2)/(2*sigma^2)); % Gaussian blur -- ran out of time!
blur = blur / sum(blur(:)); % Normalize to 1

img_cc_denoise = zeros(size(img, 1),size(img, 2),3,'double');
img_cc_denoise(:,:,1) = filter2(blur, img(:,:,1));
img_cc_denoise(:,:,2) = filter2(blur, img(:,:,2));
img_cc_denoise(:,:,3) = filter2(blur, img(:,:,3));

%img_cc_denoise = sigdenoise(img_cc_denoise);

denoised = imsharpen(rescale(img_cc_denoise));

% also denoises in frequnecy domain:
% 
% b = firpm(10,[0 0.4 0.6 1],[1 1 0 0])
% h = ftrans2(b);
% [H,w] = freqz(b,1,64,'whole');

% Shows the filter in a 3d plot: 
% colormap(jet(64))
% plot(w/pi-1,fftshift(abs(H)))
% figure, freqz2(h,[32 32])2 32]), axis([-1 1 -1 1 0 1.2])