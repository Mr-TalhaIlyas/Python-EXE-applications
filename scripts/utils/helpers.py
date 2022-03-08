# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 19:32:22 2022

@author: talha
"""

import tensorflow as tf
import cv2
import numpy as np
from gray2color import gray2color

def sigmoid_activation(pred):
    pred = tf.convert_to_tensor(pred)
    active_preds = tf.keras.activations.sigmoid(pred)
    if tf.executing_eagerly()==False:
        sess = tf.compat.v1.Session()
        active_preds = sess.run(active_preds)
    else:
        active_preds = active_preds.numpy()
        
    return active_preds

def draw_cross(img, center_pt, size, clr=(255,0,0), thickness=3):
    '''
    Draws a cross on image with center at 'center_pt' , having length 2*size.
    Parameters
    ----------
    img : input RGB image. 
    center_pt : x and y coordinates of the center of the cross. [tuple: int]
    size : length of the cross, [ int]
    clr : color of the cross. The default is (255,0,0).
    thickness : thickness of line. The default is 3.
    '''
    x, y = center_pt
    cv2.line(img, (x-size, y-size), (x+size, y+size), clr, thickness)
    cv2.line(img, (x-size, y+size), (x+size, y-size), clr, thickness)
    
    return img

def get_sem(sem, img, blend=True, custom_pallet=None):
    '''
    Parameters
    ----------
    sem : a 2D array of shape [H, W] where containing unique value for each class.
    img : Original RGB image for overlaying the semantic seg results
    blend: wether to project the inst mask over the RGB original image or not
    Returns
    -------
    blend : a 3D array in RGB format [H W 3] in which each class have a unique RGB color. 
            1. overalyed over original image if; blend=True
            2. Raw mask if; blend=False
    ''' 
    # if you get shape mismatch error try swaping the (w,h) argument of the line below.
    # i.e., from (x.shape[0], x.shape[1]) to (x.shape[1], x.shape[0]).
    img = cv2.resize(img, (sem.shape[1], sem.shape[0]), interpolation=cv2.INTER_LINEAR) 
    seg = gray2color(sem, use_pallet='pannuke', custom_pallet=custom_pallet)
    
    if blend:
        inv = 1 - cv2.threshold(sem.astype(np.uint8), 0, 1, cv2.THRESH_BINARY)[1]
        inv = cv2.merge((inv, inv, inv))
        blend = np.multiply(img, inv)
        blend = np.add(blend, seg)
    else:
        blend = seg
        
    return blend

def centeroids(img):
        
        MIN_THRESH = 0
        MAX_THRESH = 255

        ret,thresh = cv2.threshold(img, MIN_THRESH, MAX_THRESH, 0)
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE ,cv2.CHAIN_APPROX_SIMPLE)
        x_cord = []
        y_cord = []
        
        for c in contours:
        	# compute the center of the contour
            M = cv2.moments(c)
            if cv2.contourArea(c) > 1:
                
                cX = int(M["m10"] / M["m00"]) # x-coordinate of center
                cY = int(M["m01"] / M["m00"]) # y-coordinate of center
                x_cord = np.append(x_cord, [cX]).astype(np.int16)
                y_cord = np.append(y_cord, [cY]).astype(np.int16)
                
        return x_cord, y_cord, contours 
    
pallet_mine = np.array([[[  0,  0,  0],
                          [  255,0,  0],#[  0,170,  0],
                          [255,255,  0],
                        [255,0,255],
                        [255,200, 20], #  [0,  0,  255]
                        [0,  255,  0],                                              
                        [  0,255,255],
                        [255,  0,255],
                        [128,  0,  0],
                        [  0,128,  0],
                        [  0,  0,128],
                        [128,128,  0],
                        [  0,128,128],
                        [128,  0,128],
                        [128,128,128],
                        [255,128,128],
                        [152, 251, 152],#10
                        [ 70, 130, 180],#11
                        [220,  20,  60],#12
                        [  0,   0, 142],#14
                        [  0,   0,  70],#15
                        [  0,  60, 100],#16
                        [  0,  80, 100],#17
                        [  0,   0, 230],#18
                        [119,  11,  32],#19
                        [128,  64, 128],#20
                        [255, 255, 255]]], np.uint8)/255