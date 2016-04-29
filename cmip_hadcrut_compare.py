# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 14:42:57 2016

@author: hanbre
"""
from __future__ import print_function
import sys
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

CMIP=pd.read_excel('C:/Users/hanbre/Documents/CMIP5_Models_Air_Temp_One_Member.xlsx')
CMIP = CMIP[:2005]-273.15
CMIP = pd.rolling_mean(CMIP,60)

hadcrut = pd.read_excel('C:/Users/hanbre/Documents/hadcrut_temps.xlsx')
hadcrut = pd.rolling_mean(hadcrut,60)

had_20m = hadcrut.loc[1900:2000].mean()

hada = hadcrut[:2005]-had_20m

CMIPa = CMIP-had_20m['Global']

Cmean = CMIPa.mean(axis='columns')
Cstd = CMIPa.std(axis='columns')

plt.figure(figsize=(10,4))
plt.hold(True)

plt.plot(Cmean,linewidth=3,label='CMIP5 mean')
plt.plot(Cmean+Cstd,color='0.5',linewidth=2,label='CMIP5 std')
plt.plot(Cmean-Cstd,color='0.5',linewidth=2)
plt.plot(hada['Global'],linewidth=3,label='HadCRUT4')
plt.legend(fontsize=16)
plt.title('5 year rolling mean CMIP5 and HadCRUT4 global temperatures',fontsize=18)