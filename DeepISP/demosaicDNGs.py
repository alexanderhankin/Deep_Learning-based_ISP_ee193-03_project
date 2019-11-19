#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## Assumes X (dng) and Y(jpg) folders are downloaded and are in current working directory
# Will create folder X_dem with all contents of X demosaiced (png)


# In[1]:


import os
import rawpy
import matplotlib.pyplot as plt
import glob
import shutil
from PIL import Image


# In[2]:


BASE_PATH = os.getcwd()
NEW_PATH_X = os.path.join(BASE_PATH,'X_dem')
OLD_PATH_X = os.path.join(BASE_PATH,'X')


# In[3]:


if not os.path.isdir(NEW_PATH_X): os.mkdir(NEW_PATH_X)


# In[4]:


image_paths = glob.glob(OLD_PATH_X+'/'+'*.dng') # full paths to DNGs


# In[21]:


## Loop through every image in X, demosaic it, save in NEW_PATH_X
for fpath in image_paths:
    fname = fpath.split('/')[-1].split('.')[-2]
    #print(fpath)
    raw = rawpy.imread(fpath)
    rgb = raw.postprocess(demosaic_algorithm=0) # 0 is linear interpolation TODO: double check no other processing happens 
    Image.fromarray(rgb).save(os.path.join(NEW_PATH_X,fname+'.png'))
    raw.close()


# In[ ]:




