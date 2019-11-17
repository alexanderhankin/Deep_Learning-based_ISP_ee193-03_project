function scaled = cameracurve(img)
   
bits = 12;
bitrange = 2^bits;

scaled = img / bitrange;

scaled = rescale(scaled, 0, 1);
scaled = scaled.^(1/2.3); % gamma correction (gamma=2.3)

