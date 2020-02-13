# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'

#%% [markdown]

# # SciPy Family
#
# Python-based ecosystem [scipy.org](https://scipy.org)  
# 
# ![SciPy Family screenshot](SciPy_org.jpg)  
# * SciPy Library - Fundamental library for scientific computing
# * NumPy - Numeric Python: Base N-dimensional array package
# * Pandas - Data structures (Dataframes) & analysis
# * Mathplotlib - Comprehensive 2D Plotting
# * Sympy - Symbolic mathematics
# * IPython - Enhanced Interactive Console
#
# The datatypes (dtype attribute) supported by Numpy is many:  
# [Numpy basic data types](https://docs.scipy.org/doc/numpy/user/basics.types.html) 

#%%
# might need to install numpy from the terminal
# !pip install numpy
# !pip3 install numpy
# sudo pip install numpy
# sudo pip3 install numpy
# sudo -H pip3 install numpy
# conda install numpy

#%%
import numpy as np 
# or from numpy import *  
# import matplotlib.pyplot as plt
# import pandas as pd  

#%%
#
# Review lists
list0 = [9,8,7]
list0b = [6,5,4]
#
# What are the lengths of list0 and list0b?
#3
# What do you get with list01 + list0b?
list0 + list0b ##adding lists appends them!
# 


#%%
# explore data structures with list of list, how many dimensions? 
list1 = [ [11,12,13,14], [21,22,23,24], [31,32,33,34]] 
list1b = [ [41,42,43,44,45], [51,52,53,54,55], [61,62,63,64,65], [71,72,73,74,75]] 
#
len(list1)
# Again, what is list1 + list1b?
len(list1 + list1b) #appends and the length is 7, the total of items in the list
#
#%%
# Question: How do you describe (in english) these two lists? What are the "shapes" of the objects?
"They are lists of lists, nothing more!"
#
# Question: how do you get the element '32' in list1?
#
list1[2][1]

# 
# Question: how do you get the row of [31,32,33,34] in list1?
# 
list1[2]

# 
# Question: How to you get the column of 12, 22, 32 ???
# 
[ row[1] for row in list1 ]

#%%
[ row[1] for row in list1 ]

#%%
# OR Loop it
v3 = []
for row in list1: 
  v3.append(row[2])
print(v3)

#%%
list2 = [ [11,12,13], [21,22,23], [31,32,33], [41,42,43] ] # two dimensional list (2-D array)  # (4,3)
# list2b = [ [51,52,53], [61,62,63], [71,72,73], [81,82,83]] 


# How do you access the different parts of these two lists?

#%%
# How do you create a higher-dimensional list (say 2x3x4)?

list3D = [ [ [ 111,112,113,114],[121,122,123,124],[131,132,133,134]],
           [ [ 211,212,213,214],[221,222,223,224],[231,232,233,234]]]

# 

#%%
list4 = [ 5, 'a', 2, 3.5, True ]
list5 = [ 5, [1,4], 3, 1 ]

#%%
# Now try numpy
nparray1 = np.array(list1)
print("nparray1 = \n", nparray1)
print("type(nparray1) =", type(nparray1))
print("nparray1.dtype =", nparray1.dtype)  # int64
print("nparray1.shape =", nparray1.shape)
print("nparray1.strides =", nparray1.strides)  # each value is int64, hence 8-byte of memory, with four columns, it takes 8x4 = 32 bytes to the next row, same position. Strides = (32,8) to the next row and next column


#%%
# if we redo 
nparray1 = np.array(list1, dtype= np.int32)
print("nparray1 = \n", nparray1)
print("type(nparray1) =", type(nparray1))
print("nparray1.dtype =", nparray1.dtype)  # int32
print("nparray1.shape =", nparray1.shape)
print("nparray1.strides =", nparray1.strides)  # now each value is int32, 4-byte, with four columns, it takes 4x4 = 16 bytes to next row. 


#%%
# Try others
nparray2 = np.array(list2)
print("nparray2 = \n", nparray2)
print("type(nparray2) =", type(nparray2))
print("nparray2.dtype =", nparray2.dtype)  # int64
print("nparray2.shape =", nparray2.shape)

#%%
import sys
try:
  nparray12 = nparray1+nparray2
except ValueError as err :  # except (RuntimeError, TypeError, NameError):
  print("Value Error: {0}".format(err), " Try transpose...")
  nparray12 = nparray1+nparray2.T
except ValueError as err :  # except (RuntimeError, TypeError, NameError):
  print("Transpose has Value Error as well: {0}".format(err))
except:
  print("unexpected error:", sys.exc_info()[0])


#%%
# list4 = [ 5, 'a', 2, 3.5, True ]
nparray4 = np.array(list4)
print("nparray4 = \n", nparray4)
print("type(nparray4) =", type(nparray4))
print("nparray4.dtype =", nparray4.dtype)  
print("nparray4.shape =", nparray4.shape)

#%%
# list5 = [ 5, [1,4], 3, 1 ]
nparray5 = np.array(list5)
print("nparray5 = \n", nparray5)
print("type(nparray5) =", type(nparray5))
print("nparray5.dtype =", nparray5.dtype)  
print("nparray5.shape =", nparray5.shape)


#%%
# If they are 2D-arrays, and have compatible dimensions, you can multiply them as matrices
tprod12 = np.dot(nparray1,nparray2)
print("tprod12.shape =", tprod12.shape)
mprod21 = np.dot(nparray2,nparray1)
print("mprod21.shape =", mprod21.shape)


#%%
# Also try the 3d-array that we constructed...
# In physics, those are called tensors. 
nparray3D = np.array(list3D)
print("nparray3D = \n", nparray3D)
print("type(nparray3D) =", type(nparray3D))
print("nparray3D.dtype =", nparray3D.dtype)  
print("nparray3D.shape =", nparray3D.shape)

#%%
# If they are 2D-arrays, and have compatible dimensions, you can multiply them as matrices
tprod32 = np.dot(nparray3D,nparray2)
print("tprod32.shape =", tprod32.shape)


#%% [markdown]
# speed and ease of use is the strength of numpy array, compared to python lists. 
# The entire array must be of a single type, however.
# If we try to time or clock the code execution times, you will find similar functions 
# is much faster than looping thru a python list.
# This is mainly because NumPy is written in C, and optimized these specialized 
# operations in a well-designed library.

#%%
# filtering and indexing
print(nparray1[0:2,:2])  ##Just like r, (row, column)
print(nparray1[:,-1:]) ##Last column from the end

# Let us do something simpler.
# Obtain the third column of nparray1
print(nparray1)
v3 = nparray1[:,2]
print(v3) # it is a column vector, or array one by three (3,1)
print(v3.shape) # it is a column vector, or array one by three (3,1)

# Much easier than dealing with lists on the coding side of things. Speed is also maximized.

#%%
# BROADCASTING 
# 
# Let's practice slicing numpy arrays and using NumPy's broadcasting concept. 
# Remember, broadcasting refers to a numpy array's ability to VECTORIZE operations, 
# so they are performed on all elements of an object at once.
# If you need to perform some simple operations on all array elements, 
#
nparray1squared = nparray1 ** 2  #Each element will be squared, broadcasting procedure
print(nparray1squared)
nparray1mod7 = nparray1 % 7 # remainder from dividing by 7
print(nparray1mod7)
nparray1b = np.array(list1b)
nparray1bovera = nparray1b / nparray1
print(nparray1bovera) #it works, just don't have he dimensions

# Try some other operations, see if they work.

# Next try to do the above with loops or comprehensions? 

#%%
# boolean indexing 
print(nparray1)
npbool1greater = nparray1 > 21  #Now each value is broadcasted, True or False
print(npbool1greater)
print(nparray1[npbool1greater]) #these are all the true ones
print(nparray1[npbool1greater].shape) #how many true ones? 7 (7,)
npbool1mod = nparray1 %2 ==1 #odd numbers
print(npbool1mod)
print(nparray1[npbool1mod])
print(nparray1[npbool1mod].shape)

# Again, try to do these with loops or comprehensions? 


#%%



