#!/usr/bin/env python
#########################################################################
# File Name: timer_apscheduler.py
# Author: LiHongjin
# mail: 872648180@qq.com
# Created Time: Fri 27 Sep 11:40:30 2024
#########################################################################

# pip install apscheduler

from apscheduler.schedulers.blocking import BlockingScheduler

def my_callback():
    print("定时器触发")

scheduler = BlockingScheduler()
scheduler.add_job(my_callback, 'interval', seconds=5)

scheduler.start()

