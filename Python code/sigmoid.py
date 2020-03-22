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
img_cleaned = np.asarray([i for i in img.flatten() if i != 0 and i!=255])

a = np.average(img_cleaned)
b = np.std(img_cleaned)

print(a,b)

x = np.linspace(0,255,256)

def sigmoid(x):
    return 1/(1+np.exp(-(x-a)/b))*255

y = sigmoid(x)

s_trans = sigmoid(img)

#mpb.use("pgf")
mpb.rcParams['figure.dpi']=300
mpb.rcParams.update({
    #"pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    #'text.usetex': True,
    #'pgf.rcfonts': False,
})

gridspec.GridSpec(3,2)

plt.subplot2grid((3,2),(0,0))
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.xlim([0,100])
plt.ylabel('occurence [-]')
plt.xlabel('Pixel value $[-]$')
plt.hist(img_clean,101,color='black')

plt.subplot2grid((3,2),(0,1))
plt.imshow(img, cmap=plt.get_cmap('gray'), vmin=0, vmax=255)

plt.subplot2grid((3,2),(1,0), colspan=2)
plt.xlim([0,220])
plt.axvline(x=a, linestyle='-', color='grey')
plt.axvline(x=a+b, linestyle='--', color='#C0C0C0')
plt.axvline(x=a-b, linestyle='--', color='#C0C0C0')
plt.ylabel('$f(x)$')
plt.xlabel('x')
plt.plot(x,y,color="black",marker=',')

plt.subplot2grid((3,2),(2,0), colspan=1)
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.xlim([0,255])
plt.ylabel('occurence [-]')
plt.xlabel('Pixel value $[-]$')
plt.hist(s_trans.flatten(),256,color='black')

plt.subplot2grid((3,2),(2,1), colspan=1)
plt.imshow(s_trans, cmap=plt.get_cmap('gray'), vmin=0, vmax=255)

plt.gcf().set_size_inches(5, 6)
plt.subplots_adjust(hspace=0.4)
plt.savefig('sigmoid_explained.png',bbox_inches='tight')

