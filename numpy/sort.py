"""
Sorting through arrays using numpy

We use the np.sort(arr) method to sort through array and arrange them from smallest to largest, or in alphabetical order where arr is the array to be sorted.

"""
import numpy as np

list1 = [3,5,7,9,1,0,23,8,4,11]
np1 = np.array(list1)
print(np1)
print(np.sort(np1))

# Let's sort the following array alphabetically
list2 = ["John", "Dylan", "Aaron", "Christian", "Tracey", "William"]
np2 = np.array(list2)
print(np2)
print(np.sort(np2))

# Let's sort through booleans
list3 = [True, False, False, False, True, True, False]
np3 = np.array(list3)
print(np3)
print(np.sort(np3))

# Let's reshape np1 into a 2D array and sort through it
np4 = np1.reshape(2, 5)
print(np4)
print(np.sort(np4))



