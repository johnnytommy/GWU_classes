# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'

#%%
import numpy as np
# pip install pandas
# pip3 install pandas
import pandas as pd

#%% 
# Let's start with panda series
# with the simplest case, building from a python list
fiblist = [0,1,1,2,3,5,8,13,21,34] # first 10 numbers in Fibonacci sequence (seeds 0 and 1)

#%%
# pandas series
s = pd.Series(fiblist)
print(s)
print(s.values)

# add series name to it
s = pd.Series(fiblist, name='Fibonacci sequence')
print(s)
print(s.values)
# Series name is to annotate the series.
# Must be one of BIFS, usually we use str.

#%%
# selection same as list
s0 = s[0]
print(f"s0 is of type= {type(s0)}, value= {s0}" )
s3 = s[3]
print(f"s3 is of type= {type(s3)}, value= {s3}" )
s05 = s[0:5]
print(f"s05 is of type= {type(s05)}, value= {s05}?" )
print(s05)

#%% 
# Can we build from Numpy array?
nplist = np.array(fiblist)
# pandas series
s = pd.Series(nplist)
print(s)


#%%
# build pandas series from list generator?
listGen = ( 2*n+1 for n in range(10**3) )
print(listGen) # this is a generator object
print(type(listGen))

success = False
try: 
  s = pd.Series(listGen)
  print("Success! Pandas list created from list generator")
  success = True
  s0 = s[0]
  print(f"s0 is of type= {type(s0)}, value= {s0}" )
  s3 = s[3]
  print(f"s3 is of type= {type(s3)}, value= {s3}" )
  s05 = s[0:5]
  print(s05)
except:
  print("Cannot create pandas series directly from list generator")
  # pass

if success:
  print(s[10**2])
else:
  pass

#%%
# So it works? Let's try again
listGen = ( 2*n+1 for n in range(10**100000000) )
print(listGen) # this is a generator object
print(type(listGen))
print("Working so far!")

success = False
try: 
  s = pd.Series(listGen)
  print("Success! Pandas list created from list generator")
  success = True
  s0 = s[0]
  print(f"s0 is of type= {type(s0)}, value= {s0}" )
  s3 = s[3]
  print(f"s3 is of type= {type(s3)}, value= {s3}" )
  s05 = s[0:5]
  print(s05)
except:
  print("Cannot create pandas series directly from list generator")
  # pass

if success:
  print(s[10**10])
else:
  pass

# So it doesn't really work, unless later versions will create a pandas series generator 
# instead of trying to create an ordinary pandas series

#%%
# Next concept is on index  
# similar to primary key in Relational Database (RDB) structures  
# index does not have to be unique however...
pdfib = pd.Series(fiblist)
print(pdfib,'\n')
pdfib = pd.Series(fiblist, name='FibVal')
print(pdfib,'\n')
fibindex = ['one','two','three','four','five','six','seven','eight','nine','ten']
# fibindex = [9,9,7,6,5,4,3,2,1,0]
pdfib = pd.Series(fiblist, name='FibVal', index=fibindex)
print(pdfib,'\n')

#%%
# Seems like no big deal, nothing to see here.  
# We can do some more advanced indexing (for dataframes) that is consistent with primary/secondary key used in RDB 
# For now, know that index again can only be BIFS.
# Like dictionary, we often use str or int.
print(pdfib['nine'])
# The series in any case still has an intrinsic integer index as with a python list
# So the above is the same as this here
print(pdfib[8])

#%%
# We can also use simple range syntax for filtering
print(pdfib['three':'eight'], '\n')
# same as, EXCEPT ..... (fill in the ellipses...)
print(pdfib[2:7], '\n')

#%%
# The pandas series index is immutable (cannot be changed)
print(pdfib.index[5])
try:
  pdfib.index[5] = 'newSix'
  print("changed 5th-index successfully.")
except:
  pass

#%%
# you can change the entire index list however
print(pdfib.index)
try:
  pdfib.index = [9,9,9,9,5,4,3,2,1,0]
  print("changed the entire index successfully.")
  print(pdfib)
except:
  pass

#%%
# Now with integer index, we lost the ability to reference the series using the intrinsic index
# The index we assigned will take precedence. 
# What do you think the call below will produce? Guess before you run.
#
# print(pdfib[0]) # our index take precedence over the intrinsic index
# print(pdfib[1]) # our index take precedence over the intrinsic index

# What if the index is not unique? Guess.
#
# print(pdfib[9])

# What if the (integer) index is not defined in our series? 
# Will it now treat it as the intrinsic index and produce pdfib[8] -> 21 ?
# Guess.
# 
# print(pdfib[8]) # doesn't work

# but this does kind of work, using 8 and 9 as intrinsic index
print(pdfib[8:9]) 
type(pdfib[8:9]) 
# although it gives you a series instead of a single value.

#%%
# Can we still do filtering? Yeah... with intrinsic indexes 
print(pdfib[2:7], '\n') # this works. 2 and 7 are interpreted as the intrinsic index. 2 is a valid index while 7 is not in our assigned index
print(pdfib[4:1], '\n') # empty series. 4 and 1 are not interpreted as our assigned index, although both exist in our assigned index list
print(pdfib[1:4], '\n') # empty series. 4 and 1 are not interpreted as our assigned index, although both exist in our assigned index list

#%% [markdown]
#
# # Indexing in Pandas series
# - Is the index int? Can you and should you avoid int/float/boolean?
# - Is the index unique? If not, watch out when used for filtering.


#%% [Markdown]
# # Pandas Dataframe
# Let us buildi Pandas DataFrames from a few different methods.  
# First, some basic building blocks:
fiblist = [0,1,1,2,3,5,8,13,21,34] # first 10 numbers in Fibonacci sequence (seeds 0 and 1)
fibindex = ['one','two','three','four','five','six','seven','eight','nine','ten']

sqlist = [81,64,49,36,25,16,9,4,1,0] # 10 squared numbers in reversed order 
# sqlist = ['a','a','a','a','a','a','b','b','b','c'] # it's acceptable for pandas dataframe to 
# have different data type between columns, unlike numpy arrays
sqindex = ['ten','nine','eight','seven','six','five','four','three','two','one']

#%% [markdown]
# ## Method 1, from lists directly
# If no index is specified, pandas will auto generate integral index

# , and you do not specify an index, 
# pandas will use the natural integer indexing 
# Try two different scenario
# Scenario 1 - With two different pandas series, with same index (unique)
pandasdf = pd.DataFrame({'fib':fiblist, 'sq':sqlist})
print(pandasdf)

# You can add index at that time, or at a later time using pandasdf.index
pandasdf = pd.DataFrame({'fib':fiblist, 'sq':sqlist}, index=fibindex)
print(pandasdf)


#%% [markdown]
# ## Method 2, from pandas series
# If the dictionaries do not have indexes, and you do not specify an index, 
# pandas will use the natural integer indexing 
# Try two different scenario
# Scenario 1 - With two different pandas series, with same index (unique)
fiblist = [0,1,1,2,3,5,8,13,21,34] # first 10 numbers in Fibonacci sequence (seeds 0 and 1)
fibindex = ['one','two','three','four','five','six','seven','eight','nine','ten']
pdfib = pd.Series(fiblist, index=fibindex)
print(pdfib,'\n')
sqlist = [81,64,49,36,25,16,9,4,1,0] # 10 squared numbers in reversed order 
# sqlist = ['a','a','a','a','a','a','b','b','b','c'] # it's acceptable for pandas dataframe to 
# have different data type between columns, unlike numpy arrays
sqindex = ['ten','nine','eight','seven','six','five','four','three','two','one']
pdsq = pd.Series(sqlist, index=sqindex)
print(pdsq,'\n')

#%% [markdown]
pddf = pd.DataFrame({'fib':pdfib, 'sq':pdsq})
# A couple of notes:
# If the indexes from the two series are ordered the same way, there will not be re-ordering. 
# right now, it will be re-ordered alphabetically
# Column names has to be unique. Duplicate ones will overwrite the existing ones.
# print()
print(pddf)
print(type(pddf))
print(pddf.shape)
print(pddf.columns)

#%% [markdown]
# ## Method 2, Scenario 2
# if the two different pandas series indexes are not unique 
# fiblist = [0,1,1,2,3,5,8,13,21,34] # first 10 numbers in Fibonacci sequence (seeds 0 and 1)
fibindex2 = ['one','one','one','four','five','six','seven','eight','nine','ten']
pdfib2 = pd.Series(fiblist, index=fibindex2)
print(pdfib,'\n')
# sqlist = [81,64,49,36,25,16,9,4,1,0] # 10 squared numbers in reversed order 
sqindex2 = ['ten','nine','eight','seven','six','five','four','three','two','one']
pdsq2 = pd.Series(sqlist, index=sqindex2)
print(pdsq2,'\n')

pddf2 = pd.DataFrame({'fib':pdfib2, 'sq':pdsq2})
# Error creating DF with duplicate indexes
# In RDB terms, pandas will not perform *outer/inner join* when the key is not unique


#%% [markdown]
# ## Method 3 
# Let's try import a dataset (csv) and poke around
# For VS Code, I installed "Edit csv" (janisdd) plug-in (optional) to help view and edit the csv if needed.
# Also have "Excel Viewer" (GrapeCity) installed. You can find and try others.
import os
# dirpath = os.getcwd() # print("current directory is : " + dirpath)
filepath = os.path.join( os.getcwd(), 'GWU_classes/DATS_6103_DataMining/Class05_Pandas/nfl2008_fga.csv')
nfl = pd.read_csv(filepath, index_col=0 )  
# OTHER read_csv optional arguments
# use header=None if the csv file has no header row
# use names = [ list ] to supply col headers
# use na_values =  to replace na values with NaN
# use parse_dates =  to format date columns
# 
# The code above will use the GameDate as index (which is not unique. NOT a good idea, as you'll see.)

#%%
nfl.head()
nfl.tail()
nfl.info()

#%%
# You can select subsets using loc and iloc functions
# index locator iloc
colsubset = nfl.iloc[:,1:3]
colsubset.head()

#%%
# locator loc
colsubset = nfl.loc[:,'HomeTeam':'sec'] 
colsubset.head()

#%%
rowsubset = nfl.iloc[2:7 , : ]
rowsubset

#%%
rowsubset = nfl.loc[20081005:20081012 , : ]
# Error. Non-unique row index.

#%% [markdown]
#
# ## Unique Index (UI)
#
# Always try to have unique index. In this case, there is no one column that serves as 
# a unique index, you can either specify no index so that pandas will use generic rowID 
# as index, or use multi-Index.

# filepath = os.path.join( os.getcwd(), 'GWU_classes/DATS_6103_DataMining/Class05_Pandas/nfl2008_fga.csv')
nfl = pd.read_csv(filepath)
nfl.head()

#%% (Optional)
# add index name
nfl.index.name = 'gameID'
nfl.head()

#%%
# or use GameDate AND HomeTeam to create an unique pair as index (Advance Indexing)
nfl2 = pd.read_csv(filepath, index_col=[0,1] ) 
nfl2.head()


#%% [markdown]
#
# # Broadcasting
#
# This is a simple example on broadcasting, as with numpy

nfl['season']='08-09' # broadcast to all elements (in that column) with the new assignment

#%% [markdown]
# # Data Structure
# 
# If you have learned or used database before, look at this dataframe using those lenses. 
# Is that usually how the data is stored in a DB (RDB)?  
# There are some replications and redundancies. 
# Can you spot them?
#
# For example, the values for 'season' is always the same, should we use one table for each season instead? 
# 
# Knowing the minutes of the game clock, why need to record the quarter qtr?
#
# Already have the record of home and away teams, knowing which one is the kickteam, why do we need to record the defense def?
#
# There are more than 10 games on a typical day, should we group them in a table for, say, week_n, therefore 
# no need to repeat the same date for 10+ times? Is that easier for storage and for retrival for data to be 
# stored in such RDB fashion?
#
# We are not here to say which method or system is best to store data and retrival. There are just so many reasons, good reasons, 
# why things are done in certain ways. 
#
# We will find ourselves in many situations the data collect is not in a form that is convenient to our analysis. 
# We might need to perform sql joins, lookups, merge tables, pivot tables, etc, (data wrangling) to prepare the data for our analysis.

#%%
# If you did some data processing, and like to save the result as a csv file, you can
# import os
# dirpath = os.getcwd() # print("current directory is : " + dirpath)
filecleaned = os.path.join( os.getcwd(), 'GWU_classes/DATS_6103_DataMining/Class05_Pandas/nfl_clean.csv')
nfl.to_csv(filecleaned)  


#%% [markdown]
# 
# In class exercise
# 
# Task 1: import the dataset for "diet" using pandas
# 

#%%
# Task 2: Take care of the few NA values in the dataframe. You can remove them, or replace by average, or ... depending on how many are there and your goal.
#

#%%
# Task 3: create a new column to calculate the bmi of the person
#

#%%
# Task 4: create a new column to calcuate the weight loss (negative value for loss) for each person after 6 weeks
#

#%%
# Task 5: create a new column to calcuate the weight loss percentage (negative value for loss, between 0 and 100 as a percent. 
# Well technically, one can gain more than 100% in 6 weeks) for each person after 6 weeks
#

#%%
# Task 6: Save out the dataframe as csv
# 

#%%
# Task 7: Let try to make some basic plots (EDA)
#
# We would like to explore relations between (choose some that you feel is possible, some might be more difficult to plot)
# as first, plot these without diet variable
# if successful, plot these colored by diet
import matplotlib.pyplot as plt
# diet.plot(x="Weight", y='Height')  # sample to get started

# weight and height
# weight and loss
# weight and loss percentage
# age and weight loss
# age and weight loss percentage
# bmi and loss
# bmi and loss percentage


#%%
