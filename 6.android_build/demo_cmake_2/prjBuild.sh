#!/bin/bash
#########################################################################
# File Name: run.sh
# Author: LiHongjin
# mail: 872648180@qq.com
# Created Time: Thu 30 May 2024 04:40:41 PM CST
#########################################################################

create_dir()
{
    if [ ! -d $1 ]; then echo "create dir $1"; mkdir -p $1; fi
}

create_dir build
cd build

# 生成构建文件
export NDK_ROOT=/home/lhj/work/android/ndk/android-ndk-r25c

# 如果想用make进行构建，可以去掉 -G Ninja
cmake -DCMAKE_TOOLCHAIN_FILE=$NDK_ROOT/build/cmake/android.toolchain.cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DANDROID_ABI=$ANDROID_ABI \
    -DANDROID_PLATFORM=$ANDROID_PLATFORM \
    -G Ninja \
    ..

# 构建项目
ninja
# make
