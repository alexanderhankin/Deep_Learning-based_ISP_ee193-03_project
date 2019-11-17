# Compiles and trains the model with loss function adapted 
#   from the one specified in "Scwartz et. al, DeepISP:..."

if __name__ == '__main__':

    # Try running model with mnist
    from keras.datasets import mnist
    #download mnist data and split into train and test sets
    (X_train, y_train), (X_test, y_test) = mnist.load_data()
    
    import matplotlib.pyplot as plt
    #plot the first image in the dataset
    plt.imshow(X_train[0])
    
    #check image shape
    X_train[0].shape
    
    #reshape data to fit model
    X_train = X_train.reshape(60000,28,28,1)
    X_test = X_test.reshape(10000,28,28,1)
    print size(X_train)
    print size(X_test)
    paddings = tf.constant([[2, 10,], [3, 10]])
    tf.pad(X_train, paddings, "CONSTANT")
    tf.pad(X_test, paddings, "CONSTANT")
    
    X_train = tf.image.grayscale_to_rgb(X_train)
    X_test = tf.image.grayscale_to_rgb(X_test)
    
    
    from keras.utils import to_categorical
    #one-hot encode target column
    y_train = to_categorical(y_train)
    y_test = to_categorical(y_test)
    y_train[0]
    
    model = build_model(input_shape=(28, 28, 3))
    
    #compile model using accuracy to measure model performance
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
       
    #train the model
    model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=3)
    
    #predict first 4 images in the test set
    model.predict(X_test[:4])
    
    #actual results for first 4 images in test set
    y_test[:4]
    #model.summary()
    plot_model(model, to_file='model.png', show_shapes=True)
    
