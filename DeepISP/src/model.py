from tensorflow.keras.layers import Conv2D, MaxPool2D, Input, Dense, Flatten, GlobalAvgPool2D, Reshape,Layer,Lambda, concatenate, add
from tensorflow.keras.models import Model
from tensorflow.keras.utils import plot_model
import tensorflow_probability as tfp
import tensorflow as tf
import numpy as np

# One unit of RGB correction part of low level stage (right column in Fig2)
def lowLevelBlock1(input_img):
    y = Conv2D(input_shape = input_img.shape,
               filters = 3,
               kernel_size = (3,3),
               strides = (1,1),
               padding = "same",
               activation = "tanh")(input_img)
    z = add([y, input_img]) # add residual from previous stage

    return z

# One unit of feature part of low level stage (left column in Fig2)
def lowLevelBlock2(input_img):
    y = Conv2D(input_shape = input_img.shape,
               filters = 61,
               kernel_size = (3,3),
               strides = (1,1),
               padding = "same",
               activation = "relu")(input_img)

    return y

# One unit of Conv+Max-pool blocks of high level stage
def highLevelBlock(input_img):
    y = Conv2D(input_shape = input_img.shape,
               filters = 61,
               kernel_size = (3,3),
               strides = (2,2),
               padding = "same",
               activation = "relu")(input_img)
    y = MaxPool2D(pool_size=2, padding="same")(y)
    return y


# Extends the Layer class to build the T layer as explained in the paper
class LayerT(Layer):
    def __init__(self, **kwargs):
        #self.output_dim = output_dim
        super(LayerT, self).__init__(**kwargs)
        
    def call(self, inputs):
        W,I = inputs
        #Expect W to be 10x3
        #Expect I to be MxNx3 -> do pixel transformation, reshape it to MxNx10
        #output should be I x W' -> MxNx3
        c = tf.ones_like(inputs[1]) # MxNx3
        c = tf.expand_dims(c[:,:,:,0],-1) # MxNx1
        I = tf.concat([I,c],axis=3) #MxNx4
        I = tf.expand_dims(I,-1) # MxNx4x1
        It = tf.transpose(I,[0,1,2,4,3]) #MxNx1x4
        T = tfp.math.fill_triangular_inverse(tf.matmul(I,It),upper=True) # MxNx10
        S = tf.matmul(T,W)
        #print(S.shape)
        return S
        
    def build(self, input_shape):
        super(LayerT, self).build(input_shape)  # Be sure to call this at the end        

# Returns model for training and inference on joint demosaicing and denoising
def create_low_level_stage(H,W,N_ll):
    input_img = Input(shape=(H, W, 3))
    x = input_img
    for _ in range(N_ll):
        x = lowLevelBlock1(x)
    ll_model = Model(input_img,x)
    return ll_model

# Returns model for training and inference on full ISP
def create_complete_model(H,W,N_ll,N_hl):
    input_img = Input(shape=(H, W, 3))
    x = input_img
    y = input_img
    for _ in range(N_ll): # RGB correction part of lowlevel stage
        x = lowLevelBlock1(x) # output of lowlevel stage. To be reshaped and fed into T
    for _ in range(N_ll): # feature part of lowlevel stage
        y = lowLevelBlock2(y)
    # High level stage
    for _ in range(N_hl):
        y = highLevelBlock(y)
    y = GlobalAvgPool2D()(y)
    y = Dense(30)(y)          #TODO: Initialize this weights as described in the paper
    y = Reshape((10,3))(y)
    
    #out = Lambda(customT(y,x))(y,x)
    out = LayerT()([y,x])
    return Model(input_img, out)