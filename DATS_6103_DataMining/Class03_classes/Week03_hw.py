# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'

#%% [markdown]
#
# # Week03 HW
# ## By: xxx
# ### Date: xxxxxxx
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
    self.symbol = symbol.upper()
    self.name = name
    self.firstdate = firstdate
    self.lastdate = lastdate
    # below can be started with empty lists, then read in data file and calculate the rest
    self.price_eod = []
    self.volumes = []
    self.dates = [] # starts from the latest/newest date, 
    self.delta1 = [] # daily change values, the previous close minus today's close, example eod[0] - eod[1], eod[1] - eod[2]
    self.delta2 = [] 
    # change of the daily change values (second derivative, acceleration), 
    # given by, for the first entry, (delta1[0] - delta[1]), 
    # or if we want to, equals to (eod[0]-eod[1]) - (eod[1]-eod[2]) = eod[0] - 2*eod[1] + eod[2]
    self.import_history(init_filepath)
    self.compute_delta1_list()
    self.compute_delta2_list() # NEW_NEW_NEW (forgot to include this before, although it does not affect the results)
  
  def import_history(self, filepath):
    """
    import stock history from csv file, with colunms date, eod_price, volume, and save them to the lists 
    """
    with open(filepath,'r') as fh: # leaving the filehandle inside the "with" clause will close it properly when done. Otherwise, remember to close it when finished
      for aline in fh.readlines(): # readlines creates a list of elements; each element is a line in the txt file, with an ending line return character. 
        #  ######   QUESTION 1    ######   QUESTION 1    ######   QUESTION 1    ######   QUESTION 1    ######  
        # Fill in the codes here to put the right info in the lists self.dates, self.price_eod, self.volumes  
        #  ######  END QUESTION 1 ######  END QUESTION 1 ######  END QUESTION 1 ######  END QUESTION 1 ######  

    # fh.close() # close the file handle when done if it was not inside the "with" clause
    # print('fh closed:',fh.closed) # will print out confirmation  fh closed: True
    return self
  
  def compute_delta1_list(self):
    """
    compute the daily change for the entire list of price_eod 
    """
    #  ######   QUESTION 2    ######   QUESTION 2    ######   QUESTION 2    ######   QUESTION 2    ######  
    # Fill in the codes here 
    # Need to find the daily changes and save it to the list self.delta1
    # You might find it easier to use the map() function, although you are free to use any method
    # If you are using map(), you will be making a copy of self.price_eod to work with, and pop() the first element. 
    # Becareful whether you are making a shallow copy or deep copy. 
    # At the end, you might consider printing out the first few values of the delta1 list to inspect
    #  ######  END QUESTION 2 ######  END QUESTION 2 ######  END QUESTION 2 ######  END QUESTION 2 ######  

    return self
  
  def compute_delta2_list(self):
    """
    compute the daily change for the entire list of delta1, essentially the second derivatives for price_eod
    """
    #  ######   QUESTION 3    ######   QUESTION 3    ######   QUESTION 3    ######   QUESTION 3    ######  
    # Fill in the codes here 
    # Need to find the daily changes of the daily change, and save it to the list self.delta2
    # It is the second derivative, the acceleration (or deceleration if negative) of the stock momentum.
    # Essentially the same as compute_delta1_list, just on a different list 
    # Again you might want to print out the first few values of the delta2 list to inspect
    #  ######  END QUESTION 3 ######  END QUESTION 3 ######  END QUESTION 3 ######  END QUESTION 3 ######  

    return self
  
  def add_newday(self, newdate, newprice):
    """
    add a new data point at the beginning of lists
    """
    #  ######   QUESTION 4    ######   QUESTION 4    ######   QUESTION 4    ######   QUESTION 4    ######  
    # NEW_NEW_NEW (After initializing the stock with the historical price info, 
    # we will need to perform daily updates on the price. This method is to be performed 
    # daily (cron-job for example) to add the day price to the head of the price_eod list. 
    # In the process, we will also need to insert the corresponding delta1 and delta2 values 
    # to the head of those lists too.)
    #
    # Fill in the codes here 
    #
    # insert new price data to price_eod
    # calculate and insert new data to delta1
    # calculate and insert new data to delta2
    # insert newdate to dates[]
    #
    #  ######  END QUESTION 4 ######  END QUESTION 4 ######  END QUESTION 4 ######  END QUESTION 4 ######  
    return self
  
  def nday_change_percent(self,n):
    """
    calculate the percentage change in the last n days, returning a percentage between 0 and 100
    """
    #  ######   QUESTION 5    ######   QUESTION 5    ######   QUESTION 5    ######   QUESTION 5    ######  
    # Fill in the codes here 
    #
    change = 0 # change to the correct calculation
    percent = 0 # change to the correct calculation
    #
    #  ######  END QUESTION 5 ######  END QUESTION 5 ######  END QUESTION 5 ######  END QUESTION 5 ######  
    print(self.symbol,": Percent change in",n,"days is {0:.2f}".format(percent))
    return percent
    
  

#%%
import os

# dirpath = os.getcwd() # print("current directory is : " + dirpath)
# filepath = dirpath+'/GWU_classes_p/DATS_6103_DataMining/Class03_classes/AAPL_20140912_20190912_daily_eod_vol.csv' # lastdate is 9/12/19, firstdate is 9/12/14, 
# NEW_NEW_NEW (this should have gap the difference between mac/pc/platform issues how folders recorded, backslash/forward-slash/etc)
filepath = os.path.join( os.getcwd(), 'GWU_classes/DATS_6103_DataMining/Class03_classes/AAPL_20140912_20190912_daily_eod_vol.csv')
aapl = Stock('AAPL','Apple Inc','9/12/14','9/12/19',filepath)
#  ######   QUESTION 6    ######   QUESTION 6    ######   QUESTION 6    ######   QUESTION 6    ######  
#
# You can now also instantiate MSFT and GOOG from the csv files you found on github 
# Next you can try to run the functions/methods such as nday_change_percent on these stocks
# Do not use the add_newday yet, so that we can have a clean start for the next object 
#
#  ######  END QUESTION 6 ######  END QUESTION 6 ######  END QUESTION 6 ######  END QUESTION 6 ######  


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
    # below can be started with empty lists and dictionary, then update and compute the rest later
    self.stocks = {} # a dictionary in the format { 'AAPL': aaplStockObject, 'MSFT': msftStockObject, 'GOOG': googStockObject }
    self.index_eod = []
    self.index_delta1 = []
    self.index_delta1 = []
  
  def add_stock(self, stock):
    """
    add a stock (Stock class) to the list/dict self.stocks
    :param stock: a Stock class instance
    """
    #  ######   QUESTION 7    ######   QUESTION 7    ######   QUESTION 7    ######   QUESTION 7    ######  
    # Fill in the codes here 
    #
    # if the stock given, say aapl, where the symbol aapl.symbol is not yet in the self.stocks dictionary, 
    # then insert the pair  aapl.symbol : aapl  into self.stocks dictionary
    # otherwise, no need to insert
    # 
    # NEW_NEW_NEW eventually as you'll see, the add_stock method will be called like this: 
    # largeCapTech.add_stock(aapl) 
    # since aapl already exists, and has all the info we need. You will therefore need 
    # to use the stock symbol as the key to save it in the self.stocks dictionary 
    # so that the dictionary will then have { "AAPL": aapl } in there.
    #
    #  ######  END QUESTION 7 ######  END QUESTION 7 ######  END QUESTION 7 ######  END QUESTION 7 ######  
 
    # other tasks to be done later
    # to-be-implemented: some rules to overwrite firstdate and lastdate if the new stock has dates different from current records
    # to-be-implemented: updates the daily_index_eod values
    return self
  
  def del_stock(self, stocksymbol):
    """
    remove a stock (Stock class) from the list/dict self.stocks
    """
    #  ######   QUESTION 8    ######   QUESTION 8    ######   QUESTION 8    ######   QUESTION 8    ######  
    # Fill in the codes here 
    #
    # if the stocksymbol is in self.stocks, then remove it. 
    # print out some informative line in the process whether it is successful or not
    #
    #  ######  END QUESTION 8 ######  END QUESTION 8 ######  END QUESTION 8 ######  END QUESTION 8 ######      
    return self
  
  def compute_day_index(self):
    """
    with daily price update from the stock stocks, need to update the etf index value as well
    """
    # NEW_NEW_NEW (nothing to do here. Just a placeholder for future projects)
    # to-be-implemented: 
    # update index_eod
    # update index_delta1
    # update index_delta2
    return self

  def compute_day_index_list(self):
    """
    with new stock added or removed, it will be needed to update the eod_index values and the derivatives. 
    """
    # NEW_NEW_NEW (nothing to do here. Just a placeholder for future projects)
    # to-be-implemented: 
    # update index_eod
    # update index_delta1
    # update index_delta2
    return self

#%%
largeCapTech = ETF('QQQ','Large Cap Tech','9/12/14','9/12/19')
largeCapTech.add_stock(goog)
print(len(largeCapTech.stocks))

#  ######   QUESTION 9    ######   QUESTION 9    ######   QUESTION 9    ######   QUESTION 9    ######  
#
# continue to add msft and aapl to the largeCapTech ETF 
# check the length at the end to make sure it is 3
#
#  ######  END QUESTION 9 ######  END QUESTION 9 ######  END QUESTION 9 ######  END QUESTION 9 ######  

#%%
#  ######   QUESTION 10    ######   QUESTION 10    ######   QUESTION 10    ######   QUESTION 10    ######  
#
# Which stock (out of the three) perform best in the last 
# (i) 50 days
# (ii) 200 days (about 1 year)
# (iii) 600 days (about 3 years)
# NEW_NEW_NEW (use the nday_change_percent method that you defined)
#
#  ######  END QUESTION 10 ######  END QUESTION 10 ######  END QUESTION 10 ######  END QUESTION 10 ######  


#%%
# 
#  ######   QUESTION 11    ######   QUESTION 11    ######   QUESTION 11    ######   QUESTION 11    ######  
#
# So now, the largeCapTech basket has all the info of its stocks stock historical stock prices.
# When you change the stock aapl now, using the add_newday() function, does it automatically change the content of the largeCapTech?
# In other words, when we created the ETF largeCapTech, did we create a shallow copy of aapl or a deep copy to store it in largeCapTech?
# Make a guess first, then try.
# So is it shallow or deep? Is that what we want?
# NEW_NEW_NEW (after you use add_newday() method to change, say aapl price_eod, 
# you can verify the change with aapl.price_eod[0]
# Now see if largeCapTech.stocks['AAPL'].price_eod[0] is the old value or the new value. 
# We do not want to change the daily values in aapl and largeCapTech.stocks['AAPL'] separately. 
# We should update once, then all should be changed.)
#
#  ######  END QUESTION 11 ######  END QUESTION 11 ######  END QUESTION 11 ######  END QUESTION 11 ######  


#%%

