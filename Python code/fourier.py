import numpy as np
from PIL import Image
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import matplotlib as mpb
import matplotlib.gridspec as gridspec
import os
import sys

inputfile = str(sys.argv[1])

if sys.argv[1] == "":
    print('Geef werkbestand op')

path = os.getcwd()
data = path+'\\'+inputfile

img = np.array(Image.open(data).convert('L'))

img_colour = np.array(Image.open(data))

print(max(img.flatten()))

f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))

print(fshift.shape)


shape = img.shape


f_new_shift = np.zeros(shape, dtype="cfloat")


x = np.linspace(-(shape[1]-1)/2,(shape[1]-1)/2,shape[1])
y = np.linspace(-(shape[0]-1)/2,(shape[0]-1)/2,shape[0])
X, Y =np.meshgrid(x,y)

R = np.sqrt(X**2 + Y**2)

a = 8
b = 50

for j in range(0,shape[1]-1):
    for i in range(0,shape[0]-1):
        if a<R[i][j]<b:
            f_new_shift[i][j] = fshift[i][j]


"""
for y in range(ycenter-a,ycenter+a):
    for x in range(xcenter-a,xcenter+a):
        f_new_shift[y][x] = 0

for y in range(0,ycenter-2*b):
    for x in range(0,shape[1]-1):
        f_new_shift[y][x] = 0

for y in range(ycenter+2*b,shape[0]-1):
    for x in range(0,shape[1]-1):
        f_new_shift[y][x] = 0
 """

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

img_colour[:,:,0] = img_colour[:,:,0] - img_new
img_colour[:,:,1] = img_colour[:,:,1] - img_new
img_colour[:,:,2] = img_colour[:,:,2] - img_new
plt.imshow(img_colour)
plt.show()
