# common.mk

CC := gcc
CFLAGS := -Wall -O2
FOO := value_from_common

# 如果你在 common.mk 中用了 override 关键字，则子目录无法覆盖（除非强制传参）。
# 避免滥用 override，除非你确定不让别人改。
override FIX_VAL := this is fix val
