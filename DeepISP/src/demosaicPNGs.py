## This script does bilinear interpolation demosaicing for the MSR dataset
## Will create folder X_dem with all contents of X demosaiced (png)
## Rawpy does not recognize png as raw format, have to use opencv

import os
import rawpy
import matplotlib.pyplot as plt
import glob
import shutil
import cv2
from PIL import Image


BASE_PATH = os.getcwd()
NEW_PATH_X = os.path.join(BASE_PATH,'X_dem_MSR')
OLD_PATH_X = os.path.join(BASE_PATH,'MSR-Demosaicing/Dataset_LINEAR_with_noise/bayer_panasonic/input') # change this for canor or panasonic

if not os.path.isdir(NEW_PATH_X): os.mkdir(NEW_PATH_X)

image_paths = glob.glob(OLD_PATH_X+'/'+'*.png') # full paths to PNGs

## Loop through every image in X, demosaic it, save in NEW_PATH_X
for fpath in image_paths:
    fname = fpath.split('/')[-1].split('.')[-2]
    print(fpath)
    img = cv2.imread(fpath, flags=cv2.IMREAD_GRAYSCALE) 
    rgb = cv2.cvtColor(img, cv2.COLOR_BayerBG2RGB) 
    print(rgb.shape)
    Image.fromarray(rgb).save(os.path.join(NEW_PATH_X,fname+'.png'))





