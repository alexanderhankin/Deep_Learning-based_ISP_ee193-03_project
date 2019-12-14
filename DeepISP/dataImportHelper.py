import tensorflow as tf

'''def parse_images_MSR(filepathX,filepathY):
    return parse_images(filepathX,filepathY,yftype='png')'''

def parse_image_MSR(filepath):
    return parse_image(filepath,yftype='png')
    
def parse_image_S7_X(filepathX):
    img = parse_image(filepathX,yftype='png')
    return img
        
def parse_image_S7_Y(filepathY):
    img = parse_image(filepathY,yftype='jpeg')
    return img
    

'''def parse_images(filepathX,filepathY,yftype=None):
    imageX = tf.io.read_file(filepathX)  
    imageY = tf.io.read_file(filepathY)  
    imageX = tf.image.decode_png(imageX)
    imageX = tf.image.convert_image_dtype(imageX, tf.float32)
    if yftype=='jpeg':
        imageY = tf.image.decode_jpeg(imageY)
    elif yftype == 'png':
        imageY = tf.image.decode_png(imageY)
    imageY = tf.image.convert_image_dtype(imageY, tf.float32)
    #image = tf.image.resize(imageX, [width, height]) # Might want to use this during inference and if we train on other data
    return imageX, imageY'''

def preprocess_MSR(imageX,imageY):
    return imageX, imageY

def preprocess_S7(image):
    #Crop
    #Flip_left_right
    #Batch
    tf.image.random_crop(image,[1024,1024,3],seed=0)
    
    return image

def random_crop_joint(imageX,imageY):
    imgXY = tf.concat([imageX, imageY], axis=2) #MxNx6
    XY_C = tf.image.random_crop(imgXY, [256,256,6], seed=0) #crop patch from same location
    imgX_C = XY_C[:,:,:3]  #split images
    imgY_C = XY_C[:,:,3:]
    return imgX_C,imgY_C

def random_crop(image):
    img_C = tf.image.random_crop(imgXY, [200,200,3], seed=0) #crop patch from same location
    imgX_C = XY_C[:,:,:3]  #split images

    return img_C

def horizontal_flip_joint(imageX,imageY):
    return tf.image.flip_left_right(imageX),tf.image.flip_left_right(imageY) 

def random_flip_joint(imageX,imageY):
    if tf.math.round(tf.random.uniform([1])) == 1:
        return tf.image.flip_left_right(imageX),tf.image.flip_left_right(imageY)
    else:
        return tf.image.flip_up_down(imageX),tf.image.flip_left_right(imageY)
    


def parse_image(filepath,yftype=None):
    image = tf.io.read_file(filepath)
    if yftype=='jpeg':
        image = tf.image.decode_jpeg(image,channels=3)
    elif yftype == 'png':
        image = tf.image.decode_png(image,channels=3)
    image = tf.image.convert_image_dtype(image, tf.float32)
    tf.debugging.assert_less_equal(image,tf.constant(1,dtype='float32'),'max pixel value greater than 1')
    return image