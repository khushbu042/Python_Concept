# Python’s memory allocation and deallocation method is automatic. The user does not have to 
# preallocate or deallocate memory similar to using dynamic memory allocation in languages such as
#  C or C++. 
# Python uses two strategies for memory allocation: 
# Reference counting
# Garbage collection


# Create an object
x = [1, 2, 3]
# Increment reference count
y = x
# Decrement reference count
y = None

# Example 2: Reference Counting with Cyclic Reference
# Create two objects that refer to each other
x = [1, 2, 3]
y = [4, 5, 6]
x.append(y)
y.append(x)

# Example 3: Using the sys.getrefcount() function
import sys
# Create an object
x = [1, 2, 3]
# Get reference count
ref_count = sys.getrefcount(x)
print("Reference count of x:", ref_count)


# Automatic Garbage Collection of Cycles




# loading gc
import gc
 
# get the current collection 
# thresholds as a tuple
print("Garbage collection thresholds:",
                    gc.get_threshold())