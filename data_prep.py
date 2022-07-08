import pandas as pd
import json
import os
import datetime

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
    # 重采样，每分钟一个点
    df = df.resample('5t').last()
    # 用相邻值填充缺失值
    df = df.fillna(method='ffill')
    
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
    # 重采样，每分钟一个点
    df = df.resample('5t').last()
    # 用相邻值填充缺失值
    df = df.fillna(method='ffill')
    
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
    # 重采样，每分钟一个点
    df = df.resample('5t').last()
    # 用相邻值填充缺失值
    df = df.fillna(0)
    
    return df.cumsum()



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
    # 重采样，每分钟一个点
    df = df.resample('5t').last()
    # 用相邻值填充缺失值
    df = df.fillna(method='ffill')
    
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
    # 重采样，每分钟一个点
    df = df.resample('5t').last()
    # 用相邻值填充缺失值
    df = df.fillna(method='ffill')
    
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
    # 重采样，每分钟一个点
    df = df.resample('1t').last()
    # 用相邻值填充缺失值
    df = df.fillna(method='ffill')
    
    return df
    
def read_f60_heart_rate(file_name):
    
    df = pd.read_json(file_name)
    # calendar column to int
    df['calendar'] = df['calendar'].astype(int)
    
    def generate_datetime(df):
        return datetime.datetime(df['calendar']//10000, df['calendar']%10000//100, df['calendar']%100, df['time']//60, df['time']%60)
    
    df['datetime'] = df.apply(lambda x: generate_datetime(x), axis=1)
    # df['datetime'] = datetime.datetime(df['calendar']//10000, df['calendar']%10000//100, df['calendar']%100, df['time']//60, df['time']%60)
    df.drop(['calendar'], axis=1, inplace=True)
    df.drop(['time'], axis=1, inplace=True)
    df.columns = ['value', 'time']
    df.set_index('time', inplace=True)
    return df



if __name__=='__main__':
    df = read_f60_heart_rate('/home/ubuntu/working-dir/huawei_data-proj/数据比较/data/2022-7-3/History-data-heartrate-2022-06-30-21-04-00.json')
    print(df)