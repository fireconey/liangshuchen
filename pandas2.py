import numpy as np
import pandas as pd
# 表示列明不导入，自动为1，2，3.。。
pd.read_csv("ok.csv",header=None)
# columns是用于dataframe函数中
# names表示读取时的列名，index_col表示列值成行的索引（多少列）
op=pd.read_csv("ok.csv",names=[1,2,3,4])
op1=pd.read_csv("ok.csv",names=[1,2,3,4],index_col=[1,2])
print(op,"\n",op1)

# 有的行不读取
op2=pd.read_csv("ok.csv",skiprows=[1,2])
print(op2)

# 缺失的值补充
op3=pd.read_csv("ok.csv",na_values="s")


# 读取其中的几行
op4=pd.read_csv("ok.csv",nrows=2)
print(op4)


# 每隔多少行读取一次
op5=pd.read_csv("ok.csv",chunksize=1)
print(op5)

# 保存csv(只有表格结构的可以),空值使用NULL
op4.to_csv("data.csv",np_rep="NULL")