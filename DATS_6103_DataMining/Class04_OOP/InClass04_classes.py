# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'

#%%
import math
import os

print("Hello world!")




#%%
# OOP -- Object Oriented Programming 
# class
# class can be thought of bundling properties (like variables) and functions (or called methods) together
# This is not a requirement, but good practice to use Capitalize first letter for classes, 
# variables or functions instances use regular lowercase first letter.
class Person:
  """ 
  a person with properties and methods 
  height in meteres, weight in kgs
  """

  # contructor and properties
  # __init__ is also called constructor in other propgramming langs
  # it also set the attributes in here 
  def __init__(self, lastname, firstname, height, weight) :
    self.lastname = lastname
    self.firstname = firstname
    self.height_m = height
    self.weight_kg = weight
  
  # find bmi according to CDC formula bmi = weight/(height^2)
  def bmi(self) : 
    return self.weight_kg/(self.height_m ** 2)
  
  def print_info(self) :
    print( self.firstname, self.lastname+"'s height {0:.{digits}f}m, weight {1:.1f}kg, and bmi currently is {2:.{digits}f}".format(self.height_m, self.weight_kg, self.bmi(), digits=2) )

  # gain weight
  def gain_weight_kg(self,gain) : 
    self.weight_kg = self.weight_kg + gain 
    return self

  # gain height
  def gain_height_m(self,gain) : 
    self.height_m = self.height_m + gain 
    return self
  
  def height_in(self) :
    # convert meters to inches
    return self.height_m *100/2.539
  
  def weight_lb(self) :
    # convert meters to inches
    return self.height_m *100/2.539
  
  
  

#%%
# instantiate the Person object as elo, etc
elo = Person('Lo','Edwin',1.6,60)
vars(elo) # shows all attributes and their values
# dir(elo) # shows all attributes and methods

elo.print_info()
elo.gain_weight_kg(5) # no return value for this method
# same as
Person.gain_weight_kg(elo,5) # use both arguments here
elo.print_info()

#%%
superman = Person('Man','Super', 1.99, 85)
superman.gain_weight_kg(-3.5)
superman.print_info()

#%%
persons = []
persons.append(elo)
persons.append(superman)
print(len(persons))

#%%
# Add to the Person class four other attributes. At least one of the type float or int.
# Add at least three other methods to the class that might be useful


#%% [markdown]
# 
# ## From a programmer's perspective on Object-Oriented Programming (OOP)
# 
# Read this [blog at Medium on OOP](https://medium.com/@cscalfani/goodbye-object-oriented-programming-a59cda4c0e53). 
# To put all these into context, from procedural progamming (such as C) to OOP (C++, java and the likes) was a 
# huge paradigm shift. The world has progressed however, and there are new needs, and new wants, from the new generations. 
# And there are new answers in response. Keep up with the new ideas and concepts. 
# That's how to stay ahead. 
# Just like OOP still uses a lot of concepts and functionality in procedure programming, 
# the new programming paradigm will continue to use OOP concepts and tools as the backbone. 
# Try to get as much as you can, although you might not consider yourself a programmer. 
# These will serve you well, and makes you a more logical thinker.


#%%
class Cars :
  
  """ 
  a car
  """

  # contructor and properties
  # __init__ is also called constructor in other propgramming langs
  # it also set the attributes in here 
  def __init__(self) :
    
  
  def print_info(self) :
    print( "myself" )
    return

  
  #%%





#%%
# read APPL stock csv file
import os # already imported start of file
print("current directory is : " + os.getcwd())
print("Directory name is : " + os.path.basename(os.getcwd()))
# need to make sure your directory is correct for the file, and use the correct / or \ for your OS/platform

#%%
# filepath = "/Users/edwinlo/GDrive_GWU/github_elo/GWU_classes/DATS_6103_DataMining/Class04_OOP/AAPL_20140912_20190912_daily_full.csv"
appl_date = []
appl_price_eod = []
filepath = os.path.join( os.getcwd(), "AAPL_20140912_20190912_daily_full.csv")
fh = open(filepath) # fh stands for file handle
# data pulled from https://old.nasdaq.com/symbol/aapl/historical (5 years, csv format, 9/12/2019)   can also try  www.quandl.com/EOD
for aline in fh.readlines(): # readlines creates a list of elements; each element is a line in the txt file, with an ending line return character. 
  # this file gives "23.57" as the string, including the quotes
  tmp = aline.replace('"','').split(',')  # remove all double quotes, then split
  if (tmp[1] == 'close'): # skip the first line
    print('closing')
    continue
  appl_date.append(tmp[0].strip())
  appl_price_eod.append(float(tmp[1]))
  
print(appl_date)
print(appl_price_eod)


# %%
