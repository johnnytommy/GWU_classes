
###############  HW  Week03      HW  Week03      HW  Week03    ###############
# We first continue to complete the grade record that we were working on in class.

#%%
###################################### Q1 ###############################
# let us write a function find_grade(total) 
# which will take your course total (0-100), and output the letter grade (see your syllabus)
# have a habbit of putting in the docstring
total = 62.1

def find_grade(total):
  # write an appropriate and helpful docstring #TODO
  if   total >= 93:
    grade = "A"
    return grade
  elif total >=90 and total <=92:
    grade = "A-"
    return grade
  elif total >=87 and total <=89:
    grade = "B+"
    return grade
  elif total >=83 and total <=86:
    grade = "B"
    return grade
  elif total >=80 and total <=82:
    grade = "B-"
    return grade
  elif total >=77 and total <=79:
    grade = "C+"
    return grade
  elif total >=73 and total <=76:
    grade = "C"
    return grade
  elif total >=70 and total <=72:
    grade = "C-"
    return grade    
  elif total >=60 and total <=69:
    grade = "D"
    return grade
  else:
    grade = "F"
    return grade    
    

# Try:
print(find_grade(total))

# Also answer these: 
# What is the input (function argument) data type for total? 
##INTEGER

# What is the output (function return) data type for find_grade(total) ?
##STRING

#%%
###################################### Q2 ###############################
# next the function to_gradepoint(grade)
# which convert a letter grade to a grade point. A is 4.0, A- is 3.7, etc
grade = 'C-'

def to_gradepoint(grade):
  # write an appropriate and helpful docstring #TODO
  if   grade == "A":
    gradepoint = 4.0
    return gradepoint
  elif grade == "A-":
    gradepoint = 3.7
    return gradepoint
  elif grade == "B+":
    gradepoint = 3.3
    return gradepoint
  elif grade == "B":
    gradepoint = 3.0
    return gradepoint
  elif grade == " B-":
    gradepoint = 2.7
    return gradepoint
  elif grade == "C+":
    gradepoint = 2.3
    return gradepoint
  elif grade == "C":
    gradepoint = 2.0
    return gradepoint
  elif grade == "C-":
    gradepoint = 1.7
    return gradepoint    
  elif grade == "D":
    gradepoint = 1.0
    return gradepoint
  else:
    gradepoint = 0
    return gradepoint    
    

# Try:
print(to_gradepoint(grade))

# What is the input (function argument) data type for find_grade? 
##STRING

# What is the output (function return) data type for find_grade(grade) ?
##INTEGER

#%%
###################################### Q3 ###############################
# next the function to_gradepoint_credit(course)
# which calculates the total weight grade points you earned in one course. Say A- with 3 credits, that's 11.1 total grade_point_credit
course = { "class":"IntroDS", "id":"DATS 6101", "semester":"spring", "year":2018, "grade":'B-', "credits":3 } 

def to_gradepoint_credit(course):
  # write an appropriate and helpful docstring #TODO
  # ??????    fill in your codes here
  # grade_point_credit = ?????
  # eventually, if you need to print out the value to 2 decimal, you can 
  # try something like this for floating point values %f
  # print(" %.2f " % grade_point_credit)
  return grade_point_credit

# Try:
print(" %.2f " % to_gradepoint_credit(course) )

# What is the input (function argument) data type for to_gradepoint_credit? 
# What is the output (function return) data type for to_gradepoint_credit(course) ?


#%%
###################################### Q4 ###############################
# next the function gpa(courses) to calculate the GPA 
# It is acceptable syntax for list, dictionary, JSON and the likes to be spread over multiple lines.
courses = [ 
  { "class":"Intro to DS", "id":"DATS 6101", "semester":"spring", "year":2018, "grade":'B-', "credits":3 } , 
  { "class":"Data Warehousing", "id":"DATS 6102", "semester":"fall", "year":2018, "grade":'A-', "credits":4 } , 
  { "class":"Intro Data Mining", "id":"DATS 6103", "semester":"spring", "year":2018, "grade":'A', "credits":3 } ,
  { "class":"Machine Learning I", "id":"DATS 6202", "semester":"fall", "year":2018, "grade":'B+', "credits":4 } , 
  { "class":"Machine Learning II", "id":"DATS 6203", "semester":"spring", "year":2019, "grade":'A-', "credits":4 } , 
  { "class":"Visualization", "id":"DATS 6401", "semester":"spring", "year":2019, "grade":'C+', "credits":3 } , 
  { "class":"Capstone", "id":"DATS 6101", "semester":"fall", "year":2019, "grade":'A-', "credits":3 } 
  ]

def find_gpa(courses):
  # write an appropriate and helpful docstring
  total_grade_point_credit =0 # initialize 
  total_credits =0 # initialize
  # ??????    fill in your codes here
  # gpa = ?????
  return gpa

# Try:
print(" %.2f " % find_gpa(courses) )

# What is the input (function argument) data type for find_gpa? 
# What is the output (function return) data type for find_gpa(courses) ?


#%%
###################################### Q5 ###############################
# Write a function to print out a grade record for a single class. 
# The return statement for such functions should be None or just blank
# while during the function call, it will display the print.
course = { "class":"IntroDS", "id":"DATS 6101", "semester":"spring", "year":2018, "grade":'B-', "credits":3 } 

def printCourseRecord(course):
  # write an appropriate and helpful docstring
  # use a single print() statement to print out a line of info as shown here
  # 2018 spring - DATS 6101 : Intro to DS (3 credits) B-  Grade point credits: 8.10 
  # ??????    fill in your codes here
  return # or return None
  
# Try:
printCourseRecord(course)

# What is the input (function argument) data type for printCourseRecord? 
# What is the output (function return) data type for printCourseRecord(course) ?


#%%
###################################### Q6 ###############################
# write a function (with arguement of courses) to print out the complete transcript and the gpa at the end
# 2018 spring - DATS 6101 : Intro to DS (3 credits) B-  Grade point credits: 8.10 
# 2018 fall - DATS 6102 : Data Warehousing (4 credits) A-  Grade point credits: 14.80 
# ........  few more lines
# Cumulative GPA: ?????
 
def printTranscript(courses):
  # write an appropriate and helpful docstring
  for course in courses:
    # print out each record as before
  
  # after the completion of the loop, print out a new line with the gpa info
  
  return # or return None

# Try to run, see if it works as expected to produce the desired result
# courses is already definted in Q4
printTranscript(courses)

# What is the input (function argument) data type for printTranscript? 
# What is the output (function return) data type for printTranscript(courses) ?



#%% 
# ######  QUESTION 7   Recursive function   ##########
# Write a recursive function that calculates the Fibonancci sequence.
# The recusive relation is fib(n) = fib(n-1) + fib(n-2), 
# and the typically choice of seed values are fib(0) = 0, fib(1) = 1. 
# From there, we can build fib(2) and onwards to be 
# fib(2)=1, fib(3)=2, fib(4)=3, fib(5)=5, fib(6)=8, fib(7)=13, ...
# Let's set it up from here:

def fib(n):
  """
  Finding the Fibonacci sequence with seeds of 0 and 1
  The sequence is 0,1,1,2,3,5,8,13,..., where 
  the recursive relation is fib(n) = fib(n-1) + fib(n-2)
  :param n: the index, starting from 0
  :return: the sequence
  """
  # assume n is positive integer
  # ??????    fill in your codes here

  return # return what ????


# Try:
print(fib(6))  # should gives 8
print(fib(7))  # should gives 13




#%%

