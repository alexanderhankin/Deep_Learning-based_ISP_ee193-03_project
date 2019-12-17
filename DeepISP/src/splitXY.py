#!/usr/bin/env python
# coding: utf-8

# In[1]:


## splitXY
## Splits the original dataset as downloaded from Kaggle and renames the files
## 
## 
## 


# In[2]:


import os
import glob
import shutil 


# In[10]:


DATASET_DIR_NAME = 'S7-ISP-Dataset'
NEW_DATASET_DIR_NAME = 'S7-ISP-Dataset-Sorted'
BASE_PATH = os.getcwd()
DATA_PATH = os.path.join(BASE_PATH,DATASET_DIR_NAME)
NEW_DATA_PATH = os.path.join(BASE_PATH,NEW_DATASET_DIR_NAME)
if not os.path.isdir(NEW_DATA_PATH): os.mkdir(NEW_DATA_PATH)

########### Short exposure ##########
NEW_DATASET_SHORT_EXPOSURE_PATH = os.path.join(NEW_DATA_PATH,'S7-ISP-Short-Exposure')
if not os.path.isdir(NEW_DATASET_SHORT_EXPOSURE_PATH): os.mkdir(NEW_DATASET_SHORT_EXPOSURE_PATH)
NEW_PATH_X = os.path.join(NEW_DATASET_SHORT_EXPOSURE_PATH,'X')
if not os.path.isdir(NEW_PATH_X): os.mkdir(NEW_PATH_X)
NEW_PATH_Y = os.path.join(NEW_DATASET_SHORT_EXPOSURE_PATH,'Y')
if not os.path.isdir(NEW_PATH_Y): os.mkdir(NEW_PATH_Y)
######### Medium exposure ##########
'''NEW_DATASET_MEDIUM_EXPOSURE_PATH = os.path.join(NEW_DATA_PATH,'S7-ISP-Medium-Exposure')
if not os.path.isdir(NEW_DATASET_MEDIUM_EXPOSURE_PATH): os.mkdir(NEW_DATASET_MEDIUM_EXPOSURE_PATH)
NEW_PATH_X_MEDIUM_EXPOSURE = os.path.join(NEW_DATASET_MEDIUM_EXPOSURE_PATH,'X')
if not os.path.isdir(NEW_PATH_X_MEDIUM_EXPOSURE): os.mkdir(NEW_PATH_X_MEDIUM_EXPOSURE)
NEW_PATH_Y_MEDIUM_EXPOSURE = os.path.join(NEW_DATASET_MEDIUM_EXPOSURE_PATH,'Y')
if not os.path.isdir(NEW_PATH_Y_MEDIUM_EXPOSURE): os.mkdir(NEW_PATH_Y_MEDIUM_EXPOSURE)''';


# In[11]:


# Loop through each folder inside the top folder of the dataset as downloaded from Kaggle
# Put each short exposure dng in NEW_PATH_X and each medium exposure (ground truth) in NEW_PATH_Y
# The name of each image is changed to the name of the folder it belonged to. This way the names completeley match
for dirname in os.listdir(DATA_PATH):
    DNGs = glob.glob(DATA_PATH+"/"+dirname+"/"+"*.dng") #list of full paths to dng
    JPGs = glob.glob(DATA_PATH+"/"+dirname+"/"+"*.jpg") #list of full paths to jpg
    for dng_path, jpg_path in zip(DNGs,JPGs):
        dng_name = dng_path.split('/')[-1]
        jpg_name = jpg_path.split('/')[-1]
        if dng_name.split('_')[0] == 'short':
            shutil.copy(dng_path, os.path.join(NEW_PATH_X,dirname+'.dng'))
        if jpg_name.split('_')[0] == 'medium':
            shutil.copy(jpg_path, os.path.join(NEW_PATH_Y,dirname+'.jpg')) 

