# Makes new X Y dataset from S7 dataset with small patches from the original images
# Crops and saves a 200x200 patch from each image in the S7 dataset

import tensorflow as tf
from PIL import Image
import os
import glob

S7_DATA_PATH ='S7-ISP-Dataset-Sorted/S7-ISP-Short-Exposure'
DATAX_PATH = os.path.join(os.getcwd(),S7_DATA_PATH,'X_dem') 
DATAY_PATH = os.path.join(os.getcwd(),S7_DATA_PATH,'Y') 
CROPPEDX_PATH = os.path.join(os.getcwd(),S7_DATA_PATH,'X_dem_cropped')
CROPPEDY_PATH = os.path.join(os.getcwd(),S7_DATA_PATH,'Y_cropped') 
if not os.path.isdir(CROPPEDX_PATH): os.mkdir(CROPPEDX_PATH)
if not os.path.isdir(CROPPPEDY_PATH): os.mkdir(CROPPPEDY_PATH)


names = [x.split('/')[-1].split('.')[0] for x in glob.glob(os.path.join(DATAX_PATH,'*.png'))]
X_paths = [os.path.join(DATAX_PATH,name+'.png') for name in names]
Y_paths = [os.path.join(DATAY_PATH,name+'.jpg') for name in names]

area = (600, 600, 800, 800)
for Xpath,Ypath in zip(X_paths,Y_paths):
    with Image.open(Xpath) as imageX, Image.open(Ypath) as imageY :
        imageX.crop(area).save(CROPPEDX_PATH+'/'+Xpath.split('/')[-1])
        imageY.crop(area).save(CROPPEDY_PATH+'/'+Ypath.split('/')[-1])



