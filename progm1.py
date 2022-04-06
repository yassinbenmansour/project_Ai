#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 22:22:03 2022

@author: yassinebenmansour
"""

import cv2

image = cv2.imread('imag.jpg')

cv2.imshow("yassine windows",image)

cv2.waitKey(0)