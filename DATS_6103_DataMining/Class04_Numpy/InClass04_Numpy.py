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
# pip install numpy
# pip3 install numpy
# sudo pip install numpy
# sudo pip3 install numpy
# sudo -H pip3 install numpy
import numpy as np  
# or from numpy import *  
# import matplotlib.pyplot as plt
# import pandas as pd  

#%%
# explore data structures with list of list, how many dimensions? 
list1 = [ [11,12,13,14], [21,22,23,24], [31,32,33,34]] 
list1b = [ [41,42,43,44], [51,52,53,54], [61,62,63,64]] 
list2 = [ [11,12,13], [21,22,23], [31,32,33], [41,42,43] ]

# How do you describe (in english) these two lists? What are the "shapes" of the objects?

# How do you access the different parts of these two lists (say using indexes)?

# How do you create a higher-dimensional list (say 2x3x4)?


#%%
list3 = [ 5, 'a', 2, 3.5, True ]
list4 = [ 5, [1,4], 3, 1 ]

#%%
# Now try numpy
narray1 = np.array(list1)
print(narray1)
print(type(narray1))
print(narray1.dtype)
print(narray1.shape)
print(narray1.data)

#%%
# Try others
narray2 = np.array(list2)
print(narray2)
print(narray2.shape)
print(narray2.dtype)

narray3 = np.array(list3)
print(narray3)
print(narray3.shape)
print(narray3.dtype)

narray4 = np.array(list4)
print(narray4)
print(narray3.shape)
print(narray4.dtype)

#%%
# If they are 2D-arrays, and have compatible dimensions, you can multiply them as matrices
mprod12 = np.dot(narray1,narray2)
print(mprod12.shape)
mprod21 = np.dot(narray2,narray1)
print(mprod21.shape)


#%%
# Also try the 3d-array that we constructed...
# In physics, those are called tensors. 

#%% [markdown]
# speed and ease of use is the strength of numpy array, compared to python lists. 
# The entire array must be of a single type, however.
# If we try to time or clock the code execution times, you will find similar functions 
# is much faster than looping thru a python list.

#%%
# filtering and indexing
print(narray1[0:2,:2])
print(narray1[:,-1:])

# Let us do something simpler.
# Obtain the third column of narray1
print(narray1)
v3 = narray1[:,2]
print(v3) # it is a column vector, or array one by three (3,1)
print(v3.shape) # it is a column vector, or array one by three (3,1)

# NOW, write your own code to get the 3 by 1 column vector from the python list list1
# first, using for loop
v3 = []
for row in list1:
  v3.append(row[2])
print(v3)
# next, try using list comprehension
v3list = [ row[2] for row in list1 ]
print(v3)

#%%
# broadcasting
# Let's practice slicing numpy arrays and using NumPy's broadcasting concept. 
# Remember, broadcasting refers to a numpy array's ability to vectorize operations, 
# so they are performed on all elements of an object at once.
# If you need to perform some simple operations on all array elements, 
narray1squared = narray1 ** 2
print(narray1squared)
narray1mod7 = narray1 % 7 # remainder from dividing by 7
print(narray1mod7)
narray1b = np.array(list1b)
narray1bovera = narray1b / narray1
print(narray1bovera)

# Try some other operations, see if they work.

# Next try to do the above with loops or comprehensions? 

#%%
# boolean indexing 
print(narray1)
nbool1greater = narray1 > 21
print(nbool1greater)
print(narray1[nbool1greater])
print(narray1[nbool1greater].shape)
nbool1mod = narray1 %2 ==1
print(nbool1mod)
print(narray1[nbool1mod])
print(narray1[nbool1mod].shape)

# Again, try to do these with loops or comprehensions? 


#%%



