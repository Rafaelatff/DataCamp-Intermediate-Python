import numpy as np  # To use array of numbers instead of list
import matplotlib.pyplot as plt # To plot graphics
import random # To generate random numbers
from statistics import mean # To use mean from statistics package


values = np.random.randint(-10,10,1000) # Lower limit, Upper limit, number of values
print(type(values)) # Print the type for 'values' : <class 'numpy.ndarray'>
print(values) # Print the values for 'values' variable

plt.plot(values) # Prepare the plot to show the randon values
plt.show() # Show the randon values

print('Mean: ' + str(np.float64(np.mean(values)))) # It returns a <numpy.float64> type, then is converted to string
print('Standard deviation: ' + str(np.float64(np.std(values)))) # Same as before

# Média np.mean(np_array_name[:,0]).
# Standard deviation np.std(np_array_name[:,0]).
