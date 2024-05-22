[使用 Autotools 配置、制作和安装程序](https://earthly.dev/blog/autoconf/)


# Autotools工具集简介

Autotools 是一个工具集合，用于帮助开发人员编写可移植的 Unix/Linux 软件包。这个
工具集合主要由 autoconf、automake、libtool 以及一些辅助工具，如autoheader、
aclocal和autoscan等组成，它们协同工作以生成标准的configure 脚本和 Makefile 文件，
从而使软件包的编译和安装过程自动化。

以下是这些工具及其相关文件之间的关系：

1. autoconf 和 configure.ac
   * autoconf：是一个用于生成 configure 脚本的工具。configure 脚本是一个 shell
     脚本，它检查系统上是否存在所需的库、头文件和其他资源，并设置构建系统所需的
     变量。Autoconf 是用M4sh编写的，使用m4宏。m4sh提供了一些在创建configure脚本时
     可以使用的宏，这也是无需编写太多实际代码即可生成大量脚本的部分原因。
   * configure.ac（或 configure.in 在较旧的版本中）：这是一个输入文件，用于 autoconf。
     它包含了 autoconf 的宏调用，这些宏调用指定了 configure 脚本应检查哪些资源和变量。

2. automake 和 Makefile.am
   * automake：是一个用于生成 Makefile.in 文件的工具。Makefile.in 是一个模板文件，
     它包含了 configure 脚本在运行时填充的变量。
   * Makefile.am：这是 automake 的输入文件。它使用了一种类似于 Makefile 的语法，
     但添加了一些额外的变量和规则，这些变量和规则用于生成最终的 Makefile。
     Automake 使用变量和主项来实现这一点。例如：`bin_PROGRAMS = helloworld`，其中
     主项是`_PROGRAMS`后缀。这给 automake 提供了程序的一些信息，例如希望将生成的
     二进制文件安装在哪里。
     常用的其他示例是`_SCRIPTS`（当想要在某处安装脚本而不是二进制文件时可以使用它）
     和`_DATA`（当您想要在安装中包含额外的数据文件时）。
     最后要提到的是，尽管 Makefile.in 很特别，因为它包含所有这些主文件，但它仍然
     是一个常规的 Makefile。 这意味着可以根据需要编写自己的定制目标。

3. configure 和 Makefile.in
   * configure：这是由 autoconf 生成的脚本。当你运行 ./configure 时，它会检查系统
     环境，并设置一些变量（如库路径、编译器标志等）。然后，它会使用这些变量来生成
     Makefile。
   * Makefile.in：这是由 automake 生成的模板文件。它包含了 Makefile 的大部分结构，
     但其中的一些变量（如库路径、编译器标志等）是空的，等待 configure 脚本来填充。

4. Makefile
   * Makefile：这是最终的构建文件，用于编译和安装软件包。它是由 configure 脚本使用
     Makefile.in 作为模板生成的。当你运行 make 命令时，它会读取这个 Makefile 并执行
     其中的指令来编译源代码、生成库和可执行文件等。

5. aclocal
   * aclocal用于生成aclocal.m4文件，该文件包含了configure.ac中使用的所有宏的定义。
     这确保了autoconf在处理configure.ac文件时能够找到所有必需的宏定义。如果在运行
     autoconf之前aclocal没有运行，那么将收到一条错误消息，缺少宏。

总结
```
configure.ac --(autoconf)--> configure  ----> Makefile
                                          ^
                                          |
Makefile.am  --(automake)--> Makefile.in --
```
configure 脚本检查系统环境，并使用 Makefile.in 作为模板生成最终的 Makefile。
开发人员使用 make 命令和生成的 Makefile 来编译和安装软件包。


configure.ac和Makefile.am的作用区别：
* configure.ac主要用于定义系统检查和变量设置，以生成适合当前系统环境的构建脚本和Makefile模板。
* Makefile.am则用于定义项目的构建目标和依赖关系，以及构建过程中所需的编译器和链接选项。

# 使用Autotools

## 编写 configure.ac

### AM_INIT_AUTOMAKE

AM_INIT_AUTOMAKE 宏的主要功能和参数如下：

1. 功能：
   * 初始化 Automake，确保 Automake 正常工作。
   * 允许你指定一些选项来定制生成的 Makefile.in 文件。

2. 参数：
   * `[OPTIONS...]`：可以指定一系列的选项来自定义 Automake 的行为。例如，可以使用
     -Wall 选项来让 Automake 报告所有的警告，或者使用 -Werror 选项来将警告当作
     错误处理。
   * subdir-objects：用于指示 Automake 在每个子目录中生成对象文件（.o 文件），
     而不是在源代码目录中生成。这有助于保持源代码目录的整洁，并允许并行构建。
   * foreign：这个选项告诉 Automake 使用 GNU 之外的构建系统约定。在某些情况下，
     你可能需要这个选项来确保与其他非 GNU 构建系统的兼容性。

在 configure.ac 文件中，可能会这样使用 AM_INIT_AUTOMAKE：
```m4
AC_INIT([my_project], [1.0], [bug-my_project@example.com])
...
AM_INIT_AUTOMAKE([-Wall -Werror subdir-objects foreign])
...
AC_CONFIG_FILES([Makefile src/Makefile])
AC_OUTPUT
```
在这个例子中，AM_INIT_AUTOMAKE 被初始化了，并带有 -Wall -Werror subdir-objects
foreign 选项。这意味着 Automake 将报告所有的警告，并将警告当作错误处理；在每个
子目录中生成对象文件；以及使用非 GNU 的构建系统约定。

注意，AM_INIT_AUTOMAKE 宏需要在 AC_CONFIG_HEADERS、AC_CHECK_HEADERS 等其他宏之后
调用，以确保所有的检查和初始化都已完成。

### AUTOMAKE_OPTIONS

AM_INIT_AUTOMAKE用于初始化Automake，而AUTOMAKE_OPTIONS用于在配置过程中设置Automake
的选项。如果把AUTOMAKE_OPTIONS的选项带到AM_INIT_AUTOMAKE中，理解效果也是一样的。

以下是一些常见的 AUTOMAKE_OPTIONS 设置及其解释：
1. subdir-objects：这个选项告诉 Automake 在每个子目录中生成对象文件（.o 文件），
   而不是在源代码目录中生成。这有助于保持源代码目录的整洁，并允许并行构建。
2. foreign：这个选项告诉 Automake 使用非 GNU 标准的构建系统约定。如果项目不符合
   GNU 标准（例如，你的项目不使用 Makefile.am 文件），可能需要这个选项。
3. dist-bzip2：如果项目需要分发为 .tar.bz2 格式，可以使用这个选项。这将在 make dist
   时生成一个 .tar.bz2 格式的归档文件。
4. no-dist-gzip：如果不希望使用 gzip 压缩你的分发文件（.tar.gz），可以使用这个选项。
5. 1.10 或其他版本号：可以指定一个 Automake 的版本号。这通常用于确保你的构建系统与
   所期望的 Automake 版本兼容。

在 configure.ac 文件中设置 AUTOMAKE_OPTIONS 的示例如下：
```m4
AC_INIT([my_project], [1.0], [bug-my_project@example.com])
...
AUTOMAKE_OPTIONS=subdir-objects foreign
...
AC_CONFIG_FILES([Makefile src/Makefile])
AC_OUTPUT
```
在这个示例中，AUTOMAKE_OPTIONS 被设置为 subdir-objects foreign，这意味着 Automake
将在每个子目录中生成对象文件，并使用非 GNU 标准的构建系统约定。

请注意，AUTOMAKE_OPTIONS 必须在 AC_CONFIG_HEADERS、AC_CHECK_HEADERS 等其他宏之后，
但在 AC_CONFIG_FILES 和 AC_OUTPUT 之前设置。同时，你也需要确保在运行 autoconf 生成
configure 脚本之前，已经安装了 Automake 工具。


### AC_CONFIG_FILES

AC_CONFIG_FILES告诉autoconf它应该找到一个名为`Makefile.in`的文件并根据我们指定的
内容替换占位符。这可以是版本或维护者之类的东西。AC_OUTPUT要放入configure.ac脚本的
最后一行，它告诉autoconf输出最终configure脚本。configure.ac文件应包含以下内容：
```
AC_INIT([helloworld], [0.1], [maintainer@example.com])
AM_INIT_AUTOMAKE
AC_PROG_CC
AC_CONFIG_FILES([Makefile])
AC_OUTPUT
```

### Demo

以下是一个简单的configure.ac文件的示例：
```aclocal
# -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.

AC_PREREQ([2.69])
AC_INIT([FULL-PACKAGE-NAME], [VERSION], [BUG-REPORT-ADDRESS])
AC_CONFIG_SRCDIR([src/main.c])
AC_CONFIG_HEADERS([config.h])

# Checks for programs.
AC_PROG_CC
AC_PROG_INSTALL

# Checks for libraries.
# 例如，检查是否存在libxml2库
PKG_CHECK_MODULES([LIBXML2], [libxml-2.0 >= 2.6.0])

# Checks for header files.
AC_CHECK_HEADERS([stdlib.h string.h])

# Checks for typedefs, structures, and compiler characteristics.
AC_TYPE_SIZE_T

# Checks for library functions.
AC_FUNC_MALLOC
AC_FUNC_REALLOC

# Define a macro to be used in the Makefile
AC_SUBST(CC)
AC_SUBST(CFLAGS)

# Output files
AC_CONFIG_FILES([Makefile src/Makefile])
AC_OUTPUT
```

在上面的示例中：
* AC_PREREQ          定义了生成configure脚本所需的autoconf版本。
* AC_INIT            设置了包的全名、版本和错误报告地址。
* AC_CONFIG_SRCDIR   用于检查源文件的存在性，以确保源文件目录是正确的。
* AC_CONFIG_HEADERS  定义了要生成的配置头文件。
* AC_PROG_CC和AC_PROG_INSTALL等 用于检查编译和安装工具是否存在。
* PKG_CHECK_MODULES  用于检查指定的库是否存在，并设置相应的变量。
* AC_CHECK_HEADERS   用于检查头文件是否存在。
* AC_TYPE_SIZE_T等   用于检查类型、结构和编译器特性。
* AC_FUNC_MALLOC等   用于检查库函数是否存在。
* AC_SUBST           用于定义将在Makefile中使用的变量。
* AC_CONFIG_FILES    定义了要生成的Makefile文件。
* AC_OUTPUT          指示autoconf生成configure脚本和其他输出文件，同时标明结束configure.ac。

另外，还应该运行aclocal来生成aclocal.m4文件，该文件包含了configure.ac中使用的
所有宏的定义。在运行autoconf之前，确保你已经运行了aclocal。

## 编写 Makefile.am

使用时automake，必须遵守一组标准。其中之一是项目的源文件位于该src文件夹中。在此
项目中，main.c根目录中有一个文件，因此需要告知automake：
```
AUTOMAKE_OPTIONS = foreign
```

需要告诉automake，希望编译的二进制文件被调用。在本例中，希望将其称为helloworld，
因此请编写以下内容：
```
bin_PROGRAMS = helloworld
```

最后一件事，那就是告诉automake需要哪些文件来编译您的应用程序。通过编写以下内容来
做到这一点：
```
helloworld_SOURCES = main.c
```
请注意，第一部分是应用程序的名称，后跟SOURCES主应用程序的名称。现在automake知道了
它需要知道的所有内容，并且Makefile.am可以使用了。





假设有一个简单的 C 程序，它包含两个源文件：main.c 和 helper.c
```
# Makefile.am for myproject

bin_PROGRAMS = myprogram

myprogram_SOURCES = main.c helper.c
```
在这个例子中：
* bin_PROGRAMS 变量指定了要构建的可执行文件。
* myprogram_SOURCES 变量列出了构建 myprogram 所需的源文件。

## 添加子目录

在autotools中添加子目录的基本步骤如下：

1. 在子目录中，编写一个或多个Makefile.am文件，告诉automake如何编译和安装该目录下
   的文件。例如，在src目录下，可能有一个Makefile.am文件，内容如下：
   ```makefile
   bin_PROGRAMS = myprogram
   myprogram_SOURCES = main.c util.c
   ```
   这个Makefile.am告诉automake要编译一个名为myprogram的可执行文件，它由main.c和
   util.c源文件组成。

2. 在项目的顶级`Makefile.am`（通常在项目的根目录下）中，使用SUBDIRS变量来包含子目录。
   例如，如果子目录是src，顶级Makefile.am看起来像这样：
   ```makefile
   SUBDIRS = src
   ```
   告诉automake在构建过程中首先处理src子目录。

3. 在configure.ac中调用`AM_INIT_AUTOMAKE`来初始化automake，这个宏通常在AC_INIT宏
   之后调用。例如：
   ```m4
   AC_INIT([myproject], [1.0], [bug-myproject@example.com])
   AM_INIT_AUTOMAKE([-Wall -Werror foreign subdir-objects])
   ...
   AC_CONFIG_FILES([Makefile src/Makefile])
   AC_OUTPUT
   ```
   在这个例子中，AM_INIT_AUTOMAKE宏设置了automake的选项，包括-Wall（显示所有警告）、
   -Werror（将警告视为错误）以及foreign和subdir-objects（如前所述）。
4. 运行autotools命令生成Makefile


## 配置并编译


### 生成Makefile的方法

一旦编写了configure.ac和Makefile.am，分发应用程序就相对简单了。记住要从运行aclocal
开始，这样才能运行 autoconf。运行 autoconf 后，就可以运行automake --add-missing
来构建Makefile.in.

该标志--add-missing是告诉automake自动生成所需的所有附加文件，因为通常您需要的不
仅仅是Makefile.am，而且必须手动输入其他文件。

至此，已具备分发程序所需的一切。在继续之前，这里有一个简短的回顾，显示了您现在
应该运行的命令：
```
aclocal
autoconf
automake --add-missing
```
也可以使用autoreconf替代以上内容
```
autoreconf -i -f
```

### autoconf和autoreconf的关系

* autoconf

autoconf 用于生成 configure 脚本。

* autoreconf

autoreconf 是一个用于重新生成构建系统的工具。它会自动检测项目中使用的 Autotools 工具
（如 autoconf、automake 等），并调用它们来生成或更新构建系统所需的文件，如 configure
脚本和 Makefile.in 文件。

autoreconf 特别有用当你修改了 configure.ac 或 Makefile.am 文件后，需要更新整个构建
系统时。它会确保所有的构建文件都是最新的，并且与项目的当前状态一致。

autoreconf 还有一些有用的选项，比如 -i（--install），它会在重新生成构建系统之前，
先尝试安装缺少的辅助文件（如 aclocal.m4、Makefile.in 的模板等）。

* 关系

简而言之，autoconf 和 autoreconf 的关系在于它们都是用于生成构建系统的工具，但各有侧重：

autoconf 专注于从 configure.ac 文件中生成 configure 脚本。
autoreconf 则更全面地管理构建系统的生成，它会自动检测并调用必要的 Autotools 工具
来更新整个构建系统。

在开发过程中，你通常会先使用 autoconf 生成 configure 脚本，然后使用 automake
（或其他工具）生成 Makefile.in 文件。但是，当你修改了 configure.ac 或 Makefile.am
文件后，使用 autoreconf 可以更方便地更新整个构建系统。

### 编译

前边autotools生成了configure之后，编译时直接使用configure进行配置，然后执行make
就可以了

## 分发程序

分发应用程序似乎是一项艰巨的任务，但 Autotools 使其变得非常简单。所要做的就是在
运行上面的配置脚本后运行make dist。这将生成一个 tarball，然后可以将其发送给客户。
