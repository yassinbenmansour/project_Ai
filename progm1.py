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
    
    x = "files/frozen_inference_graph.pb" #poids 
    
    y = "files/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt" #configuration path
    
    net = cv2.dnn_DetectionModel(x , y)
    
    net.setInputSize(320,230)
    net.setInputMean((127.5,127.5,127.5))
    net.setInputScale(1.0/127.5)
    net.setInputSwapRB(True)
    
    Ids ,conf , b = net.detect(image, confThreshold=0.2)
#print(Ids,b)

for classId , confidence , box in zip(Ids.flatten(),conf.flatten(),b):
    cv2.rectangle(image,box,color=(131,84,202),thickness=3)
    cv2.putText(image,filesname[classId-1],
                (box[0]+10,box[1]+20),
                cv2.FONT_HERSHEY_COMPLEX,1,(252,52,52),thickness=2)    
    

cv2.imshow("yassine windows",image)

cv2.waitKey(0)
