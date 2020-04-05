# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'

#%% [markdown]
#
# # Week06 HW
# ## By: Johnny Thomas
# ### Date: 2/2/2020
#

#%% [markdown]
# Let us improve our Stock exercise with Pandas now.
#

#%%
# Standard quick checks
def dfChkBasics(dframe, valCnt = False): 
  cnt = 1
  print('\ndataframe Basic Check function -')
  
  try:
    print(f'\n{cnt}: info(): ')
    cnt+=1
    print(dframe.info())
  except: pass

  print(f'\n{cnt}: describe(): ')
  cnt+=1
  print(dframe.describe())

  print(f'\n{cnt}: dtypes: ')
  cnt+=1
  print(dframe.dtypes)

  try:
    print(f'\n{cnt}: columns: ')
    cnt+=1
    print(dframe.columns)
  except: pass

  print(f'\n{cnt}: head() -- ')
  cnt+=1
  print(dframe.head())

  print(f'\n{cnt}: shape: ')
  cnt+=1
  print(dframe.shape)

  if (valCnt):
    print('\nValue Counts for each feature -')
    for colname in dframe.columns :
      print(f'\n{cnt}: {colname} value_counts(): ')
      print(dframe[colname].value_counts())
      cnt +=1

# examples:
# dfChkBasics(df)

#%%
# Step 0, try reading the data file and make it a dataframe this time
# filepath = "/Users/edwinlo/GDrive_GWU/github_elo/GWU_classes_p/DATS_6103_DataMining/Class04_OOP/Dats_Grades.csv"
import os
import numpy as np
import pandas as pd

# os.chdir('../Class06_Pandas')  
# sometime when I opened the workspace from another folder, the working directory getcwd() 
# will be in the wrong place. You can change it with chdir()
filepath = os.path.join( os.getcwd(), "Dats_Grades.csv")
dats = pd.read_csv(filepath ) 

dfChkBasics(dats)

# What are the variables in the df? 
# What are the data types for these variables?

#%%
# The file has grades for a DATS class. Eight homeworks (out of 10 each), 2 quizzes (out of 100 each), and 2 projects (out of 100 each)
# Find out the class average for each item (HW, quiz, project)
# Hint, use .mean() function of pandas dataframe

# ######  QUESTION 1      QUESTION 1      QUESTION 1   ##########

print(dats.mean())

# ######  END of QUESTION 1    ###   END of QUESTION 1   ##########

#%%
# create a new column right after the last hw column, to obtain the average HW grade.
# use column name HWavg. Make the average out of the total of 100.
# Hint: use .iloc to select the HW columns, and then use .mean(axis=1) to find the row average

# ######  QUESTION 2      QUESTION 2      QUESTION 2   ##########

dats.insert(8, 'HWavg', dats[['H1','H2',"H3",'H4','H5','H6','H7','H8']].mean(axis=1))
# ######  END of QUESTION 2    ###   END of QUESTION 2   ##########

dats.head() # check result


#%%
# The course total = 30% HW, 10% Q1, 15% Q2, 20% Proj1, 25% Proj2. 
# Calculate the total and add to the df as the last column, named 'total', out of 100 max.

# ######  QUESTION 3      QUESTION 3      QUESTION 3   ##########

#dats['total'] = 
HW = dats.apply(lambda row: row['H1' : 'HWavg'].sum(),axis=1) * .3
tot = HW + (dats['Q1'] * .10) + (dats['Q2'] * .15) + (dats['Proj1'] * .20)+ (dats['Proj2'] * .25)

dats['total'] = tot.round(2)
# ######  END of QUESTION 3    ###   END of QUESTION 3   ##########

dats.head() # check result

#%%
# Now with the two new columns, calculate the class average for everything again. 

# ######  QUESTION 4      QUESTION 4      QUESTION 4   ##########

print(dats.mean())

# ######  END of QUESTION 4    ###   END of QUESTION 4   ##########

#%%
# Save out your dataframe as a csv file
# import os

# ######  QUESTION 5      QUESTION 5      QUESTION 5   ##########

q5 = os.path.join( os.getcwd(), 'question5.csv')
dats.to_csv(q5)  

# ######  END of QUESTION 5    ###   END of QUESTION 5   ##########



#%%
# ######  QUESTION 6      QUESTION 6      QUESTION 6   ##########

# In Week03 hw, we wrote a function to convert course total to letter grades. You can use your own, or the one from the solution file here.
def find_grade(total):
  # Function that takes an integer course total (total) and returns the letter grade.
  """
  convert total score into grades
  :param total: 0-100 
  :return: str
  """
  if   total >= 93:
    grade = "A"
    return grade
  elif total >=90 and total <93:
    grade = "A-"
    return grade
  elif total >=87 and total <90:
    grade = "B+"
    return grade
  elif total >=83 and total <87:
    grade = "B"
    return grade
  elif total >=80 and total <83:
    grade = "B-"
    return grade
  elif total >=77 and total <80:
    grade = "C+"
    return grade
  elif total >=73 and total <77:
    grade = "C"
    return grade
  elif total >=70 and total <73:
    grade = "C-"
    return grade    
  elif total >=60 and total <70:
    grade = "D"
    return grade
  else:
    grade = "F"
    return grade    
    
# ######  END of QUESTION 6    ###   END of QUESTION 6   ########## 

#%%
# Let us create one more column for the letter grade, just call it grade.
# Instead of broadcasting some calculations on the dataframe directly, we need to apply (instead of broadcast) this find_grade() 
# function on all the elements in the total column
dats['grade'] = dats['total'].apply(find_grade)
dats.head()  # check results


#%%
# Create a bar chart for the grade distribution
# Hint: use .value_counts() on the grade column to make a bar plot

# ######  QUESTION 7      QUESTION 7      QUESTION 7   ##########

import matplotlib.pyplot as plt

prob = dats.grade.value_counts()
prob.plot(kind='bar')

# ######  END of QUESTION 7    ###   END of QUESTION 7   ##########


#%%


