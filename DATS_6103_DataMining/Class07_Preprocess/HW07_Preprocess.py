# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'

#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#
# https://gssdataexplorer.norc.org 
# create an account
# create a project
# select these eight variables: ballot, id, year, hrs1 (hours worked last week), marital, childs, income, happy, 
# (use the search function to find them if needed.)
# add the variables to cart 
# extract data 
# name your extract
# add all the 8 variables to the extract
# Choose output option, select only years 2000 - 2018 
# file format Excel Workbook (data + metadata)
# create extract
# It will take some time to process. 
# When it is ready, click on the download button. 
# you will get a .tar file
# if your system cannot unzip it, google it. (Windows can use 7zip utility. Mac should have it (tar function) built-in.)
# rename file from GSS to HappyPeople
# Open in excel (or other comparable software), then save it as csv
# So now you have HappyPeople.csv to work with
#
# When we import using pandas, we need to do pre-processing like what we did in class
# So clean up the columns. You can use some of the functions we defined in class, like the total family income, and number of children. 
# Other ones like worked hour last week, etc, you'll need a new function. 
# Happy: change it to numeric codes (ordinal variable)
# Ballot: just call it a, b, or c 
# Marital status, it's up to you whether you want to rename the values. 
#
# After the preprocessing, make these plots
# Box plot for hours worked last week, for the different marital status. (So x is marital status, and y is hours worked.) 
# Violin plot for income vs happiness 
# Use happiness as numeric, make scatterplot with jittering in both x and y between happiness and number of children. 
# If you have somewhat of a belief that happiness is caused/determined/affected by number of children, or the other 
# way around (having babies/children are caused/determined/affected by happiness), then put the dependent 
# variable in y, and briefly explain your choice.


#%% [markdown]
import os
os.chdir('../Class07_Preprocess')  
# sometime when I opened the workspace from another folder, the 
# working directory getcwd() will be in the wrong place. 
# You can change it with chdir()
dirpath = os.getcwd() # print("current directory is : " + dirpath)
filepath = os.path.join( dirpath ,'HappyPeople.csv')
df = pd.read_csv(filepath)  
 




#%%
