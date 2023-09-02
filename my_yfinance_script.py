import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
plt.style.use('seaborn')

import yfinance as yf

msft = yf.Ticker('MSFT')

stockinfo=msft.info

#for key,value in stockinfo.items():
#    print(key,":",value)
#numshares=msft.info['sharesOstanding']
#print(numshares)
#print(msft.dividends)

#print(msft.institutional_holders)
#print(type(msft.dividends))

df=msft.dividends
print(df)

data=df.resample('Y').sum()

data=data.reset_index()
data['Year']=data["Date"].dt.year

plt.figure()
plt.bar(data['Year'],data['Dividends'])
plt.ylabel('Dividend Yiled($)')
plt.xlabel('Year')
plt.title("Microsoft Dividends History ")
plt.xlim(2002,2023)
plt.show()
