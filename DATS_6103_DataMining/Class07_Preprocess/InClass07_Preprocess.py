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
path2add = 'GWU_classes/DATS_6103_DataMining/Class07_Preprocess'
filepath = os.path.join( dirpath, path2add ,'GSS_xlsx.csv')
df = pd.read_csv(filepath)  
# gss = pd.read_csv(filepath)  

#%%
# Standard quick checks
def dfChkBasics(dframe): 
  cnt = 1
  
  try:
    print(str(cnt)+': info(): ')
    cnt+=1
    print(dframe.info())
  except: pass

  print(str(cnt)+': describe(): ')
  cnt+=1
  print(dframe.describe())

  print(str(cnt)+': dtypes: ')
  cnt+=1
  print(dframe.dtypes)

  try:
    print(str(cnt)+': columns: ')
    cnt+=1
    print(dframe.columns)
  except: pass

  print(str(cnt)+': head() -- ')
  cnt+=1
  print(dframe.head())

  print(str(cnt)+': shape: ')
  cnt+=1
  print(dframe.shape)

  # print(str(cnt)+': columns.value_counts(): ')
  # cnt+=1
  # print(dframe.columns.value_counts())

def dfChkValueCnts(dframe):
  cnt = 1
  for i in dframe.columns :
      print(str(cnt)+':', i, 'value_counts(): ')
      print(dframe[i].value_counts())
      cnt +=1

#%%
dfChkBasics(df)
dfChkValueCnts(df)

#%%
# Look at one of the columns that should be numeric
print(df.childs.describe())
print(df.childs.value_counts())

#%%
try: df.childs = pd.to_numeric( df.childs )
# try: df.childs = pd.to_numeric( df.childs, errors='coerce' )
except: print("Cannot handle to_numeric for column: childs")
finally: print(df.childs.describe(), '\n', df.childs.value_counts(dropna=False))
# above doesn't work, since there are many strings there

# Okay, so "Dk na" and "Eight or more" are the bad ones we needa strategy for.
# Say set "Dk na" as NaN, and "Eight or more" as 8, 
# with the understanding that most of them are actually 8, a few 9 or 10 or ... 

#%%
# So try our plan, if it works, put it in the cleaning function, 
# so that if we have newer dataset with the same issues, it will 
# works like a charm
# df.childs.str.replace('Dk na', np.nan ) # default regex=False
df.childs = df.childs.map(lambda x: np.nan if x.strip()=='Dk na' else '8' if x.strip()=='Eight or more' else x )
print( df.childs.value_counts(dropna=False) )

#%%
# Alright, it worked. 
# Look one more time, is it int or object?
print(df.dtypes)
# still object, so try again
try: df.childs = pd.to_numeric( df.childs)
except: print("Cannot handle to_numeric for column: childs")
finally: print(df.childs.describe(), '\n', df.childs.value_counts(dropna=False))

# It works, now float64 (because NaN is not int64, it's considered float64, which is okay)

#%%
# Before we move on to clean other columns, this is what I would do: 
# implement cleaning function to complete the task, per row of data 
# What we did above was transforming a single column using the pandas to_numeric( ) funcction. 
# This is not always possible or desireable when df becomes huge. Also, what about you are adding new 
# data points to your df? No reason to apply the transform to the entire column.
# We would like to have a function to perform the cleaning, using .apply( function, axis=1 ) 
# and tranform one row at a time when needed. 
# 
#
# Let us try this on the age column, which is still an object/string
try: df.age = pd.to_numeric( df.age )
except: print("Cannot handle to_numeric for column: age")
finally: print(df.age.describe(), '\n', df.age.value_counts(dropna=False))

#%%
# So let us define our cleaning function to handle the values
def cleanDfAge(row):
  thisage = row["age"]
  try: thisage = int(thisage) # if it is string "36", now int
  except: pass
  
  try: 
    if not isinstance(thisage,int) : thisage = float(thisage)  # no change if already int, or if error when trying
  except: pass
  
  if ( isinstance(thisage,int) or isinstance(thisage,float) ) and not isinstance(thisage, bool): return ( thisage if thisage>=0 else np.nan )
  if isinstance(thisage, bool): return np.nan
  # else: # assume it's string from here onwards
  thisage = thisage.strip()
  if thisage == "No answer": return np.nan
  if thisage == "89 or older": 
    # strategy
    # let us just randomly distribute it, say according to chi-square, 
    # deg of freedom = 2 (see distribution) 
    # values peak at zero, most range from 0-5 or 6. Let's cap it 100
    thisage = min(89 + 2*np.random.chisquare(2) , 100)
    return thisage # leave it as decimal
  return np.nan # catch all, just in case
# end function cleanGssAge

#%%
# Now apply to df row-wise 
# Be mindful of one key point: 
# the .map() function was applied to df.childs or df['childs'], which is a pandas Series itself. 
# The .apply( ) function only works on pandas.DataFrame, not Series. 
# So we need to apply it to df.apply( ), or df[['some subsets']].apply( ), 
# not the single square bracket df[ ].apply( ), which result in a pandas series.
df['age'] = df.apply(cleanDfAge,axis=1)
# df[['age']] = df.apply(cleanDfAge,axis=1) # this works too
print(df.dtypes)
# all works as designed
#
# Next, we can get these individual functions for each column, 
# and in the end, can also combine them all into one dedicated function for this data source

#%%
# Let us take care of one more here: rincome (respondent income), which can be similary applied to family income etc
print(df.rincome.describe(), '\n', df.rincome.value_counts(dropna=False) )
print(df.income.describe(), '\n', df.income.value_counts(dropna=False) )
# Turns out the data is not as meaningful as we had hoped. 
# For rincome (respondent's income), most freq is NA, closely follow by $25k or more. 
# The next is only 1/7 of the frequency for $20k-$25k
# It is clear that the most important info to distinguish those above $25k is not recorded in the dataset. 
# The income (family income) is even more extreme, with no NA but almost twice of those with $25k or more. 
# Nonetheless, as a practice, let us devise a strategy to convert them into slightly more useful values.
# Option 1: spread out each group evenly (but randomized) within the income ranges. 
# Note that the income ranges are not of equal sizes, and the top bin with $25k or more needs some cutoff.
# Option 2: Instead of evenly, we can spread them out using normal pdf. The effect is quite 
# similar to add jittering. We still need to find some reasonable midpoint for the top range.
# Option 3: Replace by mid-points of the range. The top one with $25k or more, 
# we can try something like something like stretching out the age values above 89. 
# But with the majority of the data points in that range, our unsubstantiated choice 
# will affect the result too significantly. 
#
#%%
# I will use Option 1, but smooth out the top bin with chi-square like drop off (deg-of-freedom 2) 
# with the freq from $20-$25k going into $25k+ as smoothly as possible.
def cleanDfIncome(row, colname): # colname can be 'rincome', 'income' etc
  thisamt = row[colname]
  if (thisamt.strip() == "Don't know"): return np.nan
  if (thisamt.strip() == "Not applicable"): return np.nan
  if (thisamt.strip() == "Refused"): return np.nan 
  if (thisamt.strip() == "Lt $1000"): return np.random.uniform(0,999)
  if (thisamt.strip() == "$1000 to 2999"): return np.random.uniform(1000,2999)
  if (thisamt.strip() == "$3000 to 3999"): return np.random.uniform(3000,3999)
  if (thisamt.strip() == "$4000 to 4999"): return np.random.uniform(4000,4999)
  if (thisamt.strip() == "$5000 to 5999"): return np.random.uniform(5000,5999)
  if (thisamt.strip() == "$6000 to 6999"): return np.random.uniform(6000,6999)
  if (thisamt.strip() == "$7000 to 7999"): return np.random.uniform(7000,7999)
  if (thisamt.strip() == "$8000 to 9999"): return np.random.uniform(8000,9999)
  if (thisamt.strip() == "$10000 - 14999"): return np.random.uniform(10000,14999)
  if (thisamt.strip() == "$15000 - 19999"): return np.random.uniform(15000,19999)
  if (thisamt.strip() == "$20000 - 24999"): return np.random.uniform(20000,24999)
  if (thisamt.strip() == "$25000 or more"): return ( 25000 + 10000*np.random.chisquare(2) )
  return np.nan
# end function cleanDfIncome

#%%
# Now apply to df row-wise. 
# Here with two arguments in the function, we use this syntax
df['income'] = df.apply(cleanDfIncome, colname='income', axis=1)
df['rincome'] = df.apply(cleanDfIncome, colname='rincome', axis=1)
print(df.dtypes)
# all works as designed
#

#%%
# We are on a roll, let's also rewrite the Childs transform with a function

def cleanDfChilds(row):
  thechildren = row["childs"]
  try: thechildren = int(thechildren) # if it is string "6", now int
  except: pass
  
  try: 
    if not isinstance(thechildren,int) : thechildren = float(thechildren)  # no change if already int, or if error when trying
  except: pass
  
  if ( isinstance(thechildren,int) or isinstance(thechildren,float) ) and not isinstance(thechildren, bool): return ( thechildren if thechildren>=0 else np.nan )
  if isinstance(thechildren, bool): return np.nan
  # else: # assume it's string from here onwards
  thechildren = thechildren.strip()
  if thechildren == "Dk na": return np.nan
  if thechildren == "Eight or more": 
    thechildren = min(8 + np.random.chisquare(2) , 12)
    return thechildren # leave it as decimal
  return np.nan # catch all, just in case
# end function cleanDfChilds

df['childs'] = df.apply(cleanDfChilds, axis=1)
print(df.dtypes)

#%%
# Now try some plots
df.age.plot.hist()
plt.show()


#%%
# scatter plot
df.plot('age', 'rincome', kind='scatter', marker='o') # OR
# plt.plot(df.age, df.rincome, 'o') # if you put marker='o' here, you will get line plot?
plt.ylabel('Respondent income (annual?)')
plt.xlabel('Age')
plt.show()


#%%
# more adjustments
fuzzyage = df.age + np.random.normal(0,1, size=len(df.age))
# fuzzyrincome = df.rincome + np.random.normal(0,1, size=len(df.rincome))
plt.plot(fuzzyage, df.rincome, 'o', markersize=3, alpha = 0.1)
plt.ylabel('Respondent income (annual?)')
plt.xlabel('Age')
plt.show()


#%% [markdown]
# Let us now try a different dataset, already cleaned, and look at some basic data structure manipulation
# namely 
# 
# * pivot (long to wide format) 
# * pivot table (pivoting with aggregating functions) 
# * melt (wide to long format) 
# * unstack (a kind of pivot)  
# * stack (a kind of melt) 
 

#%%
# drop columns
# pivot (long to wide format)
# melt (wide to long format)
# unstack (a kind of pivot)
# stack (a kind of melt)
# gapminder example 

#%%
# First read in the gapminder dataset
# import os
dirpath = os.getcwd() # print("current directory is : " + dirpath)
path2add = 'GWU_classes_p/DATS_6103_DataMining/Class07_Preprocess'
filepath = os.path.join( dirpath, path2add ,'gapmindeR.csv')
dfgap = pd.read_csv(filepath, index_col="id")
dfChkBasics(dfgap)
dfChkValueCnts(dfgap)

#%%
# add contCode as numerical value 
contCodeList = list( dfgap.continent.unique() ) # contCodeList = ['Asia', 'Europe', 'Africa', 'Americas', 'Oceania']
dfgap['contCode']=pd.Categorical(dfgap.continent.apply( lambda x: contCodeList.index(x) ))
dfgap.head()

#%%
# First, make some plots and animation
# example following https://python-graph-gallery.com/341-python-gapminder-animation/
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# plt.style.use('classic')

# import os
# dirpath = os.getcwd() # print("current directory is : " + dirpath)
# path2add = 'GWU_classes_p/DATS_6103_DataMining/Class07_Preprocess'

# pick a year
theyear = dfgap.year.unique()[0]

def plotGap1yr(yr):
  # plot 
  # initialize a figure
  my_dpi=96
  # fig = plt.figure(figsize=(680/my_dpi, 480/my_dpi), dpi=my_dpi)
  
  data = dfgap[dfgap.year==yr]

  # Change color with c and alpha. I map the color to the X axis value.
  plt.scatter(data['lifeExp'], data['gdpPercap'] , s=data['pop']/200000 , c=data['contCode'].cat.codes, cmap="Accent", alpha=0.6, edgecolors="white", linewidth=2)
  # plt.scatter(data['lifeExp'], data['gdpPercap'] , s=data['pop']/200000 , c=data['contCode'], cmap="Accent", alpha=0.6, edgecolors="white", linewidth=2)
  
  # Add titles (main and on axis)
  plt.yscale('log')
  plt.xlabel("Life Expectancy")
  plt.ylabel("GDP per Capita")
  plt.title("Year: "+str(yr) )
  plt.ylim(0,100000)
  plt.xlim(30, 90)

  # Save it
  filepath = os.path.join( dirpath, path2add ,'Gapminder_step'+str(yr)+'.png')
  plt.savefig(filepath, dpi=96)
  plt.gca()

plotGap1yr(theyear)

#%%
# Now loop thru all the years and create the png files
for yr in dfgap.year.unique():
  plotGap1yr(yr)

#%% [markdown]
# ## OPTIONAL
# create animated gif  
# ### Run these in bash (shell)  
# On Mac, you can use homebrew  
# If homebrew not install,  
# /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
# Now install ImageMagick
# brew install ImageMagick
#
# Finally, use convert (change to folder of the png's)
# convert -delay 80 Gapminder*.png animated_gapminder.gif
#
#
# Now you can view the gif 
# either in a browser (drag and drop)
# or other image software
# or IPython interactive window if you follow some steps and imports...

#%%
# Now, let's really look at data structure and reshaping.
#
# Create one more column 
# dfgap['gdp'] = dfgap.gdpPercap * dfgap.pop     # doesn't work!
dfgap['gdp'] = dfgap['gdpPercap'] * dfgap['pop'] # works

# This describes pivot, pivot table, and stack/unstack pretty well.
# https://nikgrozev.com/2015/07/01/reshaping-in-pandas-pivot-pivot-table-stack-and-unstack-explained-with-pictures/
# 
# Melt is not described in the above, and it's the opposite of pivot.
# 
# This provide a slightly different presentation, with Melt included as well
# https://pandas.pydata.org/pandas-docs/stable/user_guide/reshaping.html 
# 
# In different contexts, these are studied under 
# indexing and primary/secondary keys, 
# or group_by functions and aggregates
# 
# Think of the datasets that you used before. 
# What were the circumstances you could use these re-shaping?
# 

#%%
# pivot and pivot_table on gapminder
dfgap_pvt = dfgap.pivot(index='year', columns='country' , values='gdpPercap')
dfChkBasics(dfgap_pvt)
# dfChkValueCnts(dfgap_pv1)
#
# What is the shape of this df?
# What are the convenient things to work with this df?
# What are the cons with this structure?


#%%
# pivot gapminder, multi values
dfgap_pv2 = dfgap.pivot(index='year', columns='country' , values=['lifeExp','gdpPercap'])
dfChkBasics(dfgap_pv2)
# dfChkValueCnts(dfgap_pv2)
#
# What is the shape of this df?
# What are the convenient things to work with this df?
# What are the cons with this structure?

#%%
# The columns now are multi-indexed !!
#
print(dfgap_pv2['lifeExp'])   # OR  print(dfgap_pv2.lifeExp) 

# print(dfgap_pv2['lifeExp'].mean()) # OR
print(dfgap_pv2.lifeExp.mean()) # default axis = 0 (column-wise).  This gives you the mean for each column or country

# print(dfgap_pv2['lifeExp'].mean(axis=1)) # OR
print(dfgap_pv2.lifeExp.mean(axis=1)) # This gives you the mean for each year of all countries
#
#
# There are different ways you can pull info from this structure
# print(dfgap_pv2['lifeExp']['Spain'])  # OR
print(dfgap_pv2.lifeExp.Spain)        # column primary key, then 2nd key, list of Spain all years
print(dfgap_pv2.lifeExp.Spain[1952])  # value for Spain with single row index
print(dfgap_pv2.lifeExp.loc[1952,:])     # 1952 row index, all countries info on lifeExp
#
#
# You can see how easy it is to perform group_by or filtering/subsetting with the column multi-indexing here, if well chosen to fit your needs.

#%%
# last try on multi values
dfgap_pvall = dfgap.pivot(index='year', columns='country')
dfChkBasics(dfgap_pvall)
# dfChkValueCnts(dfgap_pvall)
#
# What is the shape of this df? (SUPER WIDE)


#%% [markdown]
# next try multiple columns, instead of multiple values
# dfgap_pc2 = dfgap.pivot(index='year', columns=['continent','country'] , values='gdpPercap')
# above doesn't work, but the next line works.  
# dfgap_pc2 = dfgap.pivot_table(index='year', columns=['continent','country'] , values='gdpPercap')
#
# Overall, the difference between pivot and pivot_table in pandas are these:  
#
# * pivot_table generalize pivot, can handle duplicate values for one pivoted index/column pair.
# * pivot_table allows aggreate functions with "aggfunc="
# * pivot_table allows multi-index (on rows)
# * pivot allows "values=" with numeric or string types. pivot_table only allow numeric (with str or categorical columns ignored)

#%% 
# so here it is, multiple columns, instead of multiple values
dfgap_pc2 = dfgap.pivot_table(index='year', columns=['continent','country'] , values='gdpPercap')
dfChkBasics(dfgap_pc2)
# dfChkValueCnts(dfgap_pc2)
#
# What is the shape of this df?
# What are the convenient things to work with this df?
# What are the cons with this structure?

#%%
dfgap_pv2b = dfgap.pivot(index='year', columns='country' , values=['continent','gdpPercap'])
dfChkBasics(dfgap_pv2b)
# dfChkValueCnts(dfgap_pv2b)
#
# Can you tell the difference between the pc2 (pivot_table with continent in the colunms) and the pv2b (pivot, with continent in the values)?  
# When is it more useful for these two different structures?

#%%
# in this case, it is actually more convenient and sensible to index by the country. 
# The previous examples simply exaggerate the pivot tables are usually "WIDE"
dfgap_ptCountryGdpp = dfgap.pivot_table(index='country', columns=['continent','year'] , values=['pop','gdpPercap'])
dfChkBasics(dfgap_ptCountryGdpp)

#%%
# Again, you can do filtering and selections like this:
# dfgap_ptCountryGdpp['gdpPercap']['Oceania'][1967] # same as 
dfgap_ptCountryGdpp.gdpPercap.Africa[1967]
# OR 
dfgap_ptCountryGdpp[ ('gdpPercap','Africa',1967) ]  # Using a tuple for selecting multi-Index (in the columns)


#%%
# next try multiple indexes, 
dfgap_pi2 = dfgap.pivot_table(index=['continent','country'], columns='year' , values=['pop','gdpPercap'])
dfChkBasics(dfgap_pi2)
# dfChkValueCnts(dfgap_pi2)
#
# Without running the code, can you tell what is the shape of this df?

#%%
# Stack: Opposite to pivot
dfgap_sptpi2 = dfgap_pi2.stack()
dfChkBasics(dfgap_sptpi2)
dfgap_pi2.head()

#%%
# Stack: Opposite to pivot
dfgap_sptCountryGdpp = dfgap_ptCountryGdpp.stack()
dfChkBasics(dfgap_sptCountryGdpp)
dfgap_ptCountryGdpp.head()

#%% [markdown]
# # Stack ~ Melt
# Melt is similar to stack, resulting in a long dataframe
# melt however does not preserve the custom index colummns!!
dfgap_mpi2 = dfgap_pi2.melt()
dfChkBasics(dfgap_mpi2)

#%% 
# need to do something like this instead
dfgap_pi2_defaultIndex = dfgap_pi2.reset_index() # reset the index from (continent,country) to default
dfgap_mpi2 = dfgap_pi2_defaultIndex.melt(id_vars=['continent','country'])
dfChkBasics(dfgap_mpi2)


#%%
# Finally, unstack is like pivot/pivot_table, which will be opposite to Stack/Melt



#%% [markdown]
# Roughly speaking:  
# long format (melt/stack) is good for data analysis of the raw data
# wide format (pivot/unstack) is goof for summary, aggregates, and presentation













#%%
