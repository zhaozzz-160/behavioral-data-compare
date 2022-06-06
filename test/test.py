from heapq import merge
import sys
import os
sys.path.append(os.path.abspath("/home/ubuntu/working-dir/huawei_data-proj/数据比较/tscompare"))
from tscompare.comp_metrics import *
from tscompare.plot import *
from tscompare.preprocessing import *

df_huawei = read_huawei_heart_rate('data/huawei_blood_oxygen.csv')
df_e66 = read_e66_heart_rate('data/e66_heart_rate.csv')

merge_df = generate_merge_df(df_huawei, df_e66)

print(merge_df)