#!/usr/bin/python

"""Get the current price of Bitcoin."""


import simplejson
import urllib


URL = 'https://api.bitcoinaverage.com/all'
CURRENCY = 'USD'


def GetData():
  return simplejson.load(urllib.urlopen(URL))
  
  
if __name__ == '__main__':
  data = GetData()
  with open('data', 'a') as f:
    f.write(str(data['USD']['global_averages']['last']) + '\n')
  
  print data['USD']['global_averages']['last']
