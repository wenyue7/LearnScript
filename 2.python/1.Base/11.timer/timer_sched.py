#!/usr/bin/env python
#########################################################################
# File Name: timer_sched.py
# Author: LiHongjin
# mail: 872648180@qq.com
# Created Time: Fri 27 Sep 11:40:02 2024
#########################################################################

import sched
import time

scheduler = sched.scheduler(time.time, time.sleep)

def my_callback():
    print("定时器触发")
    # 安排下一次执行
    scheduler.enter(5, 1, my_callback)

# 安排第一次执行
scheduler.enter(5, 1, my_callback)
scheduler.run()

