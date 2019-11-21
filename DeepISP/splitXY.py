#!/usr/bin/env python
# coding: utf-8

# In[1]:


## splitXY
## This script/notebook separates the S7 ISP Dataset used in DeepISP paper as downloaded from Kaggle into X and Y folders
## of observations (dng) and ground truths (jpg)
## 


# In[ ]:


import os
import glob
import shutil 


# In[4]:


DATASET_DIR_NAME = 'S7-ISP-Dataset'
BASE_PATH = os.getcwd()
DATA_PATH = os.path.join(BASE_PATH,DATASET_DIR_NAME)
NEW_PATH_X = os.path.join(os.getcwd(),'X')
NEW_PATH_Y = os.path.join(os.getcwd(),'Y')

if not os.path.isdir(NEW_PATH_X): os.mkdir(NEW_PATH_X) # create directories if they don't exist
if not os.path.isdir(NEW_PATH_Y): os.mkdir(NEW_PATH_Y)


# In[6]:


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
        shutil.copy(jpg_path, os.path.join(NEW_PATH_Y,dirname+'_'+jpg_name)) 

