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

try:
  inp1 = input("Enter a value: ")
except:
  inp1 = 'exceptional hello'
finally:
  # I usually put some data/input integrity checks here before moving on
  inp1 = 'changed to default' if not inp1 else 'VSCode+iPython error' if (inp1=='exceptional hello') else inp1
print('This is input1:',inp1)

#%%
# map(function, *iterables)
# the iteration stops when the shortest one reaches the end
# function can be compressed as one-liner, call it "lambda" function as an anonymous function
alist = [1, 2, 5, 3]
blist = [4, 0.5, 1, 1.5, 2, 8]
def dblval(x) : return 2*x
amap = map(dblval, alist)
# the above two lines are the same as the one below, which is useful for small (and non-reuseable) functions
amap = map(lambda x: 2*x , alist)

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
print(findDiff(100000000))



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

#%%
# read APPL stock csv file
# import os # already imported start of file
dirpath = os.getcwd()
print("current directory is : " + dirpath)
foldername = os.path.basename(dirpath)
print("Directory name is : " + foldername)
appl_date = []
appl_price_eod = []
fh = open('GWU_classes/DATS_6103_DataMining/Class03_classes/AAPL_201409_201909_daily.csv') # fh stands for file handle
# data pulled from https://www.nasdaq.com/symbol/aapl/historical (5 years, xslx format, 9/10/2019)
for aline in fh.readlines(): # readlines creates a list of elements; each element is a line in the txt file, with an ending line return character. 
  tmp = aline.split(',')
  appl_date.append(tmp[0].strip())
  appl_price_eod.append(float(tmp[1]))
  
# print(appl_date)
# print(appl_price_eod)




#%%
# class
# class can be thought of bundling properties (like variables) and functions (or called methods) together
# This is not a requirement, but good practice to use Capitalize first letter for classes, 
# variables or functions instances use regular lowercase first letter.
class Person:
  """ 
  a person with properties and methods 
  height in meteres, weight in kgs
  """

  # contructor and properties
  # __init__ is also called constructor in other propgramming langs
  # it also set the attributes in here 
  def __init__(self, lastname, firstname, height, weight) :
    self.lastname = lastname
    self.firstname = firstname
    self.height_m = height
    self.weight_kg = weight
  
  # find bmi according to CDC formula bmi = weight/(height^2)
  def bmi(self) : 
    return self.weight_kg/(self.height_m ** 2)
  
  def print_info(self) :
    print( self.firstname, self.lastname+"'s age is {0:.0f}, height {1:.{digits}f}m, weight {2:.1f}kg, and bmi currently is {3:.{digits}f}".format(self.age, self.height_m, self.weight_kg, self.bmi(), digits=2) )
  
  # gain weight
  def gain_weight_kg(self,gain) : 
    self.weight_kg = self.weight_kg + gain 

  # gain height
  def gain_height_m(self,gain) : 
    self.height_m = self.height_m + gain 
  
  def height_in(self) :
    # convert meters to inches
    return self.height_m *100/2.539
  
  def weight_lb(self) :
    # convert meters to inches
    return self.height_m *100/2.539
  
  
  

#%%
# instantiate the Person object as elo, etc
elo = Person('Lo','Edwin',1.6,60)
vars(elo) # shows all attributes and their values
dir(elo) # shows all attributes and methods

elo.print_info()
elo.gain_weight_kg(5) # no return value for this method
# same as
# Person.gain_weight_kg(elo,5) # use both arguments here
elo.print_info()

superman = Person('Man','Super', 1.99, 85)
superman.gain_weight_kg(-3.5)
superman.print_info()

persons = []
persons.append(elo)
persons.append(superman)
print(len(persons))

#%%
# Add to the Person class four other attributes. At least one of the type float or int.
# Add at least three other methods to the class that might be useful


#%% [markdown]
# 
# ## From a programmer's perspective on Object-Oriented Programming (OOP)
# 
# Read this [blog at Medium on OOP](https://medium.com/@cscalfani/goodbye-object-oriented-programming-a59cda4c0e53). 
# To put all these into context, from procedural progamming (such as C) to OOP (C++, java and the likes) was a 
# huge paradigm shift. The world has progressed however, and there are new needs, and new wants, from the new generations. 
# And there are new answers in response. Keep up with the new ideas and concepts. 
# That's how to stay ahead. 
# Just like OOP still uses a lot of concepts and functionality in procedure programming, 
# the new programming paradigm will continue to use OOP concepts and tools as the backbone. 
# Try to get as much as you can, although you might not consider yourself a programmer. 
# These will serve you well, and makes you a more logical thinker.


#%%
# recursive functions 
# essential skill for building tree type constructs
# watch out for stackoverflow and infinite loops

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

def hanoitowersdisp(): # display blocks on each hanoitower after each move
  global hanoitowers
  print("Config: ", end =" ")
  for t in hanoitowers:
    print(str(t['name'])+": "+ str(t['stack'])+" ", end =" ")
  print() # linebreak

def mvhanoitowers1(n, fromt=0, tot=1):
  """ 
  Moving stacks of blocks from one tower to another, showing the detail steps
  :param int n: the number of levels to move. The first time function call should have n = len of stack of fromTower
  :param int fromt: the id of the fromTower 
  :param int tot: the id of the toTower 
  :return: None
  """ 
  global hanoitowers
  dummyt = 3-fromt-tot
  
  if n == 1 : # only 1 level to move, I know how to do it, so let's do it
    print("Move disk 1 from tower",hanoitowers[fromt]['name'],"to tower",hanoitowers[tot]['name'])
    return  # return None
  else : # or don't use else here, would be the same
    mvhanoitowers1(n-1, fromt, dummyt) 
    # the actual move
    print("Move disk",n,"from tower",hanoitowers[fromt]['name'],"to tower",hanoitowers[tot]['name'])
    mvhanoitowers1(n-1, dummyt, tot) 

def mvhanoitowers(n, fromt=0, tot=1):
  """ 
  Moving stacks of blocks from one tower to another, showing the detail steps
  :param int n: the number of levels to move. The first time functino call should have n = len of stack of fromTower
  :param int fromt: the id of the fromTower 
  :param int tot: the id of the toTower 
  :return: None
  """ 
  global hanoitowers
  
  dummyt = 3-fromt-tot
  
  if n == 1 : # only 1 level to move, I know how to do it. Let's do it
    print("Move disk 1 from tower",hanoitowers[fromt]['name'],"to tower",hanoitowers[tot]['name'])
    hanoitowers[tot]['stack'].insert(0,hanoitowers[fromt]['stack'].pop(0))
    hanoitowersdisp()
    return  # return None
  else : # or don't use else here, would be the same
    mvhanoitowers(n-1, fromt, dummyt) 
    
    # the actual move
    print("Move disk",n,"from tower",hanoitowers[fromt]['name'],"to tower",hanoitowers[tot]['name'])
    hanoitowers[tot]['stack'].insert(0,hanoitowers[fromt]['stack'].pop(0))
    hanoitowersdisp()

    mvhanoitowers(n-1, dummyt, tot) 

def movetowers(n, fromt=0, tot=1) :
  """
  Moving stacks of blocks from one tower to another, showing the detail steps
  :param int n: the number of levels to move. 
  :param int fromt: the id of the fromTower 
  :param int tot: the id of the toTower 
  :return: None
  """
  # build the tower shell
  towers = [ { "id":0,"name":'A',"stack":[] } , { "id":1,"name":'B',"stack":[] } , { "id":2,"name":'C',"stack":[] } ]
  for i,t in enumerate(towers) :
    t['stack'] = list(range(1,n+1)) if i==fromt else []
    # if i==fromt :
    #   t['stack']=list(range(1,n+1))
    # else :
    #   t['stack']=[]

  # check input n
  n = 2 if n<1 else 50 if n>50 else math.floor(n)
  # if n<1 :
  #   n=2
  # elif n>50 :
  #   n=50
  # else :
  #   n=math.floor(n)
  
  # check input fromt (from tower id) should be 0,1, or 2
  fromt = 0 if fromt<0 else 2 if fromt >2 else math.floor(fromt)
  # if fromt < 0 :
  #   fromt = 0
  # elif fromt > 2 :
  #   fromt = 2
  # else :
  #   fromt = math.floor(fromt)
  
  # check input tot (to tower id) should be 0,1, or 2, AND not equal to fromt
  tot = 0 if tot<0 else 2 if tot>2 else math.floor(tot)
  # if tot < 0 :
  #   tot = 0
  # elif tot > 2 :
  #   tot = 2
  # else :
  #   tot = math.floor(tot)

  # make sure fromt != toto
  if tot == fromt :
    tot = (fromt+1)%3  # use of modular algebra (%-remainder) simplifies a lot of codes
  # tot = ((fromt+1)%3) if tot == fromt else tot
    
  print("At the begining:")
  localtowersdisp(towers)
      
  mvt(towers, n, fromt, tot)
  return
  
def mvt( towers, n, fromt=0, tot=1 ):
  dummyt = 3-fromt-tot
  
  if n == 1 : # only 1 level to move, I know how to do it. Let's do it
    print("Move disk 1 from tower",towers[fromt]['name'],"to tower",towers[tot]['name'])
    towers[tot]['stack'].insert(0,towers[fromt]['stack'].pop(0))
    localtowersdisp(towers) # display the config after each move
    return  # return None
  else : # or don't use else here, would be the same
    mvt(towers, n-1, fromt, dummyt) 
    
    # the actual move
    print("Move disk",n,"from tower",towers[fromt]['name'],"to tower",towers[tot]['name'])
    towers[tot]['stack'].insert(0,towers[fromt]['stack'].pop(0))
    localtowersdisp(towers) # display the config after each move

    mvt(towers, n-1, dummyt, tot) 

def localtowersdisp(towers): 
  """
  display blocks on each tower
  :param towers: the towers, a list of tower (dictionary)
  """
  print("Config: ", end =" ")
  for t in towers:
    print(str(t['name'])+": "+ str(t['stack'])+" ", end =" ")
    # print(t['name'], ":", t['stack'], end = " ")
  print() # linebreak

