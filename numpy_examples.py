"""Examples of using nuumpy arrays."""

import numpy as np

# Create a 1D numpy array
a = np.array([1.5, 2.9, 3, 4, 5], float)
#print(a[:2])

# Create a 2D numpy array
b = np.array([[1, 2, 3], [4, 5, 6], [4, 8, 7]], float)
print(b[1:3, 1:3])

#Other ways to create numpy arrays

# Create a 1D numpy array of zeros
c = np.zeros(5, float)
print(c)

# Create a 2D numpy array of zeros
d = np.zeros((3, 4), float)
print(d)

# Create a 1D numpy array of ones
e = np.ones(5, float)
print(e)