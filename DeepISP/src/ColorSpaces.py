# Convert RGB to Lab
# Code from https://github.com/affinelayer/pix2pix-tensorflow/blob/master/pix2pix.py

import tensorflow as tf

def rgb_to_lab(srgb):
    with tf.name_scope("rgb_to_lab"):
        srgb = check_image(srgb)
        #print(srgb)
        #tf.debugging.assert_all_finite(srgb,'srgb has NaN')
        srgb_pixels = tf.reshape(srgb, [-1, 3])

        with tf.name_scope("srgb_to_xyz"):
            #linear_mask = tf.cast(srgb_pixels <= 0.04045, dtype=tf.float32)
            #exponential_mask = tf.cast(srgb_pixels > 0.04045, dtype=tf.float32)
            #rgb_pixels = (srgb_pixels / 12.92 * linear_mask) + (((srgb_pixels + 0.055) / 1.055) ** 2.4) * exponential_mask
            rgb_pixels = srgb_pixels
            tf.debugging.assert_all_finite(rgb_pixels,'rgb_pixels has NaN')
            rgb_to_xyz = tf.constant([
                #    X        Y          Z
                [0.412453, 0.212671, 0.019334], # R
                [0.357580, 0.715160, 0.119193], # G
                [0.180423, 0.072169, 0.950227], # B
            ])
            xyz_pixels = tf.matmul(srgb_pixels, rgb_to_xyz)
            #tf.debugging.assert_all_finite(xyz_pixels,'xyz_pixels has NaN')
        # https://en.wikipedia.org/wiki/Lab_color_space#CIELAB-CIEXYZ_conversions
        with tf.name_scope("xyz_to_cielab"):
            # convert to fx = f(X/Xn), fy = f(Y/Yn), fz = f(Z/Zn)

            # normalize for D65 white point
            xyz_normalized_pixels = tf.multiply(xyz_pixels, [1/0.950456, 1.0, 1/1.088754])
            #tf.debugging.assert_all_finite(xyz_normalized_pixels,'xyz_normalized_pixels has NaN')
            
            
            #epsilon = 6/29
            #linear_mask = tf.cast(xyz_normalized_pixels <= (epsilon**3), dtype=tf.float32)
            #exponential_mask = tf.cast(xyz_normalized_pixels > (epsilon**3), dtype=tf.float32)
            
            #fxfyfz_pixels = (xyz_normalized_pixels / (3 * epsilon**2) + 4/29) * linear_mask 
            #tf.debugging.assert_all_finite(fxfyfz_pixels,'fxfyfz_pixels (1) has NaN')
            
            #fxfyfz_pixels=fxfyfz_pixels+ (xyz_normalized_pixels ** (1/3)) * exponential_mask 
            #tf.debugging.assert_all_finite(fxfyfz_pixels,'fxfyfz_pixels (2) has NaN')
            
            fxfyfz_pixels = xyz_normalized_pixels
            #tf.debugging.assert_all_finite(fxfyfz_pixels,'fxfyfz_pixels has NaN')
            # convert to lab
            fxfyfz_to_lab = tf.constant([
                #  l       a       b
                [  0.0,  500.0,    0.0], # fx
                [116.0, -500.0,  200.0], # fy
                [  0.0,    0.0, -200.0], # fz
            ])
            lab_pixels = tf.matmul(fxfyfz_pixels, fxfyfz_to_lab) + tf.constant([-16.0, 0.0, 0.0])
        #tf.debugging.assert_all_finite(lab_pixels,'lab_pixels has NaN')
        return tf.reshape(lab_pixels, tf.shape(srgb))


def check_image(image):
    assertion = tf.assert_equal(tf.shape(image)[-1], 3, message="image must have 3 color channels")
    with tf.control_dependencies([assertion]):
        image = tf.identity(image)

    if image.get_shape().ndims not in (3, 4):
        raise ValueError("image must be either 3 or 4 dimensions")

    # make the last dimension 3 so that you can unstack the colors
    shape = list(image.get_shape())
    shape[-1] = 3
    image.set_shape(shape)
    return image