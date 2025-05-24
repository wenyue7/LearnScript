#!/usr/bin/env python
#########################################################################
# File Name: iterator.py
# Author: LiHongjin
# mail: 872648180@qq.com
# Created Time: Sat 24 May 08:59:30 2025
#########################################################################

# Python有内置的迭代器协议，通过__iter__和__next__方法实现：

# 自定义迭代器类
class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

# 使用自定义迭代器
for num in Counter(5, 10):
    print(num, end=' ')
# 输出: 5 6 7 8 9 10

# 使用生成器函数实现迭代器
def counter_generator(low, high):
    current = low
    while current <= high:
        yield current
        current += 1

# 使用生成器迭代器
for num in counter_generator(1, 5):
    print(num, end=' ')
# 输出: 1 2 3 4 5

# 内置容器迭代器
numbers = [10, 20, 30]
it = iter(numbers)
print(next(it))  # 输出: 10
print(next(it))  # 输出: 20
