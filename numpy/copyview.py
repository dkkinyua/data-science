# Numpy copy and view

"""
A copy array is a copy of the original array but it is not connected to the original/parent array in any way or form.
A view array is a reflection of the original array and is connected to the original/parent array. Think of it as a mirror!

"""

import numpy as np

list1 = [0,1,2,3,4,5,6,7,8,9]
np1 = np.array(list1)

"""

# The view array
np2 = np1.view()

print(f'Original array: {np1}')
print(f'View array: {np2}')

# Let's change an element in the original array and see what happens
np1[0] = 20

print(f'Changed array: {np1}')
print(f'View array: {np2}')

"""

# The copy array
np2 = np1.copy()

print(f"Original/Parent array: {np1}")
print(f"Copy array: {np2}")

np1[0] = 20

print(f"Original/Parent array: {np1}")
print(f"Copy array: {np2}")
