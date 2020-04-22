# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 11:49:13 2020

@author: vanlo
"""

import numpy as np
import matplotlib.pyplot as plt
from skimage import io


image = io.imread('C:/Users/vanlo/Documents/GitHub/MicroscopyRP_Git/verslag/afbeeldingen/size/zetmeel/zetmeel_7.png')

img = plt.imshow(image)
plt.show()
plt.savefig('C:/Users/vanlo/Documents/GitHub/MicroscopyRP_Git/verslag/afbeeldingen/size/zetmeel/zetmeel_7.png')
