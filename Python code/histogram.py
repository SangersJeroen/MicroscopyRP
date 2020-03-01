import numpy as np
import matplotlib.pyplot as plt
import sys as sys

working_file = ''
output_file = ''
xlabel = ''
ylabel = ''
label = ''

def test_arg():
    if type(sys.argv[1]) != type('test'):
        raise AssertionError('File path should be type string')
    elif type(sys.argv[2]) != type('test'):
        raise AssertionError('Output name  should be type string')
    elif type(sys.argv[3]) != type('test'):
        raise AssertionError('X label should be type string')
    elif type(sys.argv[4]) != type('test'):
        raise AssertionError('Y label should be type string')
    else:
        print(sys.argv)
        output_file = sys.argv[2]
        xlabel = sys.argv[3]
        xlabel = sys.argv[4]
        working_file = sys.argv[1]
        label = sys.argv[5]

test_arg()

data = np.loadtxt(working_file)

x = np.linspace(1,len(data)+1,len(data))
y = data[:,0]

plt.plot(x,y, label=label)
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.show()
plt.savefig(output_file)