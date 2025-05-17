#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pandas as pd
import json

# JSON（JavaScript Object Notation，JavaScript 对象表示法），是存储和交换文本信息的语法，类似 XML。
# JSON 比 XML 更小、更快，更易解析

# to_string() 用于返回 DataFrame 类型的数据，
df = pd.read_json('sites.json')
print(df.to_string())
print()


# to_string() 用于返回 DataFrame 类型的数据，我们也可以直接处理 JSON 字符串
data =[
    {
      "id": "A001",
      "name": "菜鸟教程",
      "url": "www.runoob.com",
      "likes": 61
    },
    {
      "id": "A002",
      "name": "Google",
      "url": "www.google.com",
      "likes": 124
    },
    {
      "id": "A003",
      "name": "淘宝",
      "url": "www.taobao.com",
      "likes": 45
    }
]
df = pd.DataFrame(data)
print(df)
print()


# JSON 对象与 Python 字典具有相同的格式，所以我们可以直接将 Python 字典转化为 DataFrame 数据：
# 字典格式的 JSON
s = {
    "col1":{"row1":1,"row2":2,"row3":3},
    "col2":{"row1":"x","row2":"y","row3":"z"}
}
# 读取 JSON 转为 DataFrame
df = pd.DataFrame(s)
print(df)
print()


# 从 URL 中读取 JSON 数据
URL = 'https://static.runoob.com/download/sites.json'
df = pd.read_json(URL)
print(df)
print()


# 假设有一组内嵌的 JSON 数据文件 nested_list.json , 使用以下代码格式化完整内容
df = pd.read_json('nested_list.json')
print(df)
# 使用 Python JSON 模块载入数据
with open('nested_list.json','r') as f:
    data = json.loads(f.read())
# 展平数据
df_nested_list = pd.json_normalize(data, record_path =['students'])
print(df_nested_list)

# 显示结果还没有包含 school_name 和 class 元素，如果需要展示出来可以使用 meta 参数来显示这些元数据
with open('nested_list.json','r') as f:
    data = json.loads(f.read())
# 展平数据
df_nested_list = pd.json_normalize(
    data,
    record_path =['students'],
    meta=['school_name', 'class']
)
print(df_nested_list)
print()


# 更复杂的 JSON 数据，嵌套了列表和字典 nested_mix.json
# 使用 Python JSON 模块载入数据
with open('nested_mix.json','r') as f:
    data = json.loads(f.read())
# 展平数据
df = pd.json_normalize(
    data,
    record_path =['students'],
    meta=[
        'class',
        ['info', 'president'],
        ['info', 'contacts', 'tel']
    ]
)
print(df)
print()


# 读取内嵌数据中的一组数据，只读取内嵌中的 math 字段
# 这里我们需要使用到 glom 模块来处理数据套嵌，glom 模块允许我们使用 . 来访问内嵌对象的属性
from glom import glom
df = pd.read_json('nested_deep.json')
data = df['students'].apply(lambda row: glom(row, 'grade.math'))
print(data)
