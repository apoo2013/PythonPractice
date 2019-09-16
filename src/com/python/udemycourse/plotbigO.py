from math import log
import numpy as numpy
import matplotlib.pyplot as pyplot
%matplotlib inline
pyplot.style.use('bmh')

n = np.linespace(1, 10, 1000)
labels = ['Constant','Logarithmic','Linear','Log Linear','Quadratic','Cubic','Exponential']
big_o = [np.ones(n.shape), np.log(n),n,n*np.log(n),n**2,n**3,2**n]

pyplot.figure(figsize = (12,10))
pyplot.ylim(0, 50)

for i in range(len(big_o)):
	pyplot.plot(n, big_o[i], labels[i])

pyplot.legend(loc = 0)
pyplot.ylabel('Relative Runtime')
pyplot.xlabel('n')