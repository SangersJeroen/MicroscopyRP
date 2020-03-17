import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def sigmoid(x):
    return 1/(1+np.exp(-(x-a)/b))*255

mu, sigma = 128, 10

s = np.random.normal(mu, sigma, 1000000)
x = np.linspace(0,255,256)

a = np.average(s)
b = np.std(s)

y = sigmoid(x)

s_trans = sigmoid(s)


plt.subplot(311)
plt.xlim([0,255])
plt.hist(s,256,color='black')

plt.subplot(312)
plt.xlim([0,255])
plt.plot(x,y,color="black",marker=',')

plt.subplot(313)
plt.xlim([0,255])
plt.hist(s_trans,256,color='black')

plt.show()

