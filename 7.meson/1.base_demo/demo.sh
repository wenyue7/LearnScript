#!/usr/bin/env bash
#########################################################################
# File Name: demo.sh
# Author: LiHongjin
# mail: 872648180@qq.com
# Created Time: Thu 05 Sep 2024 09:19:10 AM CST
#########################################################################

prj_name="meson_prj"


# 通过 Mesonn 初始化新的 C/C++ 项目，并使用 Meson 构建项目
# 创建一个新目录来保存项目文件
mkdir ${prj_name}
# 进入项目目录
cd ${prj_name}
# 使用Meson初始化并构建一个新的C/C++项目，会自动生成"meson.build"配置文件和C/C++源文件
meson init --name ${prj_name} --build
# 项目构建完成后，默认的构建目录是build，可以直接运行构建生成的可执行文件
build/${prj_name}


# 当项目代码发生变更后，可以进入 build 目录重新构建代码
# 进入build目录
cd build
# 重新构建代码
meson compile


# Meson 项目的顶层目录结构如下
# meson_prj
# ├── build               # Meson的构建目录
# ├── meson.build         # Meson的配置文件
# └── meson_project.c     # C/C++源文件
