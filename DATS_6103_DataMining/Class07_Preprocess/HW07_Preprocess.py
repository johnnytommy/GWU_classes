# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'

#%%
import os
import pip
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from bokeh._testing.plugins import selenium
import seaborn as sns
os.chdir('../Class07_Preprocess')  
# sometime when I opened the workspace from another folder, the 
# working directory getcwd() will be in the wrong place. 
# You can change it with chdir()
dirpath = os.getcwd() # print("current directory is : " + dirpath)
filepath = os.path.join( dirpath, 'HappyPeople.csv')
df = pd.read_csv(filepath)  

#%%
# So clean up the columns. You can use some of the functions we defined in class, like the total family income, and number of children.
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

dfChkBasics(df, True)



#%%
# Other ones like worked hour last week, etc, you'll need a new function. 
# Happy: change it to numeric codes (ordinal variable)
#Change happiness to a ordinal
df['General happiness']=df['General happiness'].astype('category')

def happyFactor(row): #Function that changes happiness categories to ordinal
    happy=row['General happiness']
    try:happy=str(happy)
    except:pass
    
    try:
        if not isinstance(happy,str) : happy = str(happy)
    except: pass
  
    happy = happy.strip()
    if happy == "Very happy": 
      return 5
    if happy == "Pretty happy": 
      return 4
    if happy == "Not too happy": 
      return 3
    if happy == "Not applicable": 
      return 2
    if happy == "No Answer": 
      return 1
    if happy == "Don't KnowPretty happy": 
      return 0
    else: 
      return np.nan


df['General happiness']=df.apply(happyFactor,axis=1)
df['General happiness'].head()

#%%
# Ballot: just call it a, b, or c 
df['Ballot used for interview']=df['Ballot used for interview'].astype('category')

def ballot(row): #Function to change ballot to a b or c
  itsAballot=row['Ballot used for interview']
  try:itsAballot=str(itsAballot)
  except:pass
    
  try:
    if not isinstance(itsAballot,str) : itsAballot = str(itsAballot)
  except: pass
  
  itsAballot = itsAballot.strip()
  if itsAballot == "Ballot a": 
    return 'a'
  if itsAballot == "Ballot b": 
    return 'b'
  if itsAballot == "Ballot c": 
    return 'c'
  if itsAballot == "Ballot d": 
    return 'd'
  else: 
    return np.nan
    
df['Ballot used for interview']=df.apply(ballot,axis=1)

#%%
# Marital status, it's up to you whether you want to rename the values. 
#
df['Marital status']=df['Marital status'].astype('category')

def marriageStatus(row): #Function that turns marriage status to characters
    marriagio=row['Marital status']
    try:marriagio=str(marriagio)
    except:pass
    
    try:
        if not isinstance(marriagio,str) : marriagio = str(marriagio)
    except: pass
  
    marriagio = marriagio.strip()
    if marriagio == "Married": 
      return 'M'
    if marriagio == "Never married": 
      return 'N'
    if marriagio == "Divorced": 
      return 'D'
    if marriagio == "Widowed": 
      return 'W'
    if marriagio == "Separated": 
      return 'S'
    if marriagio == "No answer": 
      return 'NonA'
    else: 
      return np.nan
    
df['Marital status']=df.apply(marriageStatus,axis=1)


#%%
# After the preprocessing, make these plots

#%%
# Box plot for hours worked last week, for the different marital status. (So x is marital status, and y is hours worked.) 
sns.set(style="ticks", palette="pastel")
sns.boxplot(x='Marital status',y='Number of hours worked last week',data=df,
           )
plt.show()



#%%
# Violin plot for income vs happiness 
sns.violinplot(x='General happiness',y='Total family income',data=df)
plt.show()


#%%
# Use happiness as numeric, make scatterplot with jittering in both x and y between happiness and number of children. 
plt.plot(df['Number of children'], df['General happiness'],'o',alpha=0.1)
plt.ylim(0,6)  

jitta=df['General happiness']+np.random.normal(0, 2, size=len(df))
plt.plot(df ['Number of children'], jitta, 'o',markersize=3)
plt.ylim(0,6)
plt.ylabel('happy')
plt.xlabel('# of children')
plt.show() 


#%%
# If you have somewhat of a belief that happiness is caused/determined/affected by number of children, or the other way around (having babies/children are caused/determined/affected by happiness), then put the dependent variable in y, and briefly explain your choice.

#TODO


#%%
