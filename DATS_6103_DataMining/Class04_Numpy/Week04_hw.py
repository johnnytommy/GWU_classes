# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'
#%%
import math

#%%
# Example on recursive again, simplified, only one argument needed
def triangleSum(n):
  """
  Finding the sum of 1+2+...+n
  :param n: the last interger to be added
  :return: the sum
  """
  n = math.floor(n)
  return n+triangleSum(n-1) if n>1 else n
  # instead of the above one-liner, you can write it out as the three lines below
  # if n > 1 :
  #   return n+triangleSum(n-1)
  # return n # execute when n <= 1, this will allow n to be non-integer if choose so

# test
print(triangleSum(4))
print(triangleSum(6))

#%% 
# ######  QUESTION 1   QUESTION 1   QUESTION 1   ##########
# Write a recursive function that calculates the Fibonancci sequence.
# The recusive relation is F(n) = F(n-1) + F(n-2), 
# and the typically choice of seed values are F(0) = 0, F(1) = 1. 
# From there, we can build F(2) and onwards to be 
# F(2)=1, F(3)=2, F(4)=3, F(5)=5, F(6)=8, F(7)=13, ...
# Let's set it up from here:

def fib(n):
  """
  Finding the Fibonacci sequence with seeds of 0 and 1
  The sequence is 0,1,1,2,3,5,8,13,..., where 
  the recursive relation is F(n) = F(n-1) + F(n-2)
  :param n: the index, starting from 0
  :return: the sequence
  """
  n = math.floor(n)
  if n > 1 :
    return pass # replace pass with neccessary codes
  elif n==1 :
    return pass # replace pass with neccessary codes
  else :
    return pass # replace pass with neccessary codes

# test
fib(6)
fib(7)

#%% 
# Suppose we have a "deep-list", which is a potentially a list of list of list of...
thelist = [ 0, [10,11], [20, [[2100,2101],211]], 3] # four-level deep
# Write a recursive function to perform, and return a deep-copy of thelist

def deeplistcopy(lll):
  """
  Deep copy for list of list of list...
  :param lll: list of list of list...
  :return: a deep copy of the list
  """
  if type(lll) != list : # if the argument we need to copy is just a primitive value, then just duplicate it. This is not shallow.
    return lll
  else : # now lll is a list, need to first create an empty list, and loop thru this list, then append each value to this empty list
    result = []
    for lo in lll: # lo stands for list-object. Assuming the elements in the list lll might actually be a list itself
      result.append(deeplistcopy(lo)) # whether lo is a list or not, we *trust* that the deeplistcopy() function can handle it (recursively). We just need to append the result to the end.
    return result # after the loop ends, we just need to return the copied list to the right place.

# ######  QUESTION 2   QUESTION 2   QUESTION 2   ##########
# write some codes to test the function
# (a) print out thelist first 
# (b) using the deeplistcopy function, make a copy of thelist, and save it as copylist
# (c) print out copylist. Should be the same as thelist. Hopefully, it's a deep copy
# (d) change the element for copylist[2][1][0][1] from 2101 to 'changed' (a string)
# (e) print out thelist and copylist again. Are they still the same? Deep copy or shallow copy?
# #



#%%
# Review
# list comprehension examples
alist = [ 1,4,0,2,3 ]
listComp = [ 2*n+1 for n in alist ]
print(listComp)
# result: [3, 9, 1, 5, 7]

# Conditionals in list comprehensions
grades = ['A','C+','B-','A-']
# gradeValues = []
# for val in grades:
#   if val=='A' : gradeValues.append(4)
#   elif val=='A-' : gradeValues.append(3.7)
#   elif val=='B+' : gradeValues.append(3.3)
#   elif val=='B' : gradeValues.append(3)
#   elif val=='B-' : gradeValues.append(2.7)
#   elif val=='C+' : gradeValues.append(2.3)
#   elif val=='C' : gradeValues.append(2)
#   elif val=='C-' : gradeValues.append(1.7)
#   elif val=='D' : gradeValues.append(1)
#   else : gradeValues.append(0)
# print(gradeValues)

# or 
gradeValues = [ 4 if v=='A' else 3.7 if v=='A-' else 3.3 if v=='B+' else 3 if v=='B' else 2.7 if v=='B-' else 2.3 if v=='C+' else 2 if v=='C' else 1.7 if v=='C-' else 1 if v=='D' else 0 for v in grades ]
print(gradeValues)
# result: [4, 2.3, 2.7, 3.7]

#%%
# ######  QUESTION 3   QUESTION 3   QUESTION 3   ##########
# Using list comprehension, write a line of code to produce the [1, 10, 100, ...]
# Imagine we need to make a log plot, so the values on the 
# y-axis should be 1, 10, 100, 1000, instead of 0, 1, 2, 3, 

# thelistcomp = [ ?use range(10) as the iterable? ] 

# test
print(thelistcomp)



#%%
# ######  QUESTION 4   QUESTION 4   QUESTION 4   ##########
# Create two numpy arrays, one with dimension 5x3, the other 3x5 
# Follow the way we had in class, using intergers consistent with the standard
# matrix indexing convention, to have 11, 12, 13, etc as the first row etc
# 



#%%
# ######  QUESTION 5   QUESTION 5   QUESTION 5   ##########
# Confirm the shapes of the two numpy array are indeed 5x3 and 3x5 
# What are the datatype for these numpy arrays?


#%%
# ######  QUESTION 6   QUESTION 6   QUESTION 6   ##########
# Use filtering, create an array of size 3x2 with the middle three rows, and the last two columns



#%%
# ######  QUESTION 7   QUESTION 7   QUESTION 7   ##########
# Use the 5x3 (say narray1) and the Transpose of the 3x5 array (say narray2t). (Look up Transpose if needed)
# Obtain the boolean indexing array on the condition that 
# the element in narray1 is greater than the element in narray2t
# print out the resulting boolean index array



#%%
# ######  QUESTION 8   QUESTION 8   QUESTION 8   ##########
# Use the boolean array in Question 7 to select those elements in narray1 (the 5x3 array) 
# print the resulting array



