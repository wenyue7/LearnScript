FLAGS = -Wall -Wextra
# 生成多个可执行文件
TARGETs = test test2

# SRCs = $(wildcard *.c)
SRCs = mfunc.c \
	   mfunc2.c \
	   test.c
OBJs = $(patsubst %.c, %.o, $(SRCs))
DEPs = $(wildcard *.h)
TARGET = test
MCRODEF = -D MCRO_TEST -DMCRO_TEST2=\"mcro2\"

SRCs2 = mfunc.c \
	   mfunc2.c \
	   test2.c
OBJs2 = $(patsubst %.c, %.o, $(SRCs2))
DEPs2 = $(wildcard *.h)
TARGET2 = test2

# $@ 在模式规则中，表示规则中的目标文件集。如果有多个目标，那么，"$@"就是匹配
#    目标中模式定义的集合。
# $< 依赖目标中的第一个目标名字。如果依赖目标是以模式（即"%"）定义的，那么"$<"将
#    是符合模式的一系列的文件集。注意，其是一个一个取出来的。
# $^ 所有的依赖目标的集合。以空格分隔。如果在依赖目标中有多个重复的，那个这个
#    变量会去除重复的依赖目标，只保留一份。
#
# 注意：
# 这里 $@ 的集合 和 $</$^ 的集合 含义是不一样的：
# $@ 的集合，意义在于使用规则模式时，用作推导，每次推导使用 $@ 中的一个元素，类似for循环
# $</$^ 的集合，与规则模式和推导无关，如果用在推导模式中使用，每次推导的值都是一样的，不会像 $@ 一样推导
#
# 使用模式规则时，一条指令可以多次执行的条件是:
# 1. 有多个目标文件，模式规则多次执行与依赖文件无关，只与目标文件有关
# 2. 目标文件被需要，即有其他目标依赖当前的目标文件，如果不被需要，则不会推导执行
# 验证demo如下：
# obj = obja objb
# src = test.c
#
# all : $(obj)
#
# # $(obj) : $(src)
# $(obj) :
# 	@echo ""
# 	@echo "obj: "$(obj)
# 	@echo '@: '$@
# 	@echo '^: '$^
# 	@echo '<: '$<



all : $(TARGETs)
.PHONY : all

$(TARGET) : $(OBJs)
	gcc -o $@ $^

$(OBJs) :
	gcc $(MCRODEF) -c $(subst .o,.c,$@) -o $@

$(TARGET2) : $(OBJs2)
	gcc -o $@ $^

$(OBJs2) :
	gcc $(MCRODEF) -c $(subst .o,.c,$@) -o $@

clean :
	-rm $(OBJs)
	-rm $(OBJs2)
	-rm $(TARGETs)
.PHONY : clean
