import numpy as np
import matplotlib.pyplot as plt
import os
import sys

inputfile = str(sys.argv[1])

path = os.getcwd()
data = np.loadtxt(path+'\\'+inputfile)

plt.rcParams['figure.dpi'] = 200


def find_extremities(threshold):
    searching_for = "high"

    highest_high = 0
    highest_high_loc = 0
    lowest_low = 0
    lowest_low_loc = 0

    highs = np.asarray([])
    highs_loc = np.asarray([])

    lows = np.asarray([])
    lows_loc = np.asarray([])

    current_value = 0


    for i in range(0,len(data)-1):
        #print(searching_for)
        #print(highest_high, lowest_low)
        if searching_for == "high":
            if data[i] >= highest_high:
                highest_high = data[i]
                highest_high_loc = i
            else:
                lowest_low = data[i]
                lowest_low_loc = i
                if data[i] + threshold < highest_high:
                    highs = np.append(highs, highest_high)
                    highs_loc = np.append(highs_loc, highest_high_loc+1)
                    searching_for = 'low'
        if searching_for == 'low':
            if data[i] <= lowest_low:
                lowest_low = data[i]
                lowest_low_loc = i
            else:
                highest_high = data[i]
                highest_high_loc = i
                if data[i] - threshold > lowest_low:
                    lows = np.append(lows, lowest_low)
                    lows_loc = np.append(lows_loc, lowest_low_loc+1)
                    searching_for = 'high'

    return highs_loc, highs, lows_loc, lows

x = np.linspace(1,len(data)+1,len(data))
highs_loc, highs, lows_loc, lows = find_extremities(10)


plt.plot(x,data)
plt.plot(lows_loc,lows, 'ro')
plt.plot(highs_loc, highs, 'go')
plt.grid()
plt.show()

