#!/bin/bash
#########################################################################
# File Name: run.sh
# Author: LiHongjin
# mail: 872648180@qq.com
# Created Time: Thu 30 May 2024 03:55:52 PM CST
#########################################################################

create_dir()
{
    if [ ! -d $1 ]; then echo "create dir $1"; mkdir -p $1; fi
}

create_dir build
cd build


CMAKE_PROGRAM=`which cmake`

ANDROID_NDK=${HOME}/work/android/ndk/android-ndk-r25c
TOOLCHAIN_FILE=${ANDROID_NDK}/build/cmake/android.toolchain.cmake
BUILD_TYPE="Release"
MAKE_PROGRAM=`which make`
ANDROID_ABI="armeabi-v7a with NEON"
ANDROID_STL="system"

${CMAKE_PROGRAM} -DCMAKE_TOOLCHAIN_FILE=${TOOLCHAIN_FILE}   \
    -DCMAKE_BUILD_TYPE=${BUILD_TYPE}                        \
    -DCMAKE_MAKE_PROGRAM=${MAKE_PROGRAM}                    \
    -DANDROID_FORCE_ARM_BUILD=ON                            \
    -DANDROID_NDK=${ANDROID_NDK}                            \
    -DANDROID_ABI=${ANDROID_ABI}                            \
    -DANDROID_NATIVE_API_LEVEL=${NATIVE_API_LEVEL}          \
    -DANDROID_STL=${ANDROID_STL}                            \
    ..

make
