# -*- coding: utf-8 -*-
"""
Created on Fri May  1 21:14:56 2020

@author: HP
"""
import re
import numpy as np
from PIL import Image

from sklearn.model_selection import train_test_split
from keras import backend as K
from keras.layers import Activation
from keras.layers import Input, Lambda, Dense, Dropout, Convolution2D, MaxPooling2D, Flatten,Concatenate,Reshape
from keras.models import Sequential, Model
from keras.optimizers import RMSprop

import tensorflow as tf

def multi_modal_network(input_shape):
   kernel_size = 3
   seq = Sequential()
   seq.add(Convolution2D(6, kern