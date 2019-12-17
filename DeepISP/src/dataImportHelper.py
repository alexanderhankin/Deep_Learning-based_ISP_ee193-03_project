# Various functions for 1) reading in the dataset as tf.data.Dataset object and 2) Augmenting the dataset
# These functions are used in the training scripts in the .map() calls
import tensorflow as tf

# Input a filepath, get a tensorflow Tensor image
def parse_image_MSR(filepath):
    return parse_image(filepath,yftype='png')
    
def parse_image_S7_X(filepathX):
    img = parse_image(filepathX,yftype='png')
    return img
        
def parse_image_S7_Y(filepathY):
    img = parse_image(filepathY,yftype='jpeg')
    return img

# Not used for now
def preprocess_MSR(imageX,imageY):
    return imageX, imageY

# Input a "raw" image and its ground truth, return two 256x256 patches 
def random_crop_joint(imageX,imageY):
    imgXY = tf.concat([imageX, imageY], axis=2) #MxNx6
    XY_C = tf.image.random_crop(imgXY, [256,256,6], seed=0) #crop patch from same location
    imgX_C = XY_C[:,:,:3]  #split images
    imgY_C = XY_C[:,:,3:]
    return imgX_C,imgY_C


def horizontal_flip_joint(imageX,imageY):
    return tf.image.flip_left_right(imageX),tf.image.flip_left_right(imageY) 

def random_flip_joint(imageX,imageY):
    if tf.math.round(tf.random.uniform([1])) == 1:
        return tf.image.flip_left_right(imageX),tf.image.flip_left_right(imageY)
    else:
        return tf.image.flip_up_down(imageX),tf.image.flip_up_down(imageY)
    

def parse_image(filepath,yftype=None):
    image = tf.io.read_file(filepath)
    if yftype=='jpeg':
        image = tf.image.decode_jpeg(image,channels=3)
    elif yftype == 'png':
        image = tf.image.decode_png(image,channels=3)
    image = tf.image.convert_image_dtype(image, tf.float32)
    #tf.debugging.assert_less_equal(image,tf.constant(1,dtype='float32'),'max pixel value greater than 1')
    return image