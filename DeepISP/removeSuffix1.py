#!/usr/bin/env python
# coding: utf-8

# In[2]:


## removeSuffix1
## script/notebook to remove the suffix 1 from [0-9]_short_exposure1.dng###### This problem is not in the jpg files
## needed if have already demosaiced the dng files
## not  needed if just downloaded the dataset and have version of splitXY that uses this fix


# In[ ]:


import os
import glob
import shutil 


# In[3]:


BASE_PATH = os.getcwd()
PATH_X = os.path.join(os.getcwd(),'X_dem')


# In[11]:


for png_path in glob.glob(PATH_X+'/'+'*.png'):
    name = png_path.split('.')[-2]
    if name[-1]=='1':  os.rename(png_path, name[:-1]+'.png')  

