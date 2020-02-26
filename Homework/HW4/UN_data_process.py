# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 14:17:35 2020

@author: Dustin
"""

import pandas as pd

data = pd.read_csv('UNdata_Export_20200218_211115801.csv')

data.notnull().sum()
# Out[16]: 
# Country or Area    3757
# Year(s)            3757
# Variant            3757
# Value              3263
# dtype: int64

data.isnull().sum()
# Country or Area      0
# Year(s)              0
# Variant              0
# Value              494
# dtype: int64


data.dropna(inplace = True)

data.notnull().sum()
# Out[19]: 
# Country or Area    3263
# Year(s)            3263
# Variant            3263
# Value              3263
# dtype: int64

data.isnull().sum()
# Out[18]: 
# Country or Area    0
# Year(s)            0
# Variant            0
# Value              0
# dtype: int64

data.to_csv('UNdata_nulldrop.csv')
