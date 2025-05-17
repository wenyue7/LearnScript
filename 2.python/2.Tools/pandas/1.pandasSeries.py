#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd

# Pandas Series 类似表格中的一个列（column），类似于一维数组，可以保存任何数据类型。
# Series 由索引（index）和列组成，函数如下：
#     pandas.Series( data, index, dtype, name, copy)
# 参数说明：
#     data：一组数据(ndarray 类型)。
#     index：数据索引标签，如果不指定，默认从 0 开始。
#     dtype：数据类型，默认会自己判断。
#     name：设置名称。
#     copy：拷贝数据，默认为 False。

# Series 可以通过设置的索引或者下标访问

a = [3, 6, 9]
# 第一列是索引，第二列是值
myvar = pd.Series(a)
print(myvar)
print(myvar[1])
print()


# 指定索引值
myvar2 = pd.Series(a, index=["x", "y", "z"])
print(myvar2)
print(myvar2["y"])
print(myvar2[2])
print()


sites = {1: "Google", 2: "Runoob", 3: "Wiki"}
# 也可以使用 key/value 对象，类似字典来创建 Series
myvar3 = pd.Series(sites)
print(myvar3)
print()


# 如果只需要字典中的一部分数据，只需要指定需要数据的索引即可
myvar4 = pd.Series(sites, index = [1, 3])
print(myvar4)
print()


# 设置 Series 名称参数
myvar5 = pd.Series(sites, index = [1, 2], name="RUNOOB-Series-TEST" )
print(myvar5)
print()
