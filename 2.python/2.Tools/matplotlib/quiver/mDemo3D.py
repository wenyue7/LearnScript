#!/usr/bin/env python
#########################################################################
# File Name: mDemo3D.py
# Author: LiHongjin
# mail: 872648180@qq.com
# Created Time: Mon 26 Aug 20:09:26 2024
#########################################################################

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

x = np.array([0, 0])
y = np.array([1, 0])
z = np.array([1, 0])
u = np.array([4, -4])
v = np.array([4, 0])
w = np.array([4, 0])

# Make the direction data for the arrows
# normallize: 归一化，False可以让变量保持正常大小
ax.quiver(x, y, z, u, v, w, normalize=False, arrow_length_ratio=0.1)

# 设置坐标轴范围
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
ax.set_zlim([-5, 5])

# 设置标签
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
