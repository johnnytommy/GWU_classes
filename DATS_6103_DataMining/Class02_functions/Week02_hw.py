#%%
# import math
# import os
print("Hello world!")

#%%
###############  HW  Week02      HW  Week02      HW  Week02    ###############
# Our Goal: print out the 366 days in 2020
# 2020/1/1 
# 2020/1/2 and so forth
#

#%%
###################################### Q1 ###############################
#

dowt = ('Sun','Mon','Tue','Wed','Thu','Fri','Sat') # day-of-week-tuple
year = 2020
cnt = 3 # 2020/1/1 is a Wednesday, so let us start a counting index of 3 for Wednesday, and keep adding one
m = 0 # this will be a variable to be looped through eventually. I use the convention of 0-11 for the twelve months 
month = m+1 # this is the month to be displayed/printed. The way it is set up now, it will NOT change automatically when you change the value of m. Beware of that.
maxdays = 7 # this variable will be conditional on the month eventually. Right now, just try 7
# write a for loop, to print out the day value
# fill in the ??????
for d in (range(maxdays)) :
  day = dowt[d]
  print(day)

#%%
###################################### Q2 ###############################
#

# dowt = ('Sun','Mon','Tue','Wed','Thu','Fri','Sat') # day-of-week-tuple
year = 2020
# cnt = 3 # 2020/1/1 is a Wednesday, so let us start a counting index of 3 for Wednesday, and keep adding one
m = 3 # this will be a variable to be looped through eventually. I use the convention of 0-11 for the twelve months 
# month = m+1 # this is the month to be displayed/printed. The way it is set up now, it will NOT change automatically when you change the value of m. Beware of that.

# write a condition statement to determine the maxdays depending on the m value.
# For example, when m=0 (Jan), maxdays should be 31, m=3 (Apr), maxdays should be 30, etc.
# Try both ways, as a chunk of codes, or a one-liner

a = [0,2,4,6,7,10,11] #31 days
b = [3,5,8,9] #30 days
if m in a:  
  maxdays = 31
  print(maxdays)
elif m in b:
  maxdays = 30
  print(maxdays)
else:
  maxdays = 29
  print(maxdays)
#
# Change your m value (between 0 and 11, inclusive) and run the chunk to see if prints out the correct result.
#
# Challenge: if you can take into account that year is multiple of 4, EXCEPT when year is multiple of 100, the days 
# in Feb should be 29. Otherwise, there should be 28.  
# Examples: 2004, 2008, 2012, Feb has 29 days, but 2001, 2002, 2003, 2005, 2006, ... 28 days. Year 2000 or any 
# century marks, multiples of 100, they are non-leap years, so only 28 days.

###The code above takes care of this.
#%%
###################################### Q3 ###############################
#

dowt = ('Sun','Mon','Tue','Wed','Thu','Fri','Sat') # day-of-week-tuple
# year = 2020
cnt = 3 # 2020/1/1 is a Wednesday, so let us start a counting index of 3 for Wednesday, and keep adding one
# m = 3 # this will be a variable to be looped through eventually. I use the convention of 0-11 for the twelve months 
#
# As the cnt value changes, we want to print out the day-of-week info.
# So 3 gives Wed, 7 gives Sat, 8 should gives Sun, and so forth.
# use the very common method of finding the remainder (mod 7), print out that info in a single line of code

#chunk
for  d in (range(366)):
  w = cnt % 7
  day = dowt[w]
  cnt += 1
  print(day)

# %%
#one liner
start2020 = 3
end2020 = 369
dow = [dowt[cnt % 7] for cnt in range(start2020,end2020)]

#%%
###################################### Q4 ###############################
# Put all these together, and print out something like this: 
# Wed - 2020/1/1
# Thu - 2020/1/2
# Fri - 2020/1/3
# Sat - 2020/1/4
# Sun - 2020/1/5
# Mon - 2020/1/6
# Tue - 2020/1/7
# Wed - 2020/1/8
# Thu - 2020/1/9
# Fri - 2020/1/10
# Sat - 2020/1/11
# Sun - 2020/1/12
# Mon - 2020/1/13
# Tue - 2020/1/14
# Wed - 2020/1/15
# Thu - 2020/1/16

dowt = ('Sun','Mon','Tue','Wed','Thu','Fri','Sat') # day-of-week-tuple
year = 2020
cnt = 3 # 2020/1/1 is a Wednesday, so let us start a counting index of 3 for Wednesday, and keep adding one

mon = 12

#function to determine maxdays, see Q2
def monthMax(m):
  a = [0,2,4,6,7,10,11] #31 days
  b = [3,5,8,9] #30 days
  if m in a:  
    maxdays = 31
    return(maxdays)
  elif m in b:
    maxdays = 30
    return(maxdays)
  else:
    maxdays = 29
    return(maxdays)

cnt = 3
for m in range(mon) : # loop thru the 12 months
  month = m + 1
  maxdays = monthMax(m) #new function
  for d in range(maxdays): #loop through all the days
    day = (d+1)
    dow = dowt[cnt % 7]  # day of week 
    print("%s - %d/%d/%d" % (dow,year,month,day) )
    cnt += 1  # advance the count by 1

# check your code


# %%
###################################### Q5 ###############################
# A math question
# For a integer n, let us try to find all the factors and print them out
import math # if you ever need some math functions like floor()
n = 1862

# pseudocode
# loop through an index i (from 1, not zero)
#   if n/i is integer, print i
import math 
n = 1862
for i in range(1,n):
  if n % i == 0:
    print(i)

#%%