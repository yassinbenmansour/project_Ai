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
    print(filesname)

cv2.imshow("yassine windows",image)

cv2.waitKey(0)
