#!/bin/python3
#########################################################################
# File Name: tqdm_demo.py
# Author: LiHongjin
# mail: 872648180@qq.com
# Created Time: Thu Oct 19 14:09:27 2023
#########################################################################

import time
from tqdm import tqdm, trange

# ======> 基于迭代对象运行: tqdm(iterator) <======

#trange(i)是tqdm(range(i))的一种简单写法
for i in trange(100):
    time.sleep(0.05)

for i in tqdm(range(100), desc='Processing'):
    time.sleep(0.05)

dic = ['a', 'b', 'c', 'd', 'e']
pbar = tqdm(dic)
for i in pbar:
    pbar.set_description('Processing ' + i)
    time.sleep(0.2)


# ======> 手动进行更新 <======

with tqdm(total=200) as pbar:
    pbar.set_description('Processing:')
    # total表示总的项目, 循环的次数20*10(每次更新数目) = 200(total)
    for i in range(20):
        # 进行动作, 这里是过0.1s
        time.sleep(0.1)
        # 进行进度更新, 这里设置10个
        pbar.update(10)
