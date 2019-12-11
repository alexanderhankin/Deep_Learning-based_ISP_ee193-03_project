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


# In[4]:


# TODO: delete this once the rest of the code is completed
'''DATASET_DIR_NAME = 'S7-ISP-Dataset'
BASE_PATH = os.getcwd()
DATA_PATH = os.path.join(BASE_PATH,DATASET_DIR_NAME)
NEW_PATH_X = os.path.join(os.getcwd(),'X')
NEW_PATH_Y = os.path.join(os.getcwd(),'Y')

if not os.path.isdir(NEW_PATH_X): os.mkdir(NEW_PATH_X) # create directories if they don't exist
if not os.path.isdir(NEW_PATH_Y): os.mkdir(NEW_PATH_Y)

# This loop splits the original dataset to X and Y. All dng's in X and all jpegs in Y
# Will not be used for training. May be useful in some other scenario
for dirname in os.listdir(DATA_PATH):
    DNGs = glob.glob(DATA_PATH+"/"+dirname+"/"+"*.dng") #list of full paths to dng
    JPGs = glob.glob(DATA_PATH+"/"+dirname+"/"+"*.jpg") #list of full paths to jpg
    #print("DNG:", DNGs)
    #print("JPG:", JPGs)
    for dng_path, jpg_path in zip(DNGs,JPGs):
        dng_name = dng_path.split('/')[-1]
        ## Remove the suffix 1 from [0-9]_short_exposure1.dng###### This problem is not in the jpg files
        dng_name = dng_name.split('.')[-2][:-1] if dng_name.split('.')[-2][-1]=='1' else pass
        ##########################
        jpg_name = jpg_path.split('/')[-1]
        #print("Names are: ",dng_name,"/n", jpg_name)
        shutil.copy(dng_path, os.path.join(NEW_PATH_X,dirname+'_'+dng_name))
        shutil.copy(jpg_path, os.path.join(NEW_PATH_Y,dirname+'_'+jpg_name))''';


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

