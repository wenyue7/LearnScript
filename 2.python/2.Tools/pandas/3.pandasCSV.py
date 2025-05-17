#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd

# CSV（Comma-Separated Values，逗号分隔值，有时也称为字符分隔值，因为分隔字符也可以不是逗号），
# 其文件以纯文本形式存储表格数据（数字和文本）。

# CSV 是一种通用的、相对简单的文件格式，被用户、商业和科学广泛应用。


df = pd.read_csv('nba.csv')
print(df.to_string())
print()


# to_string() 用于返回 DataFrame 类型的数据，如果不使用该函数，则输出结果为数据的
# 前面 5 行和末尾 5 行，中间部分以 ... 代替
print(df)
print()


# 也可以使用 to_csv() 方法将 DataFrame 存储为 csv 文件：
# 三个字段 name, site, age
nme = ["Google", "Runoob", "Taobao", "Wiki"]
st = ["www.google.com", "www.runoob.com", "www.taobao.com", "www.wikipedia.org"]
ag = [90, 40, 80, 98]
# 字典
dict = {'name': nme, 'site': st, 'age': ag}
df = pd.DataFrame(dict)
# 保存 dataframe
df.to_csv('site.csv')
print()


# head( n ) 方法用于读取前面的 n 行，如果不填参数 n ，默认返回 5 行, 指定参数可以返回指定的行数
df = pd.read_csv('nba.csv')
print(df.head(2))
print()


# tail( n ) 方法用于读取尾部的 n 行，如果不填参数 n ，默认返回 5 行，空行各个字段的值返回 NaN，
# 指定参数可以返回指定的行数
df = pd.read_csv('nba.csv')
print(df.tail(3))
print()


# info() 方法返回表格的一些基本信息
df = pd.read_csv('nba.csv')
print(df.info())
print()
