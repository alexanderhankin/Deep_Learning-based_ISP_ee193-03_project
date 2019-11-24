from tensorflow.keras.layers import Conv2D, MaxPool2D, Input, Dense, Flatten, GlobalAvgPool2D, Reshape,Layer, concatenate, add
from tensorflow.keras.models import Model
from tensorflow.keras.utils import plot_model

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
    y = Dense(30)(y)
    y = Reshape((3,10))(y)
    x = Reshape((H*W,10))(x) #TODO: this should be custom layer to get MxNx3 image to MxNx10
    #TODO: layers.Dot(y,x), then reshape to MxNx3
    return Model(input_img, [y,x])