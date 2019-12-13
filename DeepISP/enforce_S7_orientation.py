#!/usr/bin/env python
# coding: utf-8

# In[32]:


## Preprocessing on S7 dataset
## Correct orientation in X_dem
## After splitXY


# In[ ]:


import numpy as np
import os
from PIL import Image
import glob


# In[33]:


S7_DATA_PATH ='S7-ISP-Dataset-Sorted/S7-ISP-Short-Exposure'
DATAX_PATH = os.path.join(os.getcwd(),S7_DATA_PATH,'X_dem') 
DATAY_PATH = os.path.join(os.getcwd(),S7_DATA_PATH,'Y') 


# In[34]:


names = [x.split('/')[-1].split('.')[0] for x in glob.glob(os.path.join(DATAX_PATH,'*.png'))]
X_paths = [os.path.join(DATAX_PATH,name+'.png') for name in names]
Y_paths = [os.path.join(DATAY_PATH,name+'.jpg') for name in names]


# In[45]:


dimsX = []
dimsY = []
to_transposeX = []
to_transposeY = []


# In[44]:


# Correct orientation of the few images in X_dem to match the orientation of all images
# Ground truth images have correct rotation
for Xpath,Ypath in zip(X_paths,Y_paths):
    with Image.open(Xpath) as imageX, Image.open(Ypath) as imageY :
        dimsX.append(imageX.size)
        dimsY.append(imageY.size)
        if imageX.size[0] < imageX.size[1]:
            to_transposeX.append(Xpath)
            #Image.show(test_image)
            #test_image.save(path)
            imageX.transpose(Image.ROTATE_90).save(Xpath)
        if imageY.size[0] < imageY.size[1]:
            to_transposeY.append(Ypath)
        


# In[46]:


# Test that images were rotated correctly
'''for Xpath in X_paths:
    with Image.open(Xpath) as imageX :
        dimsX.append(imageX.size)'''
    


# In[ ]:




