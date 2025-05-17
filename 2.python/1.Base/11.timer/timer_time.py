#!/usr/bin/env python
#########################################################################
# File Name: timer_time.py
# Author: LiHongjin
# mail: 872648180@qq.com
# Created Time: Fri 27 Sep 11:37:50 2024
#########################################################################

import time

def timer(interval, callback):
    start_time = time.time()
    while True:
        elapsed_time = time.time() - start_time
        if elapsed_time >= interval:
            callback()
            start_time = time.time()  # 重置计时器

def my_callback():
    print("定时器触发")

# 设置定时器，每5秒执行一次回调函数
timer(5, my_callback)

