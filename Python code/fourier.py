import numpy as np
from PIL import Image
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import matplotlib as mpb
import matplotlib.gridspec as gridspec
import os
import sys

inputfile = str(sys.argv[1])

path = os.getcwd()
data = path+'\\'+inputfile

img = np.array(Image.open(data).convert('L'))

f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))

print(fshift.shape)

f_new_shift = fshift

for i in range(200,700):
    for j in range(200,1000):
        f_new_shift[i][j] = 0



f_new = np.fft.ifftshift(f_new_shift)

img_new = np.abs(np.fft.ifft2(f_new))

magnitude_spectrum_new = 20*np.log(np.abs(f_new_shift))



plt.subplot(221),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])


plt.subplot(223),plt.imshow(img_new, cmap = 'gray')
plt.title('Output Image'), plt.xticks([]), plt.yticks([])
plt.subplot(224),plt.imshow(magnitude_spectrum_new, cmap = 'gray')
plt.title('Magnitude Spectrum New'), plt.xticks([]), plt.yticks([])
plt.show()