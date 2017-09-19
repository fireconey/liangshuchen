# 行索引可以打印出来但是不能修改，为了多个
# 数据中数据对应
import numpy as np
import pandas as pd
data=pd.Series([1,2,4])#一维向量，是一列，左边有index
data1=pd.Series([1,2,3],index=["a","b","c"])
print(data1["a"])


# 使用字典进行一维向量
data3=pd.Series({"a":2,
	"b":3})
print(data3.index.values[1],"****")

# loc 通过索引。可以第二个参数没有
data2=pd.DataFrame({
	"a":[1,2,3,4]
	})
print(data2.loc[0,["a"]])
# iloc 通过行数，列数来找
print(data2.iloc[0,0])

index=data2.index[1]

print(data2)