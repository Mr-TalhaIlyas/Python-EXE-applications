# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 19:32:24 2022

@author: talha
"""
import tensorflow as tf
import os
import numpy as np
from utils.helpers import sigmoid_activation, get_sem, centeroids, draw_cross, pallet_mine
PATH = os.getcwd()

class SurvedModel:

    def __init__(self):
        '''
        Model should be loaded on memory here.  
        '''
        self.model = tf.keras.models.load_model(filepath=PATH+'/model.h5',
                                                compile=False) 
    
        
    def predict (self, img):
        '''
        Preprocessing & inference & postprocessing part.
        # img;attribute = {shape:[H, W, 3],  type : ndarray}
        # or in brain scans case a [H, W, 4] ndarray
        # return;attribute = {shape : [H, W, 3], type : ndarray}
        
        # return your_postprocessing(self.your_model(your_preprocessing(img)))
        '''
        print('start from inside')
        pred = self.model.predict(img[np.newaxis, :,:,:] / 255)
        pred = sigmoid_activation(pred.squeeze())
        
        pred = (pred > 0.5).astype(np.uint8)
        
        x_coords, y_coords, _ = centeroids(pred)
        temp = np.zeros(pred.shape)
        for i in range(len(x_coords)):
            center_coordinates = (x_coords[i], y_coords[i])
            temp = draw_cross(temp, center_coordinates, size=10, clr=(1,0,0), thickness=4)
            
        o_pred = get_sem(temp, img.astype(np.uint8),
                            blend=True, custom_pallet=pallet_mine)
        
        print('sent op')
        return o_pred