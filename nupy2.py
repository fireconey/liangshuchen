# 数据的列累加运算
import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)
result=arr.cumsum(0)
# print("*********",result)

# 行的累乘
result=arr.cumprod(1)
print("*****",result)

arr1=np.arange(10)
print(np.sort(arr1))