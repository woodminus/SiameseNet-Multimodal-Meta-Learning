# -*- coding: utf-8 -*-
"""
Created on Fri May  1 21:15:25 2020

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
import feature_extractor
import fusion

def siamese_network(input_dim_img,input_dim_aud):
    
    img_a = Input(shape=input_dim_img)
    img_b = Input(shape=input_dim_img)
    aud_a = Input(shape=input_dim_aud)
    aud_b = Input(shape=input_dim_aud)

    img_network = feature_extractor.image_feat_netwo