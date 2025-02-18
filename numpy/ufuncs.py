"""
This file contains the ufuncs that are used in numpy. Ufuncs are functions that operate on ndarrays in an element-by-element fashion, supporting array broadcasting, type casting, and several other standard features. That is, a ufunc is a “vectorized” wrapper for a function that takes a fixed number of scalar inputs and produces a fixed number of scalar outputs.

Learn more at https://numpy.org

In this file, we will use classes and functions to create ufuncs that will be used in numpy arrays, you can add a custom array and mess around with the functions to see how they work. Happy hacking!

"""
import numpy as np

class UniversalFunctions:
    def __init__(self, arr):
        self.arr = arr

    def add(self):
        np_arr = np.array(self.arr)
        return np.add(np_arr, 2)
    
    def subtract(self):
        np_arr = np.array(self.arr)
        return np.subtract(np_arr, 2)
    
    def multiply(self):
        np_arr = np.array(self.arr)
        return np.multiply(np_arr, 2)
    
    def divide(self):
        np_arr = np.array(self.arr)
        return np.divide(np_arr, 2)
    
    def square_root(self):
        np_arr = np.array(self.arr)
        return np.sqrt(np_arr)
    
    def square(self):
        np_arr = np.array(self.arr)
        return np.square(np_arr)
    

list1 = [0,1,2,3,4,5,6,7,8,9]
uf = UniversalFunctions(list1)
print(list1)
print(uf.multiply())
    


    
