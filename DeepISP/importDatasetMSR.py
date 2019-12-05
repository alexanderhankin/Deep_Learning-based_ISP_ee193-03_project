#!/usr/bin/env python
# coding: utf-8

# In[13]:


## importDataset
## Prepare dataset for training
## Assumes png filenames in X have been corrected to remove suffix 1


# In[14]:


import numpy as np
#import matplotlib.pyplot as plt
import os
import tensorflow as tf
#import pathlib
#import cv2
#import rawpy
import glob
from importDataset import parse_imagePNG


AUTOTUNE = tf.data.experimental.AUTOTUNE
BATCH_SIZE = 3 #TODO: increase 

DATAX_PATH = os.path.join(os.getcwd(),'X_dem_MSR')
DATAY_PATH = os.path.join(os.getcwd(),'MSR-Demosaicing/Dataset_LINEAR_with_noise/bayer_panasonic/groundtruth')

fnames = [name.split('.')[-2] for name in os.listdir(DATAX_PATH)] # unique data names (no file extensions or path hierarchy)

# step 1: Lists of paths to each training data point and ground truth
#X_file_paths = tf.constant([os.path.join(DATAX_PATH,xname+'.png') for xname in fnames]) #this would be equivalent to glob.glob but ensures one-to-one correspondence in X and Y
#Y_file_paths = tf.constant([os.path.join(DATAY_PATH,xname+'.jpg') for xname in fnames])

X_file_paths = [tf.constant(os.path.join(DATAX_PATH,xname+'.png')) for xname in fnames] #this would be equivalent to glob.glob but ensures one-to-one correspondence in X and Y
Y_file_paths = [tf.constant(os.path.join(DATAY_PATH,xname+'.png')) for xname in fnames]


#list_ds = tf.data.Dataset.list_files(str(flowers_root/'*/*'))


# step 2: create a dataset returning slices of `filenames`
#dataset = tf.data.Dataset.from_tensor_slices(X_file_paths)
#list_dsX = tf.data.Dataset.list_files(X_file_paths)
#list_dsY = tf.data.Dataset.list_files(Y_file_paths)

list_dsX = tf.data.Dataset.list_files(DATAX_PATH+str('/*.png'))
list_dsY = tf.data.Dataset.list_files(DATAY_PATH+str('/*.png'))


# In[ ]:


# step3: map pare function to each (x,y) TODO: add batch size
dsX = list_dsX.map(parse_imagePNG, num_parallel_calls=AUTOTUNE) # For every path in list_dsX call parse_images
dsY = list_dsY.map(parse_imagePNG, num_parallel_calls=AUTOTUNE)
# TODO: figure out why dimensions are shown as None when .elementspec
# This shows that data is actually loaded
'''for f in dsX.take(1):
    print(f.numpy()[:10])'''


# In[ ]:


labeled_ds = tf.data.Dataset.zip((dsX, dsY)) #combine to one dataset TODO: read more documentation


# In[ ]:


#dataset = prepare_for_training(dataset) # If everything is correct, this is the dataset to be used in training


# In[ ]:


# step 4: create iterator and final input tensor
