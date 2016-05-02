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
matplotlib.use('PS')
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(font_scale=1.5)

CMIP=pd.read_excel('CMIP5_Models_Air_Temp_One_Member.xlsx')
CMIP = CMIP-273.15
CMIP = pd.rolling_mean(CMIP,60)

hadcrut = pd.read_excel('hadcrut_temps.xlsx')
hadcrut = pd.rolling_mean(hadcrut,60)

had_20m = hadcrut.loc[1900:2000].mean()

hada = hadcrut-had_20m

CMIPa = CMIP-had_20m['Global']

Cmean = CMIPa.mean(axis='columns')
Cstd = CMIPa.std(axis='columns')

fig=plt.figure(figsize=(10,4))
plt.hold(True)

plt.plot(CMIPa[:2005],linewidth=1,color='0.8')
plt.plot(Cmean[:2005],linewidth=3,label='CMIP5 mean')
plt.plot(Cmean[:2005]+Cstd[:2005],color='0.5',linewidth=2,label='CMIP5 std')
plt.plot(Cmean[:2005]-Cstd[:2005],color='0.5',linewidth=2)
plt.plot(hada['Global'].loc[:2005],linewidth=3,label='HadCRUT4')
plt.legend(fontsize=14,loc='upper left')
plt.title('5 year rolling mean CMIP5 and HadCRUT4 global temperatures',fontsize=16)
plt.xlabel('Year',fontsize='14')
plt.ylabel('Temperature ralative to HadCRUT4 1900-2000')

fig.savefig('hadcrut_cmip_comparison.png',bbox_inches='tight')

fig2=plt.figure(figsize=(10,4))
plt.hold(True)

plt.plot(CMIPa[2005:2016],linewidth=1,color='0.8')
plt.plot(Cmean[2005:2016],linewidth=3,label='CMIP5 mean')
plt.plot(Cmean[2005:2016]+Cstd[2005:2016],color='0.5',linewidth=2,label='CMIP5 std')
plt.plot(Cmean[2005:2016]-Cstd[2005:2016],color='0.5',linewidth=2)
plt.plot(hada['Global'].loc[2005:2016],linewidth=3,label='HadCRUT4')
plt.legend(fontsize=14,loc='upper left')
plt.title('5 year rolling mean CMIP5 and HadCRUT4 global temperatures',fontsize=16)
plt.xlabel('Year',fontsize='14')
plt.ylabel('Temperature ralative to HadCRUT4 1900-2000')

fig2.savefig('hadcrut_cmip_comparison2005-2016.png',bbox_inches='tight')
