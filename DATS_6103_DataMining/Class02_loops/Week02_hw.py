import math
import os

print("Hello world!")

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
# now just need to start from the current working directory (cwd) and point to the file
fh = open('GWU_classes/DATS_6103_DataMining/Class02_loops/presidents.txt') 
# fh stands for file handle
for k in fh.readlines(): # readlines creates a list of elements; each element is a line in the txt file, with an ending line return character. 
  print(type(k) ,k ,  end='')


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

###############  HW  Week02      HW  Week02      HW  Week02    ###############
###################################### Q1 - Q2 ###############################
letterGrade = 'A-'
# Q1: What is the data type for letterGrade?

# Q2: Start with the template below, write a function to convert a letterGrade to its grade-value. 
# Example: A -> 4.0, A- -> 3.7
# Please provdie some reasonble docstring
def gradeValue(letter):
  """
  docstring
  """
  gradeval = 0 # initial placeholder
  # use conditional statement to set the correct gradeval
  #######################

  return gradeval

# Try to run, see if it works as expected
# gradeValue(letterGrade)


###################################### Q3 - Q4 ###############################
gradeRecord = { "class":"IntroDS", "semester":"spring", "year":2018, "grade":'A-', "credits":3 }
# Q3: What is the datatype for gradeRecord?

# Q4: write a function to calculate the grade points from a single grade record. 
# Example, a C+ for a 3-credit class should have grade points (2.3*3) = 6.9 grade points.
def gradePoint(record):
  """
  docstring
  """
  gradept = 0 # initial placeholder
  # calculate the gradept from the info in the record
  # you might find it handy to use the previous function gradeValue here

  return gradept

# Try to run, see if it works as expected
# gradePoint(gradeRecord)


###################################### Q5 ###############################
# Q5: write a function to print out a grade record for a single class. 
# The return statement for such functions should be None or just blank
# while during the function call, display will shows the printout.
def printGradeRecord(record):
  """
  docstring
  """
  # use a single print() statement to print out the info as here
  # 2018 spring - IntroDS (3 credits) A-  Grade points: 11.1    (or 11.100000000000001, I don't care at this point)

  return # or return None
  
# Try to run, see if it works as expected
# printGradeRecord(gradeRecord)


###################################### Q6 - Q8 ###############################
my_grades = [ { "class":"IntroDS", "semester":"spring", "year":2018, "grade":'A-', "credits":3 } , { "class":"IntroDataMining", "semester":"fall", "year":2018, "grade":'B', "credits":4 } , { "class":"Machine Learning 1", "semester":"spring", "year":2019, "grade":'C+', "credits":4 } , { "class":"Maching Learning 2", "semester":"fall", "year":2019, "grade":'A', "credits":4 } , { "class":"Visualization", "semester":"fall", "year":2019, "grade":'B-', "credits":3 } ]
# Q6: What is the datatype for my_grades? 
# Instead of just answering "It is a xxx", can you give a little more details "It is a xxx of yyy"?

# Q7: write a function (with arguement of records) to calculate the GPA 
def gpa(records):
  """
  docstring
  """
  totalgp = 0 # initialize cumulative grade-point total
  totalcredits = 0 # initialize cumulative credits total
  for record in records:
    # do something, add to the totalgp and totalcredits
    
    
    
  # after the completion of the loop, calculate and return the gpa
  return totalgp/totalcredits

# Try to run, see if it works as expected
# gpa(my_grades)

# Q8: write a function (with arguement of records) to print out the complete record and the gpa at the end
# 2018 spring - IntroDS (3 credits) A-  Grade points: 11.1    (or 11.100000000000001, I don't care at this point)
# 2018 fall - IntroDataMining (4 credits) B  Grade points: 12
# ........  three more lines
# Cumulative GPA: ?????
 
def printFullRecord(records):
  """
  docstring
  """
  for record in records:
    # print out each record as before
    
  
  # after the completion of the loop, print out a new line with the gpa info
  
  return # or return None

# Try to run, see if it works as expected
# printFullRecord(my_grades)

