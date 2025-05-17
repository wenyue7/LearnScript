#!/usr/bin/env python
#########################################################################
# File Name: mDemo.py
# Author: LiHongjin
# mail: 872648180@qq.com
# Created Time: Mon 26 Aug 18:09:50 2024
#########################################################################

import matplotlib.pyplot as plt
import numpy as np

# Create a single vector
# 两个向量的起点由X，Y指定，分别是：(0, 1) (0, -1)
# 两个向量的终点由X，Y指定，分别是：(4, 5) (-4, -1)
# 终点的值是相对于起点的偏移，因此要以原点叠加偏移
X = np.array([0, 0])
Y = np.array([1, -1])
U = np.array([4, -4])
V = np.array([4, 0])

# Create the plot
fig, ax = plt.subplots()

# Add the vector V to the plot
q = ax.quiver(X, Y, U, V, angles='xy', scale_units='xy', scale=1, color='r')
ax.quiverkey(q, X=0.3, Y=1.1, U=10,
             label='Quiver key, length = 10', labelpos='E')

# Set the x-limits and y-limits of the plot
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])

# Show the plot along with the grid
plt.grid()
plt.show()
