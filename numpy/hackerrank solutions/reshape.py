"""
Shape and Reshape in numpy

Question: 

You are given a space separated list of nine integers. Your task is to convert this list into a 3X3 NumPy array.

Input Format

A single line of input containing  space separated integers.

Output Format

Print the 3X3 NumPy array.

Sample Input

1 2 3 4 5 6 7 8 9
Sample Output

[[1 2 3]
 [4 5 6]
 [7 8 9]]

"""

import numpy as np

def reshape(arr):
    np1 = np.array(arr)
    return np1.reshape(3, 3)

arr1 = [9, 8, 7, 6, 5, 4, 2, 3, 1]
print(reshape(arr1))