#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 22:22:03 2022

@author: yassinebenmansour
"""

import cv2

image = cv2.imread('imag.jpg')


names = []
filesname = 'files/thing.names'

with open(filesname,'rt') as f:
    filesname = f.read().rstrip('\n').split('\n')
    #print(filesname)
    
    x = "files/frozen_inference_graph.pb"
    
    y = "files/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
    
    net = cv2.dnn_DetectionModel(x , y)
    
    net.setInputSize(320,230)
    net.setInputMean((127.5,127.5,127.5))
    net.setInputScale(1.0/127.5)
    net.setInputSwapRB(True)
    
    
    

cv2.imshow("yassine windows",image)

cv2.waitKey(0)
