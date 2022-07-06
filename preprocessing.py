import pandas as pd
import json
import os


### Read data File ###

def read_huawei_heart_rate(file_name):
    """
    Reads a csv file and returns a dataframe
    """
    
    df = pd.read_csv(file_name)
    # 第三列为空，删除第三列
    df = df.drop(df.columns[2], axis=1)
    # 列名重命名
    df.columns = ['time', 'value']
    # time列转换为日期格式
    df['time'] = pd.to_datetime(df['time'])
    # 只读取2022-05-18之后的数据
    df = df[df['time'] > '2022-05-18']
    df = df[df['time'] < '2022-05-19']
    # 设置时间列为索引
    df.set_index('time', inplace=True)
    df.sort_index(inplace=True)
    
    
    return df


def read_huawei_blood_oxygen(file_name):
    
    df = pd.read_csv(file_name)
    # 第三列为空，删除第三列
    df = df.drop(df.columns[2], axis=1)
    # 列名重命名
    df.columns = ['time', 'value']
    # time列转换为日期格式
    df['time'] = pd.to_datetime(df['time'])
    # 只读取2022-05-18之后的数据
    df = df[df['time'] > '2022-05-18']
    df = df[df['time'] < '2022-05-19']
    # 设置时间列为索引
    df.set_index('time', inplace=True)
    df.sort_index(inplace=True)

    
    return df


def read_huawei_step_count(file_name):
    
    df = pd.read_csv(file_name)
    # 第三列为空，删除第三列
    df = df.drop(df.columns[2], axis=1)
    # 列名重命名
    df.columns = ['time', 'value']
    # time列转换为日期格式
    df['time'] = pd.to_datetime(df['time'])
    # 只读取2022-05-18之后的数据
    df = df[df['time'] > '2022-05-18']
    df = df[df['time'] < '2022-05-19']
    # 设置时间列为索引
    df.set_index('time', inplace=True)
    df.sort_index(inplace=True)
    
    return df



def read_e66_heart_rate(file_name):
    """
    Reads a json file and returns a dataframe
    """
    df = pd.read_json(file_name)
        
    # 只留下时间列和心率列
    df = df[['startTime', 'heartValue']]
    # 重命名
    df.columns = ['time', 'value']
    # 时间列转换为日期格式
    df['time'] = pd.to_datetime(df['time'], origin='1970-01-01 08:00:00', unit='ms')
    # 只留下5-18日的数据
    df = df[df['time'] > '2022-05-18']
    df = df[df['time'] < '2022-05-19']
    # 设置时间列为索引
    df.set_index('time', inplace=True)
    df.sort_index(inplace=True)
    
    return df


def read_e66_blood_oxygen(file_name):
    
    df = pd.read_json(file_name)
        
    # 只留下时间列和血氧列
    df = df[['startTime', 'OOValue']]
    # 重命名
    df.columns = ['time', 'value']
    # 时间列转换为日期格式
    df['time'] = pd.to_datetime(df['time'], origin='1970-01-01 08:00:00', unit='ms')
    # 只留下5-18日的数据
    df = df[df['time'] > '2022-05-18']
    df = df[df['time'] < '2022-05-19']
    # 设置时间列为索引
    df.set_index('time', inplace=True)
    df.sort_index(inplace=True)
    
    return df

    
def read_e66_step_count(file_name):
    
    df = pd.read_json(file_name)
        
    # 只留下时间列和步数列
    df = df[['startTime', 'stepValue']]
    # 重命名
    df.columns = ['time', 'value']
    
    df.to_csv('1.csv')
    # 时间列转换为日期格式
    df['time'] = pd.to_datetime(df['time'], origin='1970-01-01 08:00:00', unit='ms')
    df.to_csv('2.csv')
    # 只留下5-18日的数据
    df = df[df['time'] > '2022-05-18']
    df = df[df['time'] < '2022-05-19']
    # 设置时间列为索引
    df.set_index('time', inplace=True)
    df.sort_index(inplace=True)
    
    return df.diff()


def resample_5t(df):
    """
    Resamples the dataframe to 5 minutes
    """
    df = df.resample('5t').ffill()
    return df

def resample_1h(df):
    """
    Resamples the dataframe to 1 hour
    """
    df = df.resample('1h').sum()
    return df



### manipulate data ###
def generate_merge_df(df1, df2):
    """
    Generates a dataframe that contains all the data from both dataframes
    """
    df = pd.merge(df1, df2, on='time')
    df = df.dropna()
    df.columns = ['value1', 'value2']
    return df
    
def generate_np_array(df_column):
    """
    Generates a numpy array from a dataframe column
    """
    return df_column.values

def generate_description(df):
    """
    Generates a description of the dataframe
    """
    return df.describe()