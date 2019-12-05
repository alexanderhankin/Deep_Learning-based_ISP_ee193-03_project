import tensorflow as tf

def parse_images_MSR(filepathX,filepathY):
    return parse_images(filepathX,filepathY,yftype='png')

def parse_image_MSR(filepath):
    return parse_image(filepath,yftype='png')
    
def parse_images_S7(filepathX,filepathY):
    return parse_image(filepathX,filepathY,yftype='jpeg')
    

def parse_images(filepathX,filepathY,yftype=None):
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
    return imageX, imageY
def preprocess_MSR(imageX,imageY):
    return imageX, imageY


def parse_image(filepath,yftype=None):
    image = tf.io.read_file(filepath)
    if yftype=='jpeg':
        image = tf.image.decode_jpeg(image,channels=3)
    elif yftype == 'png':
        image = tf.image.decode_png(image,channels=3)
    image = tf.image.convert_image_dtype(image, tf.float32)
    return image
    
def demosaic_raw(RAW_PATH=None,NEW_PATH=None,ftype=None):
    image_paths = glob.glob(RAW_PATH_X+'/'+'*.'+'ftype') # full paths to raw
    