import numpy as np

# Create a numpy array
np1 = np.array([0,1,2,3,4,5,6,7,8,9])
print(np1)

# Create a numpy array using a range of numbers
np2 = np.arange(10)
print(np2)

# Get the shape of the 2nd numpy array
print(np2.shape)

# Get the 1st item of the 1st nmpy array
print(np1[0])

# Create a step numpy array
np3 = np.arange(0,10, 2)
print(np3)

# Create a numpy array of zeros
np4 = np.zeros(10)
print(np4)

# Create a multidimensional array of zeros
np5 = np.zeros((2, 10))
print(np5)

# Create a multidimesional array of 7s
np6 = np.full((2, 10), 7)
print(np6)

# Convert a Python list to a np array
my_list = [0,1,2,3,4,5,6]
np7 = np.array(my_list)
print(np7)

# Create a np array full of 7, not multidimensional
np8 = np.full(10, 7)
print(np8)