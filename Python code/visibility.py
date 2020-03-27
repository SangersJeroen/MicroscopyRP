import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpb


#mpb.use("pgf")
mpb.rcParams['figure.dpi']=300
mpb.rcParams.update({
    #"pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    #'text.usetex': True,
    #'pgf.rcfonts': False,
})

def visibility(array):
    if array.shape[0] != 5:
        raise AssertionError("Array must have length 5")
    average_low = (array[0]+array[2]+array[4])/3
    #error = np.std(array[0]+array[2]+array[4])
    average_high = (array[1]+array[3])/2
    return (average_high-average_low)/(average_high+average_low)

uI = 0.5

def errorval(array):
    if array.shape[0] != 5:
        raise AssertionError("Array must have length 5")
    average_low = (array[0]+array[2]+array[4])/3
    average_high = (array[1]+array[3])/2
    return np.sqrt(((uI*2*average_low)/(average_high + average_low)**2)**2+((uI*-2*average_high)/(average_high+average_low)**2)**2)



m1g5 = np.array([[0,158,0,165,0],[0,178,0,180,0],[0,186,0,182,0],[1,191,1,194,1],[3,195,5,197,4],[7,196,5,200,6],[9,199,10,193,11],[8,196,6,196,11],[12,191,11,195,17],[17,187,11,189,16],[21,189,28,186,18],[40,189,40,186,41],[56,156,40,160,59],[66,127,54,175,39],[85,131,63,155,41],[68,146,72,106,82],[98,113,73,130,94],[98,113,82,113,98]])
#m1g6 = np.array([[9,199,10,193,11],[40,189,40,186,41],[21,189,28,186,18],[17,187,11,189,16],[12,191,11,195,17],[8,196,6,196,11]])
#m1g7 = np.array([[56,156,40,160,59],[66,127,54,175,39],[85,131,63,155,41],[68,146,72,106,82],[98,113,73,130,94],[98,113,82,113,98]])
m2g5 = np.array([[0,72,0,76,0],[0,69,0,65,0],[0,76,0,60,0],[0,76,0,74,0],[0,74,0,74,0],[0,76,0,75,0],[0,84,0,112,0],[0,116,0,118,0],[0,98,0,111,0],[0,116,0,106,0],[0,104,0,114,0],[1,105,0,108,1],[0,105,0,98,0],[0,101,0,92,0],[0,104,0,101,3],[2,80,5,85,2],[2,71,7,94,6],[5,55,10,71,5]])
#m2g6 = np.array([[0,84,0,112,0],[0,116,0,118,0],[0,98,0,111,0],[0,116,0,106,0],[0,104,0,114,0],[1,105,0,108,1],])
#m2g7 = np.array([[0,105,0,98,0],[0,101,0,92,0],[0,104,0,101,3],[2,80,5,85,2],[2,71,7,94,6],[5,55,10,71,5]])
m3g6 = np.array([[7,81,7,75,6],[14,120,12,128,16],[13,133,17,143,16],[18,145,8,137,11],[15,141,15,130,15],[17,128,17,117,15],[5,87,4,88,5],[6,97,3,89,5],[3,92,7,91,7],[7,89,8,89,8],[8,89,9,89,10],[0,89,10,87,8]])
#m3g7 = np.array([[5,87,4,88,5],[6,97,3,89,5],[3,92,7,91,7],[7,89,8,89,8],[8,89,9,89,10],[0,89,10,87,8]])

spatial_frequencies = np.array([32,35.9,40.3,45.3,50.8,57,64,71.8,80.6,90.5,101,114,128,143,161,181,203,228])

m1_visibilities = np.asarray([])
m1_visibilities_error = np.asarray([])

m2_visibilities = np.asarray([])
m2_visibilities_error = np.asarray([])

m3_visibilities = np.asarray([])
m3_visibilities_error = np.asarray([])

for i in range(len(m1g5)):
    m1_visibilities = np.append(m1_visibilities, visibility(m1g5[i]))
    m1_visibilities_error = np.append(m1_visibilities_error, errorval(m1g5[i]))

    m2_visibilities = np.append(m2_visibilities, visibility(m2g5[i]))
    m2_visibilities_error = np.append(m2_visibilities_error, errorval(m2g5[i]))

for i in range(len(m3g6)):
    m3_visibilities = np.append(m3_visibilities, visibility(m3g6[i]))
    m3_visibilities_error = np.append(m3_visibilities_error, errorval(m3g6[i]))

plt.subplot(311)
plt.errorbar(spatial_frequencies, m1_visibilities, m1_visibilities_error, c='red', marker='.')
plt.xlabel('spatial frequency $[mm^{-1}]$')
plt.ylim(0.0,1.2)
plt.ylabel('Visibility $[-]$')
plt.title("$40x$ magnification")
#plt.show()

plt.subplot(312)
plt.errorbar(spatial_frequencies, m2_visibilities, m2_visibilities_error, c='red', marker='.')
plt.xlabel('spatial frequency $[mm^{-1}]$')
plt.ylim(0.5,1.2)
plt.ylabel('Visibility $[-]$')
plt.title("$100x$ magnification")
#plt.show()

plt.subplot(313)
plt.errorbar(spatial_frequencies[6:35], m3_visibilities, m3_visibilities_error, c='red', marker='.')
plt.xlabel('spatial frequency $[mm^{-1}]$')
plt.ylabel('Visibility $[-]$')
plt.ylim(0.5,1.2)
plt.title("$400x$ magnification")

print(m3_visibilities_error)


plt.subplots_adjust(hspace=0.9)
plt.gcf().set_size_inches(5, 6)
plt.savefig('visibilities.png',bbox_inches='tight')

'''
plt.plot(spatial_frequencies, m1_visibilities, 'r.',label='NA = 1')
plt.plot(spatial_frequencies, m2_visibilities, 'b.',label='NA = 2')
plt.plot(spatial_frequencies[6:35], m3_visibilities, 'g.',label='NA = 3')
plt.xlabel('Numercial frequency $mm^{-1}$')
plt.ylim(0,1.2)
plt.ylabel('Visibility')
plt.title("Visibility 1")
plt.show()
'''