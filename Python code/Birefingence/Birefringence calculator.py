# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 16:56:37 2020

@author: vanlo
"""
import pprint
import numpy as np
import matplotlib.pyplot as plt
from scipy.odr import ODR, Model, Data, RealData
plt.clf()

def func(x,b):
    return b*x


    # Focal location for to the bottom and 1st layer, 2nd layer and 3rd layer to bottom
f_0_a = np.array([14.9, 14.2, 14.5, 15.9])*1e-6
f_2_a = np.array([25, 25.1, 25.2, 25])*1e-6

f_2_b = np.array([22, 23.1, 23.4, 24.1, 26])*1e-6
f_3_b = np.array([23.5, 24.1, 25, 26.2, 27.9])*1e-6
f_5_b = np.array([33.3, 34.8, 37.2, 36.5, 33.9])*1e-6

f_4_c = np.array([69.9,70.9,70.3,70.2,70.9])*1e-6
f_3_c = np.array([65, 65.1,65.1,65.2,65.6])*1e-6

f_1_d = np.array([59.7,60.1,61.1,60.8, 60.2])*1e-6
f_2_d = np.array([63.6,64.5,64.8,64.2,64.6])*1e-6


    # Thickness of each serepate layer
d_0_2 = f_2_a - f_0_a
d_1_2 = f_2_d - f_1_d
d_2_3 = f_3_b - f_2_b
d_3_4 = f_4_c - f_3_c
d_3_5 = f_5_b - f_3_b

    
    # Cumulative thickness of the layers, so total thickness
D_1 = np.average(d_0_2)-np.average(d_1_2)
D_2 = np.average(d_0_2)
D_3 = np.average(d_0_2) + np.average(d_2_3)
D_4 = np.average(d_0_2) + np.average(d_2_3) + np.average(d_3_4)
D_4_b = np.average(d_0_2) + np.average(d_2_3) - np.average(d_3_4)
D_5 = np.average(d_0_2) + np.average(d_2_3) + np.average(d_3_5)

D = np.array([D_1, D_2, D_3, D_5])
D_2 = np.array([D_1, D_2, D_3, D_4_b, D_5])
print(D)

print(D_4)
    # The path difference for the colours in order from thin to thicker layer
delay_1 = np.array([270, 510, 600, 1210])*1e-9
delay_2 = np.array([270, 960, 1150, 640, 1700])*1e-9

    # Caculate the birefringence with average
#bf_1 = delay_1/D
#
#
#bf_1_avg = np.average(bf_1)


    # Error calculations
    
u_f = 2e-6
u_delay = np.array([20, 10, 10, 20])*1e-9

u_d = np.sqrt(2*(u_f**2))
u_d_0_2_avg = 1/len(f_0_a) * np.sqrt(len(f_0_a)* u_d**2)
u_d_1_2_avg = 1/len(f_1_d) * np.sqrt(len(f_1_d)* u_d**2)
u_d_2_3_avg = 1/len(f_2_b) * np.sqrt(len(f_2_b)* u_d**2)
u_d_3_5_avg = 1/len(f_3_b) * np.sqrt(len(f_3_b)* u_d**2)
u_d_3_4_avg = 1/len(f_3_c) * np.sqrt(len(f_3_c)* u_d**2)

u_D_1 = np.sqrt(u_d_0_2_avg**2 + u_d_1_2_avg**2)
u_D_2 = u_d_0_2_avg
u_D_3 = np.sqrt(u_d_0_2_avg**2 + u_d_2_3_avg**2)
u_D_4 = np.sqrt(u_d_0_2_avg**2 + u_d_2_3_avg**2 + u_d_3_4_avg**2)
u_D_5 = np.sqrt(u_d_0_2_avg**2 + u_d_2_3_avg**2 + u_d_3_5_avg**2)
u_D = np.array([u_D_1, u_D_2, u_D_3, u_D_5])


    # Best fit of birefringe
linear = Model(func)
data_1 = Data(D, delay_1, wd=1./u_D, we=1./u_delay)
linear = Model(func)
data_2 = Data(D_2, delay_2, wd=1./u_D, we=1./u_delay)


odr_1 = ODR(data_1, linear, beta0=[0])
odr_2 = ODR(data_2, linear, beta0=[0])

out_1 = odr_1.run()
out_2 = odr_2.run()

out_1.pprint()


    # Plot the lot
x = np.linspace(0,2.5e-5,200)
y_1 = func(x, out_1.beta)
y_2 = func(x, out_2.beta)

    # Best fits
plt.plot(x,y_1, label="Birefringe 1")
#plt.plot(x,y_2, label="Birefringe 2")


    # Data
plt.errorbar(D, delay_1, xerr=u_D, yerr=u_delay, mec='k', linestyle='none',elinewidth=1,capsize=2)
plt.errorbar(D_4, (1190e-9), xerr=u_D_4, yerr=(20e-9), mec='k', linestyle='none',elinewidth=1,capsize=2, marker='x')
plt.ylabel('$\Delta l_{path} \; (m)$')
plt.xlabel('$D \; (m)$')
plt.ticklabel_format(style='sci', axis='x',scilimits=(1,4))
plt.ticklabel_format(style='sci', axis='y',scilimits=(1,4))
plt.savefig('C:/Users/vanlo/Documents/GitHub/MicroscopyRP_Git/verslag/afbeeldingen/bf_plot.png')
plt.show()

print(''' Birefringence 1 = %.3e +- %.3e'''
      %(out_1.beta, out_1.sd_beta))


