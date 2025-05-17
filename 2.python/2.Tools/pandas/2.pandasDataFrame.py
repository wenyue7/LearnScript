#!/usr/bin/python
# -*- coding: UTF-8 -*-

import numpy as np
import pandas as pd

# DataFrame 是一个表格型的数据结构，它含有一组有序的列，每行/列都可以看做是一个Series,
# 每列可以是不同的值类型（数值、字符串、布尔型值）。
# DataFrame 既有行索引也有列索引，它可以被看做由 Series 组成的字典（共同用一个索引）。
# DataFrame 构造方法如下：
#     pandas.DataFrame( data, index, columns, dtype, copy)
# 参数说明：
#     data：一组数据(ndarray、series, map, lists, dict 等类型)。
#     index：索引值，或者可以称为行标签。
#     columns：列标签，默认为 RangeIndex (0, 1, 2, …, n) 。
#     dtype：数据类型。
#     copy：拷贝数据，默认为 False。

# 从DataFrame中通过 loc/iloc 取出多行多列时，返回的时 DataFrame 类型
# 取出一行/列时，返回的时 Series 类型
# 取出一行一列，即一个单元格时，loc 返回的是 DataFrame 类型，iloc 返回的时当前单元格的数据类型
# 使用 loc/iloc 取数据时，行列索引是不计算在内的


data = [['Google',10],['Runoob',12],['Wiki',13]]
df = pd.DataFrame(data, columns=['Site','Age'], dtype=float)
print(df)
print()


# 以下实例使用 ndarrays 创建，ndarray 的长度必须相同， 如果传递了 index，则索引的长度应
# 等于数组的长度。如果没有传递索引，则默认情况下，索引将是range(n)，其中n是数组长度。
data = {'Site':['Google', 'Runoob', 'Wiki'], 'Age':[10, 12, 13]}
df = pd.DataFrame(data)
print(df)
print()


# 还可以使用字典（key/value），其中字典的 key 为列名，没有对应的部分数据为 NaN。
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
print(df)
print()


# Pandas 可以使用 loc 属性返回指定行的数据，如果没有设置索引，第一行索引为 0，第二行索引为 1，以此类推,
# 这时返回结果其实就是一个 Pandas Series 数据。
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
# 数据载入到 DataFrame 对象
df = pd.DataFrame(data)
print(df)
# 返回第一行
print(df.loc[0])
# 返回第二行
print(df.loc[1])
# 也可以返回多行数据，使用 [[ ... ]] 格式，... 为各行的索引，以逗号隔开,
# 这时返回结果其实就是一个 Pandas DataFrame 数据
print(df.loc[[0, 1]])
print()


# 可以指定索引值
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df)
print()


# Pandas 可以使用 loc 属性返回指定索引对应到某一行：
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
# 指定索引
print(df.loc["day2"])
print()


# iloc函数根据行号/列号取值
# loc函数根据行/列具体的 属性/行索引名 取值
# 在没有给定属性或者行名时，会默认以索引编号，这个时候loc可以通过索引名来取值
# 当通过loc取到数据之后，也可以直接根据索引取值，因为这个时候实际上是对Series操作，而非 dataFrame
print("========> iloc and loc <========")

# iloc取一行
data = pd.DataFrame(np.arange(16).reshape(4, 4),
                    index=['tony', 'andy', 'lucy', 'john'],
                    columns=['math', 'history', 'chemicy', 'english'])
print(data)
print("==> iloc取一行")
data1 = data.iloc[1]
print('data1:', data1)
print(type(data1))
# iloc取多行
print("==> iloc取多行")
data2 = data.iloc[0:2]
print('data2:', data2)
print(type(data2))
# iloc取一列
print("==> iloc取一列")
data3 = data.iloc[:, 1]
print('data3:', data3)
print(type(data3))
# iloc取多列
print("==> iloc取多列")
data4 = data.iloc[:, 1:3]
print('data4:', data4)
print(type(data4))
# iloc取一行一列
print("==> iloc取一行一列")
data5 = data.iloc[1, 2]
print('data5:', data5)
print(type(data5))
# iloc取多行多列
print("==> iloc取多行多列")
data6 = data.iloc[0:2, 1:3]
print('data6:', data6)
print(type(data6))
# iloc取所有行所有列
print("==> iloc取所有行所有列")
data66 = data.iloc[:, :]
print('data66:', data66)
print(type(data66))
print()

# loc取一行
print("==> loc取一行")
data7 = data.loc['andy']
print('data7:', data7)
print(type(data7))
# loc取多行
print("==> loc取多行")
data8 = data.loc[['andy', 'john'], :]
print('data8:', data8)
print(type(data8))
# loc取一列
print("==> loc取一列")
data9 = data.loc[:, 'chemicy']
print('data9:', data9)
print(type(data9))
# loc取多列
print("==> loc取多列")
data10 = data.loc[:, ['english', 'history']]
print('data10:', data10)
print(type(data10))
# loc取一行一列
print("==> loc取一行一列")
data11 = data.loc[['john'], ['history']]
print('data11:', data11)
print(type(data11))
# loc取多行多列
print("==> loc取多行多列")
data12 = data.loc[['andy', 'john'], ['english', 'history']]
print('data12:', data12)
print(type(data12))
# loc取所有行所有列
print("==> loc取所有行所有列")
data122 = data.loc[:, :]
print('data122:', data122)
print(type(data122))
