#coding:utf-8
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv("./data/alarm information/info_preprocessing.csv")
df = data.drop("故障描述", axis=1)
print(df.describe())
# 各个部件的平均停机时间
print(df.groupby("部件位置").mean())

# 1.齿轮箱故障详细分析
gearBox = data[data["部件位置"] == "齿轮箱"].drop("故障时长(分)", axis=1)
print(gearBox.groupby("故障描述").count())


plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
sns.set(font='SimHei')
sns.set_style(style="whitegrid")
sns.set_context(context="talk", font_scale=0.4)
sns.set_palette([sns.color_palette("RdBu", n_colors=7)[5]])
sns.countplot(y="故障描述", data=gearBox)
plt.show()