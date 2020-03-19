import pandas as pd
import matplotlib.pyplot as plt

datafile = '../stock/AAPL.csv'
#This creates a dataframe from the CSV file:
data = pd.read_csv(datafile, index_col = 'Date')
data

#This selects the 'Adj Close' column
close = data['Adj Close']
#This converts the date strings in the index into pandas datetime format:
close.index = pd.to_datetime(close.index)
close


sma50 = close.rolling(window=50).mean()
sma50.iloc[45:52]

sma20 = close.rolling(window=20).mean()

#The size for our chart:
plt.figure(figsize = (12,6))
#Plotting price and SMA lines:
plt.plot(close, label='AAPL Adj Close', linewidth = 2)
plt.plot(sma20, label='20 day rolling SMA', linewidth = 1.5)
plt.plot(sma50, label='50 day rolling SMA', linewidth = 1.5)
#Adding title and labeles on the axes, making legend visible:
plt.xlabel('Date')
plt.ylabel('Adjusted closing price ($)')
plt.title('Price with a single Simple Moving Average')
plt.legend()
plt.show()
