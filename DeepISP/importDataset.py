#!/usr/bin/env python
# coding: utf-8

# In[1]:


## importDataset
## Prepare dataset for training
## Assumes png filenames in X have been corrected to remove suffix 1


# In[2]:


import numpy as np
#import matplotlib.pyplot as plt
import os
import tensorflow as tf
#import pathlib
#import cv2
#import rawpy
import glob


# In[3]:


AUTOTUNE = tf.data.experimental.AUTOTUNE
BATCH_SIZE = 3 #TODO: increase 


# In[4]:


# Reads an image from a file, decodes it into a dense tensor.
# TODO: Figure out how to split tensor string 'filepath' and use filetype to call appropriate decode function
def parse_imagePNG(filepath):
    print('here')
    image = tf.io.read_file(filepath)  
    #image = tf.image.decode_png(image) if tf.strings.split(filepath,sep='.').numpy[-1] == b'png'[-1] else tf.image.decode_jpeg(image) 
    image = tf.image.decode_png(image)
    image = tf.image.convert_image_dtype(image, tf.float32)
    #image = tf.image.resize(imageX, [width, height]) # Might want to use this during inference and if we train on other data
    return image


# In[5]:


# TODO: figure out how to split screen so that there is one pare_image function
def parse_imageJPEG(filepath):
    image = tf.io.read_file(filepath)  
    #image = tf.image.decode_png(image) if tf.strings.split(filepath,sep='.').numpy[-1] == b'png'[-1] else tf.image.decode_jpeg(image) 
    image = tf.image.decode_jpeg(image)
    image = tf.image.convert_image_dtype(image, tf.float32)
    #image = tf.image.resize(imageX, [width, height]) # Might want to use this during inference and if we train on other data
    return image


# In[6]:


def prepare_for_training(ds, cache=True, shuffle_buffer_size=1000):
    if cache:
        if isinstance(cache, str): # cache preprocessing work in file
            ds = ds.cache(cache)
        else:
            ds = ds.cache() #cache in memory
    ds = ds.shuffle(buffer_size=shuffle_buffer_size)

    # Repeat forever
    #ds = ds.repeat() # ?? number of epochs ??

    ds = ds.batch(BATCH_SIZE)

    # `prefetch` lets the dataset fetch batches in the background while the model
    # is training.
    ds = ds.prefetch(buffer_size=AUTOTUNE)

    return ds


# In[7]:


DATAX_PATH = os.path.join(os.getcwd(),'X_dem')
DATAY_PATH = os.path.join(os.getcwd(),'Y')


# In[8]:


fnames = [name.split('.')[-2] for name in os.listdir(DATAX_PATH)] # unique data names (no file extensions or path hierarchy)


# In[9]:


# step 1: Lists of paths to each training data point and ground truth
#X_file_paths = tf.constant([os.path.join(DATAX_PATH,xname+'.png') for xname in fnames]) #this would be equivalent to glob.glob but ensures one-to-one correspondence in X and Y
#Y_file_paths = tf.constant([os.path.join(DATAY_PATH,xname+'.jpg') for xname in fnames])

X_file_paths = [tf.constant(os.path.join(DATAX_PATH,xname+'.png')) for xname in fnames] #this would be equivalent to glob.glob but ensures one-to-one correspondence in X and Y
Y_file_paths = [tf.constant(os.path.join(DATAY_PATH,xname+'.jpg')) for xname in fnames]


# In[10]:


#list_ds = tf.data.Dataset.list_files(str(flowers_root/'*/*'))


# In[11]:


# step 2: create a dataset returning slices of `filenames`
#dataset = tf.data.Dataset.from_tensor_slices(X_file_paths)
#list_dsX = tf.data.Dataset.list_files(X_file_paths)
#list_dsY = tf.data.Dataset.list_files(Y_file_paths)

list_dsX = tf.data.Dataset.list_files(DATAX_PATH+str('/*.png'))
list_dsY = tf.data.Dataset.list_files(DATAY_PATH+str('/*.jpg'))


# In[12]:


# step3: map pare function to each (x,y) TODO: add batch size
dsX = list_dsX.map(parse_imagePNG, num_parallel_calls=AUTOTUNE) # For every path in list_dsX call parse_images
dsY = list_dsY.map(parse_imageJPEG, num_parallel_calls=AUTOTUNE)
# TODO: figure out why dimensions are shown as None when .elementspec
# This shows that data is actually loaded
'''for f in dsX.take(1):
    print(f.numpy()[:10])'''


# In[38]:


labeled_ds = tf.data.Dataset.zip((dsX, dsY)) #combine to one dataset TODO: read more documentation


# In[115]:


dataset = prepare_for_training(dataset) # If everything is correct, this is the dataset to be used in training


# In[10]:


# step 4: create iterator and final input tensor


# In[14]:


dsY.get_output_shapes


# In[ ]:




