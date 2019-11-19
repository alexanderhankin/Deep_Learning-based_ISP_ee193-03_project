# Preprocessing of the dataset
# This code does the necessary manipulations to the dataset 
#   to prepare it to be fed in to the network

import cv2
import os
import glob
import shutil 
import re
import rawpy

BASE_PATH = os.getcwd()
DATA_PATH = os.path.join(BASE_PATH,'S7-ISP-Dataset')
NEW_PATH_X = os.path.join(os.getcwd(),'X')
NEW_PATH_Y = os.path.join(os.getcwd(),'Y')

if ~os.path.isdir(NEW_PATH_X): os.mkdir(NEW_PATH_X)
if ~os.path.isdir(NEW_PATH_Y): os.mkdir(NEW_PATH_Y)

for dirname in os.listdir(DATA_PATH):
    DNGs = glob.glob(DATA_PATH+"/"+dirname+"/"+"*.dng") #list of full paths to dng
    JPGs = glob.glob(DATA_PATH+"/"+dirname+"/"+"*.jpg") #list of full paths to jpg
    for dng_path, jpg_path in zip(DNGs,JPGs):
        dng_name = dng_path.split('/')[-1]
        jpg_name = jpg_path.split('/')[-1]
        shutil.copy(dng_path, os.path.join(NEW_PATH_X,dirname+dng_name))
        shutil.copy(jpg_path, os.path.join(NEW_PATH_Y,dirname+jpg_name)) 


# Form X_train, X_test, Y_train, and Y_test
# 'se' and 'me' denote short and medium exposure, respectively
num_se_files=110
num_me_files=110

percent_train_set=.60
num_train_examples=int(num_se_files*percent_train_set)

# Instantiate train and test tensors 
X_se_train = {}
X_se_test = {} 
X_me_train = {}
X_me_test = {} 
Y_se_train = {}
Y_se_test = {} 
Y_me_train = {}
Y_me_test = {} 

for _class in ['X', 'Y']:
    for exposure_type in ['short_exposure', 'medium_exposure']:
        for _iter, file_path in enumerate(glob.glob(_class + '/*' + exposure_type + '*')):
            print ('File iterator: ' + str(_iter))
            print ('File path: ' + file_path)
            
            # Read in image file
            if _class == 'X': # .dng file
                img = rawpy.imread(file_path) 
            else: # .jpg file
                img = cv2.imread(file_path, flags=cv2.IMREAD_COLOR) 
                    
            # Grab file ID # from path
            id_num = ''.join(re.findall(r'\d+', file_path))
            print ('ID #: ' + id_num)
            
            # Add image to appropriate set
            if _class == 'X' and exposure_type == 'short_exposure':
                # Add to train set
                if _iter < num_train_examples:
                    print('Adding to X_se_train\n')
                    X_se_train[id_num] = img
                else: # Add to test set
                    print('Adding to X_se_test\n')
                    X_se_test[id_num] = img
            
            elif _class == 'X' and exposure_type == 'medium_exposure':
                # Add to train set
                if _iter < num_train_examples:
                    print('Adding to X_me_train\n')
                    X_me_train[id_num] = img
                else: # Add to test set
                    print('Adding to X_me_test\n')
                    X_me_test[id_num] = img
            
            elif _class == 'Y' and exposure_type == 'short_exposure':
                # Add to train set
                if _iter < num_train_examples:
                    print('Adding to Y_se_train\n')
                    Y_se_train[id_num] = img
                else: # Add to test set
                    print('Adding to Y_se_test\n')
                    Y_se_test[id_num] = img
            
            elif _class == 'Y' and exposure_type == 'medium_exposure':
                # Add to train set
                if _iter < num_train_examples:
                    print('Adding to Y_me_train\n')
                    Y_me_train[id_num] = img
                else: # Add to test set
                    print('Adding to Y_me_test\n')
                    Y_me_test[id_num] = img

