import math
import os

print("Hello world!")

# From last week
abool = True    # boolean
azero = 0    # int
aint = 35    # int
afloat = -2.8     # float
anumbzerostr = "0"     # str
aemptystr = ""     # str
aletter = 'a'     # str
astr = "three-five"     # str
# list / array
alist = [1,'person',1,'heart',10,'fingers']
# tuple # like list, but immutable (faster access and processing)
atuple = (1,'person',1,'heart',10,'fingers')
# set  # un-ordered, and distinct elements.  
aset = { 1,'person',1,'heart',10,'fingers' }
# dictionary
adictionary = { "name": "Einstein", 1: "one", astr: 35, aint: 'thirty five', "last": alist }

# some more 
# note anything unexpected/unusual
list1 = [1,5,3,8,2]
list2 = [2]
tuple1 = (1,5,3,8,2)
type(tuple1)
len(tuple1)
tuple2 = (2)
type(tuple2)
# len(tuple2) # does not work
tuple3 = tuple([2])
type(tuple3)
len(tuple3)
tuple4 = ()
type(tuple4)
len(tuple4)



# Slicing parts of list/tuple/set
# Try
# write some notes/comments for each case, so that you can review them easily yourself
alist[1:4]  # inclusive on the start index, exclusive of the end index
alist[:4]
alist[:]
# optional argument, skipping every 1 element with :2 at the end
alist[1:4:2]
alist[1:5:2]
alist[1:3:2]
# what do you expect the result of this to be?
alist[1::2]
# Also try 
alist[-4]
alist[-4:-2]
alist[-4:]
alist[-2:-4]

# Now try tuple, set, and dictionary
# Put some notes for yourself
# comment out the illegal ones so that you can run your entire file gracefully
atuple[1:4]
aset[1:4]


# conditional
# if :
income = 60000
if income >100000 :
  print("rich")

# if else:
if income >100000 :
  print("rich")
else :
  print("not rich")

# if elif elif .... :
if income >200000 :
  print("super rich")
elif income > 100000 :
  print("rich")
elif income > 40000 :
  print("not bad")
elif income > 0 :
  print("could be better")
else :
  print("no idea")

# The above can be compacted into a one-liner
print("super rich" if income > 200000 else "rich" if income > 100000 else "not bad" if income > 40000 else "could be better" if income > 0 else "no idea" )
# or 
incomelevel = "super rich" if income > 200000 else "rich" if income > 100000 else "not bad" if income > 40000 else "could be better" if income > 0 else "no idea" 
print(incomelevel)

# write your conditional statment to assign letter grades A, A-, B+ etc according to the syllabus


# loops 
# any difference among the three below?
# for val in list :
for val in [ 4,'2',("a",5),'end' ] :
  print(val, type(val))
# for val in tuple :
for val in ( 4,'2',("a",5),'end' ) :
  print(val, type(val))
# for val in set :
for val in { 4,'2',("a",5),'end' } :
  print(val, type(val))
# for val in dictionary :
for key in { "k0":4, "k8":'2', "k1":("a",5), "k5":'end' } :
  print(key, type(key))

thedictionary = { "k0":4, "k8":'2', "k1":("a",5), "k5":'end' }    
for key in thedictionary :
  print("key: ",key, type(key))
  print("val: ", thedictionary[key], type(thedictionary[key]))
    
# for val in string :
for char in 'GW Rocks' :
  print(char, type(char))
  
# for index, val in enumerate(list) :
thething = [ 4,'2',("a",5),'end' ]
for index, val in enumerate(thething) :
  print("index", index, "value", val, thething[index], type(val))

# Try tuple, set, and dictionary
thething = { 4,'2',("a",5),'end' }
thething = { "k0":4, "k8":'2', "k1":("a",5), "k5":'end' }
# re-run the for loop above -> error
# what happened to set and dictionary? 
# Remember that set is un-ordered, and dictionary uses keys, not index. They cannot be enumerated.

# for dictionary, you do not need to enumerate to get key, value pair
# either of these works
thething = { "k0":4, "k8":'2', "k1":("a",5), "k5":'end' }
for key in thething :
  print("key:", key, "value:", thething[key], "type of value", type(thething[key]))

# or try this
thething.items() # creates a object type of dict_items, which can be looped thru as key/value pairs   
for key, val in thething.items() :
  print("key:", key, "value:", val, "type of value", type(val))



# external file
# import os # already imported start of file
dirpath = os.getcwd()
print("current directory is : " + dirpath)
foldername = os.path.basename(dirpath)
print("Directory name is : " + foldername)
fh = open('GWU_classes/DATS_6103_DataMining/Class02_loops/presidents.txt') # fh stands for file handle
for k in fh.readlines():
  print(type(k), ' ' ,k,  end='')
# notice that fh will be empty at the end of the loop. Will need to readlines again if you need it


# function
# good habit to have (at least) a return statement for any functions
def my_add(a=0, b=0):
  my_sum = a+b
  print(my_sum)
  return my_sum
  # return 

bnow = my_add(5,8)

def my_times(a=1, b=1):
  """ 
  multiplying two floats
  :param float a: any number 
  :param float b: any number 
  :return: float
  """
  my_product = a*b
  print(my_product)
  return my_product
  # return


grade = 'A-'
# write a function (with arguement grade) to convert a grade to its grade-point

grades = [ { "class":"IntroDS", "semester":"spring", "year":2018, "grade":'A-', "credits":3 } , { "class":"IntroDataMininS", "semester":"fall", "year":2018, "grade":'A', "credits":4 } ]
# write a function (with arguement of grades) to calculate the GPA 


# recursive function
# watch out for stackoverflow

# You can just as easily write this following function with loops
def triangleSum(maxn, sum=0):
  """
  Finding the sum of 1+2+...+n
  :param maxn: the last interger to be added
  :param sum: the culmulative sum
  :return: the sum
  """
  maxn = math.floor(maxn)
  if maxn > 1 :
    sum = maxn+triangleSum(maxn-1,sum)
    return sum
  return 1 # execute when maxn = 1

# Try write a recursive function to calculate the "factorial". Example, 4-factorial = 4*3*2*1 returns 24



# Let's work together on a challenging problem:
# The recusive tower of Hanoi
# Starting with tower A having disks of sizes 1,2,3 stacked, 
# our goal is to move them all to tower B, one disk at a time
# with tower C as a buffer. At any time, the disks on each tower 
# cannot have larger disks above smaller disks. Show the steps of 
# how to do move them.


hanoitowers = []
hanoitowers.append( { "id":0, "name":'A', "stack":[1,2,3] } )
hanoitowers.append( { "id":1, "name":'B', "stack":[] } )
hanoitowers.append( { "id":2, "name":'C', "stack":[] } )
