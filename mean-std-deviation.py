import numpy as np  # To use array of numbers instead of list
import matplotlib.pyplot as plt # To plot graphics
import random # To generate random numbers
from statistics import mean # To use mean from statistics package
import math # To use log methods,

## Generating and plotting random values with uniform distribution

values = np.random.randint(-10,10,1000) # Lower limit, Upper limit, number of values
print('values is: ' + str(type(values))) # Print the type for 'values' : <class 'numpy.ndarray'>
print(values) # Print the values for 'values' variable

plt.subplot(2,2,1) # plt.subplot(nrows, ncols, index)
plt.plot(values) # Prepare the plot to show the randon values
plt.xlabel('Time domain') 
plt.ylabel('Amplitude') 
plt.title('Random values, uniform distribution')

plt.subplot(222) # Also works, even whitout the coma
plt.hist(values, bins=20)
plt.title('Histogram')

print('Mean: ' + str(np.float64(np.mean(values)))) # It returns a <numpy.float64> type, then is converted to string
print('Standard deviation: ' + str(np.float64(np.std(values)))) # Same as before

## Generating and plotting random values with normal distribution
# I_could_just = np.random.normal(0, 0.1, 1000)
# But let's follow the Chapter 2, Statistics, Probability and Noise
# from book The Scientist and Engineer's Guide to Digital Signal Processing
# by By Steven W. Smith, Ph.D.


# X = (-2logR1)^1/2 * cos(2piR2)

R1 = [random.random() for _ in range(1000)]
R2 = [random.random() for _ in range(1000)]

print('R1 is: ' + str(type(R1))) # It returns <class 'list'>

R1 = np.array(R1) # Converts <list> into <numpy.ndarray>
R2 = np.array(R2)

print('R1 is: ' + str(type(R1))) # It returns <class 'numpy.ndarray'>

#X = np.array(2 * math.pi() * R2)
#print(type(X))
#X = math.log(R1)

plt.subplot(2,2,3) # 
plt.plot(R1) # Prepare the plot to show the randon values
plt.xlabel('Time domain') 
plt.ylabel('Amplitude') 
plt.title('Random values, normal distribution')

plt.subplot(2,2,4) # Shows plots in 1 = 1 row, 2 = two column, 1 = plot 1
plt.hist(R1, bins=20)
plt.title('Histogram')

plt.show()






