# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'

#%% [markdown]
#
# # Week06 HW
# ## By: xxx
# ### Date: xxxxxxx
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
# filepath = "/Users/edwinlo/GDrive_GWU/github_elo/GWU_classes_p/DATS_6103_DataMining/Class04_OOP/AAPL_20140912_20190912_daily_eod_vol.csv"
import os
import numpy as np
import pandas as pd

# os.chdir('../Class06_Pandas')  
# sometime when I opened the workspace from another folder, the working directory getcwd() 
# will be in the wrong place. You can change it with chdir()
filepath = os.path.join( os.getcwd(), "AAPL_20140912_20190912_daily_eod_vol.csv")
dfaapl = pd.read_csv(filepath, index_col=0 )  # use date as index

dfChkBasics(dfaapl)

# ######  QUESTION 1      QUESTION 1      QUESTION 1   ##########

# What are the variables in the df? 
# What are the data types for these variables?

# ######  END of QUESTION 1    ###   END of QUESTION 1   ##########

#%%
# You can access pd dataframe columns using the dot notation as well as using column names
print(dfaapl.price, '\n')
# same as 
print(dfaapl['price'])


#%% 
# Step 1
# Create the Stock class 
# 

class Stock:
  """
  Stock class of a publicly traded stock on a major market
  """
  def __init__(self, symbol, name, init_filepath) :
    """
    :param symbol: stock symbol
    :param name: company name
    :param init_filepath: locate the file for date, price (eod) and volume lists
    """
    # note that the complete list of properties/attributes below has more than items than 
    # the numnber of arguments of the constructor. That's perfectly fine. 
    # Some property values are to be assigned later after instantiation.
    self.symbol = symbol.upper()
    self.name = name
    self.data = self.import_history(init_filepath) # this is the pandas df, make sure import_history() returns a pd dataframe
    # the pandas df self.data will have columns price, volume, delta1, delta2, and index is date
    self.init_delta1() # Calculate the daily change values from stock price itself, append to df
    self.init_delta2() # Calculate the daily values second derivative, append to df
    self.firstdate = self.data.index[-1] 
    self.lastdate = self.data.index[0] 
  
  def import_history(self, filepath):
    """
    import stock history from csv file, with colunms date, eod_price, volume, and save them to data as pd.dataframe
    """
    return pd.read_csv( filepath, index_col=0 )  # use date as index
  
  def init_delta1(self):
    """
    compute the daily change from price_eod, append to data as new column as delta1
    """
    # notice that:
    # aapl['price'] returns a pandas series
    # aapl[['price']] returns a pandas dataframe
    # aapl['price'].values returns a numpy array of the values only

    self.data['delta1'] = 0  # initialize a new column with 0s
    self.data['delta1'] = self.data['price'][0:-1] - self.data.price.values[1:]   # self.data['price'] is same as self.price for df
    # the first term on the right is the full pd series with index attached. Second one is a simple numpy array without the date 
    # index. That way, the broadcasting will not try to match the indices/indexes on the two df
    return # you can choose to return self
  
  def init_delta2(self):
    """
    compute the daily change for the entire list of delta1, essentially the second derivatives for price_eod
    """
    # essentially the same function as init_delta1.

    # ######  QUESTION 2      QUESTION 2      QUESTION 2   ##########

    # write your codes here
    
    # ######  END of QUESTION 2    ###   END of QUESTION 2   ##########

    return # you can choose to return self


  def add_newday(self, newdate, newprice, newvolume):
    """
    add a new data point at the beginning of data df
    """
    # Make plans 
    # insert a new row to self.data with 
    # (date, price, volume, delta1, delta2) to the pandas df, 
    # and also should update self.lastdate
    #

    # update self.lastdate 
    # ######  QUESTION 3      QUESTION 3      QUESTION 3   ##########

    # write your codes here, should be just one line
    
    # ######  END of QUESTION 3    ###   END of QUESTION 3   ##########

    # get ready a new row, in the form of a pandas dataframe.
    # Pandas dataframe does not have an insert function. The usual method is to use .append() 
    # and .append() is most efficient to append a df to another df of the same columns.
    newRow = self.setNewRow(newdate, newprice, newvolume) # we do this quite a lot: assume it's done already, then implement it later, as long as it doesn't break the codes
    # need this function setNewRow() to return a dataframe

    self.data = newRow.append(self.data) # this will put the new row on top, and push self.data after the new data

    return self

  
  def setNewRow(self, newdate, newprice, newvolume):
    df = self.data.iloc[[0]].copy() # first create a true copy of the first row
    # use iloc[[0]] to create a dataframe, instead of iloc[0,:] which results in a Pandas.Series
    # then put in the new values
    # df.index[0] = newdate # doesn't work. Pandas index is immutable.
    df.index = [ newdate ] # Can change the entire series of index however.
    df.price[0] = newprice
    # ######  QUESTION 4      QUESTION 4      QUESTION 4   ##########

    # write your codes here
    # set volume value
    # set delta1 value
    # set delta2 value
    
    # ######  END of QUESTION 4    ###   END of QUESTION 4   ##########
    return df  # return the dataframe with one one row of data
  
  def nday_change_percent(self,n):
    """
    calculate the percentage change in the last n days, returning a percentage between 0 and 100
    """
    # ######  QUESTION 5      QUESTION 5      QUESTION 5   ##########

    # change = ??
    # percent = ??
    
    # ######  END of QUESTION 5    ###   END of QUESTION 5   ##########
    print(self.symbol,": Percent change in",n,"days is {0:.2f}".format(percent))
    return percent
  

  def nday_max_price(self,n):
    """
    find the highest price within the last n days 
    """
    # ######  QUESTION 6      QUESTION 6      QUESTION 6   ##########

    # return ??  # you can try to use the .max() function of a pandas dataframe
    
    # ######  END of QUESTION 6    ###   END of QUESTION 6   ##########

  def nday_min_price(self,n):
    """
    find the lowest price within the last n days 
    """
    # ######  QUESTION 7      QUESTION 7      QUESTION 7   ##########

    # return ?? 
    
    # ######  END of QUESTION 7    ###   END of QUESTION 7   ##########

#%%
# Try these:
filepath = os.path.join( os.getcwd(), 'AAPL_20140912_20190912_daily_eod_vol.csv')
aapl = Stock('AAPL','Apple Inc',filepath)
aapl.data.head()
aapl.data.tail()

# ######  QUESTION 8      QUESTION 8      QUESTION 8   ##########

aapl.nday_max_price(333) # record the answer here
aapl.nday_min_price(500) # record the answer here
aapl.nday_change_percent(500)  # record the answer here

aapl.add_newday('1/1/11',1,1234)
aapl.data.head()

# ######  END of QUESTION 8    ###   END of QUESTION 8   ##########


