#!/usr/bin/env python
#########################################################################
# File Name: sliders.py
# Author: LiHongjin
# mail: 872648180@qq.com
# Created Time: Mon 26 Aug 08:17:02 2024
#########################################################################

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

# 创建一个图形和轴
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)  # 为滑杆留出空间
t = np.arange(0.0, 1.0, 0.001)
s = np.sin(2 * 2 * np.pi * t)
l, = plt.plot(t, s, lw=2)

# 初始化两个滑杆
axcolor = 'lightgoldenrodyellow'
axfreq = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
axamp = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)

sfreq = Slider(axfreq, 'Freq', 0.1, 30.0, valinit=2)
samp = Slider(axamp, 'Amp', 0.1, 10.0, valinit=1)

# 定义更新函数，根据滑杆的值更新图形
def update(val):
    amp = samp.val
    freq = sfreq.val
    l.set_ydata(amp*np.sin(2*np.pi*freq*t))
    fig.canvas.draw_idle()

# 链接滑杆事件到更新函数
sfreq.on_changed(update)
samp.on_changed(update)

# 显示图形
plt.show()
