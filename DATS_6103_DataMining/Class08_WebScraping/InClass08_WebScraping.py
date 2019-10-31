# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'

#%% [markdown]
# # Web scraping
#
# Our goal here is to learn
# * Basic HTML structure
# * Basic CSS structure and selector rules
# * Basic webpage inspection tools from browsers
# * Use of BeautifulSoup or other web scraping libraries, plus parsers

#%%
import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
# plt.style.use('classic')

#%%
# We can use Python library "requests" to download the html file (via a GET request to the web server). 
import requests
# You can get a list of attributes and methods for the python requests object from w3school very handy
# https://www.w3schools.com/python/ref_requests_response.asp


#%%
myportfolio = ( 'MSFT', 'AAPL', 'GOOG' )
url = 'https://money.cnn.com/quote/quote.html?symb=MSFT' # we aim to loop thru our portfolio later when things are working
thispage = requests.get(url)
print(thispage)
# a response object, with status_code [200] means successful. It could be a blank page or error page, however...
print(thispage.status_code)
# a status code starting with a 2 generally indicates success, and a code starting with a 4 or a 5 indicates an error.

#%%
# To get the html body (and head) from the response object, we can use
print(thispage.content)
# The results typically should be like this
# b'<!DOCTYPE html>\n ...
# The starting 'b' character indicates it's in bytes, where as 
print(thispage.text)
# will be in unicodes

# These are what you would see from "downloading" or "inspecting" a webpage in chrome/firefox/safari/etc.
# Try that.

#%%
# Next step is to use some kind of parsers to parse the HTML codes into standard tree-like or object-like structure (HTML DOM  Document-Object-Model)

# Useful to have basic HTML knowledge, the (XML) structure

# CSS (Cascade Style Sheet) is also an integral part of most HTML design these days.

# Most parsers can use CSS-style selectors, as well as Xpaths

#%%
# We will use the library beautifulSoup with the default parser lxml. Another common one is the scrapy library.
# Need to install for the first time:
# pip install bs4
# or pip3 install bs4
# Beautiful Soup also relies on a parser, the default is lxml. 
# You might already have itYou may already have it. 
# If not, do: $ pip install lxml or $ apt-get install python-lxml.
# We can also use html.parser, or html5lib
from bs4 import BeautifulSoup

#%%
# soup = BeautifulSoup(thispage.content, 'lxml')
# soup = BeautifulSoup(thispage.content, 'html.parser')
soup = BeautifulSoup(thispage.content, 'html5lib')

#%%
print(soup.prettify())

#%% 
# What is the structure of soup?
soupkids = list(soup.children)
print(len(soupkids)) # length of 3 if html.parser is used, or 2 if lxml or html5.lib is used.
# soupkids = ['HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"', '\n', <html> <head> <title> ...

# Use list comprehension to see what is in the list
[type(item) for item in soupkids]

#%%
print(soupkids[0])   # HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"

#%%
print(soupkids[1]) # the actual html document that we really care about

#%%
thecontent = soupkids[1] # the html codes itself

#%%
# break this object (bs4.element.Tag) up further
thehtml = list(thecontent.children)
print(len(thehtml)) # length of 3 
# thehtml = [ <head> <title> ..., '\n' , <body> ... ]

# Use list comprehension to see what is in the list
[type(item) for item in thehtml]

#%%
# For our purpose, we want the info inside the body
thebody = thehtml[2]

#%%
# break this object (bs4.element.Tag) up further
thebodychildren = list(thebody.children)
print(len(thebodychildren)) # length of 3 
# thebodychildren = [ <head> <title> ..., '\n' , <body> ... ]

# Use list comprehension to see what is in the list
[type(item) for item in thebodychildren]

#%%
# STOP
# Won't work like that except for very simple sites
# Let rewind and start from the beginning with soup
# soup = BeautifulSoup(thispage.content, 'html5lib')

# know what you want to find. Use .find() or .find_all()
foundlast = soup.find('td', class_='wsod_last')
print(foundlast)
print(foundlast.text) # almost got it

#%%
# Try
print(list(foundlast.children)) # Here you are, the quote, in the first element of the list
print(list(foundlast.children)[0].text) # the stock quote 


#%%
# Also try to use CSS selectors
# Use dot . for className, use # for id
selectlast = soup.select('tr td.wsod_last span') 
selectlast[0].text
# Or if we know for sure there is only one, or just want the first one, we can do
# selectlast = soup.select_one('tr td.wsod_last span') # return a single node instead of a list
# selectlast.text


#%%
# myportfolio = ( 'MSFT', 'AAPL', 'GOOG' )

# So with all these hard work, we can now streamline all these into a combined function call
import requests
from bs4 import BeautifulSoup
def getStockQuote(stocksymbol):
  sourcemain = 'https://money.cnn.com/quote/quote.html?symb='
  url = sourcemain + stocksymbol.upper()
  thispage = requests.get(url)
  # soup = BeautifulSoup(thispage.content, 'lxml')
  # soup = BeautifulSoup(thispage.content, 'html.parser')
  soup = BeautifulSoup(thispage.content, 'html5lib')
  selectlast = soup.select_one('tr td.wsod_last span') # return a single node instead of a list
  return float(selectlast.text)


#%%
# Testing...
getStockQuote('aapl') # works
getStockQuote('silly') # error
# try to make your codes fool-proof

#%%
import requests
from bs4 import BeautifulSoup

def getStockQuote(stocksymbol):
  sourcemain = 'https://money.cnn.com/quote/quote.html?symb='
  url = sourcemain + stocksymbol.upper()
  thispage = requests.get(url)  # thispage.status_code is still 200 whether the stock symbol exists or not. 
  # soup = BeautifulSoup(thispage.content, 'lxml')
  # soup = BeautifulSoup(thispage.content, 'html.parser')
  soup = BeautifulSoup(thispage.content, 'html5lib')
  selectlast = soup.select('tr td.wsod_last span') # return a list
  return float(selectlast[0].text) if (len(selectlast)==1) else -1 # or anything that you can flag easily. I try to keep the return value numeric. Another option would be return np.nan

# Now it works for 'silly'



# %%
