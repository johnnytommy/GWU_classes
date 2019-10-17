# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'

#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('classic')

#%% [markdown]
import os
dirpath = os.getcwd() # print("current directory is : " + dirpath)
path2add = 'GWU_classes/DATS_6103_DataMining/Class06_Visualization'
filepath = os.path.join( dirpath, path2add ,'gss_gwu_6103_2019f/GSS.csv')
gss = pd.read_csv(filepath, index_col=11 )  
# gss = pd.read_csv(filepath)  

#%%
print('\n',gss.head(),'\n')

# Try these
rowind = 2
colind = 1
colname = 'degree'
try: print(gss.iloc[rowind,colind]) 
except: print("iloc[rowind,colind] error") 

try: print(gss.loc[rowind][colname]) 
except: print("loc[rowind][colname] error") 

try: print(gss.iat[rowind,colind]) 
except: print("iat[rowind,colind] error") 

try: print(gss.at[rowind,colname]) 
except: print("at[rowind,colname] error") 


#%%
# what was the problem?
# Make sure index is unique
# gss = pd.read_csv(filepath, index_col=[11,0] )
# gss = pd.read_csv(filepath, index_col=['id','year'] )
gss = pd.read_csv( filepath )
gss.set_index(['id','year'], inplace=True)
print('\n',gss.head(),'\n')

#%%
# Is the index unique?
gss.index.is_unique
# False

#%%
# What's next?
dups = gss.index.duplicated()
print(dups)

#%%
dupentries = gss[dups]
dupentries.shape

#%%
# Not too many. Let's take a peek at those entries.
print(dupentries)


#%%
# figure out how you want to clean it. 
# In this case, either just use dups to clean, or condition id>=0 to clean
gssc = gss[ dups==False ]
##################  Fill in the code
print(gssc.shape)
print(gssc.index.is_unique)

#%%
# Mission accomplished!
# Now we can try some basic df manipulation with multi-index / hierarchical index
print(gssc.loc[1,:])
print(gssc.loc[(1,2012),:])

try: print( gssc.loc[1:2,:] )
except: print("does not work with range for multi index with numeric as index")

try: print( gssc.loc[(1,2012):(2,2012)] )
except: print("nor using tuple-index as range for multi index with numeric as index")

# slicer doesn't work neither
# print(gssc.loc[( slice(1,4)  ,2012),age])

# will try to deal with these next time.


#%%
# for now, let's go back to basics, use the dataframe with the intrinsic interger position as index. 
print('\n',gssc.head(),'\n')
gssc = gssc.reset_index()
print('\n',gssc.head(),'\n')
# At least we removed the id == -1 entries already

#%%
# Look at educ ("Highest year of school completed")
educ = gssc['educ']

#%%
plt.hist(educ.dropna(), label='educ')
# plt.savefig('nice_fig.png')
plt.show()

#%% 
# That was terrible. Let's see what are these non-sensible data points.
##
##################  Fill in the code

#%% 
## If there are not too many of them, let's drop them.
##################  Fill in the code

#%% 

plt.hist(educ.dropna(), label='educ',edgecolor='black', linewidth=1.2)
plt.xlabel('Years of Education')
plt.ylabel('Rel freq.')
filepath = os.path.join( dirpath, path2add ,'hist_educ.png')
plt.savefig(filepath)
plt.show()

#%%
# When the numerical variable is not truely continuous, but some discrete 
# or integer values with a finite range, histogram with arbitrary number of bins might 
# not be the best way to present it.
# We can use Probability Mass Function PMF instead. (Similar to Probability Density Function pdf)
# Without an built-in function, you either google 
# or use this hack (if you know the range of values 

bins = np.linspace(0.5, 20.5, 21)
plt.hist(educ, bins, alpha=0.5, edgecolor='black', linewidth=1)
plt.xticks(np.arange(0,21, step=2))
plt.xlabel('Years of Education')
plt.ylabel('PMF / Frequency')
plt.show() 
filepath = os.path.join( dirpath, path2add ,'pmf_educ.png')
plt.savefig(filepath)
plt.show() 


#%% 
# Next plot it with 2 series by gender
# get two subsets for male and female separately##
##################  Fill in the code


#%%
# Here is the plot

bins = np.linspace(0.5, 20.5, 21)
plt.style.use('seaborn-deep')
plt.hist(educ_s1, bins, alpha=0.5, label='s1',edgecolor='black', linewidth=1)
plt.hist(educ_s2, bins, alpha=0.5, label='s2',edgecolor='black', linewidth=1)

plt.xticks(np.arange(0,21, step=2))
plt.xlabel('Years of Education')
plt.ylabel('Frequency')
plt.legend(loc='upper right')

plt.show() 

#%%
# easier to see 

bins = np.linspace(0.5, 20.5, 21)
plt.style.use('seaborn-deep')
plt.hist([educ_s1,educ_s2], bins, alpha=0.5, label=['s1','s2'],edgecolor='black', linewidth=1)

plt.xticks(np.arange(0,21, step=2))
plt.xlabel('Years of Education')
plt.ylabel('Frequency')
plt.legend(loc='upper right')

filepath = os.path.join( dirpath, path2add ,'hist_educ_gender.png')
plt.savefig(filepath)
plt.show() 

#%% [markdown]
# ## IMAGINE 
# How much it will be better if we had used our python skill and rename sex 1/2 to M/F  
# Same for others such as industry, etc.
# On the other hand, it's much easier with the current libraries and setup to leave them 
# in numerical form to perform machine learning... 

#%%
# Let us try some different plots
# But first, get some better idea of the dataframe
gssc.describe()

#%% 
# Let us get a box plot of age for the subset degree == 1 ( or 2 and 3 and 4)
# model from https://matplotlib.org/3.1.1/gallery/statistics/boxplot_demo.html
# import matplotlib.pyplot as plt
# import numpy as np
from matplotlib.patches import Polygon

subDegree1 = gssc[ gssc['degree']==1 ]

# create a 2x3 subplot areas for contrasts
fig, axs = plt.subplots(2, 3) 

# basic plot
axs[0, 0].boxplot(subDegree1['age'])
axs[0, 0].set_title('basic plot')

# notched plot
axs[0, 1].boxplot(subDegree1['age'], 1)
axs[0, 1].set_title('notched plot')

# change outlier point symbols
axs[0, 2].boxplot(subDegree1['age'], 0, 'gD')
axs[0, 2].set_title('change outlier\npoint symbols')

# don't show outlier points
axs[1, 0].boxplot(subDegree1['age'], 0, '')
axs[1, 0].set_title("don't show\noutlier points")

# horizontal boxes
axs[1, 1].boxplot(subDegree1['age'], 0, 'rs', 0)
axs[1, 1].set_title('horizontal boxes')

# change whisker length
axs[1, 2].boxplot(subDegree1['age'], 0, 'rs', 0, 0.75)
axs[1, 2].set_title('change whisker length')

fig.subplots_adjust(left=0.08, right=0.98, bottom=0.05, top=0.9, hspace=0.4, wspace=0.3)

# Next plot multiple boxplots on one Axes
subDegree2 = gssc[ gssc['degree']==2 ]
subDegree3 = gssc[ gssc['degree']==3 ]
subDegree4 = gssc[ gssc['degree']==4 ]

# Multiple box plots on one Axes
fig, ax = plt.subplots()
data = [ subDegree1['age'], subDegree2['age'], subDegree3['age'], subDegree4['age'] ]
plt.boxplot(data)
plt.xlabel('Degree (code)')
plt.ylabel('Age')

filepath = os.path.join( dirpath, path2add ,'boxplot_age_degree.png')
# plt.savefig(filepath)
plt.show()

#%%
# Let us also try a violinplot, similar to boxplot
# fig, axes = plt.subplots()

plt.violinplot( [ list(subDegree1['age']), list(subDegree2['age']), list(subDegree3['age']), list(subDegree4['age'])] , positions = [1,2,3,4] )
plt.xticks(np.arange(0,5))
plt.xlabel('Degree (code)')
plt.ylabel('Age')


filepath = os.path.join( dirpath, path2add ,'violin_age_degree.png')
# plt.savefig(filepath)
plt.show()


#%%
# One more plot - scatterplot
# income (respondent) vs age

plt.plot(gssc.age, gssc.rincome, 'o')
plt.ylabel('Respondent income')
plt.xlabel('Age')
plt.show()

# Doesn't really work

#%%
# subset
weThePeople = gssc[ gssc['rincome'] < 80 ]
weThePeople.shape
weThePeople.describe()

#%%
plt.plot(weThePeople.age, weThePeople.rincome, 'o')
plt.ylabel('Respondent income monthly? ($1k)')
plt.xlabel('Age')
plt.show()

#%%
# Change alpha value
plt.plot(weThePeople.age, weThePeople.rincome, 'o', alpha = 0.1)
plt.ylabel('Respondent income monthly? ($1k)')
plt.xlabel('Age')
plt.show()

#%%
# Change marker size 
plt.plot(weThePeople.age, weThePeople.rincome, 'o', markersize=3, alpha = 0.1)
plt.ylabel('Respondent income monthly? ($1k)')
plt.xlabel('Age')
plt.show()

#%%
# Add jittering 
fuzzyincome = weThePeople.rincome + np.random.normal(0,2, size=len(weThePeople.rincome))
plt.plot(weThePeople.age, fuzzyincome, 'o', markersize=3, alpha = 0.1)
plt.ylabel('Respondent income monthly? ($1k)')
plt.xlabel('Age')
plt.show()

#%%
# Add jittering to x as well
fuzzyage = weThePeople.age + np.random.normal(0,1, size=len(weThePeople.age))
plt.plot(fuzzyage, fuzzyincome, 'o', markersize=3, alpha = 0.1)
plt.ylabel('Respondent income monthly? ($1k)')
plt.xlabel('Age')
plt.show()

filepath = os.path.join( dirpath, path2add ,'scatter_income_age.png')
plt.savefig(filepath)
plt.show()




#%%
# HW
# Go to http://gss.norc.org
# Download a dataset of your choice. 
# You need to have at least 25 variables/features, 
# at least 8 of them quantitative, and 8 of them categorical 
# (although most categorical data are stored as numeric codes, they 
# are still categorical)
# download the data set for at least 10 years of data
# in either excel of stata format
# clean the data like what we did above, 
# find some relevant and interesting variables and
# make some plots.
# At least one histogram, one multiple-boxplot, one multi-violin plot, and the scattered plots that we had in class, with increasing sophistication. 