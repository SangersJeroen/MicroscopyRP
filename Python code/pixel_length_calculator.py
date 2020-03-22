# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 16:04:14 2020

@author: vanlo
"""

import numpy as np

n_calibration = np.array([684.5, 1246.73, 1249.65])
u_pixels = 4
l_real = np.array([1, 0.8, 0.2])*1e-3        #real lent


l_pixel = l_real/n_calibration
u_l_pixel = u_pixels*l_real/(n_calibration**2)

n_hair = 410.55
n_gf = 788.57 

M_4_40 = l_pixel[0]/l_pixel[2]
u_M_4_40 = np.sqrt((u_l_pixel[2]*l_pixel[0]/(l_pixel[2]**2))**2 + (u_l_pixel[0]/l_pixel[2])**2)

M_4_10 = l_pixel[0]/l_pixel[1]
u_M_4_10 = np.sqrt((u_l_pixel[1]*l_pixel[0]/(l_pixel[1]**2))**2 + (u_l_pixel[0]/l_pixel[1])**2)

M_10_40 = l_pixel[1]/l_pixel[2]
u_M_10_40 = np.sqrt((u_l_pixel[2]*l_pixel[1]/(l_pixel[2]**2))**2 + (u_l_pixel[1]/l_pixel[2])**2)

print(M_4_10)
print(M_10_40)
print(M_4_40)
