import pandas as pd
import numpy as np
import os
import seaborn as sns
import matplotlib.pyplot as plt
# 批量读入173台风机的故障信息
os.chdir('./data/alarm information/')
file_chdir = os.getcwd()

filecsv_list = []
for root, dirs, files in os.walk(file_chdir):
    for file in files:
        if os.path.splitext(file)[1] == '.csv':
            filecsv_list.append(file)

data = pd.DataFrame()
for csv in filecsv_list:
    # 只读入需要的列
    data = data.append(pd.read_csv(csv, usecols=['故障描述', '故障时长(分)', '部件位置'], encoding='gb18030'))
# data = pd.read_csv("./data/alarm information/HFJ001 2017.01.02--2019.03.31.csv", encoding='gb18030')
# print(data.head(100))
# 故障描述共435种，部件位置19种
# print(data.describe())

# 去掉机组正常待机的数据
data1 = data[(data['故障描述'] != "机组正常待机") &
             (data['故障描述'] != "小风正常停机") &
             (data['故障描述'] != "维护模式") &
             (data['故障描述'] != "偏航自动解缆中") &
             (data['故障描述'] != "塔基手动正常停机")]
print(data1.describe())

print(data1.groupby(['部件位置']).count())
# 保存初步处理的数据
# data1.to_csv('info_preprocessing.csv', index=0)




