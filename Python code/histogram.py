import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as image
import os
import sys

inputfile = str(sys.argv[1])

path = os.getcwd()
Image.open(path+'\\'+inputfile).save(path+'\\'+inputfile+'.png')
data = image.imread(path+'\\'+inputfile+'.png')

plt.rcParams['figure.dpi'] = 200

x = np.linspace(0,255,256)
y = np.zeros(256)
b = np.zeros(256)
r = np.zeros(256)

for i in range(0,data.shape[1]-1):
    for j in range(0,data.shape[0]-1):
        y[int((data[j][i][0])*255)] += 1
        r[int((data[j][i][1])*255)] += 1
        b[int((data[j][i][2])*255)] += 1

plt.plot(x, y, 'y.')
plt.plot(x, r, 'r.')
plt.plot(x, b, 'b.')
plt.show()