# Slicing through numpy arrays. We'll use Python slicing methods
import numpy as np

list1 = [1,2,3,4,5,6,7,8,9]

np1 = np.array(list1)
print(np1[:5])
print(np1[2:])
print(np1[::2])
print(np1[-3:-1])
print(np1[1:5:2])

# Slicing through a 2D array
# When creating a 2D array, the first array is the 0th index while the 2nd array is the 1st index
# So to access, let's say 10 in the 2nd array, we'll take np2[1, 4] as np2[index of array, position of search item]
np2 = np.array([[0,1,2,3,4,5], [6,7,8,9,10,11]])
print(np2[1, 2:4])

print(np2[0:1, 1:4]) # This only prints the slice result of the 2nd and 5th items of the 1st array
print(np2[0:2, 1:4]) # This prints the slice result of the 2nd and 5th item of both arrays