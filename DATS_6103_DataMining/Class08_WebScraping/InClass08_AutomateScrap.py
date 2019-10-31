# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'

#%% [markdown]
# Other web info are not encoded in the url. 
# The previous example uses what is called "get-method" query 
# variables (with the question mark ? in the url address for key => value pairs) in the url to request info 
# from the web server. Many modern websites do not use such methods.
# Interactions with the server can nowadays be using ajax, jQuery, other backend DB connections, 
# asynchronous in nature and so forth.
# 
# For such situations, we can try to automate the browswer experience and navigate the site to pull the content 
# with the (chrome) driver



#%%
# First, install selenium
# $ pip install selenium (or use pip3)
#
# follow the url from the messages when you install selenium, 
# or directly from https://chromedriver.chromium.org/home
# or https://chromedriver.chromium.org/downloads
#

#%%
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
# import csv
import pandas as pd

# urlfilepath = os.path.join( dirpath, path2add ,'')

testWeatherData = pd.DataFrame( columns=['zip','temperature','datetime','lat','long','elevation'])

zips = [90210,20052,20051,20050]
zip0 = zips[0]
driver = webdriver.Chrome(r'/Users/edwinlo/Downloads/dev/chromedriver')
# also need to install and locate the webdriver.Chrome location
# for my install, I need to set 
# driver = webdriver.Chrome(r'/Users/edwinlo/Downloads/dev/chromedriver')  # mac OS
# driver = webdriver.Chrome(r'/Users/edwinlo/Downloads/dev/chromedriver.exe')  # windows

driver.get("https://www.weather.gov")

# Selenium
# To find multiple elements (these methods will return a list):
# find_element_by_id
# find_element_by_name
# find_element_by_xpath
# find_element_by_link_text
# find_element_by_partial_link_text
# find_element_by_tag_name
# find_element_by_class_name
# find_element_by_css_selector

# To find multiple elements (these methods will return a list):
# find_elements_by_name
# find_elements_by_xpath
# find_elements_by_link_text
# find_elements_by_partial_link_text
# find_elements_by_tag_name
# find_elements_by_class_name
# find_elements_by_css_selector

# inp = driver.find_element_by_id('inputstring') 
inp = driver.find_element_by_css_selector('input#inputstring') 
sleep(0.1)
inp.clear() # search input box
print('cleared')
sleep(0.1)
inp.send_keys(zip0)
print('zip0')
sleep(1.0)
inp.send_keys(Keys.DOWN) 
print('down')
sleep(0.1)
driver.find_element_by_id('btnSearch').click() # go Button
driver.find_element_by_css_selector('input#btnSearch').click() # go Button
print('go clicked')
sleep(1)
driver.refresh()

def getGovWeatherTemperature(soup):
  selectTemp = soup.select('div#current_conditions-summary p.myforecast-current-lrg') # return a list
  return (selectTemp[0].text) if (len(selectTemp)==1) else "error" 


from bs4 import BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html5lib')
print(len(soup))

# selectTemp = soup.select('div#current_conditions-summary p.myforecast-current-lrg') # return a list
thistemperature = getGovWeatherTemperature(soup)
# append data to dataframe
# testWeatherData = testWeatherData.append({ 'zip': zip0, 'temperature': thistemperature }, ignore_index=True)

# NOW
# pull the other data to the dataframe
# datetime
# lat
# long
# elevation


# terminates the automtion browser
# driver.quit()


# %% [markdown]
#
# Other things to consider...
#
# # Generator functions and recursive functions
#
# Let's say we are using automation to construct a web crawler, from one site, crawling to 
# other web links. A typical function to perform such task will be nested/recursive. And it is 
# often such task will be written as generator functions (remember them? list comprehension and 
# generator functions?) That way, the list could go on forever, from one site crawl to another, 
# but python will not wait for the entire list to be stored in memory to continue.
#
# # Async nature of web traffic, Promises, Watchers
#
# Procedural programming and traditional OOP are all sequential in nature. The flow of logic 
# is well structured. The web programming has provided a lot of challenges to these fundamental 
# practices in recent years. Communications between servers and clients are often routed in 
# complicated and asynchronous fashion. There is no guaranteed the codes executed first will be 
# completed first. For example, when the web client trying to connect to the server DB for query, 
# the response might not be received for a while, depending on the routing and the other connections. 
# It is impractical and almost impossible to always wait for the response before moving on to 
# other tasks. 
#
# So the latest web programming, with ajax, angular, typescript, and many others new frameworks, 
# all have the asynchronous nature in mind. The function calls often have options to wait for 
# the *promise* to be delivered before executing other related codes. (Called a promise.) 
# In many situations, we just move on and carry on with the rest of the codes, by there are 
# *watchers* implemented throughout. When the data (called model) is changed, say from the 
# server response eventually, for example, the watchers will alerted all involved to change 
# their status, and update their values if needed. If these are not setup properly, 
# there could be a lot of inconsistent and unexpected behavior on the web applications. 
#
