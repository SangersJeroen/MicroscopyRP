# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 11:49:13 2020

@author: vanlo
"""

import numpy as np
import matplotlib.pyplot as plt
from skimage import io

plt.clf()
image = io.imread("C:/Users/vanlo/Documents/GitHub/MicroscopyRP_Git/RP/Magn 3 fiber.jpg")

img = plt.imshow(image)

plt.savefig('C:/Users/vanlo/Documents/GitHub/MicroscopyRP_Git/verslag/afbeeldingen/size/gf.jpg')
