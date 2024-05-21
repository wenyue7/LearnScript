[Makefile由浅入深--教程、干货](https://zhuanlan.zhihu.com/p/47390641)


# Makefile 组成
Makefile里主要包含了五个东西：变量定义、显式规则、隐晦规则、文件指示和注释。
1、变量的定义。在Makefile中我们要定义一系列的变量，变量一般都是字符串，这个有点像
    C语言中的宏，当Makefile被执行时，其中的变量都会被扩展到相应的引用位置上。
2、显式规则。显式规则说明了，如何生成一个或多的的目标文件。这是由Makefile的书写者
    明显指出，要生成的文件，文件的依赖文件，生成的命令。 刚才写的疑似shell脚本的
    Makefile全部都是显示规则。
3、隐晦规则。由于我们的make有自动推导的功能，所以隐晦的规则可以让我们比较粗糙地
    简略地书写Makefile，这是由make所支持的。
4、文件指示。其包括了三个部分，一个是在一个Makefile中引用另一个Makefile，就像C语言
    中的include一样。
5、注释。Makefile中只有行注释，和UNIX的Shell脚本一样，其注释是用“#”字符，这个就像
    C/C++中的“//”一样。如果你要在你的Makefile中使用“#”字符。

# 复杂一些的Makefile
接下来对Makefile一层一层的改写，首先是隐晦规则，告诉大家其中一种用法：
这个隐晦规则其实在指明，后缀为cpp的文件怎么编译成.o，后缀为c的文件怎么编译成.o。
代码如下
```Makefile
#隐含规则
INCL=-I${HOME}/incl

.SUFFIXES: .cpp .c
.cpp.o:
	g++ ${INCL} -c $<

.c.o:
	gcc ${INCL} -c $<

#C++编译
hellocpp:hellocpp.o
	# 隐含变量已经定义 g++ ${INCL} -c hellocpp.cpp 无需再写
	echo "开始编译"
	g++ -o hellocpp hellocpp.o
	rm -f hellocpp.o
	mv hellocpp ${HOME}/bin
	echo "编译结束"

#C编译
hello:hello.o
	# 隐含变量已经定义 g++ ${INCL} -c hello.cpp 无需再写
	echo "开始编译"
	gcc -o hello hello.o
	rm -f hello.o
	mv hello ${HOME}/bin
	echo "编译结束"
```
# 预定义变量
```
$*    不包含扩展名的目标文件名称。
$+    所有的依赖文件，以空格分开，并以出现的先后为序，可能包含重复的依赖文件。
$<    第一个依赖文件的名称。
$?    所有的依赖文件，以空格分开，这些依赖文件的修改日期比目标的创建日期晚。
$@    所有目标文件的完整名称。
$^    所有的依赖文件，以空格分开，不包含重复的依赖文件。
$%    如果目标是归档成员，则该变量表示目标的归档成员名称。
```

举例：
```Makefile
INCL=-I${HOME}/incl
BIN=$(HOME)/bin
OBJ1=hellocpp.o
OBJ2=hello.o

.SUFFIXES: .cpp .c
.cpp.o:
	g++ ${INCL} -c $<

.c.o:
	gcc ${INCL} -c $<

all: hellocpp hello

#C++编译
hellocpp:${OBJ1}
	@echo "============开始编译============"
	g++ -o $@ $?
	@rm -f ${OBJ1}
	@mv $@ ${BIN}
	@echo "============编译结束============"
	@echo ""

#C编译
hello:${OBJ2}
	@echo "============开始编译============"
	gcc -o $@ $?
	@rm -f ${OBJ2}
	@mv $@ ${BIN}
	@echo "============编译结束============"
	@echo ""
```
命令前加@，表示当前命令不显示