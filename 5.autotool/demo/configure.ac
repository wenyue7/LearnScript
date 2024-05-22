# configure.ac

AC_PREREQ([2.69])
AC_INIT([m_project], [1.0], [your.email@example.com])
# 用于检查源文件的存在性，以确保源文件目录是正确的
AC_CONFIG_SRCDIR([src/main.c])
# 定义了要生成的配置头文件。
AC_CONFIG_HEADERS([config.h])

# Checks for programs.
# 用于检查编译和安装工具是否存在
AC_PROG_CC
AC_PROG_INSTALL

# 指定一个或多个子目录，这些子目录应该包含自己的 configure.ac 文件和相关的
# Makefile 模板。
# AC_CONFIG_SUBDIRS([src lib doc])
AC_CONFIG_SUBDIRS([src])

AM_INIT_AUTOMAKE([-Wall -Werror foreign])
AUTOMAKE_OPTIONS = subdir-objects 

# 定义了要生成的Makefile文件
AC_CONFIG_FILES([Makefile src/Makefile])

AC_OUTPUT
