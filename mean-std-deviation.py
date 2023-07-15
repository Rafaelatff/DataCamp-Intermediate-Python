import numpy as np  # To use array of numbers instead of list
import matplotlib.pyplot as plt # To plot graphics
import random # To generate random numbers
from statistics import mean # To use mean from statistics package
import math # To use log and pi methods.
from scipy.stats import norm # To show gaussian curve # pip3 install scipy   

## Generating and plotting random values with uniform distribution

values = np.random.randint(-10,10,1000) # Lower limit, Upper limit, number of values
print('values is: ' + str(type(values))) # Print the type for 'values' : <class 'numpy.ndarray'>
print(values) # Print the values for 'values' variable

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

# Calculate logarithm for each element in the array
log_R1 = [math.log(x) for x in R1]

plt.subplot(4,2,1) # plt.subplot(nrows, ncols, index)
plt.plot(log_R1) # Prepare the plot to show the randon values
plt.ylabel('Amplitude') 
plt.title('log_R1')

plt.subplot(422) # Also works, even whitout the coma
plt.hist(log_R1, bins=20)
plt.title('Histogram')

log_R1 = np.array(log_R1)
log_R1 = log_R1 * -2 # To multiply, must be np.array instead of list
sqrtM2log_R1 = np.sqrt(log_R1) # Then I do the square root of the value (same as ^1/2)

print('log_R1 * -2 is: ' + str(type(log_R1))) # It returns <numpy.ndarray>
print(log_R1)

plt.subplot(4,2,3) 
plt.plot(sqrtM2log_R1) 
plt.ylabel('Amplitude') 
plt.title('(-2logR1)^1/2') # First part of the equation

plt.subplot(4,2,4) 
plt.hist(sqrtM2log_R1, bins=20)

cos2piR2 = 2 * math.pi * R2
cos2piR2 = np.cos(cos2piR2)

plt.subplot(4,2,5) 
plt.plot(cos2piR2) 
plt.ylabel('Amplitude') 
plt.title('cos2piR2') # Second part of the equation

plt.subplot(4,2,6) 
plt.hist(cos2piR2, bins=20)

X = sqrtM2log_R1 * cos2piR2

plt.subplot(4,2,7) 
plt.plot(X) # Prepare the plot to show the randon values
plt.xlabel('Time domain') 
plt.ylabel('Amplitude') 
plt.title('X')#'Random values, normal distribution')

plt.subplot(4,2,8)
plt.hist(X, bins=20)

print('Mean: ' + str(np.float64(np.mean(X)))) # It returns a <numpy.float64> type, then is converted to string
print('Standard deviation: ' + str(np.float64(np.std(X)))) # Same as before


x = np.linspace(np.mean(X) - 4 * np.std(X), np.mean(X) + 4 * np.std(X), 100)  # Valores de x para a distribuição gaussiana
y = norm.pdf(x, np.mean(X), np.std(X))

plt.subplot(4,2,8)
plt.twinx() # To plot over the histogram, but with different scale for Y
plt.plot(x, y, color='red', linewidth=2)

plt.show()

# X Mean: 0.003880677981061158
# X Standard deviation: 1.017240401517945




