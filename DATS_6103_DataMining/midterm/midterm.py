# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'


#%% [markdown]
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
os.chdir('../midterm')  
dirpath = os.getcwd() 
filepath = os.path.join( dirpath ,'Pizza.csv')
pizza = pd.read_csv(filepath, index_col="id")


#%%
# QUESTION 01   xxxxxxx
# Violin plots
#
# From the pizza dataframe, make violin plots of the variable carb with brands A-C combined 
# into one group, brands D-F in one group, and G-J into the last group. (3 subgroups)

#Violin Plots
#Make a subset for each brand
subDegree1 = pizza[pizza['brand']=='A' ]
subDegree2 = pizza[pizza['brand']=='B' ]
subDegree3 = pizza[pizza['brand']=='C' ]
subDegree4 = pizza[pizza['brand']=='D' ]
subDegree5 = pizza[pizza['brand']=='E' ]
subDegree6 = pizza[pizza['brand']=='F' ]
subDegree7 = pizza[pizza['brand']=='G' ]
subDegree8 = pizza[pizza['brand']=='H' ]
subDegree9 = pizza[pizza['brand']=='I' ]
subDegree10 = pizza[pizza['brand']=='J' ]

#combine subsets as specified into a list
group1 = [subDegree1, subDegree2, subDegree3]
group2 = [subDegree4, subDegree5, subDegree6]
group3 = [subDegree7, subDegree8, subDegree9, subDegree10]

#combine dataframes
group1Cat = pd.concat(group1)
group2Cat = pd.concat(group2)
group3Cat = pd.concat(group3)

#plot baby!
plt.violinplot( [ list(group1Cat['carb']), list(group2Cat['carb']), list(group3Cat['carb']), list(subDegree4['carb'])] , positions = [1,2,3,4] )

#a little icing on top, ya feel?
plt.xlabel('Brand Group')
plt.ylabel('Carbs')

#30 minutes later....
plt.show()



#%%
# QUESTION 02   xxxxxxx
# Broadcasting 
#
# I need to find the following subset and calculate a new feature/variable.
# The subset is for carb greater than 18, I need to calulate a new number which is fat/prot
# Please get this result in a dataframe (name it pizza2) for me, 
# with the extra variable call 'newratio' 

#subset
pizza2 = pizza[pizza.carb > 18]
#create new ratio
pizza2['newratio'] = pizza2.fat / pizza2.prot
#mamma mia, we get a pizza...2!
print(pizza2.head())



#%%
# First read in the gapminder dataset
# import os
os.chdir('../midterm')  
dirpath = os.getcwd() # print("current directory is : " + dirpath)
filepath = os.path.join( dirpath ,'gapmindeR.csv')
dfgap = pd.read_csv(filepath, index_col="id")

#%%
# add contCode as numerical value 
contCodeList = list( dfgap.continent.unique() ) 
contCodeList = ['Asia', 'Europe', 'Africa', 'Americas', 'Oceania']
dfgap['contCode']=pd.Categorical(dfgap.continent.apply( lambda x: contCodeList.index(x) ))
dfgap.head()

#%%
# QUESTION 03   xxxxxxx
# Create a pivot table with multi-index for the rows, as (continent, country), 
# and the column headers are the individual years.
# the table values are the population, 
# call it dfgap_pop
#  

#Pivot table created
dfgap_pop = dfgap.pivot_table(values='pop', index=['continent', 'country'], columns='year')

print(dfgap_pop.shape)
print(dfgap_pop.head())

#%%
# QUESTION 04   xxxxxxx
# Similarly create a pivot table with the same structure, but gdpPercap as values 
# save as dfgap_gdppp
#  

#second verse, same as the first.
dfgap_gdppp = dfgap.pivot_table(values='gdpPercap', index=['continent', 'country'], columns='year')

print(dfgap_gdppp.shape)
print(dfgap_gdppp.head())

#%%
# QUESTION 05   xxxxxxx
# From the above two pivot tables, use BROADCASTING, get a new table 
# with the GDP data. Note GDP equals to GDPpercapita times population
# Call the new dataframe dfgap_gdp

#GDP is every entry of GDPpercapita times every entry of the population, here synced up.
dfgap_gdp =  dfgap_gdppp * dfgap_pop

print(dfgap_gdp.shape)
print(dfgap_gdp.head())


#%%
# QUESTION 06   xxxxxxx
# From the dfgap_gdppp table, find out the average gdpPercap value for all the 
# Africa countries in 2007, and the value for all the Americas.

#dataframe of the means of all the countries in the continent
mean_dgppp = dfgap_gdppp.groupby('continent').mean()

#Africa in 2007; bless the rains baby
print(mean_dgppp.at['Africa', 2007])


#All the Americas; bless the USA baby
print(mean_dgppp.loc['Americas',:].mean())

#%%
# We have a JSON object (just a dictionary of dictionary of list of dictionary of dictionary of list of...) for the menu items at a cafe, we called it foodItems.

#%%
# Just run this cell
foodItems = {   # level 1
  "sweets":     # level 1
    {                            # level 2
      "serve hours": "10a-4p",   # level 2
      "items":                   # level 2
        [                               # level 3, a list, no key, just index
          {                                    # level 4
            "id": "0001",                      # level 4
            "type": "donut hole",              # level 4
            "name": "anti-cake",               # level 4
            "price": 4.95,                     # level 4
            "ingredients":                     # level 4
              {                                        # level 5
                "batter":                              # level 5 
                  [                                               # level 6
                    { "id": "1001", "type": "Regular", "add": 0.0 },       # level 7
                    { "id": "1003", "type": "Blueberry", "add": 0.5 },     # level 7
                    { "id": "1006", "type": "Caramel", "add": 0.5 },       # level 7
                    { "id": "1007", "type": "Mulberry", "add": 0.5 },
                    { "id": "1008", "type": "Angel's Food", "add": 0.75 },
                    { "id": "1009", "type": "Fudge", "add": 0.75 },
                    { "id": "1010", "type": "Strawberry", "add": 0.5 },
                    { "id": "1011", "type": "Diet", "add": 0.5 }
                  ]
                ,
                "topping":                             # level 5 
                  [                                               # level 6
                    { "id": "3001", "type": "None", "add": 0.0 },          # level 7
                    { "id": "3002", "type": "Glazed", "add": 0.5 },        # level 7
                    { "id": "3003", "type": "Sugar", "add": 0.25 },
                    { "id": "3005", "type": "Cinnamon Sugar", "add": 0.5 },
                    { "id": "3006", "type": "Sea Salt", "add": 0.25 },
                    { "id": "3008", "type": "Chocolate with Sprinkles", "add": 0.75 },
                    { "id": "3009", "type": "Chocolate", "add": 0.5 },
                    { "id": "3010", "type": "M and M", "add": 0.5 },
                    { "id": "3011", "type": "Sour kids", "add": 0.5 },
                    { "id": "3012", "type": "Oreo", "add": 0.5 },
                    { "id": "3013", "type": "Nutella", "add": 0.5 }
                  ]
              }
          },
          {
            "id": "0002",
            "type": "fried donut",
            "name": "unicorn butt sneeze",
            "price": 5.95,
            "ingredients":
              {
                "batter":
                  [
                    { "id": "1001", "type": "Regular", "add": 0.0 },
                    { "id": "1002", "type": "Chocolate", "add": 0.5 },
                    { "id": "1003", "type": "Blueberry", "add": 0.5 },
                    { "id": "1004", "type": "Devil's Food", "add": 0.5 },
                    { "id": "1005", "type": "Sour", "add": 0.5 },
                    { "id": "1006", "type": "Caramel", "add": 0.5 },
                    { "id": "1007", "type": "Mulberry", "add": 0.5 },
                    { "id": "1009", "type": "Fudge", "add": 0.75 },
                    { "id": "1010", "type": "Strawberry", "add": 0.5 }
                  ]
                ,
                "topping":
                  [
                    { "id": "3001", "type": "None", "add": 0.0 },
                    { "id": "3002", "type": "Glazed", "add": 0.5 },
                    { "id": "3003", "type": "Sugar", "add": 0.25 },
                    { "id": "3004", "type": "Powdered Sugar", "add": 0.5 },
                    { "id": "3005", "type": "Cinnamon Sugar", "add": 0.5 },
                    { "id": "3008", "type": "Chocolate with Sprinkles", "add": 0.75 },
                    { "id": "3009", "type": "Chocolate", "add": 0.5 },
                    { "id": "3010", "type": "M and M", "add": 0.5 },
                    { "id": "3011", "type": "Sour kids", "add": 0.5 },
                    { "id": "3013", "type": "Nutella", "add": 0.5 },
                    { "id": "3014", "type": "Maple", "add": 0.75 },
                    { "id": "3015", "type": "Special", "add": 1.25 },
                  ]
              }
          },
          {
            "id": "0003",
            "type": "bagel",
            "name": "einstein",
            "price": 3.95,
            "ingredients":
              {
                "batter":
                  [
                    { "id": "1001", "type": "Regular", "add": 0.0 },
                    { "id": "1003", "type": "Blueberry", "add": 0.5 },
                    { "id": "1004", "type": "Devil's Food", "add": 0.5 },
                    { "id": "1005", "type": "Sour", "add": 0.5 },
                    { "id": "1006", "type": "Caramel", "add": 0.5 },
                    { "id": "1007", "type": "Mulberry", "add": 0.5 },
                    { "id": "1008", "type": "Angel's Food", "add": 0.75 },
                    { "id": "1010", "type": "Strawberry", "add": 0.5 },
                    { "id": "1011", "type": "Diet", "add": 0.5 }
                  ]
                ,
                "topping":
                  [
                    { "id": "3001", "type": "None", "add": 0.0 },
                    { "id": "3005", "type": "Cinnamon Sugar", "add": 0.5 },
                    { "id": "3006", "type": "Sea Salt", "add": 0.25 },
                    { "id": "3007", "type": "Old Bay", "add": 0.5 },
                    { "id": "3008", "type": "Chocolate with Sprinkles", "add": 0.75 },
                    { "id": "3009", "type": "Chocolate", "add": 0.5 },
                    { "id": "3010", "type": "M and M", "add": 0.5 },
                    { "id": "3012", "type": "Oreo", "add": 0.5 },
                    { "id": "3013", "type": "Nutella", "add": 0.5 },
                    { "id": "3014", "type": "Maple", "add": 0.75 }
                  ]
              }
          }
        ]
    }
  ,
  "beverages": 
    {
      "serve hours": "8a-10p",
      "items":
        [
          {
            "id": "2001",
            "type": "coffee",
            "name": "irish",
            "price": 8.95,
            "ingredients":
              {
                "base":
                  [
                    { "id": "5001", "type": "Regular", "add": 0.0 },
                    { "id": "5002", "type": "Decaf", "add": 0.95 },
                    { "id": "5003", "type": "Double", "add": 0.95 }
                  ]
                ,
                "condiment":
                  [
                    { "id": "7001", "type": "None", "add": 0.0 },
                    { "id": "7002", "type": "Cream", "add": 0.25 },
                    { "id": "7003", "type": "Sugar", "add": 0.0 },
                    { "id": "7004", "type": "Almond milk", "add": 0.75 },
                    { "id": "7005", "type": "Soy milk", "add": 0.75 }
                  ]
              }
          },
          {
            "id": "2002",
            "type": "capucino",
            "name": "Fusion",
            "price": 6.95,
            "ingredients":
              {
                "base":
                  [
                    { "id": "5001", "type": "Regular", "add": 0.0 },
                    { "id": "5002", "type": "Double shot", "add": 0.75 },
                    { "id": "5003", "type": "Triple shot", "add": 1.5 }
                  ]
                ,
                "condiment":
                  [
                    { "id": "7001", "type": "None", "add": 0.0 },
                    { "id": "7002", "type": "Cream", "add": 0.25 },
                    { "id": "7003", "type": "Sugar", "add": 0.0 },
                    { "id": "7004", "type": "Almond milk", "add": 0.75 },
                    { "id": "7005", "type": "Soy milk", "add": 0.75 }
                  ]
              }
          }
        ]
    }
}


#%%
# QUESTION 07   xxxxxxx
# What is the python data type of foodItems?

print(type(foodItems))
"DICTIONARY, multiple levels!"

#%%
# QUESTION 08   xxxxxxx
# What is the length of foodItems?
print(len(foodItems))
"This has a length of 2!"

#%%
# QUESTION 09   xxxxxxx
# First let us loop through the foodItem in the foodItems object, and print out what python data type it is for the foodItem (the value of the foodItem as "key")
# The first line you see in the printout should be: 
# The food item type is sweets, and the python data type of sweets is <class 'dict'>.
# 
for foodItem in foodItems:
  print(f"The food item type is {foodItem}, and the python data type of {foodItem} is {type(foodItem)}.")

#%%
# QUESTION 10   xxxxxxx
# If you look at the foodItems object, you will find a line with the "Special" ingredients. Write a line of code that will extract the "add" value for that line.
# Something like this:

#Dict of a dict! We find the special topping ;)
foodItems['sweets']["items"][1]['ingredients']["topping"][11]["add"]



#%%
# QUESTION 11   xxxxxxx
# The following function is NOT working as intended. Fix it.
def func1(obj):
  if (type(obj) == dict): 
    print('This is a dictionary.')
    return
  if (type(obj) == list):
    print('This is a list.')
    return
  if (type(obj) == str):
    print('This is a string.')
    return
  if (type(obj) == int or type(obj)== float):
    print('This is a number.')
    return
  if (type(obj) == bool):
    print('This is a boolean.')
    return
  else:
   print('Unknown type.')
   return

func1(foodItems)  # Should produce 'This is a dictionary.'
func1([8,9,1])  # Should produce 'This is a list.'
func1('hi')  # Should produce 'This is a string.'
func1(2.87)  # Should produce 'This is a number.'
func1(False)  # Should produce 'This is a boolean.'
func1( type(foodItems) )  # Should produce 'Unknown type.'


#%%
# Having the same problem here as the previous Q / function. Fix it here as well.
# QUESTION 12   xxxxxxx
def printStr(obj, level=1):
  if (type(obj) == dict): 
    print(f'(L{level}) dictionary')
    for key in obj:
      print('-' * level, f"(L{level}) key: {key}, value: ", end='')
      printStr(obj[key], level+1)
    return
  if (type(obj) == list):
    print(f'(L{level}) list')
    for elt in obj:
      print('-' * level, f"(L{level}) list element: ", end='')
      printStr(elt, level+1,)
    return
  if ( type(obj) == str):
    print(obj)
    return
  if ( type(obj) == int or type(obj)== float):
    print(obj)
    return
  if ( type(obj) == bool):
    print(obj)
    return
  else:
    print('Unknown type.')
    return


printStr(foodItems)

# Should produce the following:
# (L1) dictionary
# - (L1) key: sweets, value: (L2) dictionary
# -- (L2) key: serve hours, value: 10a-4p
# -- (L2) key: items, value: (L3) list
# --- (L3) list element: (L4) dictionary
# ---- (L4) key: id, value: 0001

#%%
# QUESTION 13   xxxxxxx
# What is the highest level  (L?)  involved in the foodItems object?
"7"

#%%
# no need to answer anything here. just run the cell.

# Our next goal is to pull the info from the foodItems JSON file and 
# save it organized in a dataframe.

import numpy as np

# Let us create an empty dataframe with only the headers first
foodDF = pd.DataFrame( columns=['category', # sweets or beverages
                                'hours',
                                'itemid', 
                                'itemtype', # donut hole, fried donut, etc
                                'itemname', # anti-cake, unicorn butt sneeze, etc
                                'itemprice',
                                'ingredient', # (sweets) batter or topping or (beverages) base or condiment
                                'ingredientid', 
                                'ingredienttype', 
                                'addprice'
                                ])


#%%
# QUESTION 14   xxxxxxx
# Test insert/appending to the dataframe. Write 
# a simple line of code to add something there, say category as 'hi', hours as '5p'
print('before')
print(foodDF.head())

df2 = pd.DataFrame([("hi","5p")], columns= ['category','hours'])
foodDF.append(df2)

print('after')
print(foodDF.head())

#%%
# Now assume all is working, remove that trial row. You can run the previous code 
# to recreate foodDF, just run the lines below. Either way. Don't forget to use 
# inplace=True. It's often the operations only return a dataframe to you, but won't 
# change the original dataframe. You can save it back as the original name, or use 
# inplace=True if applicable.
foodDF = pd.DataFrame( columns=['category', # sweets or beverages
                                'hours',
                                'itemid', 
                                'itemtype', # donut hole, fried donut, etc
                                'itemname', # anti-cake, unicorn butt sneeze, etc
                                'itemprice',
                                'ingredient', # (sweets) batter or topping or (beverages) base or condiment
                                'ingredientid', 
                                'ingredienttype', 
                                'addprice'
                                ])
print(foodDF.head())

#%%
# Now we need to pull the info from the JSON into the dataframe foodDF 
# You need to insert the data to the dataframe foodDF at "level 6" (see below) 
# everything else are set up to work. Just complete the small task of inserting the row.
def insertFoodRow(obj, level=1, category="", hours="", itemid=0, itemtype="", itemname="", itemprice=0.0, ingredient="", ingredientid=0, ingredienttype="", addprice=0.0 ):
  global foodDF
  # first set the default values of these ten variables to blank or 0 or 0.0 first.
  # Each level of depth we read into the foodItems structure (level = level + 1), we continue to put in the correct value 
  # for the appropriate variables. When we reach the final level (which you have already found before),    
  # we will write the data into the dataframe foodDF.
  if (level == 1): # level 1 is a dictionary with two possible keys: "sweets" or "beverages". We need to loop thru them and pull all the info
    for key in obj: # key = "sweets" or "beverages" here
      category = key # assign the correct value to the variable 'category' to later insert to the dataframe
      insertFoodRow(obj[key], 2, category, hours, itemid, itemtype, itemname, itemprice, ingredient, ingredientid, ingredienttype, addprice)
      # recursively continue to level 2 now, witih category value set
    return # end case level == 1

  if (level == 2): # level 2 is also a dictionary, with two things: "serve hours" and "items"
    for key in obj:   # key can be "serve hour" or "items"
      if key == "serve hours": 
        hours = obj[key]
      else: # key == "items" 
        insertFoodRow(obj[key], 3, category, hours, itemid, itemtype, itemname, itemprice, ingredient, ingredientid, ingredienttype, addprice) 
        # recursively continue to level 3 now, witih hours value set
    return # end case level == 2

  if (level == 3): # level 3 is a list, each item in the list is basically a kind of food for purchase. 
    for fooditem in obj:   # each fooditem is a dictionary now, with keys: "id", "type", "name", etc. Need to pass to the next level for processing
      insertFoodRow(fooditem, 4, category, hours, itemid, itemtype, itemname, itemprice, ingredient, ingredientid, ingredienttype, addprice) 
    return # end case level == 3

  if (level == 4): # level 4 is is a dictionary, with keys: "id", "type", "name", "price", "ingredients"
    for key in obj:   
      if key == "id": 
        itemid = obj[key]
      elif key == "type":  
        itemtype = obj[key]
      elif key == "name":  
        itemname = obj[key]
      elif key == "price":  
        itemprice = obj[key]
      elif key == "ingredients":  
        insertFoodRow(obj[key], 5, category, hours, itemid, itemtype, itemname, itemprice, ingredient, ingredientid, ingredienttype, addprice) 
    return # end case level == 4

  if (level == 5): # level 5 is a dictionary, with keys: "batter", "topping", "base", or "condiment", depending on whether it's "sweets" or "beverages"
    for key in obj:   # keys: "batter", "topping", "base", or "condiment"
      # need to save this info in the dataframe as ingredienttype
      ingredient = key
      insertFoodRow(obj[key], 6, category, hours, itemid, itemtype, itemname, itemprice, ingredient, ingredientid, ingredienttype, addprice) 
    return # end case level == 5

  if (level == 6): # level 6 is a list, like level 3. Each item in the list is basically an addon to the foodItem order  
    for addon in obj:   # each addon is a dictionary now, with keys: "id", "type", "add"
      # Instead of passing the values down to level 7 to process, we can 
      # complete it right here, as we know every value (key-value pairs) is a simple object. 
      # There is no complicated list or dictionary as value at level 7.
      #
      ingredientid = addon["id"]
      ingredienttype = addon["type"]
      addprice = addon["add"]
      #
      # 
      #foodDF.append(obj, ingnore_index = True)
      # QUESTION 15   xxxxxxx 
      # Use what you got in Q 14.
      # If you cannot complete this part, use the next three lines. 
      # Then you can at least continue the next tasks without getting stuck.
      dtype_dic= { 'category':str,'hours':str,'itemid':str,'itemtype':str,'itemname':str,'itemprice':float,'ingredient':str,'ingredientid':str,'ingredienttype':str,'addprice':float }
      filepath = os.path.join( os.getcwd() ,'foodDF.csv')
      foodDF = pd.read_csv(filepath, dtype = dtype_dic)

    return # end case level == 6


#%%
# add items to foodDF
insertFoodRow(foodItems)
# check if it works
foodDF.head()

"I genuinely tried here with putting foodDF.append(obj) but to no avail."

# You should see this:

# category	hours	itemid	itemtype	itemname	itemprice	ingredient	ingredientid	ingredienttype	addprice
# 0	sweets	10a-4p	0001	donut hole	anti-cake	4.95	batter	1001	Regular	0.00
# 1	sweets	10a-4p	0001	donut hole	anti-cake	4.95	batter	1003	Blueberry	0.50
# 2	sweets	10a-4p	0001	donut hole	anti-cake	4.95	batter	1006	Caramel	0.50
# 3	sweets	10a-4p	0001	donut hole	anti-cake	4.95	batter	1007	Mulberry	0.50
# 4	sweets	10a-4p	0001	donut hole	anti-cake	4.95	batter	1008	Angel's Food	0.75

#%%
# QUESTION 16   xxxxxxx
# What is the shape of foodDF?  (Should have 75 rows!!)
print(foodDF.shape)
"75,10"

#%%
# Just read and run this cell
# Now I need to create a list (dataframe) of all the possible addons 
# example 
# batter - id - Regular - add 0
# topping - id - Glazed - add 0.5 
# etc
#
# Need to filter out the last four columns here?
addonDF = foodDF.loc[ : ,'ingredient':'addprice' ]

print(addonDF.head())
print(addonDF.info())
print(addonDF.shape)


#%%
# addonDF is not unique,  
# Just run this cell
addonDF[ addonDF.ingredientid == '3005' ]

#%%
# Just run this cell
addonDF.drop_duplicates('ingredientid', inplace=True)
print(addonDF.shape)


#%%
# Now, set new index
# Just run this cell
addonDF.set_index('ingredientid', inplace=True)
print(addonDF.head())
# addonDF.ingredientid.is_unique

#%% 
# OOP (food item)
class Addon:
  """ 
  Addon item on the food menu
  """

  def __init__(self, ingredient, iid, itype, iadd) : 
    self.ingredient = ingredient
    self.iid = iid  # ingredientid
    self.itype = itype # ingredienttype
    self.iadd = iadd # addprice
    self.inventory = True  # not used
    self.allergyWarn = False  # not used
    self.kosher = False  # not used
    self.vegan = False  # not used
    self.calories = 0  # not used
    self.qty = 0
    self.maxqty = 2
  
  # add or subtract order quantity
  def stepqty(self, subtract=False) : # add or subtract 1, make sure result between 0 and maxqty 
    #
    # QUESTION 17   xxxxxxx
    # set the self.qty to add one if subract is False, otherwise, subtract one. 
    # Make sure the final qty is not less than 0, and not greater than 2
    #
    return self
  
  # change qty directly
  def changeqty(self, newqty) :
    self.qty = self.maxqty if newqty > self.maxqty else 0 if newqty < 0 else newqty
    return self

  # total addon price for this item
  def subtotal(self) : 
    # QUESTION 18   xxxxxxx
    # Calculate the subtotal here for the qty included, times the price (iadd) 
    subt = 0  # shouldn't zero. Change this.
    return subt


#%% 
# Just read and run this cell
# Let us create a couple of add-ons for testing
pdindex = '1006'
pdseries = addonDF.loc[pdindex]
caramelbatter = Addon(pdseries.ingredient, pdindex, pdseries.ingredienttype, pdseries.addprice)
print( caramelbatter.stepqty().subtotal() ) 
print (caramelbatter.qty)

#%% 
# Just read and run this cell
# Try add one more qty
print( caramelbatter.stepqty().subtotal() ) 
# But can't over the max
print( caramelbatter.stepqty().subtotal() ) 
print( caramelbatter.stepqty().subtotal() ) 


#%%
# Just read and run this cell
# have one more addon
pdindex = '3008'
pdseries = addonDF.loc[pdindex]
cinnamontopping = Addon(pdseries.ingredient, pdindex, pdseries.ingredienttype, pdseries.addprice)
print( cinnamontopping.stepqty().subtotal() ) 
print( cinnamontopping.stepqty().subtotal() ) 
print( cinnamontopping.stepqty().subtotal() ) 

# Now we have caramelbatter and cinnamontopping at our disposal.
  

#%%
# Just read and run this cell
# Similarly, create a DF for the food items itself
# Example
# 	category	hours	itemid	itemtype	itemname	itemprice
# 0	sweets	10a-4p	0001	donut hole	anti-cake	4.95
# 1	sweets	10a-4p	0001	donut hole	anti-cake	4.95
# 2	sweets	10a-4p	0001	donut hole	anti-cake	4.95
# 3	sweets	10a-4p	0001	donut hole	anti-cake	4.95
# 4	sweets	10a-4p	0001	donut hole	anti-cake	4.95
baseDF = foodDF.loc[ : ,'category':'itemprice' ]
print(baseDF.head())
print(baseDF.info())
print(baseDF.shape)

#%%
# Just read and run this cell
# again, not unique
baseDF[ baseDF.itemid == '0003' ]

#%%
# Just read and run this cell
# drop duplicates
baseDF.drop_duplicates('itemid', inplace=True)
print(baseDF.shape)
print(baseDF.head())

# baseDF.itemid = baseDF.itemid.astype(int)

#%%
# Just read and run this cell
# set new index
baseDF.set_index('itemid', inplace=True)

#%%
# Finally, we have to order a bagel, a cake or coffee
class Orderitem:
  """ 
  food item in a basket
  """

  def __init__(self, itemid , itemtype, itemprice) :
    self.itemid = itemid  # itemid
    self.itemtype = itemtype # itemtype
    self.itemprice = itemprice # itemprice
    self.addons = [] # start with an empty list of addon
    self.inventory = True
    self.allergyWarn = False
    self.kosher = False
    self.vegan = False
    self.calories = 0
  
  # find the total price of the item
  # as an example, we can have 
  # self.addons = [ addon object, with qty = 2, iadd = 0.50...   ]
  def itemtotal(self) : 
    # QUESTION 19   xxxxxxx
    # The self.addons might or might not be an empty list. If there are some addons 
    # there, we'll need to tally up the total, 
    # which should be the itemprice here plus looping thru 
    # the addons, and add the addon subtotals to here.
    tot = self.itemprice # this is the base price
    # 
    for i in self.addons:
        tot = i[1]
    #
    return tot
  
  def insertaddon(self, addon) :
    self.addons.append(addon)
    return self

#%%
# Just read and run this cell
# Let us create an item in the basket
pdindex = '0002'
pdseries = baseDF.loc[pdindex]
yummy = Orderitem(pdindex, pdseries.itemtype, pdseries.itemprice)
print( yummy.itemtotal() ) 

#%%
# Just read and run this cell
# Let's see if our caramelbatter and cinnamontopping still has a quantity of 2 for each. If not, fix it.
print(f"caramelbatter.qty = {caramelbatter.qty}")
print(f"cinnamontopping.qty = {cinnamontopping.qty}")

#%%
# Just read and run this cell
# Add these to our order, and compute the total price for checkout
yummy.insertaddon(caramelbatter).insertaddon(cinnamontopping).itemtotal()

#%%
# One final challenge
# Change my mind, need to decrease the caramel quantity to 1. 
# Perform that operation, and re-calculate the item total.

# Trial #1
# You should be able to access the caramel object inside yummy, and use 
# the methods we wrote to subtract qty by 1. 
# something like 
# yummy.addons[0].step????
# print out the total again.
yummy.addons[0].stepqty(True)  # subtract qty 1
yummy.itemtotal()

#%%
# Trial #2
# What is we change the caramelbatter object directly?
# something like 
# caramelbatter.change????
# change the quantity back to 3 this time.
# Does this affect the yummy itemtotal??
# Try it.
caramelbatter.changeqty(3)
yummy.itemtotal()
# QUESTION 20   xxxxxxx
# 
# Explain why or why not. In words, not in codes.

#%%
