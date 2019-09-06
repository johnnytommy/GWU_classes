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
  print(val, type(key))
  
# for val in string :
for char in 'GW Rocks' :
  print(char, type(char))
  
# for index, val in enumerate(list) :
thething = [ 4,'2',("a",5),'end' ]
for index, val in enumerate(thething) :
  print("index", index, "value", val, thething[index], type(val))

# Try tuple, set, and dictionary
thething = { 4,'2',("a",5),'end' }

# what happened to set and dictionary? 
# Remember that set is un-ordered, and dictionary uses keys, not index. They cannot be enumerated.


# external file
# import os # already imported start of file
dirpath = os.getcwd()
print("current directory is : " + dirpath)
foldername = os.path.basename(dirpath)
print("Directory name is : " + foldername)
fh = open('GWU_classes/DATS_6103_DataMining/Class02_Functions/presidents.txt') # fh stands for file handle
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

