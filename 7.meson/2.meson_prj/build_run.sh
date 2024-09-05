#!/usr/bin/env bash
#########################################################################
# File Name: build_run.sh
# Author: LiHongjin
# mail: 872648180@qq.com
# Created Time: Thu 05 Sep 2024 09:52:48 AM CST
#########################################################################

meson setup builddir
meson compile -C builddir
meson test -C builddir
