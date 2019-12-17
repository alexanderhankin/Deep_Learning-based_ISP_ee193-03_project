
## Assumed S7 dataset has been downloaded from Kaggle
## Assumes X (dng) and Y(jpg) folders have been created with splitXY and are in current working directory
# Will create folder X_dem with all contents of X demosaiced (png)

import os
import rawpy
import matplotlib.pyplot as plt
import glob
from PIL import Image

BASE_PATH = os.path.join(os.getcwd(),'S7-ISP-Dataset-Sorted','S7-ISP-Short-Exposure')
NEW_PATH_X = os.path.join(BASE_PATH,'X_dem') # Will save bilinear demosaiced images here
OLD_PATH_X = os.path.join(BASE_PATH,'X')
OLD_PATH_Y = os.path.join(BASE_PATH,'Y')

if not os.path.isdir(NEW_PATH_X): os.mkdir(NEW_PATH_X)

image_paths = glob.glob(OLD_PATH_X+'/'+'*.dng') # full paths to DNGs

## Loop through every image in X, demosaic it, save in NEW_PATH_X
for fpath in image_paths:
    fname = fpath.split('/')[-1].split('.')[-2]
    #print(fpath)
    raw = rawpy.imread(fpath)
    rgb = raw.postprocess(demosaic_algorithm=0) # 0 is linear interpolation 
    Image.fromarray(rgb).save(os.path.join(NEW_PATH_X,fname+'.png'))
    raw.close()




