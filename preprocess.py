#!/usr/bin/env python
# coding: utf-8

# Preprocessing of the dataset
# This code does the necessary manipulations to the dataset 
#   to prepare it to be fed in to the network

import os
import glob
import shutil 

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

