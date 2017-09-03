import sys 
import json 
from datetime import datetime 
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates 
import pandas as pd 
import numpy as np 

def reseries(all_dates):
    idx = pd.DatetimeIndex(all_dates) 
    ones = np.ones(len(all_dates)) 
    # the actual series (at series of 1s for the moment) 
    my_series = pd.Series(ones, index=idx) 
 
    # Resampling / bucketing into 15-minute buckets 
    per_minute = my_series.resample('15Min').sum().fillna(0) 

    return per_minute

with open('fakenewsq.json', 'r') as f: 
    all_dates = [] 
    
    for line in f: 
      tweet = json.loads(line) 
      all_dates.append(tweet.get('created_at'))

    per_minute = reseries(all_dates)

    # Plotting the series 
    fig, ax = plt.subplots() 
    ax.grid(True) 
    ax.set_title("Tweet Frequencies") 
     
    hours = mdates.MinuteLocator(interval=60) 
    date_formatter = mdates.DateFormatter('%H:%M') 
 
    datemin = datetime(2017, 8, 18, 10, 0) 
    datemax = datetime(2017, 8, 18, 20, 59) 
 
    ax.xaxis.set_major_locator(hours) 
    ax.xaxis.set_major_formatter(date_formatter) 
    ax.set_xlim(datemin, datemax) 
    max_freq = per_minute.max() 
    ax.set_ylim(0, max_freq) 
    ax.plot(per_minute.index, per_minute) 
    plt.show()

