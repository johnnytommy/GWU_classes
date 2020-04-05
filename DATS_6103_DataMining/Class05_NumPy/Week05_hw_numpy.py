# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'

#%% [markdown]
#
# # Week05 HW
# ## By: Johnny Thomas
# ### Date: 2/23/2020
#


#%% 
# Suppose we have a "deep-list", which is a potentially a list of list of list of...
thelist = [ 0, [10,11], [20, [[2100,2101],211]], 3] # four-level deep
# We will try to write a recursive function to perform, and return a deep-copy of thelist

#%%
# ######  QUESTION 1      QUESTION 1      QUESTION 1   ##########
# But first, repeat what we did in class (if you had been taking notes...)
# Run some codes to show that a regular simple copying is only a shallow copy
thecopy = thelist
# example: thecopy[0] = ... etc
#
thecopy[3] = 69
print(thelist[3]) 
#unsure if this is what you were looking for but here's me at my shallowest
#
# ######  END of QUESTION 1    ###   END of QUESTION 1   ##########


#%% 
# Next, let us try to use the copy function of the list object 
thelist = [ 0, [10,11], [20, [[2100,2101],211]], 3] # four-level deep
thecopy2 = thelist.copy()
# Notice that dictionary also has a similar copy function. But tuples, 
# being immutable, do not have, and do not need a copy function.
# ctuple = atuple    this will all point to the sample tuple object 
# memory location which is immutable.
#
# ######  QUESTION 2      QUESTION 2      QUESTION 2   ##########
# Run some codes to show that a this copy method is not a completely shallow copy
# Include some examples which show it is indepent of thelist
# and also some examples which show it is still tied to thelist
#
thecopy2[0] = "We're no strangers to love"
print(thecopy2[0])
print(thelist[0]) #So they are different. But what if I change thelist?

thecopy2[1][0] = "You know the rules, and so do I"
print(thelist)
print(thecopy2) #and thus they are still linked at the secod level
#
# ######  END of QUESTION 2    ###   END of QUESTION 2   ##########


#%% 
# Next, let us try to use another method to copy 
thelist = [ 0, [10,11], [20, [[2100,2101],211]], 3] # four-level deep
thecopy3 = list(thelist) 
#
# ######  QUESTION 3      QUESTION 3      QUESTION 3   ##########
# Run some codes to find out if this is shallow or deep. 
# If it is deep, how deep?
#
thelist[2][1] = "A full commitment's what I'm thinking of"
print(thelist)
print(thecopy3) #the same!
#This is shallow, just like my ex girlfriend.

#
# ######  END of QUESTION 3    ###   END of QUESTION 3   ##########


#%% 
# Yet another method to copy 
thelist = [ 0, [10,11], [20, [[2100,2101],211]], 3] # four-level deep
thecopy4 = thelist[:] 
#
# ######  QUESTION 4      QUESTION 4      QUESTION 4   ##########
# Run some codes to find out if this is shallow or deep. 
# If it is deep, how deep?
#
thelist[2][1] = "You wouldn't ask this of any other guy"
print(thelist)
print(thecopy4)
## SHALLOW!
#
# ######  END of QUESTION 4    ###   END of QUESTION 4   ##########


#%% 
# Notice that after copying, if either of them is re-assigned (the variable name is used to point to a different object), instead of mutating (altering part of the elements), then the left over one is an "orphan" in CS term. They will no longer be shallow.  
thelist = [ 0, [10,11], [20, [[2100,2101],211]], 3] # four-level deep
thecopy5 = thelist # shallow copy created
thelist = [ 0, [10,11], [20, [[2100,2101],211]], 3] # re-assigned, albeit re-assigned to the same original values
#
# ######  QUESTION 5      QUESTION 5      QUESTION 5   ##########
# Run some codes to show that thelist and thecopy5 are not shallow anymore. 
# In other words, you can change any elements in the list of one, and it won't affect the other one.
#
thelist[0] = "And if you askin' how I'm feein'"
print(thelist[0])
print(thecopy5[0]) #oh they different different!
#
# ######  END of QUESTION 5    ###   END of QUESTION 5   ##########


#%%
# Now let me define a function to create deep copies of list of lists
def deepLcopy(obj):
  """
  Deep copy for list of list of list...
  :param obj: list of list of list...
  :return: a deep copy of the list
  """
  if (type(obj) == int or type(obj) == float or type(obj) == bool or type(obj) == str) : # if the argument we need to copy is just a primitive value, then just duplicate it. This is will be a true copy of that element.
    return obj
  elif (type(obj) == list): # now obj is a list, need to first create an empty list, and loop thru this list, then append each value to this empty list
    result = []
    for lo in obj: # lo for list-object. Assuming the elements in the list obj might actually be a list itself
      result.append(deepLcopy(lo)) # whether lo is a list or not, we *trust* that the deepLcopy() function can handle it (recursively). We just need to append the result to the end.
    return result # after the loop ends, we just need to return the copied list to the right place.
  else:
    return obj # cannot handle other types. Just let it be shallow.

#%%
#
# ######  QUESTION 6      QUESTION 6      QUESTION 6   ##########
thelist = [ 0, [10,11], [20, [[2100,2101],211]], 3] # four-level deep
thedeep = deepLcopy(thelist)
# Run some codes to show that thedeep is a true copy of thelist.
#
thelist[2][1] = "Don't tell me you're too blind to see"
print(thelist[2][1])
print(thedeep[2][1])
#
# ######  END of QUESTION 6    ###   END of QUESTION 6   ##########

#%%
# You can modify the codes above to make it work for dictionary 
# instead of list. Try that. 
#
# ######  QUESTION 7      QUESTION 7      QUESTION 7   ##########
#
def deepDcopy(obj):
    """
    Deep copy for dictionary of dictionary of dictionary...
    :param obj: dictionary of dictionary of dictionary...
    :return: a deep copy of the dictionary
    """
    if (type(obj) == int or type(obj) == float or type(obj) == bool or type(obj) == str):
        return obj
    elif (type(obj) == dict):
        result = dict()
        for (k, v) in obj.items():
            result[k]=deepDcopy(v)
        return result 
    else:
        return obj
 

# ######  END of QUESTION 7    ###   END of QUESTION 7   ##########

#%%
#
# ######  QUESTION 8      QUESTION 8      QUESTION 8   ##########
# then test the code
theD = {  'L0': 0, 
          'L1': {'L10':10,'L11':11}, 
          'L2': {'L20':20, 'L21': { 'L210': {'L2100':2100, 'L2101':2101},'L211':211 } }, 
          'L3': 3
        } # four-level deep
theDeepD = deepDcopy(theD)
# Run some codes to show that theDeepD is a true copy of theD.
#
theD['L1'] = "That's what she said" 
print(theD['L1'])
print(theDeepD['L1'])

theD['L2']['L21']['L210']['L2101'] = "C'mon it was too easy!"
print(theD['L2']['L21']['L210']['L2101'])
print(theDeepD['L2']['L21']['L210']['L2101'])
#
# ######  END of QUESTION 8    ###   END of QUESTION 8   ##########


#%%
# We can modify the above to get a more general function to copy 
# any nested lists or dictionaries, which is a rather common scenario 
# in everyday programming
def deepDLcopy(obj):
  """
  Deep copy for nested dictionary or list 
  :param obj: nested dictionary or list 
  :return: a deep copy of the same nested object
  """
  if (type(obj) == int or type(obj) == float or type(obj) == bool or type(obj) == str) : return obj
  elif (type(obj) == list): 
    result = []
    for o in obj: result.append(deepDLcopy(o)) 
    return result 
  elif (type(obj) == dict):
    result = dict()
    for (k, v) in obj.items():
     result[k]=deepDcopy(v)
    return result 
  else: return obj # cannot handle other types. Just let it be shallow.

#%%
# Instead of using this deepDLcopy() function, such nested list/dictionary are the basis of the JSON format. So we can use these to make deep copies for such objects 
import json
# import json5

theJ = {  'L0': 0, 
          'L1': [10,11], 
          'L2': [20, { 'L210': [ 2100, 2101 ],'L211':211 } ], 
          'L3': 3
        } # four-level deep, with object of list of object of list (2100 and 2101)
theDeepJsonCopy = json.loads(json.dumps(theJ))
# json.dumps will convert dictionaries (and lists) to a string, unstructured. 
# Then it will be loaded back as a json-like object, which is a nested 
# dictionary/list. This will be true copy, as long as only {} and [] is involved.

#%%
#
# ######  QUESTION 9      QUESTION 9      QUESTION 9   ##########
# Run some codes to show that theDeepJsonCopy is a true copy of theJ.
# Change theDeepJsonCopy['L2'][1]['L210'][1] to some other values, 
# then inspect theDeepJsonCopy and theJ
#
theDeepJsonCopy['L2'][1]['L210'][1] = "Never Gonna Give You Up"
print(theDeepJsonCopy['L2'][1]['L210'][1])
print(theJ['L2'][1]['L210'][1]) #they deep and different!
#
# ######  END of QUESTION 9    ###   END of QUESTION 9   ##########
#
# This seems awesome, easy enough to get a deep copy. If you have an 
# object of say, basket of Stocks (and any other custom objects, with 
# its own methods as well as attributes) and so forth, that's 
# another story when making deep copies.


#%%
# NumPy
#
# Let us start with a python list
flatlist = list(range(1,25))
print(flatlist) # print your result, or it will not be graded.
import numpy as np
#
# ######  QUESTION 10      QUESTION 10      QUESTION 10   ##########
# Follow the examples in class, and 
# also from https://www.machinelearningplus.com/python/101-numpy-exercises-python/ 
# and https://www.w3resource.com/python-exercises/numpy/index-array.php
# Complete the following tasks
# 

#%%
# 10.1) create a numpy array from flatlist, call it nparray1. What is the shape of nparray1?

nparray1 = np.array(flatlist)
print(nparray1)
print(nparray1.shape) #here's the shape!

#%%
# 10.2) reshape nparray1 into a 3x8 numpy array, call it nparray2
# remember to print the result
#
nparray2 = np.reshape(nparray1, (3, 8))
print(nparray2)
print(nparray2.shape) #we got it!
#

#%%
# 10.3) swap columns 0 and 2 of nparray2, and call it nparray3
# remember to print the result

nparray3 = nparray2.copy()
nparray3[:,0] = nparray2[:,2]
nparray3[:,2] = nparray2[:,0]
print(nparray3)
#I feel like there's an easier but if it fits it ships!
#

#%%
# 10.4) swap rows 0 and 1 of nparray3, and call it nparray4
# remember to print the result
#
nparray4 = nparray3.copy()
nparray4[1,:] = nparray3[0,:]
nparray4[0,:] = nparray3[1,:]
print(nparray4)
#Now we cookin' 
#
#%%
# 10.5) reshape nparray4 into a 2x3x4 numpy array, call it nparray3D
# remember to print the result
#
nparray3D = np.reshape(nparray4, (2,3,4))
print(nparray3D) #uhhh, looks right?
#

#%%
# 10.6) from nparray3D, create a numpy array with boolean values True/False, whether 
# the value is a multiple of three. Call this nparray5
# remember to print the result
# 

nparray5 = nparray3D % 3 == 0 #multiple of 3
print(nparray5) #This checks out!
#

#%%
# 10.7) from nparray5 and nparray3D, filter out the elements that are divisible 
# by 3, and save it as nparray6a. What is the shape of nparray6a?
# remember to print the result
#
condition = nparray5 % 3 == 0
nparray6a = nparray5[condition]
print(nparray6a)

condition3D = nparray3D % 3 == 0
nparray6a = nparray3D[condition]
print(nparray6a)
#Unclear on unstructions but here it is on both arrays
#

#%%
# 10.8) Instead of getting a flat array structure, can you try to perform the filtering 
# in 10.7, but resulting in a numpy array the same shape as nparray3D? Say if a number 
# is divisible by 3, keep it. If not, replace by zero. Try.
# Save the result as nparray6b
# remember to print the result
# 
nparray6b = np.where(nparray3D % 3 == 0, nparray3D, 0)
print(nparray6b)
print(nparray6b.shape)

#

#%%
# As you can see, there are a lot of things we can do (and do it much faster) with numpy arrays. As always, we'll learn and search as we go.
# 
# The stock eod price in last homework probably would be better to store as numpy arrays, so we can vectorize the calculations needed. Instead of going back now and changing it, we'll just wait to use Pandas to save them as dataframes. Pandas is built on numpy, so all these will be applicable and useful.
#
# ######  END of QUESTION 10    ###   END of QUESTION 10   ##########

#%%
# ######  QUESTION 11      QUESTION 11      QUESTION 11   ##########
# 
# This last exercise is to test copying numpy arrays
# 11.1) copy nparray2 as nparray2c
nparray2c = nparray2
# now change nparray2c 1,1 position to 0. Check nparray2 and nparray2c again. 
# Are they true copies?
# 
nparray2c[1,1] = 0

print(nparray2)
print(nparray2c)

##They are shallow copies, do something to one and it happens to the other.
#

#%%
# 11.2) Let us try again. 
nparray2c = nparray2.copy() # numpy array has a copy function too!
# now change nparray2c 0,2 position value to -1. Check nparray2 and nparray2c again.
# Are they true copies?
# 
nparray2c[0,2] = -1

print(nparray2)
print(nparray2c)
#

#This seems to be a deep copy!
#%%
# Since numpy can only have an array with all values of the same type, we usually do not need to worry about deep levels copying. 
# 
# ######  END of QUESTION 11    ###   END of QUESTION 11   ##########

#%%
