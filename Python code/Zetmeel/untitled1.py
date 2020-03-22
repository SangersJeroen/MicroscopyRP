# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 11:38:33 2020

@author: vanlo
"""

import numpy as np
import matplotlib.pyplot as plt
import os


plt.clf()

l_pixel = 1.60045e-07
u_l_pixel = 5.12287e-10


n_a = np.array([84,83,85,72,97,58,70,105,92,84,115,146,119,76,112,127,99,84,135,80,86,112,105,74,117,90,100,117,100,99])
n_b = np.array([76,75,77,67,94,58,66,95,90,82,115,128,110,75,108,125,90,81,123,78,84,106,103,72,116,83,91,104,97,92])
a = l_pixel*n_a
b = l_pixel*n_b
u_n_a = 2
u_a = np.sqrt((u_n_a*l_pixel)**2 + (u_l_pixel*n_a)**2)
A = 1/4*np.pi*n_a*n_b*l_pixel**2
u_A = 1/4 *np.pi*np.sqrt((u_n_a*n_a*l_pixel**2)**2 + (u_n_a*n_b*l_pixel**2)**2 + (2*u_l_pixel*n_a*n_b*l_pixel)**2)

table = np.transpose([np.arange(1,31),n_a,n_b,A,u_A])

print(table)
np.savetxt('tabel_zetmeel.csv', table)

histogram = plt.hist(A, bins=16, ec='black')
plt.xlabel('$ A \; (m^2)$')
plt.ylabel('Frequency')
plt.ticklabel_format(style='sci', axis='x',scilimits=(1,4))
plt.savefig('C:/Users/vanlo/Documents/GitHub/MicroscopyRP_Git/verslag/afbeeldingen/histogram_zetmeel.png')
plt.show()