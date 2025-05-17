#!/opt/homebrew/anaconda3/bin/python

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(1, 2)


# cell color
colColors = ["#377eb8"]
colColors.extend(["#00ccff"] * 2)
cellColors = [colColors, colColors, colColors, colColors, colColors]
# 单元格数据
data = [[1, 1, 0],
        [0, 0, 0],
        [1, 0, 0],
        [0, 0, 1],
        [0, 0, 0]]

# 左图侧边栏，如果不需要，在plt.table中注释即可
# rowLabels 与 rowColours中的数据长度要保持一致，同时和数据中的元素个数保持一致--len(data)
rowLabels = ['state', '↑', '↓', '←', '→']
rowColours = ["#EBB25E", "#F0C9C0", "#F0C9C0", "#F0C9C0", "#F0C9C0"]

# 列表头颜色，需要和单条数据长度保持一致--len(data[0])
column_labels = ["1", "2", "3"]
colColors = ["#377eb8"]
colColors.extend(["#00ccff"] * 20)

column_w = [0.1, 0.2, 0.1]

# 取消坐标轴
ax[0].axis('off')
ax[0].table(cellText=data,           # 单元格内容
            cellColours=cellColors,  # 单元格颜色
            cellLoc='center',        # 单元格文本对齐方式
            colWidths=column_w,      # 单元格宽度，以ax横轴为单位，整个 ax 为一个单位，因此这里的值需要为小数
            colLabels=column_labels, # 列表头文本
            colColours=colColors,    # 列表头背景色
            colLoc='center',         # 列表头对齐方式
            rowLabels=rowLabels,     # 行表头文本
            rowColours=rowColours,   # 行表头背景色
            rowLoc='center',         # 行表头对齐方式
            loc="center")            # 单元格相对于子图的位置


#数据转置，右侧图数据
transpose_data = np.array(data)
transpose_data = np.transpose(transpose_data).tolist()
# print(transpose_data)
# 取消坐标轴
ax[1].axis('off')
ax[1].table(cellText=transpose_data,
            colLabels=rowLabels,
            colColours=rowColours,
            rowLabels=column_labels,
            rowColours=colColors,
            cellLoc='center',
            rowLoc='center',
            colLoc='center',
            loc="center")

# 将图标保存到硬盘
# plt.savefig('fix.jpg', dpi=300)
plt.show()

