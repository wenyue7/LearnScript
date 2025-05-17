#!/usr/bin/env python
#########################################################################
# File Name: timer_threading.py
# Author: LiHongjin
# mail: 872648180@qq.com
# Created Time: Fri 27 Sep 11:38:28 2024
#########################################################################

import threading

def my_timer(interval, callback):
    threading.Timer(interval, callback).start()

def my_callback():
    print("定时器触发")
    # 递归调用以重复定时器
    my_timer(5, my_callback)

# 设置定时器，5秒后执行回调函数
my_timer(5, my_callback)

