import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
import sys

inputfile = str(sys.argv[1])

path = os.getcwd()
data = path+'\\'+inputfile

plt.rcParams['figure.dpi'] = 200

def hist(file):
    x = np.linspace(1,256,256)
    for i in range(0,file.shape[0]):
        for k in range(0,file.shape[1]):
            x[int(file[i][k])] += 1
    return x, file.shape[0]*file.shape[1]

img = np.array(Image.open(data).convert('L'))
y, p = hist(img)

plt.plot(np.linspace(0,255,256), y)
plt.show()

plt.imshow(img, cmap=plt.get_cmap('gray'), vmin=0, vmax=255)
plt.show()
