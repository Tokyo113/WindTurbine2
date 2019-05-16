import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("./data/alarm information/info_preprocessing.csv")
df = data.drop("故障时长(分)", axis=1)
print(df.describe())

# 1.部件位置分析：
pos = df["部件位置"]
# 各个位置故障百分比

pos = pos.where((pos == "桨叶硬件") |
          (pos == "控制器") |
          (pos == "偏航") |
          (pos == "变流器（控制器部分）") |
          (pos == "安全链") | (pos == "桨叶软件")
          | (pos == "齿轮箱")).fillna("其他")
print(pos.value_counts(normalize=True))

# 绘制饼图
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
lbs = pos.value_counts().index
plt.pie(pos.value_counts(normalize=True), labels=lbs, autopct="%1.1f%%",
        colors=sns.color_palette("Reds"))
plt.show()



