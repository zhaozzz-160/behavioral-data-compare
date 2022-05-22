import imp
from operator import index
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import json 
import os
import sys


def read_csv(file_name):
    """
    Reads a csv file and returns a dataframe
    """
    df = pd.read_csv(file_name)
        
    # drop the third column
    df = df.drop(df.columns[2], axis=1)
    
    # rename the columns
    df.columns = ['time', 'value']
    
    # convert to date time
    df['time'] = pd.to_datetime(df['time'])
    
    # 
    df = df[df['time'] > '2022-05-18']
    
    df.set_index('time', inplace=True)
    
    df = df.resample('1t').last()
    
    df = df.fillna(method='ffill')
    
    return df


def main():
    
    data_path = './data/raw/huawei.csv'
    
    data_df = read_csv(data_path)
    
    plt.plot(data_df.index, data_df['value'])
    plt.show()
    
    print(data_df)
    print(data_df.describe())
    
    


if __name__ == '__main__':
    main()