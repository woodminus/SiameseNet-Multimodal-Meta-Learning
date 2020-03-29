
# -*- coding: utf-8 -*-
"""
Created on Sat May  2 13:08:47 2020

@author: HP
"""

import tensorflow as tf
import matplotlib.pyplot as plt

def data():
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
    count=[]
    for i in range(0,10):
        count.append(0)
    x_num=[]
    y_num=[]
    num=0
    i=0
    while(num!=10 and i<1000):
        if(count[y_train[i]]<2):
            x_num.append(x_train[i])
            y_num.append(y_train[i])