#!/bin/python3
#########################################################################
# File Name: 2.Tools/pyecharts/test2.py
# Author: LiHongjin
# mail: 872648180@qq.com
# Created Time: Tue Sep 12 09:41:25 2023
#########################################################################

# reference: https://pyecharts.org/#/zh-cn/quickstart

from pyecharts.charts import Bar

bar = Bar()
bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
bar.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
# render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
# 也可以传入路径参数，如 bar.render("mycharts.html")
bar.render()
