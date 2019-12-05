import tensorflow as tf

def PSNR_metric(im1,im2):
    #im1 = tf.image.convert_image_dtype(im1, tf.float32)
    #im2 = tf.image.convert_image_dtype(im2, tf.float32)
    return tf.image.psnr(im1, im2, max_val=1.0)