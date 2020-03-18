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

img = np.array(Image.open(data).convert('L'))

'''
def average(array):
    data = array.flatten()
    sum_ = 0
    for i in range(0,len(data)):
        if data[i] != 0 and data[i] != 255:
            sum_ += data[i]
    return sum_/len(data)

def stdev(array):
    return np.nanstd(img.flatten())
'''

data_clean = [x if x!=0 and x!=255 else np.nan for x in img.flatten()]

def sigmoid(x):
    return 1/(1+np.exp(-(x-a)/b))*255

a = np.nanmean(data_clean)
b = np.nanstd(data_clean)
print(a,b)

new = sigmoid(img)

#mpb.use("pgf")
mpb.rcParams['figure.dpi']=300
mpb.rcParams.update({
    #"pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    #'text.usetex': True,
    #'pgf.rcfonts': False,
})

plt.hist(img.flatten(),255)
plt.show()
plt.imshow(img, cmap=plt.get_cmap('gray'), vmin=0, vmax=255)
plt.show()
plt.hist(new.flatten(),255)
plt.show()
plt.imshow(new, cmap=plt.get_cmap('gray'), vmin=0, vmax=255)
plt.show()


"""
plt.rcParams['figure.dpi'] = 400
mpb.rcParams.update({
    #"pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    #'text.usetex': True,
    #'pgf.rcfonts': False,
})

plt.subplot(121)
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.xlabel('pixel intensity value [-]')
plt.ylabel('relative occurence [-]')
#plt.hist(img_clean,256,color='black')
plt.plot(np.linspace(0,255,256), y/p,color='black',marker=',')
plt.fill_between(np.linspace(0,255,256),0,y/p,color='black')

plt.subplot(122)
plt.imshow(img, cmap=plt.get_cmap('gray'), vmin=0, vmax=255)
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.gcf().set_size_inches(6, 2)
plt.savefig(inputfile.replace('.bmp','')+'histogram.png',bbox_inches='tight')
"""
