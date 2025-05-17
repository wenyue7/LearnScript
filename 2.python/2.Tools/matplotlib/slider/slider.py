#!/usr/bin/env python
#########################################################################
# File Name: slider.py
# Author: LiHongjin
# mail: 872648180@qq.com
# Created Time: Mon 26 Aug 21:17:02 2024
#########################################################################

import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np

# 生成数据
x = np.linspace(0, 10, 100)
a_initial = 1  # 初始值

# 创建图形和轴
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.25)  # 调整图表以留出空间放置滑杆
line, = ax.plot(x, a_initial * np.sin(x), lw=2)

# 设置坐标轴范围
ax.set_xlim([0, 10])
ax.set_ylim([-10, 10])

# 创建滑杆
ax_slider = plt.axes([0.1, 0.1, 0.8, 0.03])  # 滑杆位置 [left, bottom, width, height]
slider = Slider(ax_slider, 'Amplitude', 0.1, 10.0, valinit=a_initial)

# 定义滑杆更新函数
def update(val):
    amp = slider.val
    line.set_ydata(amp * np.sin(x))  # 更新曲线数据
    fig.canvas.draw_idle()  # 更新图形

# 连接滑杆和更新函数
slider.on_changed(update)

plt.show()
