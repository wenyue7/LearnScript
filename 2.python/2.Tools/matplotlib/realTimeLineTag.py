#!/usr/bin/env python
#########################################################################
# File Name: realtimeline2.py
# Author: LiHongjin
# mail: 872648180@qq.com
# Created Time: Thu 26 Sep 21:00:11 2024
#########################################################################

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import itertools
import threading
import queue
import time

# 初始化数据
x_data = []
y_data = {}
lines = {}
tags = []  # 用于存储每条曲线的标签
texts = {}  # 用于存储每条曲线的文本对象

# 创建一个队列，用于线程间通信
tag_queue = queue.Queue()

# 创建图形
fig, ax = plt.subplots()

# 初始化函数：清空线条数据
def init():
    for line in lines.values():
        line.set_data([], [])
    return list(lines.values()) + list(texts.values())

# 更新函数：更新每帧数据
def update(frame):
    x_data.append(frame)

    # 处理来自其他线程的曲线调整请求
    while not tag_queue.empty():
        new_tags = tag_queue.get()
        adjust_curves(new_tags)

    # 动态生成 y 数据并更新每条曲线的数据
    for tag, line in lines.items():
        index = tags.index(tag)  # 每个标签的索引
        if len(y_data[tag]) == 0:
            y_data[tag] = []

        # 更新y数据
        y_data[tag].append(np.sin(frame + (index * np.pi / len(tags))))  # 不同标签有不同相位偏移

        # 确保x_data和y_data长度一致
        if len(y_data[tag]) < len(x_data):
            # 如果y_data短于x_data，用None或NaN填充
            y_data[tag] = [np.nan] * (len(x_data) - len(y_data[tag])) + y_data[tag]

        # 如果y_data比x_data长，截取x_data
        line.set_data(x_data[:len(y_data[tag])], y_data[tag])

        # 在曲线的右端显示标签
        if len(x_data) > 0 and len(y_data[tag]) > 0:
            texts[tag].set_position((x_data[-1], y_data[tag][-1]))  # 将文本放在线的终点
            texts[tag].set_text(tag)  # 设置标签内容

    # 动态调整 x 轴和 y 轴范围
    ax.set_xlim(min(x_data) - 1, max(x_data) + 1)
    ax.set_ylim(-1.5, 1.5)

    return list(lines.values()) + list(texts.values())

# 动态添加或删除曲线，并给每条曲线分配标签
def adjust_curves(new_tags):
    global tags, lines, y_data, texts

    # 如果有新标签，添加新曲线和对应的文本
    for tag in new_tags:
        if tag not in tags:
            tags.append(tag)
            line, = ax.plot([], [], lw=2)  # 创建新曲线
            lines[tag] = line
            y_data[tag] = []  # 初始化对应标签的y数据
            # 在曲线的最右端创建对应的文本标签
            texts[tag] = ax.text(0, 0, '', fontsize=9, verticalalignment='center')

    # 删除不存在的标签对应的曲线和文本
    for tag in tags[:]:
        if tag not in new_tags:
            # 移除对应的曲线
            lines[tag].remove()  # 从图中移除曲线
            texts[tag].remove()  # 从图中移除文本标签
            del lines[tag]  # 删除该标签对应的曲线对象
            del y_data[tag]  # 删除该标签对应的y数据
            del texts[tag]  # 删除该标签对应的文本对象
            tags.remove(tag)

# 模拟一个在后台运行的数据源变动
def data_source_simulation():
    time.sleep(2)  # 等待2秒后开始模拟数据变化
    for _ in range(5):
        # 每隔一段时间动态调整曲线标签
        new_tags = [f'curve_{i+1}' for i in range(np.random.randint(1, 5))]
        tag_queue.put(new_tags)
        time.sleep(3)

# 创建一个无限的迭代器
frames = itertools.count(start=0, step=0.1)

# 初始化曲线（初始有两条曲线）
adjust_curves(['curve_1', 'curve_2'])

# 创建动画
ani = FuncAnimation(fig, update, frames=frames, init_func=init, blit=True)

# 启动后台线程模拟数据源变动
threading.Thread(target=data_source_simulation, daemon=True).start()

# 显示动画
plt.show()
