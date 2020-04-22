# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 14:09:12 2020

@author: vanlo
"""


import numpy as np
import matplotlib.pyplot as plt

from skimage.filters.rank import median
from skimage.filters.rank import mean_bilateral
from skimage.filters.rank import enhance_contrast
from skimage.morphology import disk
from skimage import img_as_ubyte
from skimage import data
from skimage import exposure
import os
from skimage import io
import skimage

plt.clf()

image = io.imread('licht_zonder_rand.bmp', as_gray=True)
image_cut = image[int(np.shape(image)[0]/2-300):int(np.shape(image)[0]/2+300),int(np.shape(image)[1]/2-600):int(np.shape(image)[1]/2+600)]

bilat = mean_bilateral(image_cut, disk(20), s0=20, s1=20)

cont = exposure.equalize_hist(image_cut) * 255
cont_bilat = exposure.equalize_hist(bilat) * 255

morph = enhance_contrast(image_cut, disk(5))
morph_bilat = enhance_contrast(bilat, disk(5))
morph_cont_bilat = enhance_contrast(cont_bilat/255, disk(5))
morph_cont = enhance_contrast(cont/255, disk(5))


print(np.shape(image))



img = plt.imshow(image_cut,cmap='gray')
plt.savefig('C:/Users/vanlo/Documents/GitHub/MicroscopyRP_Git/verslag/afbeeldingen/rank/img.png', bbox_inches='tight')

plt.clf


img_bilat = plt.imshow(bilat,cmap='gray')
plt.savefig('C:/Users/vanlo/Documents/GitHub/MicroscopyRP_Git/verslag/afbeeldingen/rank/img_bilat.png', bbox_inches='tight')

plt.clf

img_cont = plt.imshow(cont,cmap='gray')
plt.savefig('C:/Users/vanlo/Documents/GitHub/MicroscopyRP_Git/verslag/afbeeldingen/rank/img_cont.png', bbox_inches='tight')

plt.clf

img_morph = plt.imshow(morph,cmap='gray')
plt.savefig('C:/Users/vanlo/Documents/GitHub/MicroscopyRP_Git/verslag/afbeeldingen/rank/img_morph.png', bbox_inches='tight')

plt.clf

img_morph_bilat = plt.imshow(morph_bilat,cmap='gray')
plt.savefig('C:/Users/vanlo/Documents/GitHub/MicroscopyRP_Git/verslag/afbeeldingen/rank/img_morph_bilat.png', bbox_inches='tight')

plt.clf

img_morph_glob_bilat = plt.imshow(morph_cont_bilat,cmap='gray')
plt.savefig('C:/Users/vanlo/Documents/GitHub/MicroscopyRP_Git/verslag/afbeeldingen/rank/img_morph_cont_bilat.png', bbox_inches='tight')

plt.clf

img_cont_bilat = plt.imshow(cont_bilat,cmap='gray')
plt.savefig('C:/Users/vanlo/Documents/GitHub/MicroscopyRP_Git/verslag/afbeeldingen/rank/img_cont_bilat.png', bbox_inches='tight')

plt.clf

img_morph_cont = plt.imshow(morph_cont,cmap='gray')
plt.savefig('C:/Users/vanlo/Documents/GitHub/MicroscopyRP_Git/verslag/afbeeldingen/rank/img_morph_cont.png', bbox_inches='tight')




#fig, ax = plt.subplots(1, 2, figsize=(10, 7), sharex=True, sharey=True)
#
#ax1.imshow(image, vmin=0, vmax=255, cmap=plt.cm.gray)
#ax1.set_title('Noisy image')
#ax1.axis('off')
#
#
#ax2.imshow(median(image, disk(1)), vmin=0, vmax=255, cmap=plt.cm.gray)
#ax2.set_title('Median $r=1$')
#ax2.axis('off')


#
#ax3.imshow(median(image, disk(5)), vmin=0, vmax=255, cmap=plt.cm.gray)
#ax3.set_title('Median $r=5$')
#ax3.axis('off')
#
#
#
#ax4.imshow(median(image, disk(20)), vmin=0, vmax=255, cmap=plt.cm.gray)
#ax4.set_title('Median $r=20$')
#ax4.axis('off')

