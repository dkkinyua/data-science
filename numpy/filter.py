"""
Filtering through arrays using numpy.

"""
import numpy as np

list1 = [0,10,20,30,44,55,66,77,88,99,101]
np1 = np.array(list1)

# Let's filter through this array using boolean list True/False
# Let's initialize an empty list filtered to store these boolean values to represent the filtered values
filtered = []
for i in np1:
    if i % 2 == 0:
        filtered.append(True)
    else:
        filtered.append(False)

print(np1)
print(filtered)

# There's an easy way of doing so. Instead of using a for loop to access these values, we can use the filtered variable and make it equals to the conditional. Both methods yield the same result but this is much more simpler and efficient.

filt = np1 % 2 == 0
print(filt)