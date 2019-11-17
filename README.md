# EE193-03 "Imaging Systems: From Photons to Bits and Back" Final Project

**Team Members:** Alex Hankin, Stam Aleiferis, Alejandro Colina-Valeri, Olive Garst


Recent research in the image processing literature claims to be able to reproduce an end-to-end
image processing pipeline using deep learning. For the EE 193-03 "Imaging Systems: From Photons to
Bits and Back" course final project in the Electrical and Computer Engineering Department at Tufts
University, we will reproduce a deep learning-based (DeepISP: https://arxiv.org/abs/1801.06724) image signal processor
pipeline (using a publicly released dataset) in Python using Keras with a Tensorflow backend and
compare images processed using DeepISP with images processed using a traditional sequential image
processing pipeline (adapted from the one developed in Homework 4 using MATLAB). We will do this for
(1) the subtask of joint demosaicing and denoising, and (2) the full end-to-end image signal
processor pipeline. To understand the sensitivity of the model to a particular image sensor, we
augment the test set with images captured from different image sensors. To evaluate the processed
images for the task of joint demosaicing and denoising, we use the metrics discussed in the course:
Color Peak Signal to Noise Ratio (CPSNR), S-CIELAB, and computational complexity. To evaluate the
processed images for the task of the full end-to-end image processing pipeline, we use subjective
human assessment. 

