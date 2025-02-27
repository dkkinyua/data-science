"""
Concatenate arrays in Numpy

Question:
You are given two integer arrays of size NXP and MXP ( N&M  are rows, and P is the column). Your task is to concatenate the arrays along axis .

Input Format

The first line contains space separated integers N, M and P.
The next N lines contains the space separated elements of the P columns.
After that, the next M lines contains the space separated elements of the P columns.

Output Format

Print the concatenated array of size X.

Sample Input

4 3 2
1 2
1 2 
1 2
1 2
3 4
3 4
3 4 
Sample Output

[[1 2]
 [1 2]
 [1 2]
 [1 2]
 [3 4]
 [3 4]

"""

import numpy as np

n, m, p = map(int,input().split())

arrA = np.array([input().split() for _ in range(n)],int)
arrB = np.array([input().split() for _ in range(m)],int)
print(np.concatenate((arrA, arrB), axis = 0))
