# submit 编辑器中文件名和模块必须不同名
# 否则将变成此模块没有这个属性。
import numpy as np
# 带有判断语句的赋值
x=np.array([1,2,3])
y=np.array([4,5,6])
cond=np.array([True,False,True])
result=[(x if c else y) for x,y,c in zip(x,y,cond)]
print(result)
# 使用where函数来达到相同结果

arr=np.where(cond,x,y)
print(arr)
# 两个where还可以圈套。




