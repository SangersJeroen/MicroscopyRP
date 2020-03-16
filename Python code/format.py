import numpy as np
import matplotlib.pyplot as plt
import os
import sys

inputfile = sys.argv[1]

path = os.getcwd()
data = np.loadtxt(path+inputfile)
