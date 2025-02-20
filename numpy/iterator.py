"""
Iterating through numpy ndarrays.

We can use Python for loops to iterate through loops. But it would get crazier to loop through let's say 7D arrays as you need 7 nested for loops which in DSA, isn't good practice too.

Using the np.ndinter() function from numpy, we can loop through various elements of the array.
It's usage is as shown below.

"""
import numpy as np

list1 = [1,2,3,4,5,6,7,8,9,10,11,12]
np1 = np.array(list1)

# To iterate through this array
#for i in np1:
#    print(i)

# Reshape this into a 2D array and iterate through it using for loops
# You need 2 nested for loops to print out all elements of the 2D array
np2 = np1.reshape(2, 6)
for i in np2:
    for j in i:
        print(j)

# Let's iterate through the reshaped 3D array using the np.nditer() function
np3 = np1.reshape(2,3,2)
for i in np.nditer(np3):
    print(i)