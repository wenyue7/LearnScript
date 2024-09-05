#!/usr/bin/env bash
#########################################################################
# File Name: build.sh
# Author: LiHongjin
# mail: 872648180@qq.com
# Created Time: Thu 05 Sep 2024 09:52:48 AM CST
#########################################################################

meson setup build --cross-file cross_file.txt
meson compile -C build
meson test -C build
