#%%
import math
import os

print("Hello world!")

#%%
# function
# good habit to have (at least) a return statement for any functions
# python use indentations instead of (curly) brackets
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

#%%
santa = 'ho'
# Question: What is the difference these two ways of doing things:
# first
def myfunction(a):
  out = a+a+a
  print(out)

myfunction(santa)

# second way
def myfunction2(a):
  out = a+a+a
  return out

print(myfunction2(santa))

# Answer: seond method is better for many reasons...
# Do you see the function as a "user-interface" function that interact with the user, or 
# do you see it as a tripling function? 
# GIVE functions a return value, give them a purpose, a clear reason of their existence.

#%%
# let us write a function find_grade(total) 
# which will take your course total (0-100), and output the letter grade (see your syllabus)
# have a habbit of putting in the docstring
total = 82.74

#%%
# Let us write a function to_gradepoint(grade)
# which convert a letter grade to a grade point. A is 4.0, A- is 3.7, etc
grade = 'B-'

#%%
# Next write a function to_gradepoint_credit(course)
# which calclates the total weight grade points you earned in one course. Say A- with 3 credits, that's 11.1 total grade_point_credit
course = { "class":"IntroDS", "semester":"spring", "year":2018, "grade":'B-', "credits":3 } 

#%%
# Now write a function gpa(courses) to calculate the GPA 
courses = [ { "class":"IntroDS", "semester":"spring", "year":2018, "grade":'B-', "credits":4 } , { "class":"IntroDataMining", "semester":"fall", "year":2018, "grade":'A', "credits":3 } ]

