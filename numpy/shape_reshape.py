"""
Numpy shape and reshape functionalities

1. shape.
    shape can be used to obtain the shape of a ndarray as so:
    Usage:
        np1.shape where np1 is the ndarray

2. reshape.
    reshape can be used to reshape ndarray into 2D and 3D arrays and many more dimensions. It can also be used to flatten n-darrays into 1D arrays.
    NOTE: reshape() doesn't change data on the original array
    Usage:
        np1.reshape(dimensions, no of elements)

"""
import numpy as np

list1 = [1,2,3,4,5,6,7,8,9,10,11,12]

# Let's get the shape of this array
np1= np.array(list1)
print(np1.shape)

# Let's reshape this array into a 2D array
np2 = np1.reshape(2, 6)
print(np2)
print(np2.shape)

# Let's reshape it into a 3D array
np3 = np1.reshape(3, 4)
print(np3)
print(np3.shape)

# Let's flatten the np3 array back to a 1D array
np4 = np1.reshape(-1)
print(np4)
print(np4.shape)

# This will originally changes the shape of the original array while reshape() doesn't
np1.shape = (3,4)
print(np1)