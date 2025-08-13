"""
Examples: Creation of arrays in Python
"""

# Using list as array
arr1 = [1, 2, 3, 4, 5]
print("Array using list:", arr1)

# Using array module
import array
arr2 = array.array('i', [10, 20, 30, 40])
print("Array using array module:", arr2)

# Using numpy array (requires numpy package)
try:
    import numpy as np
    arr3 = np.array([100, 200, 300])
    print("Array using numpy:", arr3)
except ImportError:
    print("Numpy is not installed.")
