# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'

#%%
import math
import os

print("Hello world!")

#%%
# Reviews/Summary
# BIFS
# list 
# subsetting
# tuple, set, dictionary 
# loops 
for i in range(0,7) : print(i)
# for index, val in enumerate(list) :
thething = [ 4,'2',("a",5),'end' ]
for val in thething : print (val)
for index, val in enumerate(thething) : print("index", index, ", value", val)
# for looping over dictionaries
thething = { "k0":4, "k8":'2', "k1":("a",5), "k5":'end' }
for key in thething : print("key:", key, ", value:", thething[key] )
# or use thething.items() # creates a object type of dict_items, which can be looped thru as key:value pairs   
for key, val in thething.items() : print("key:", key, ", value:", val)

#%%
# input (in terminal, not working with VSCode+iPython) 
# the line below produces an error in iPython window
# inp1 = input("Enter a value: ") 
# Use "Run Python File in Terminal" instead. 
# Make sure the terminal is in the shell mode

# inp1 = input("Enter a value: ")

try:
  inp1 = input("Enter a value: ")
except:
  inp1 = 'exceptional hello'
finally:
  # I usually put some data/input integrity checks here before moving on
  inp1 = 'changed to default' if not inp1 else 'VSCode+iPython error' if (inp1=='exceptional hello') else inp1
print('This is input1:',inp1)

#%%
# map(function, *iterables) (It does the function to a list)
# the iteration stops when the shortest one reaches the end
# function can be compressed as one-liner, call it "lambda" function as an anonymous function
alist = [1, 2, 5, 3]
blist = [4, 0.5, 1, 1.5, 2, 8]
def dblval(x) : return 2*x
amap = map(dblval, alist)
# the above two lines are the same as the one below, which is useful for small (and non-reuseable) functions
amap = map(lambda x: 2*x, alist)

#%% 
# Be careful. The map object is transient and fleeting ...
amap = map(lambda x: 2*x , alist)
print(amap)
print(list(amap))
print(list(amap))
# notice that the first time you list out amap, it iterated the entire sequence and removed each element
# save it out right away is the common practice
resultlist = list(map(lambda x: 2*x , alist))
print(resultlist)
print(list(resultlist))
print(list(resultlist)) # still here, still the same

#%% [markdown]
# ## Using the map function 
#
# Try to get a list of numbers given by 1/n^2 using the map() function.
# Next using a loop to add all those numbers from n=1 to 1000 (nmax)
# What is the difference of the value and pi^2 / 6?
# Can you make these into a single function that returns the difference, depending on nmax?
# def findDiff(nmax) :

#%%
nmax = 1000
seq = list( map(lambda n: n**(-2), range(1,nmax+1) ) )
sum = 0
for v in seq: sum = sum+v
print(sum)
print(math.pi**2/6)
print("Difference =", math.pi**2/6-sum)

def findDiff(nmax):
  seq = list( map(lambda n: n**(-2), range(1,nmax+1) ) )
  sum=0
  for v in seq: sum = sum+v
  return (math.pi**2/6 - sum)

print(findDiff(1000))
# print(findDiff(100000000))



#%%
# Now with multiple argument functions
def mypower(x,y): return x ** y 
resultlist = list( map(mypower, alist, blist) )
# or
resultlist = list( map(lambda x,y: x ** y , alist, blist) )
print(resultlist)

#%%
# We could perform the task above ourselves with loops (as a practice)
resultlist = [] # initialize an emtpy list
for i in range(0, min( len(alist),len(blist) ) ):
  resultlist.append( alist[i] ** blist[i] )
print(resultlist)
# Of course when things get more complicated, or if you already have the function defined, it should be much easier to use the map() function.

