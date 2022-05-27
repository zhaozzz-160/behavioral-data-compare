from unittest import result
import pandas as pd
import json
import os
from matplotlib import pyplot as plt
from sklearn.metrics import mean_absolute_error
from scipy import spatial

from data_prep import *


def compare_df(df1, df2):
    
    result = {}
    
    df = pd.merge(df1, df2, on='time')
    
    plt.plot(df.index, df[['value_x', 'value_y']])
    plt.show()
    
    result['mae'] = mean_absolute_error(df['value_x'], df['value_y'])
    result['describe'] = df.describe()
    result['cos_similarity'] = 1 - spatial.distance.cosine(df['value_x'], df['value_y'])
    
    return result


def main():
    
    huawei_data_path = '/home/ubuntu/working-dir/huawei_data-proj/数据比较/data/raw/huawei_heart_rate.csv'
    e66_data_path = '/home/ubuntu/working-dir/huawei_data-proj/数据比较/data/raw/e66.json'
    
    df1 = read_huawei_heart_rate(huawei_data_path)
    df2 = read_e66_heart_rate(e66_data_path)
    
    doc = compare_df(df1, df2)

    print(doc)
    
    

if __name__ == '__main__':
    main()
    