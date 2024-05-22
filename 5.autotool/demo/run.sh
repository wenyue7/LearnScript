#!/bin/bash
#########################################################################
# File Name: run.sh
# Author: LiHongjin
# mail: 872648180@qq.com
# Created Time: Tue 21 May 2024 08:18:45 PM CST
#########################################################################

set -e

autoreconf -i -f
# aclocal
# autoconf
# automake --add-missing
./configure
make
make dist
# sudo make install  # 如果需要安装的话
./src/mprj

set +e
