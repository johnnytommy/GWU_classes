# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'

#%%
import os
import pip
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from bokeh._testing.plugins import selenium
os.chdir('../Class07_Preprocess')  
# sometime when I opened the workspace from another folder, the 
# working directory getcwd() will be in the wrong place. 
# You can change it with chdir()
dirpath = os.getcwd() # print("current directory is : " + dirpath)
filepath = os.path.join( dirpath, 'HappyPeople.csv')
df = pd.read_csv(filepath)  

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
