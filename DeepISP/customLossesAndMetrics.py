import tensorflow as tf
from tensorflow.keras.losses import Loss
from ColorSpaces import rgb_to_lab
from dataImportHelper import random_crop_joint


def PSNR_metric(im1,im2):
    #im1 = tf.image.convert_image_dtype(im1, tf.float32)
    #im2 = tf.image.convert_image_dtype(im2, tf.float32)
    return tf.image.psnr(im1, im2, max_val=1.0)

def HL_loss(im1,im2):
    ## L shoudl be ssim_multiscale
    alpha = 0.5
    L1 = rgb_to_lab(im1)
    #tf.debugging.assert_all_finite(L1,'is not finite')
    L2 = rgb_to_lab(im2)
    #print(tf.expand_dims(L1[:,:,:,0],-1))
    #print(tf.expand_dims(L2[:,:,:,0],-1))
    #tf.debugging.assert_all_finite(L2,'is not finite')
    #L1 = im1
    #L2 = im2
    G = tf.reduce_sum(tf.math.abs(tf.math.subtract(L1,L2))) #Global corrections
    #C1, C2 = random_crop(L1,L2)
    L = tf.image.ssim_multiscale(
            tf.expand_dims(L1[:,:,:,0],-1),
            tf.expand_dims(L2[:,:,:,0],-1),
            1, #max val
            power_factors=[0.2363, 0.1333],
            filter_size=11,
            filter_sigma=1.5,
            k1=0.01,
            k2=0.03
        )
    #L=0
    #print(L.shape)
    #print(L1.shape)
    #print(L2.shape)
    #print(G.shape)
    #print(L.shape)
    #print(L)
    return ((1-alpha) * G - alpha * L)
     

def random_crop(imageX,imageY):
    '''imgXY = tf.concat([imageX, imageY], axis=3) #BatchxMxNx6
    XY_C = tf.image.random_crop(imgXY, [10,10,2], seed=0) #crop patch from same location
    imgX_C = XY_C[:,:,0]  #split images
    imgY_C = XY_C[:,:,1]'''
    #print(imageX.shape)
    imgX = tf.image.central_crop(imageX,0.0002)
    imgY = tf.image.central_crop(imageX,0.0002)
    #return imgX,imgY
    return imageX,imageY


# Not used for now
class MSSSIM(Loss):
    
    def random_crop(self,imageX,imageY):
        '''imgXY = tf.concat([imageX, imageY], axis=3) #BatchxMxNx6
        XY_C = tf.image.random_crop(imgXY, [10,10,2], seed=0) #crop patch from same location
        imgX_C = XY_C[:,:,0]  #split images
        imgY_C = XY_C[:,:,1]'''
        #print(imageX.shape)
        #imgX = tf.image.central_crop(imageX,0.002)
        #imgY = tf.image.central_crop(imageX,0.002)
        #return imgX,imgY
        return imageX,imageY

    
    def call(self, im1, im2):
        
        alpha = 0.5
        L1 = rgb_to_lab(im1)
        L2 = rgb_to_lab(im2)
        #L1 = im1
        #L2 = im2
        #G = tf.reduce_sum(tf.math.abs(tf.math.subtract(L1,L2))) #Global corrections
        C1, C2 = self.random_crop(L1,L2)
        L = tf.image.ssim_multiscale(
            tf.expand_dims(C1[:,:,:,0],-1),
            tf.expand_dims(C2[:,:,:,0],-1),
            1, #max val
            power_factors=[0.0448, 0.2856],
            filter_size=11,
            filter_sigma=1.5,
            k1=0.01,
            k2=0.03
        )
        #print(L.shape)
        #print(L1.shape)
        #print(L2.shape)
        #print(G.shape)
        print(L.shape)
        print(L)
        #return -1*((1-alpha) * G + alpha * L)
        return -L

    