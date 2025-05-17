#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd


df = pd.read_excel('excel_testdata.xlsx')

print(df)

# 返回第一行
print(df.loc[0])
# 返回第一行和第二行
print(df.loc[[0,1]])
# 返回第二列和第三列
print(df.iloc[:, 1:3])

# 返回第一行第三列的数据
print()
print(df.loc[[0], ["客户分类"]])
print(df.iloc[0, 3])
# 对返回的Series操作
print(df.loc[0][3])
print(df.iloc[0][3])
