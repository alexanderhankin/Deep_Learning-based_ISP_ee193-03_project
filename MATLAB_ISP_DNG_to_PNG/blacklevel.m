% This function 
% Inputs: img - a .tif file from camera sensors
% Outputs: a matrix of .tif pixels. 

function result = blacklevel(img)

    % converts image to type double 
    y = double(img);

    % shifts the image to the left by minimum value (so that the histogram
    % data starts at 0)
    ynew = y - (min(y(:)));
    
    % rescales image
    ynew = rescale(ynew);
    
    % stretches the image by a certain factor. I played around with the
    % stretching of the image and it seemed to create the most natural
    % black level correction when scaled not to 0 to 1 but keeping with the
    % image's original values. This way, if the inputted .tif file goes
    % from true black to true white (0 to 1 after scaling), then the ynew
    % scaled stays as 0-1. However, this increases contrast for all images.
    ynew = ynew .* (2 - (max(ynew(:))));

    % rescaling data to range from 0 to 1
    ynew = rescale(ynew);
    
    % brightens image in case the original is too dark. This is a built in
    % matlab function that adds 0.5 to all intensity values. 
    ynew = brighten(ynew, 0.5);
    
    % output results
    result = ynew;