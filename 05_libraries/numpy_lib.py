# NumPy is a Python library.
# NumPy is used for working with arrays.
# NumPy is short for "Numerical Python".
import numpy as np

arr = np.array([2,4,6,8,10])
print(arr)
print(type(arr))

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
print(c[0,2])


# BroadCasting in Numpy 
