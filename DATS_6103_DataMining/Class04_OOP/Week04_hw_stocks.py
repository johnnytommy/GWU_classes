# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'

#%% [markdown]
#
# # Week03 HW
# ## By: Johnny Thomas
# ### Date: 2/16/2020
#

#%% [markdown]
# Let us try to put together our idea of getting some useful stock market data for future data analysis.
#
# We will first take one stock, pull in the basic and free data from online, store it into a Stock class object. 
# Next, derive some useful numbers out of it.
# We are focusing on the data collection and basic manipulation part here, storing the info in an convenient object form.
# 
# When that is done, we will elevate the stock object into a basket of stocks (called electronic trading fund-ETF).
# Step by step, we will build it from the ground up.
# 
# Fill in the steps below to make everything functional as instructed

#%%
# Step 0, try reading the data file to make sure it works.
# Run this cell as is. If you see some output in the interactive python window, then it is 
# working. If not, you might need to fix the file path accordingly for your OS/platform.
# filepath = "/Users/edwinlo/GDrive_GWU/github_elo/GWU_classes_p/DATS_6103_DataMining/Class04_OOP/AAPL_20140912_20190912_daily_eod_vol.csv"
import os
appl_date = []
appl_price_eod = []
filepath = os.path.join( os.getcwd(), "AAPL_20140912_20190912_daily_eod_vol.csv")
fh = open(filepath) # fh stands for file handle
# data pulled from https://old.nasdaq.com/symbol/aapl/historical (5 years, csv format, 9/12/2019)   can also try  www.quandl.com/EOD
for aline in fh.readlines(): # readlines creates a list of elements; each element is a line in the txt file, with an ending line return character. 
  # this file gives "23.57" as the string, including the quotes
  tmp = aline.split(',')
  appl_date.append(tmp[0].strip())
  appl_price_eod.append(float(tmp[1]))
  
print(appl_date)
print(appl_price_eod)

#%% 
# Step 1
# Create a class for a stock with daily end-of-day price recorded, along with the daily volume.
# 

class Stock:
  """
  Stock class of a publicly traded stock on a major market
  """
  def __init__(self, symbol, name, firstdate, lastdate, init_filepath) :
    """
    :param symbol: stock symbol
    :param name: company name
    :param firstdate: the first date (end of list) of the price list
    :param lastdate: the last date (beginning of list) of the price list
    :param init_filepath: locate the file for date, price (eod) and volume lists
    """
    # note that the complete list of properties/attributes below has more than items than 
    # the numnber of arguments of the constructor. That's perfectly fine. 
    # Some property values are to be assigned later after instantiation.
    self.symbol = symbol.upper()
    self.name = name
    self.firstdate = firstdate
    self.lastdate = lastdate
    # below can be started with empty lists, then read in data file and calculate the rest
    self.price_eod = [] # record the end-of-day prices of the stock in a list. The 0-th position is the latest end-of-day price
    self.volumes = [] # a list recording the daily trading volumn
    self.dates = [] # starts from the latest/newest date, 
    self.delta1 = [] # daily change values, today's close price minus the previous close price. Example eod[0] - eod[1], eod[1] - eod[2], 
    self.delta2 = [] # daily change values, the previous close minus today's close, example eod[0] - eod[1], eod[1] - eod[2]
    # change of the daily change values (second derivative, acceleration), 
    # given by, for the first entry, (delta1[0] - delta[1]), 
    # or if we want to, equals to (eod[0]-eod[1]) - (eod[1]-eod[2]) = eod[0] - 2*eod[1] + eod[2]
    self.import_history(init_filepath)
    self.compute_delta1_list() # Calculate the daily change values from stock price itself.
    self.compute_delta2_list() # Calculate the daily values of whether the increase or decrease of the stock price is accelerating. A.k.a. the second derivative.
  
  def import_history(self, filepath):
    """
    import stock history from csv file, with colunms date, eod_price, volume, and save them to the lists 
    """
    with open(filepath,'r') as fh: # leaving the filehandle inside the "with" clause will close it properly when done. Otherwise, remember to close it when finished
      for aline in fh.readlines(): # readlines creates a list of elements; each element is a line in the txt file, with an ending line return character. 

        #  ######   QUESTION 1    ######   QUESTION 1    ######   QUESTION 1    ######   QUESTION 1    ######  
        # Fill in the codes here to put the right info in the lists self.dates, self.price_eod, self.volumes  
        # Should be similar to the codes in Step 0 above. 
        #  ######  END QUESTION 1 ######  END QUESTION 1 ######  END QUESTION 1 ######  END QUESTION 1 ######  


    # fh.close() # close the file handle when done if it was not inside the "with" clause
    # print('fh closed:',fh.closed) # will print out confirmation  fh closed: True
    return self
  
  def compute_delta1_list(self):
    """
    compute the daily change for the entire list of price_eod 
    """
    # goal: calculate the daily price change from the eod prices.
    # idea: 
    # 1. duplicate the eod list 
    # 2. shift this new list by removing the 0-th element. 
    # 3. use the map function to find a list of delta's by subtracting the eod list from this new list. 
    # Okay, let's try
    #
    # eod_shift1 = self.price_eod # THIS WILL NOT WORK. Try. A shallow copy. We'll talk more about that next class.
    eod_shift1 = self.price_eod.copy() # if you do not use the copy method here, you will get a shallow copy.
    # The list here is a simple list of floats, not list of lists or list of dictionaries. 
    # So the copy() function will work. No need for other "deepcopy" variations
    eod_shift1.pop(0) # remove the first element (shifting the day)
    self.delta1 = list(map(lambda x,y: x-y, self.price_eod, eod_shift1))
    print(self.name.upper(),": The latest 5 daily changes in delta1: ")
    for i in range(0,5): print(self.delta1[i]) # checking the first five values
    return self
  
  def compute_delta2_list(self):
    """
    compute the daily change for the entire list of delta1, essentially the second derivatives for price_eod
    """
    # essentially the same function as compute_delta1_list. With some hindsight, or when the codes are re-factored, we can properly combine them

    #  ######   QUESTION 2    ######   QUESTION 2    ######   QUESTION 2    ######   QUESTION 2    ######  
    eod_shift1 = self.price_eod.copy() 
    eod_shift1.pop(0) # remove the first element (shifting the day)
    self.delta2 = list(map(lambda x,y: x-y, self.price_eod, eod_shift1))
    print(self.name.upper(),": The latest 5 daily changes in delta2: ")
    for i in range(0,5): print(self.delta2[i]) # checking the first five values
    # Need to find the daily changes of the daily change, and save it to the list self.delta2
    # It is the second derivative, the acceleration (or deceleration if negative) of the stock momentum.
    # Essentially the same as compute_delta1_list, just on a different list 
    # Again you might want to print out the first few values of the delta2 list to inspect
    #  ######  END QUESTION 2 ######  END QUESTION 2 ######  END QUESTION 2 ######  END QUESTION 2 ######  

    return self
  
  def add_newday(self, newdate, newprice, newvolume):
    """
    add a new data point at the beginning of lists
    """
    #  ######   QUESTION 3    ######   QUESTION 3    ######   QUESTION 3    ######   QUESTION 3    ######  
    # After we have the batch of historical data to import, we 
    # most likely will need to do some daily updates (cron jobs, for example) 
    # going forward.  There is no need to re-import the old data. 
    # This method is then used to insert just one row of new data point daily. 
    # We will need to insert the new date, the new eod value, the new delta1 value, 
    # the new delta2 value, as well as the new volume data.
    #
    # insert new price data to price_eod
    # calculate and insert new data to delta1
    # calculate and insert new data to delta2
    # insert newdate to dates[]
    #
    # Fill in the codes here 
    #
    # insert newdate to dates[]
    self.dates.insert(?????????)
    # insert newvolume to volumes[]
    self.volumes.insert(?????????)
    # insert new eod data value to price_eod
    self.price_eod.insert(???????)
    # calculate and insert new data to delta1
    self.delta1.insert(????????)
    # calculate and insert new data to delta2
    self.delta2.insert(??????????)
    #
    #  ######  END QUESTION 3 ######  END QUESTION 3 ######  END QUESTION 3 ######  END QUESTION 3 ######  

    return self
  
  def nday_change_percent(self,n):
    """
    calculate the percentage change in the last n days, returning a percentage between 0 and 100
    """
    #  ######   QUESTION 4    ######   QUESTION 4    ######   QUESTION 4    ######   QUESTION 4    ######  
    change = ?????? # calculate the change of price between newest price and n days ago
    percent = ?????? # calculate the percent change (using the price n days ago as the base)
    print(self.symbol,": Percent change in",n,"days is {0:.2f}".format(percent))
    #  ######  END QUESTION 4 ######  END QUESTION 4 ######  END QUESTION 4 ######  END QUESTION 4 ######  

    return percent
    
  

#%%
import os

# dirpath = os.getcwd() # print("current directory is : " + dirpath)
# filepath = dirpath+'/AAPL_20140912_20190912_daily_eod_vol.csv' # lastdate is 9/12/19, firstdate is 9/12/14, 
# using os.path.join will take care of difference between 
# mac/pc/platform issues how folder paths are used, backslash/forward-slash/etc
filepath = os.path.join( os.getcwd(), 'AAPL_20140912_20190912_daily_eod_vol.csv')
aapl = Stock('AAPL','Apple Inc','9/12/14','9/12/19',filepath)

#%%
# Great! Now we can get the competitors easily
filepath = os.path.join( os.getcwd(), 'MSFT_20140912_20190912_daily_eod_vol.csv')
msft = Stock('MSFT','Microsoft Inc','9/12/14','9/12/19',filepath)

filepath = os.path.join( os.getcwd(), 'GOOG_20140912_20190912_daily_eod_vol.csv')
goog = Stock('GOOG','Alphabet Inc','9/12/14','9/12/19',filepath)


#%%
# Next step, create a class for a basket of stocks, called electronic trading fund ETF
# 

class ETF:
  """
  ETF class of a collection of Stocks in a similar/related sector
  """
  def __init__(self, name, sector, firstdate, lastdate) :
    self.name = name
    self.sector = sector
    self.firstdate = firstdate
    self.lastdate = lastdate
    # below can be started with empty lists, then update and compute the rest later
    self.stocks = {} # a dictionary in the format { 'AAPL': aaplStockObject, 'MSFT': msftStockObject, 'GOOG': googStockObject }
    self.index_eod = []  # The EFT is an index fund, which has an eod price as well, calculated from the basket of stocks.
    self.index_delta1 = []  # So we also need to calculate the daily changes delta1
    self.index_delta2 = []
  
  def add_stock(self, stock):
    """
    add a stock (Stock class) to the dict/list self.stocks
    :param stock: a Stock class instance
    """
    # check if already exist stock list
    if stock.symbol in self.stocks.keys():
      print("new stock symbol already exist in stock list (dict): ", stock.symbol)
      # return self # exit from the function

    # continue below if not exist/duplicate, add it to the dictionary
    self.stocks[stock.symbol] = stock
    # to-be-implemented: some rules to overwrite firstdate and lastdate if the new stock has dates different from current records
    # to-be-implemented: updates the daily_index_eod values

    return self
    
  
  def del_stock(self, stocksymbol):
    """
    remove a stock (Stock class) from the list self.stocks
    """
    #  ######   QUESTION 5    ######   QUESTION 5    ######   QUESTION 5    ######   QUESTION 5    ######  
    # Fill in the codes here 
    #
    # if the stocksymbol is in self.stocks, then remove it. 
    # print out some informative line in the process whether it is successful or not
    #
    #  ######  END QUESTION 5 ######  END QUESTION 5 ######  END QUESTION 5 ######  END QUESTION 5 ######      
    
    return self
  
  def compute_day_index(self):
    """
    with daily price update from the stock stocks, need to update the etf index value as well
    """
    # (nothing to do here. Just a placeholder for future projects)
    # to-be-implemented: 
    # update index_eod
    # update index_delta1
    # update index_delta2
    return self

  def compute_day_index_list(self):
    """
    with new stock added or removed, it will be needed to update the eod_index values and the derivatives. 
    """
    # (nothing to do here. Just a placeholder for future projects)
    # to-be-implemented: 
    # update index_eod
    # update index_delta1
    # update index_delta2
    return self

#%%
largeCapTech = ETF('QQQ','Large Cap Tech','9/12/14','9/12/19')
largeCapTech.add_stock(goog)
print(len(largeCapTech.stocks))

#  ######   QUESTION 6    ######   QUESTION 6    ######   QUESTION 6    ######   QUESTION 6    ######  
#
# continue to add msft and aapl to the largeCapTech ETF 
# check the length at the end to make sure it is 3
#
#  ######  END QUESTION 6 ######  END QUESTION 6 ######  END QUESTION 6 ######  END QUESTION 6 ######  

#%%
#  ######   QUESTION 7    ######   QUESTION 7    ######   QUESTION 7    ######   QUESTION 7    ######  
#
# Which stock (out of the three) perform best in the last 
# (i) 50 days
# (ii) 200 days (about 1 year)
# (iii) 600 days (about 3 years)
# NEW_NEW_NEW (use the nday_change_percent method that you defined)
#
#  ######  END QUESTION 7 ######  END QUESTION 7 ######  END QUESTION 7 ######  END QUESTION 7 ######  


#%%
# 
#  ######   QUESTION 8    ######   QUESTION 8    ######   QUESTION 8    ######   QUESTION 8    ######  
#
# So now, the largeCapTech basket has all the info of its stocks stock historical stock prices.
# When you change the stock aapl now, using the add_newday() function, does it automatically change the content of the largeCapTech?
# In other words, when we created the ETF largeCapTech, did we create a shallow copy of aapl or a deep copy to store it in largeCapTech?
# Make a guess first, then try.


aapl.add_newday('9/13/19',224)
print("aapl daily change position 0:" ,aapl.delta1[0])

print("aapl in largeCapTech, daily change position 0" ,largeCapTech.stocks[aapl.symbol].delta1[0])

# So is it shallow or deep copy? Is that what we want?
# Just type in your answer here as comments.
#

#  ######  END QUESTION 8 ######  END QUESTION 8 ######  END QUESTION 8 ######  END QUESTION 8 ######  


#%%

