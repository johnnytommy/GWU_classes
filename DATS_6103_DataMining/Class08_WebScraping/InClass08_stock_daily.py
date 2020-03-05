# -*- coding: utf-8 -*-
#
#%%
import datetime
# import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from time import sleep

# # Web scraping
#
# Samples
# https://finance.yahoo.com/quote/msft
# https://finance.yahoo.com/quote/%5EDJI?p=^DJI
# https://finance.yahoo.com/quote/%5EDJI
# https://finance.yahoo.com/quote/^DJI

#%%
def getUrl(sym):
  url = 'https://finance.yahoo.com/quote/'+sym
  return url

def getSoup(url,timer=0,parser=''):
  # import requests
  # from bs4 import BeautifulSoup
  # from time import sleep
  p = parser if ( parser=='lxml' or parser=='html.parser') else 'html5lib'
  r = requests.get(url, sleep(timer))
  if (timer > 0):
      print('slept',timer,'s')
      r = requests.get(url, sleep(timer))
  else:
      r = requests.get(url)
  s = BeautifulSoup(r.content, p) # or 'lxml' or 'html.parser'
  return s

def getDiv(soup): # Yahoo finance v201911  # works on ^DJI
  # from bs4 import BeautifulSoup
  div = soup.select_one('div#quote-header-info div#quote-market-notice')
  # div#quote-header-info > div.My\(6px\).Pos\(r\).smartphone_Mt\(6px\) > div > div
  return div

def getClose(sym,timer=0): # Yahoo finance v201911  # works on ^DJI
  # from bs4 import BeautifulSoup
  # import time
  while timer < 6:
    s = getSoup(getUrl(sym),timer/4)
    if s is None:
      print('type s NoneType. timer =',timer)
      timer += 1
      continue
    d = getDiv(s)
    if d is None:
      print('type d NoneType. timer =',timer)
      timer += 1
      continue
    html = d.parent.previous_sibling  # works on ^DJI
    # html = soup.select_one('div#quote-header-info div#quote-market-notice')
    # html = soup.select_one('div#quote-header-info div#quote-market-notice').previous_sibling
    # html = soup.select_one('div#quote-header-info div#quote-market-notice').previous_sibling.previous_sibling
    # div#quote-header-info > div.My\(6px\).Pos\(r\).smartphone_Mt\(6px\) > div > div
    if html is None:
      print('type html NoneType. timer =',timer)
      timer += 1
      continue
    return html.text.replace(',','')  # remove comma for (floats more than triple digits)
  return 'tried 5x'

# import pandas as pd
import os
os.chdir('../Class08_WebScraping')  # make sure it's the correct working folder
# os.chdir('/Users/edwinlo/GDrive_GWU/Classes/DATS_6103_DataMining/Class08_WebScraping')  
filename = 'stockportfolio.csv'
# filepath = '/home/physicsland/hw/'+filename  # for pythonanywhere setup
filepath = filename

def getDayQuotes(filepath):
  # import datetime
  tday = datetime.datetime.today()
  if tday.weekday() > 4 : return None   # 6-Sunday,5-Saturday, do nothing
  tdaystr = tday.strftime('%Y-%m-%d')


  # open file, import df
  df_last = pd.read_csv(filepath, header=[0,1], index_col=0, date_parser=lambda x: datetime.datetime.strptime(x, '%Y-%m-%d') )

  df_new = pd.DataFrame(columns=df_last.columns) # empty dataframe for new day data
  df_new = df_new.append(pd.Series(name=tdaystr)) # add a blank row

  # print(df_last.shape)
  # print(df_last.head())
  # from cvs file,

  for i, sym in enumerate(df_last.columns): # loop through all the stock smybols in the csv file
    x = getClose(sym[0])
    # try: x = float(x) if i >5 else round(float(x))
    # except: pass

    df_new.iloc[0,i] = x
    # read online data
    # print( sym[0], sym[1], 'ind', i, ':', x )

    # check date info
    # if exist, determine if overwrite
    # if not exist, get new row

#   print(df_new.head())

  df_last = pd.concat([df_new,df_last])
  df_last.index = pd.to_datetime(df_last.index, format='%Y-%m-%d') # row index = 'Date'
#   print(df_last.head())

  df_last = df_last.iloc[0:25,:]
  # trim number of rows to max 25, save to file

  df_last.to_csv(filepath, encoding='utf_8_sig')
  # df_last.to_csv(filepath, sep='\t')

  return None

getDayQuotes(filepath)



# %%
