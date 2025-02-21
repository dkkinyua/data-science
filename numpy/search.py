"""
Searching through arrays in numpy using the np.where(conditional) function where conditional is the conditional we'd use to search for this item.
this returns a tuple of the positions of the found items in the array and their data type, int str whatever as so:
(array[0,3], dtype=int64)

"""
import numpy as np

list1 = [0,1,2,3,4,5,6,7,8,9,10,7,8]
np1 = np.array(list1)

# Let's look for positions where 7 is in the array
x = np.where(np1 == 7)
print(np1)
print(x)
print(np1[x[0]]) # this gets the values of the positions of the search items in the tuple as the array of positions is the 0th index in the tuple

# Let's get all the even numbers in the array
y = np.where(np1 % 2 == 0)
print(y[0])
print(np1[y[0]])

# Let's get all the odd numbers in the array
z = np.where(np1 % 2 != 0)
print(z[0])
print(np1[z[0]])

