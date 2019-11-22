function rgb_interp = isp_demosaic(img)

w = size(img, 2);
h = size(img, 1);

red = double(img(1:2:h, 2:2:w));
% Average the two green pixel values
green = mean(cat(3, double(img(1:2:h, 1:2:w)), double(img(2:2:h, 2:2:w))), 3);
blue = double(img(2:2:h, 1:2:w));

rgb = cat(3, red, green, blue);

% Do cubic interpolation for each color channel
rgb_interp = zeros(size(img, 1)-1,size(img, 2)-1,3,'double');
rgb_interp(:,:,1) = interp2(rgb(:,:,1), 1, 'cubic');
rgb_interp(:,:,2) = interp2(rgb(:,:,2), 1, 'cubic');
rgb_interp(:,:,3) = interp2(rgb(:,:,3), 1, 'cubic');


