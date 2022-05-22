import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import json 
import os
import sys


def read_json(file_name):
    """
    Reads a json file and returns a dataframe
    """
    df = pd.read_json(file_name)
        
    # drop the third column
    df = df[['startTime', 'heartValue']]
    
    # rename the columns
    df.columns = ['time', 'value']
    
    # convert to date time
    # df['time'] = df['time'].dt.date
    
    df['time'] = pd.to_datetime(df['time'], unit='ms')
    
    # # 
    df = df[df['time'] > '2022-05-18']
    df = df[df['time'] < '2022-05-19']
    
    df.set_index('time', inplace=True)
    
    df = df.resample('1t').last()
    
    df = df.fillna(method='ffill')
    
    return df


def main():
    
    data_path = './data/raw/e66.json'
    
    data_df = read_json(data_path)
    
    plt.plot(data_df.index, data_df['value'])
    plt.show()
    
    print(data_df)
    print(data_df.describe())
    
    


if __name__ == '__main__':
    main()