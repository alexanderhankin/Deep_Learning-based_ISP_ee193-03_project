function result = blacklevel(img)

figure(2)
histogram(img);
img=rescale(img, 0, 255);

% Histogram equalization to improve gray level contrast
h = size(img,1);
w = size(img,2);
[counts,binLocations] = imhist(uint8(img));

cdf=zeros(256,1);

for i=1:256
    p_c = round((counts(i)/(h*w))*255);
    if i==1
        cdf(i)=p_c;
    else
        cdf(i)=p_c+cdf(i-1);
    end
end

for i=1:h
    for j=1:w
        img(i,j)=cdf(uint8(img(i,j))+1);
    end
end

result=double(img);
figure(3)
histogram(result)
