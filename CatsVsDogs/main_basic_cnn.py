import os
import random
import warnings
warnings.filterwarnings("ignore")
from utils import train_test_split

from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Dropout, Flatten, Dense, BatchNormalization #batch normalization may be used for optimizing so i added it
from keras.preprocessing.image import ImageDataGenerator

# from project pdf:
# Conv2D class will be used for the convolution layers, MaxPooling2D for pooling layers,
# and Dense for the fully connected layers. (Note that you will need to add a Flatten layer
# between the last pooling layer and the first fully connected layer for reshaping purposes).

#keras documentation: https://keras.io/2/api/

#these will be the hyperparameters:

filterSize = (3,3) 
numOfFilters = 32
inputSize = (150,150,3) #every image will be resized to 150x150 pixels, and it will have 3 color channels aka rgb
poolingSize = (2,2)

model = Sequential()

#following the diagram on the project pdf, i only have 2 convolution+pooling layers then the last
#is the fully connected layer responsible for the predictions. to optimize, maybe an another hidden layer
#with either the same or more filters than the last layer.

model.add((Conv2D(numOfFilters,filterSize, activation='relu',input_shape = inputSize)))
#model.add(BatchNormalization()) could be used to optimize
model.add((MaxPooling2D(pool_size=poolingSize,strides=2)))


model.add((Conv2D(numOfFilters*2,filterSize, activation='relu')))
#model.add(BatchNormalization()) could be used to optimize
model.add(MaxPooling2D(pool_size=poolingSize))


model.add(Flatten())
model.add(Dense(64, activation='relu'))
model.add(Dense(1, activation='sigmoid')) #pdf says to use sigmoid for the classification
#if model overfits during training, consider using dropout 

#to start off question 3
model.compile(optimizer = "adam", loss = "binary_crossentropy", metrics = ["accuracy"])

