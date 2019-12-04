function img = loadData()
%LOADDATA Summary of this function goes here
%   Detailed explanation goes here

%cd MSR-Demosaicing;
cd Dataset_LINEAR_with_noise;
cd bayer_panasonic;
cd input;

% length of the file to be used in the for loop
length = 500;

% creates array of image files
%imgArray = zeros(500, 500, 500);


for k = 1 : length
%     fil e_path = char(strcat(files(i).folder, filesep, files(i).name));
%     array = load(file_path); %#ok<NASGU>    
%     disp(file_path);
    %img = imread('1.png');
%    fileName = k + '.png';
    fileName = sprintf('%d',k);
    imgArray(:,:,k) = imread(fileName, 'png');
    
end

cd ..
cd ..
cd ..
save('Hello');

end

