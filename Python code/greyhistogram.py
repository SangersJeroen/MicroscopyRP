import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib as mpb
import os
import sys

inputfile = str(sys.argv[1])

path = os.getcwd()
data = path+'\\'+inputfile

plt.rcParams['figure.dpi'] = 400
mpb.rcParams.update({
    #"pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    #'text.usetex': True,
    #'pgf.rcfonts': False,
})

def hist(file):
    x = np.linspace(1,256,256)
    for i in range(0,file.shape[0]):
        print(str(i/file.shape[0]*100) + "%")
        for k in range(0,file.shape[1]):
            if file[i][k] != 255:
                x[int(file[i][k])] += 1
    return x, file.shape[0]*file.shape[1]

img = np.array(Image.open(data).convert('L'))
y, p = hist(img)

plt.subplot(121)
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.xlabel('pixel intensity value [-]')
plt.ylabel('relative occurence [-]')
plt.plot(np.linspace(0,255,256), y/p,color='black',marker=',')

plt.subplot(122)
plt.imshow(img, cmap=plt.get_cmap('gray'), vmin=0, vmax=255)
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.gcf().set_size_inches(6, 2)
plt.savefig(inputfile.replace('.bmp','')+'histogram.png',bbox_inches='tight')

