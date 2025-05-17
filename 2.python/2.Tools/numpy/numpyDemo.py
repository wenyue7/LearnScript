#!/usr/bin/env python
#########################################################################
# File Name: numpyDemo.py
# Author: LiHongjin
# mail: 872648180@qq.com
# Created Time: Fri  6 Sep 18:15:12 2024
#########################################################################

import numpy as np

# 数组创建
arr = np.array([1, 2, 3, 4, 5])
print("一维数组:", arr)

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("二维数组:\n", arr_2d)

# 使用arange和linspace创建数值范围数组
range_arr = np.arange(0, 10, 2)  # 从0到10（不包括10），步长为2
print("arange数组:", range_arr)

linspace_arr = np.linspace(0, 10, 5)  # 从0到10，均匀生成5个数
print("linspace数组:", linspace_arr)

# 基本运算
arr_plus = arr + 5  # 数组与标量的加法
print("数组加标量:", arr_plus)

arr_mult = arr * arr  # 数组元素相乘
print("数组元素相乘:", arr_mult)

# 索引与切片
print("索引第一个元素:", arr[0])
print("切片第二个到第四个元素（不包括第四个）:", arr[1:4])

# 数组重塑
arr_reshape = arr_2d.reshape(1, 6)  # 将二维数组重塑为一行六列的数组
print("重塑后的数组:\n", arr_reshape)

# 广播机制
# 创建两个形状兼容的数组
arr_5x1 = np.array([[1], [2], [3], [4], [5]])  # 形状为 (5, 1)
arr_1x3 = np.array([[1, 2, 3]])  # 注意这里是一个 1x3 的数组，而不是 2x3
# 使用广播进行元素级乘法
# arr_5x1 的第二维（列）会被广播到与 arr_1x3 的第二维（列）相同的大小
result = arr_5x1 * arr_1x3
print("广播后的元素级乘法结果:\n", result)

# 线性代数
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# 矩阵乘法
print("矩阵A乘以矩阵B:\n", np.dot(A, B))

# 逆矩阵
if np.linalg.det(A) != 0:  # 检查行列式是否非零
    print("矩阵A的逆矩阵:\n", np.linalg.inv(A))

# 统计函数
print("数组arr的均值:", np.mean(arr))
print("数组arr的标准差:", np.std(arr))
print("数组arr的最大值:", np.max(arr))
print("数组arr的最小值及其索引:", np.min(arr), np.argmin(arr))

# 排序
sorted_arr = np.sort(arr)
print("排序后的数组:", sorted_arr)

# 过滤（布尔索引）
filtered_arr = arr[arr > 3]
print("大于3的元素:", filtered_arr)
