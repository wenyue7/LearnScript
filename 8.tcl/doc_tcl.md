references:
[Tcl/Tk教程](https://www.w3ccoo.com/tcl-tk/tcl_operators.html)
[数字芯片设计武器 -- TCL脚本语言介绍（上篇）](https://zhuanlan.zhihu.com/p/416370937)

# 简介

Tcl（Tool Command Language） 是一种通用的多范式系统编程语言。 它是一种脚本语言，
旨在为应用程序提供相互通信的能力。是一种被EDA工具广泛兼容的脚本语言，通常作为EDA
工具的shell使用。

Tk(“Tool Kit”) 是一个跨平台小部件工具包，用于构建多种语言的 GUI。大多数情况下，
Tcl和Tk库同时使用，Tk是一系列令Tcl易于编写图形用户接口的命令和过程。

TCL的一个重要特性是它的扩展性。如果一个程序需要使用某些标准Tcl没有提供的功能，可以
使用c语言创造一些新的Tcl命令，并很容易的融合进去。正是由于TCL易于扩展，所以赋予了
其在IC设计中的无限可能。

安装：`sudo apt-get install tcl tk`


# 特殊变量

| 特殊变量 | 描述 |
|--|--|
| argc             | 指的是许多命令行参数 |
| argv             | 引用包含命令行参数的列表 |
| argv0            | 指正在解释的文件的文件名或我们调用脚本的名称 |
| env              | 用于表示作为环境变量的元素数组 |
| errorCode        | 提供最后一个 Tcl 错误的错误代码 |
| errorInfo        | 提供最后一个 Tcl 错误的堆栈跟踪 |
| tcl_interactive  | 用于在交互和非交互模式之间切换，分别将其设置为 1 和 0 |
| tcl_library      | 用于设置标准Tcl库的位置 |
| tcl_pkgPath      | 提供通常安装软件包的目录列表 |
| tcl_patchLevel   | 指的是 Tcl 解释器的当前补丁级别 |
| tcl_platform     | 用于表示包含 byteOrder、machine、osVersion、platform 和 os 等对象的元素数组 |
| tcl_ precision   | 指的是精度，即在将浮点数转换为字符串时要保留的位数。 默认值为 12 |
| tcl_prompt1      | 指主要提示 |
| tcl_prompt2      | 指带有无效命令的辅助提示 |
| tcl_rcFileName   | 提供用户特定的启动文件 |
| tcl_traceCompile | 用于控制字节码编译的跟踪。 使用 0 表示无输出，1 表示摘要，2 表示详细 |
| tcl_traceExec    | 用于控制字节码执行的跟踪。 使用 0 表示无输出，1 表示摘要，2 表示详细 |
| tcl_version      | 返回 Tcl 解释器的当前版本 |

举例：
```
# 环境变量
puts $env(PATH)
# Tcl 环境变量
puts $env(PATH)
# 版本信息
puts $tcl_version
```


# 基本语法

## 标识符

Tcl 标识符是用于标识变量、函数或任何其他用户定义项的名称。 标识符以字母 A 到 Z 或
a 到 z 或下划线 (_) 开头，后跟零个或多个字母、下划线、美元 ($) 和数字（0 到 9）。

Tcl 不允许在标识符中使用标点符号，例如 @ 和 %。 Tcl 是一种区分大小写_的语言。 因此
Manpower和manpower在Tcl中是两个不同的标识符。

## 启动TCL

通常Linux系统下都预装了TCL解释器，可以通过which tcl命令查看其安装路径，用tclsh
可以启动解释器。

tcl有两种运行方法:
* 直接在解释器中运行，类似python的交互模式
* 写成以.tcl结尾的文件，在文件头加上`“#！/tool/pandora64/bin/tcl”`，脚本在执行的
  时候就会自动调用解释器。


## 命令结构

一个 TCL 脚本可以包含一个或多个命令，命令之间必须用换行符或分号隔开。指令格式通常
为`commandName argument1 argument2 ... argumentN`, 举例如下：
```tcl
% set a 1
% set b 2
% set c "wingo"；set d "zhihu"
```
'%' 为tcl交互模式时的命令提示符

在TCL中，注释用#，且必须用在开头,＃和直到所在行结尾的所有字符都被 TCL 看作注释。
在行尾注释是不允许的


## 置换

TCL 提供三种形式的置换：反斜杠置换、变量置换、命令置换。每种置换都会导致一个或多个
变量被其他的值所代替。置换可以发生在包括命令名在内的每一个单词中，而且置换可以嵌套。

变量置换：用 $ 符号进行，`$`用在变量名之前，这将返回变量的内容。
```
% set testVal "hello"
hello
% put $testVal
hello
% put testVal
testVal
```

反斜杠置换：主要把换行符、空格、[、$等被 TCL 解释器当作特殊符号对待的字符，置换成
原本的样子，或给原本的符号增加一些特殊用法。

举例如下，可以看出 put $testVal 输出的是赋值给他的变量，put \$testVal 则输出的是
字符 $testVal
```
% set testVal "hello"
hello
% put $testVal
hello
% put \$testVal
$testVal
% put testVal
testVal

puts "Hello\nWorld"
```

命令置换：命令置换用一对[]来表示， []中是另一组TCL 命令及其参数，命令置换会导致
某一个命令的所有或部分单词被另一个命令的结果所代替。[]中脚本的值为最后一个命令的
返回值。

命令置换的本质就表示TCL命令之间是可以嵌套的，即一个命令的结果可以作为别的命令的参数。

举例如下：
```
% set val [expr 2*3]
6
```

## 变量

在Tcl中，没有变量声明的概念。 一旦遇到新的变量名，Tcl就会定义一个新的变量。


### 变量命名

变量的名称可以包含任意字符和长度。 甚至可以通过将变量括在大括号中来获得空格，但这
不是首选。

set命令用于给变量赋值。 设置命令的语法是`set variableName value`，举例如下：
```
#!/usr/bin/tclsh

set variableA 10
set {variable B} test
puts $variableA
puts ${variable B}
```

### 动态类型

Tcl 是一种动态类型语言。 需要时可以动态地将变量的值转换为所需的类型。 例如，存储为
字符串的数字 5 在进行算术运算时将转换为数字。
```
#!/usr/bin/tclsh

set variableA "10"
puts $variableA
set sum [expr $variableA +20];
puts $sum
```
输出如下：
```
10
30
```


### 数学表达式

expr 用于表示数学表达式。 Tcl的默认精度是12位。 为了获得浮点结果，应该添加至少一位
小数。 举例如下：
```
#!/usr/bin/tclsh

set variableA "10"
set result [expr $variableA / 9];
puts $result
set result [expr $variableA / 9.0];
puts $result
set variableA "10.0"
set result [expr $variableA / 9];
puts $result
```
输出如下：
```
1
1.1111111111111112
1.1111111111111112
```

在上面的代码中，您可以使用 tcl_ precision 特殊变量来更改精度：
```
#!/usr/bin/tclsh

set variableA "10"
set tcl_precision 5
set result [expr $variableA / 9.0];
puts $result
```
输出如下：
```
1.1111
```


## 运算符

数学运算指令格式为：`expr <expression>`


基本数学运算：
```
a+b、a-b、a*b、a/b、a%b
```
关系运算符：
```
==  !=  >  <  >=  <=
```
逻辑运算符：
```
&&  ||  !
```
位运算符：
```
&  |  ^
```
三元运算符：
```
? :
如果条件为真 ? 则值 X ：否则值 Y
```

Tcl 中的运算符优先级，优先级最高的运算符出现在表的顶部，优先级最低的运算符出现在底部：

| 类别 | 运算符 | 关联性 |
|--|--|--|
| 一元     | + -       | 从右到左 |
| 乘除法   | * / %     | 从左到右 |
| 加减法   | + -       | 从左到右 |
| 位移     | << >>     | 从左到右 |
| 关系     | < <= > >= | 从左到右 |
| 按位与   | &         | 从左到右 |
| 按位异或 | ^         | 从左到右 |
| 按位或   | \|        | 从左到右 |
| 逻辑与   | &&        | 从左到右 |
| 逻辑或   | \|\|        | 从左到右 |
| 三元     | ?:        | 从右到左 |


## 过程


过程是带有一系列命令的代码块，这些命令提供了特定的可重用功能。 它用于避免相同的
代码在多个位置重复。 过程相当于许多编程语言中使用的函数，并且可以在 Tcl 中借助
proc 命令来使用。

语法：
```
proc procedureName {arguments} {
   body
}
```
举例：
```
下面给出了一个简单的过程示例 −

#!/usr/bin/tclsh

proc helloWorld {} {
   puts "Hello, World!"
}
helloWorld
```

#### 具有多个参数的过程

举例：
```
#!/usr/bin/tclsh

proc add {a b} {
   return [expr $a+$b]
}
puts [add 10 30]
```

#### 带有可变参数的过程

举例：
```
#!/usr/bin/tclsh

proc avg {numbers} {
   set sum 0
   foreach number $numbers {
      set sum  [expr $sum + $number]
   }
   set average [expr $sum/[llength $numbers]]
   return $average
}
puts [avg {70 80 50 60}]
puts [avg {70 80 50 }]
```

#### 带有默认参数的过程

默认参数用于提供在未提供值时可以使用的默认值。 下面显示了带有默认参数（有时称为
隐式参数）的过程的示例
```
#!/usr/bin/tclsh

proc add {a {b 100} } {
   return [expr $a+$b]
}
puts [add 10 30]
puts [add 10]
```

#### 递归过程

举例：
```
#!/usr/bin/tclsh

proc factorial {number} {
   if {$number <= 1} {
      return 1
   }
   return [expr $number * [factorial [expr $number - 1]]]

}
puts [factorial 3]
puts [factorial 5]
```

# 数据类型

Tcl 的原始数据类型是字符串，我们经常可以在 Tcl 上找到仅字符串语言的引号。 这些原始
数据类型依次为列表和关联数组创建复合数据类型。

在Tcl中，数据类型不仅可以表示简单的Tcl对象，还可以表示复杂的对象，例如句柄、图形
对象（主要是部件）和I/O通道。


## 简单 Tcl 对象

在Tcl中，无论是整数、布尔值、浮点数还是字符串。 当你想使用一个变量时，可以直接给
它赋值，没有Tcl中声明的步骤。 这些不同类型的对象可以有内部表示。 它可以在需要时将
一种数据类型转换为另一种数据类型。这些变量没有任何默认值，必须在使用之前为其赋值。

举例：
```
set myVariable 18
puts $myVariable
```

## 字符串

### 使用方法

与其他语言不同，在 Tcl 中，当它只是一个单词时，不需要包含双引号，当想要表示多个
字符串时，可以使用双引号或大括号

举例：
```
set myVariable hello
puts $myVariable

set myVariable "hello world"
puts $myVariable
set myVariable {hello world}
puts $myVariable
```

布尔值 1、yes 或 true 表示 true；0、no 或 false 表示 false


字符串也有一些转义字符，类似C语言的`\n`，`\r`等


### 字符串命令

| 命令 | 说明 |
|--|--|
| compare string1 string2    | 按字典顺序比较 string1 和 string2。 如果相等则返回 0，如果 string1 在 string2 之前则返回 -1，否则返回 1 |
| first string1 string2      | 返回 string1 在 string2 中第一次出现的索引。 如果没有找到，则返回-1 |
| index string index         | 返回索引处的字符 |
| last string1 string2.      | 返回 string1 在 string2 中最后一次出现的索引。 如果没有找到，则返回-1 |
| length string              | 返回字符串的长度 |
| match pattern string       | 如果字符串与模式匹配，则返回 1 |
| range string index1 index2 | 返回字符串中从索引 1 到索引 2 的字符范围 |
| tolower string             | 返回小写字符串 |
| toupper string             | 返回大写字符串 |
| trim string ?trimcharacters?      | 删除字符串两端的修剪字符。 默认的修剪字符是空格 |
| trimleft string ?trimcharacters?  | 删除字符串左开头的修剪字符。 默认的修剪字符是空格 |
| trimright string ?trimcharacters? | 删除字符串左端的修剪字符。 默认的修剪字符是空格 |
| wordend findstring index          | 返回包含索引处字符的单词之后的字符在 findstring 中的索引 |
| wordstart findstring index        | 返回包含索引处字符的单词中第一个字符在 findstring 中的索引 |


举例：
```
#!/usr/bin/tclsh
# 字符串索引

set s1 "Hello"
set s2 "World"
set s3 "World"
puts [string compare $s1 $s2]
if {[string compare $s2 $s3] == 0} {
   puts "String \'s1\' and \'s2\' are same.";
}

if {[string compare $s1 $s2] == -1} {
   puts "String \'s1\' comes before \'s2\'.";
}

if {[string compare $s2 $s1] == 1} {
   puts "String \'s2\' comes after \'s1\'.";
}
```

```
#!/usr/bin/tclsh
# 字符串长度

set s1 "Hello World"
puts "Length of string s1"
puts [string length $s1]
```

```
#!/usr/bin/tclsh
# 修剪字符

set s1 "Hello World"
set s2 "World"
puts "Trim right $s2 in $s1"
puts [string trimright $s1 $s2]

set s2 "Hello"
puts "Trim left $s2 in $s1"
puts [string trimleft $s1 $s2]

set s1 " Hello World "
set s2 " "
puts "Trim characters s1 on both sides of s2"
puts [string trim $s1 $s2]
```

```
#!/usr/bin/tclsh
# 匹配字符串

set s1 "test@test.com"
set s2 "*@*.com"
puts "Matching pattern s2 in s1"
puts [string match "*@*.com" $s1 ]
puts "Matching pattern tcl in s1"
puts [string match {tcl} $s1]
```

```
#!/usr/bin/tclsh
# append 命令

set s1 "Hello"
append s1 " World"
puts $s1
```


格式化命令
| 说明符 | 使用 |
|--|--|
| %s | 字符串表示 |
| %d | 整数表示 |
| %f | 浮点表示 |
| %e | 尾数指数形式的浮点表示 |
| %x | 十六进制表示 |

举例：
```
#!/usr/bin/tclsh

puts [format "%f" 43.5]
puts [format "%e" 43.5]
puts [format "%d %s" 4 tuts]
puts [format "%s" "Tcl Language"]
puts [format "%x" 40]
```

Scan 命令，Scan 命令用于根据格式说明符解析字符串：

举例：
```
#!/usr/bin/tclsh

puts [scan "90" {%[0-9]} m]
puts [scan "abc" {%[a-z]} m]
puts [scan "abc" {%[A-Z]} m]
puts [scan "ABC" {%[A-Z]} m]
```


## 数组

### 数组定义

在 Tcl 中，所有数组本质上都是关联的。 数组的存储和检索没有任何特定的顺序。 关联
数组的索引不一定是数字，并且可以稀疏填充。 它通常是一个类似于键值对的字符串。书写
格式为：
```
set <arrayName>(<mapName>) <value>
```
数组的索引可以是任意字符

举例：
```
#!/usr/bin/tclsh

set  marks(english) 80
puts $marks(english)
set  marks(mathematics) 90
puts $marks(mathematics)
```
输出如下：
```
80
90
```

### 数组大小

语法：
```
[array size variablename]
```

举例：
```
#!/usr/bin/tclsh

set languages(0) Tcl
set languages(1) "C Language"
puts  [array size languages]
```


### 数组迭代

数组索引可以是不连续的，例如为索引 1 指定的值，然后为索引 10 指定的值，依此类推。
但是，如果它们是连续的，我们可以使用数组迭代来访问数组的元素。

举例：
```
#!/usr/bin/tclsh

set languages(0) Tcl
set languages(1) "C Language"
for { set index 0 }  { $index < [array size languages] }  { incr index } {
   puts "languages($index) : $languages($index)"
}
```
输出如下：
```
languages(0) : Tcl
languages(1) : C Language
```


可以使用数组的索引来迭代关联数组：
```
#!/usr/bin/tclsh

set personA(Name) "Dave"
set personA(Age) 14
foreach index [array names personA] {
   puts "personA($index): $personA($index)"
}
```

## 列表

list是TCL中非常重要的一种数据结构 ，list 是由一堆元素组成的有序集合，list 可以
嵌套定义，list 每个元素可以是任意字符串，也可以是 list。

需要注意的是，这些列表完全表示为字符串，并在需要时进行处理以形成单独的项目。因此，
在这种情况下，请避免使用大型列表，大型列表建议改为使用数组。

### 创建列表

语法：
```
set listName { item1 item2 item3 .. itemn }
# or
set listName [list item1 item2 item3]
# or
set listName [split "items separated by a character" split_character]
```

举例：
```
#!/usr/bin/tclsh

set colorList1 {red green blue}
set colorList2 [list red green blue]
set colorList3 [split "red_green_blue" _]
puts $colorList1
puts $colorList2
puts $colorList3
```

### 追加内容

语法：
```
append listName split_character value
# or
lappend listName value
```

举例：
```
#!/usr/bin/tclsh

set var orange
append var " " "blue"
lappend var "red"
lappend var "green"
puts $var
```

### 列表长度

语法：
```
llength listName
```

举例：
```
#!/usr/bin/tclsh

set var {orange blue red green}
puts [llength $var]
```


### 在索引处列出项目

语法：
```
lindex listname index
```
举例：
```
#!/usr/bin/tclsh

set var {orange blue red green}
puts [lindex $var  1]
```


### 在索引处插入项目

语法：
```
linsert listname index value1 value2..valuen
```
举例：
```
#!/usr/bin/tclsh

set var {orange blue red green}
set var [linsert  $var 3 black white]
puts $var
```


### 替换索引处的项目

语法：
```
lreplace listname firstindex lastindex value1 value2..valuen
```
举例：
```
#!/usr/bin/tclsh

set var {orange blue red green}
set var [lreplace $var 2 3 black white]
puts $var
```


### 在索引处设置项目

语法：
```
lset listname index value
```
举例：
```
#!/usr/bin/tclsh

set var {orange blue red green}
lset var 0 black
puts $var
```

### 将列表转换为变量
语法：
```
lassign listname variable1 variable2.. variablen
```
举例：
```
#!/usr/bin/tclsh

set var {orange blue red green}
lassign $var colour1 colour2
puts $colour1
puts $colour2
```


### 对列表进行排序

语法：
```
lsort listname
```
举例：
```
#!/usr/bin/tclsh

set var {orange blue red green}
set var [lsort $var]
puts $var
```

## 字典

语法：
```
dict set dictname key value
# or
dict create dictname key1 value1 key2 value2 .. keyn valuen
```
举例：
```
#!/usr/bin/tclsh

dict set colours  colour1 red 
puts $colours
dict set colours  colour2 green
puts $colours

set colours [dict create colour1 "black" colour2 "white"]
puts $colours
```

### 字典大小

语法：
```
[dict size dictname]
```
举例：
```
#!/usr/bin/tclsh

set colours [dict create colour1 "black" colour2 "white"]
puts [dict size $colours]
```

### 字典迭代

用于打印字典键和值的简单字典迭代如下所示
```
#!/usr/bin/tclsh

set colours [dict create colour1 "black" colour2 "white"]
foreach item [dict keys $colours] {
   set value [dict get $colours $item]
   puts $value
}
```

### 字典中键的值

语法：
```
[dict get $dictname $keyname]
```
举例：
```
#!/usr/bin/tclsh

set colours [dict create colour1 "black" colour2 "white"]
set value [dict get $colours colour1]
puts $value
```

### 字典中的所有键

语法：
```
[dict keys $dictname]
```
举例：
```
#!/usr/bin/tclsh

set colours [dict create colour1 "black" colour2 "white"]
set keys [dict keys $colours]
puts $keys
```

### 字典中的所有值

语法：
```
[dict values $dictname]
```
举例：
```
#!/usr/bin/tclsh

set colours [dict create colour1 "black" colour2 "white"]
set values [dict values $colours]
puts $values
```

### 字典中是否存在键

语法：
```
[dict exists $dictname $key]
```
举例：
```
#!/usr/bin/tclsh

set colours [dict create colour1 "black" colour2 "white"]
set result [dict exists $colours colour1]
puts $result
```


## 句柄

Tcl 句柄通常用于表示文件和图形对象。 这些可以包括网络请求的句柄以及其他通道，如
串行端口通信、套接字或 I/O 设备。 以下是创建文件句柄的示例:
```
set myfile [open "filename" r]
```

# 工作流

## 分支工作流

### if

语法：
```
if {boolean_expression} {
   # statement(s) will execute if the Boolean expression is true
}
```

举例：
```
#!/usr/bin/tclsh

set a 10

#check the boolean condition using if statement
if { $a < 20 } {
   # if condition is true then print the following
   puts "a is less than 20"
}
puts "value of a is : $a"
```

### if else

语法：
```
if {boolean_expression} {
   # statement(s) will execute if the boolean expression is true
} else {
   # statement(s) will execute if the boolean expression is false
}
```
举例：
```
#!/usr/bin/tclsh

set a 100

#check the boolean condition
if {$a < 20 } {
   #if condition is true then print the following
   puts "a is less than 20"
} else {
   #if condition is false then print the following
   puts "a is not less than 20"
}
puts "value of a is : $a"
```

### if...else if...else

语法：
```
if {boolean_expression 1} {
   # Executes when the boolean expression 1 is true
} elseif {boolean_expression 2} {
   # Executes when the boolean expression 2 is true
} elseif {boolean_expression 3} {
   # Executes when the boolean expression 3 is true
} else {
   # executes when the none of the above condition is true
}
```
举例：
```
#!/usr/bin/tclsh

set a 100

#check the boolean condition
if { $a == 10 } {
   # if condition is true then print the following
   puts "Value of a is 10"
} elseif { $a == 20 } {
   # if else if condition is true
   puts "Value of a is 20"
} elseif { $a == 30 } {
   # if else if condition is true
   puts "Value of a is 30"
} else {
   # if none of the conditions is true
   puts "None of the values is matching"
}

puts "Exact value of a is: $a"
```

### switch

语法：
```
switch switchingString {
   matchString1 {
      body1
   }
   matchString2 {
      body2
   }
...
   matchStringn {
      bodyn
   }
}
```
也可写成如下形式：
```
switch switchingString matchString1 {body1} matchString2 {body2} ... matchStringn {bodyn}
```

举例：
```
#!/usr/bin/tclsh

set grade B;

switch $grade {
   A {
      puts "Well done!"
   }
   B {
      puts "Excellent!"
   }

   C {
      puts "You passed!"
   }
   F {
      puts "Better try again"
   }
   default {
      puts "Invalid grade"
   }
}
puts "Your grade is  $grade"
```
```
#!/usr/bin/tclsh

set grade C;

switch $grade A { puts "Well done!" } B { puts "Excellent!" } C { puts "You passed!"  } F { puts "Better try again" } default { puts "Invalid grade" }
puts "Your grade is  $grade"
```


## 循环工作流

### while

语法：
```
while {condition} {
   statement(s)
}
```

举例：
```
#!/usr/bin/tclsh

set a 10

#while loop execution
while { $a < 20 } {
   puts "value of a: $a"
   incr a
}


while {1} {
   puts "This loop will run forever."
}
```

### for

语法：
```
for {initialization} {condition} {increment} {
   statement(s);
}
```
举例：
```
#!/usr/bin/tclsh

# for loop execution
for { set a 10}  {$a < 20} {incr a} {
   puts "value of a: $a"
}
```

### break


举例：
```
#!/usr/bin/tclsh

set a 10

# while loop execution
while {$a < 20 } {
   puts "value of a: $a"
   incr a
   if { $a > 15} {
      # terminate the loop using break statement
      break
   }
}
```

### continue


举例：
```
#!/usr/bin/tclsh

set a 10
# do loop execution
while { $a < 20 } {
   if { $a == 15} {
      #skip the iteration
      incr a
      continue
   }
   puts "value of a: $a"
   incr a
}
```

# 软件包

包用于创建可重用的代码单元。 包由提供特定功能的文件集合组成。 该文件集合由包名称
标识，并且可以具有相同文件的多个版本。 该包可以是 Tcl 脚本、二进制库或两者的组合
的集合。

Package使用命名空间的概念来避免变量名和过程名的冲突。

## 创建包

可以在至少两个文件的帮助下创建包。 一个文件包含包代码。 其他文件包含用于声明包的
索引包文件。

下面给出了创建和使用包的步骤列表。

1. 创建代码

为 HelloWorld 文件夹内的包创建代码。 将文件命名为HelloWorld.tcl，代码如下 −
```
# /Users/rajkumar/Desktop/helloworld/HelloWorld.tcl
# Create the namespace
namespace eval ::HelloWorld {
    # Export MyProcedure
    namespace export MyProcedure

    # My Variables
    set version 1.0
    set MyDescription "HelloWorld"

    # Variable for the path of the script
    variable home [file join [pwd] [file dirname [info script]]]
}

# Definition of the procedure MyProcedure
proc ::HelloWorld::MyProcedure {} {
    puts $HelloWorld::MyDescription
}

package provide HelloWorld $HelloWorld::version
package require Tcl 8.0
```

2. 创建包索引

打开 tclsh。 切换到 HelloWorld 目录，使用 pkg_mkIndex 命令创建索引文件，如下所示 −
```
% cd /Users/rajkumar/Desktop/helloworld
% pkg_mkIndex . *.tcl
```

3. 将目录添加到自动路径

使用 lappend 命令将包添加到全局列表中，如下所示 −
```
% lappend auto_path "/Users/rajkumar/Desktop/helloworld"
```

4. 添加包

接下来使用 package require 语句将包添加到程序中，如下所示 −
```
% package require HelloWorld 1.0
```

5. 调用过程

现在，一切都已设置完毕，我们可以调用我们的程序，如下所示 −
```
% puts [HelloWorld::MyProcedure]
```
You will get the following result −
```
HelloWorld
```
前两步创建包。 创建包后，您可以通过添加最后三个语句在任何 Tcl 文件中使用它，如下所示 −
```
lappend auto_path "/Users/rajkumar/Desktop/helloworld"
package require HelloWorld 1.0
puts [HelloWorld::MyProcedure]
```
得到以下结果 −
```
HelloWorld
```


# 命名空间

命名空间是一组标识符的容器，用于对变量和过程进行分组。 从 Tcl 版本 8.0 开始可以
使用命名空间。 在引入命名空间之前，只有单一的全局作用域。现在有了命名空间，就有了
额外的全局范围分区。

## 创建命名空间

命名空间是使用namespace命令创建的。 创建命名空间的简单示例如下所示：
```
#!/usr/bin/tclsh

namespace eval MyMath {
    # Create a variable inside the namespace
    variable myResult
}

# Create procedures inside the namespace
proc MyMath::Add {a b } {
    set ::MyMath::myResult [expr $a + $b]
}
MyMath::Add 10 23

puts $::MyMath::myResult
```

执行上述代码时，会产生以下结果：
```
33
```

## 嵌套命名空间

Tcl 允许命名空间嵌套。 下面给出了嵌套命名空间的一个简单示例
```
#!/usr/bin/tclsh

namespace eval MyMath {
   # Create a variable inside the namespace
   variable myResult
}

namespace eval extendedMath {
   # Create a variable inside the namespace
   namespace eval MyMath {
      # Create a variable inside the namespace
      variable myResult
   }
}
set ::MyMath::myResult "test1"
puts $::MyMath::myResult
set ::extendedMath::MyMath::myResult "test2"
puts $::extendedMath::MyMath::myResult
```
执行上述代码时，会产生以下结果 −
```
test1
test2
```


## 导入和导出命名空间

可以看到，在前面的命名空间示例中，使用了很多范围解析运算符，并且使用起来比较复杂。
实际上，可以通过导入和导出名称空间来避免这种情况。 举例如下：
```
#!/usr/bin/tclsh

namespace eval MyMath {
   # Create a variable inside the namespace
   variable myResult
   namespace export Add
}

# Create procedures inside the namespace
proc MyMath::Add {a b } {
   return [expr $a + $b]
}

namespace import MyMath::*
puts [Add 10 30]
```
执行上述代码时，会产生以下结果：
```
40
```

## forget命名空间

您可以使用forget子命令删除导入的命名空间。 一个简单的例子如下所示：
```
#!/usr/bin/tclsh

namespace eval MyMath {
   # Create a variable inside the namespace
   variable myResult
   namespace export Add
}

# Create procedures inside the namespace
proc MyMath::Add {a b } {
   return [expr $a + $b]
}
namespace import MyMath::*
puts [Add 10 30]
namespace forget MyMath::*
```
执行上述代码时，会产生以下结果：
```
40
```


# 文件I/O

Tcl 通过内置命令 open、read、puts、gets 和 close 来支持文件处理。

文件代表字节序列，无论是文本文件还是二进制文件。

## 打开文件

Tcl 使用 open 命令在 Tcl 中打开文件。 打开文件的语法如下：
```
open fileName accessMode
```
此处，filename 是字符串文字，使用它来命名文件，accessMode 可以具有以下值之一：

| 模式 | 描述 |
| r  | 打开现有文本文件以进行读取，并且该文件必须存在。 这是未指定 accessMode 时使用的默认模式 |
| w  | 打开一个文本文件进行写入，如果不存在，则创建一个新文件，否则现有文件将被截断 |
| a  | 打开一个文本文件以追加模式写入，并且文件必须存在。 在这里，您的程序将开始在现有文件内容中附加内容 |
| r+ | 打开一个文本文件以进行读写。 文件必须已经存在 |
| w+ | 打开一个文本文件以进行读写。 如果文件存在，它首先将其截断为零长度，否则创建文件（如果不存在） |
| a+ | 打开一个文本文件以进行读写。 如果文件不存在，它将创建该文件。 阅读会从头开始，但写作只能追加 |


## 关闭文件

要关闭文件，使用 close 命令。 close的语法如下：
```
close fileName
```
程序使用完该文件后，必须关闭该程序打开的任何文件。 在大多数情况下，文件不需要显式
关闭；当 File 对象自动终止时，它们也会自动关闭。

## 写入文件

Puts 命令用于写入打开的文件。
```
puts $filename "text to write"
```
下面显示了写入文件的简单示例。
```
#!/usr/bin/tclsh

set fp [open "input.txt" w+]
puts $fp "test"
close $fp
```
当上面的代码编译并执行时，它会在启动的目录（程序的工作目录）中创建一个新文件input.txt。

## 读取文件

以下是从文件读取的简单命令：
```
set file_data [read $fp]
```
完整的读写示例如下所示：
```
#!/usr/bin/tclsh

set fp [open "input.txt" w+]
puts $fp "test"
close $fp
set fp [open "input.txt" r]
set file_data [read $fp]
puts $file_data
close $fp
```
当上面的代码被编译并执行时，它会读取上一节中创建的文件并产生以下结果：
```
test
```
这是另一个逐行读取文件直到文件末尾的示例：
```
#!/usr/bin/tclsh

set fp [open "input.txt" w+]
puts $fp "test\ntest"
close $fp
set fp [open "input.txt" r]

while { [gets $fp data] >= 0 } {
   puts $data
}
close $fp
```
当上面的代码被编译并执行时，它会读取上一节中创建的文件并产生以下结果：
```
test
test
```


# 错误处理

Tcl 中的错误处理是在 error 和 catch 命令的帮助下提供的。 每个命令的语法如下所示。

error 语法
```
error message info code
```
在上述错误命令语法中，message为错误消息，info设置在全局变量errorInfo中，code设置
在全局变量errorCode中。

Catch 语法
```
catch script resultVarName
```
在上面的catch命令语法中，script是要执行的代码，resultVarName是保存错误或结果的
变量。 如果没有错误，catch 命令返回 0，如果有错误，则返回 1。

下面显示了简单错误处理的示例：
```
#!/usr/bin/tclsh

proc Div {a b} {
   if {$b == 0} {
      error "Error generated by error" "Info String for error" 401
   } else {
      return [expr $a/$b]
   }
}

if {[catch {puts "Result = [Div 10 0]"} errmsg]} {
   puts "ErrorMsg: $errmsg"
   puts "ErrorCode: $errorCode"
   puts "ErrorInfo:\n$errorInfo\n"
}

if {[catch {puts "Result = [Div 10 2]"} errmsg]} {
   puts "ErrorMsg: $errmsg"
   puts "ErrorCode: $errorCode"
   puts "ErrorInfo:\n$errorInfo\n"
}
```
执行上述代码时，会产生以下结果 −
```
ErrorMsg: Error generated by error
ErrorCode: 401
ErrorInfo:
Info String for error
   (procedure "Div" line 1)
   invoked from within
"Div 10 0"

Result = 5
```
正如在上面的示例中看到的，可以创建自己的自定义错误消息。 同样，可以捕获 Tcl 生成
的错误。 一个例子如下所示：
```
#!/usr/bin/tclsh

catch {set file [open myNonexistingfile.txt]} result
puts "ErrorMsg: $result"
puts "ErrorCode: $errorCode"
puts "ErrorInfo:\n$errorInfo\n"
```
执行上述代码时，会产生以下结果 −
```
ErrorMsg: couldn't open "myNonexistingfile.txt": no such file or directory
ErrorCode: POSIX ENOENT {no such file or directory}
ErrorInfo:
couldn't open "myNonexistingfile.txt": no such file or directory
   while executing
"open myNonexistingfile.txt"
```


# 内置函数

Tcl 提供了许多用于各种操作的内置函数（过程）。这包括：
* 列表处理函数
* 字符串处理函数
* 数组处理函数
* 字典处理函数
* 文件 I/O 处理函数
* 用于创建命名空间和包的函数
* 数学运算函数
* 系统操作函数

前面的章节中介绍了除数学和系统函数之外的所有内容。 数学和系统内置函数解释如下

## 数学函数

下表列出了 Tcl 中可用的数学函数：

| 方法 | 描述 |
|--|--|
| abs arg    | 计算arg的绝对值 |
| acos arg   | 计算arg的反余弦 |
| asin arg   | 计算arg的反正弦 |
| atan arg   | 计算arg的反正切 |
| atan2 y x  | 计算其参数 (y/x) 的商的反正切 |
| ceil arg   | 计算大于或等于数字的最小整数 |
| cos arg    | 计算arg的余弦 |
| cosh arg   | 计算arg的双曲余弦 |
| double arg | 计算arg是否为浮点值，返回arg，否则将arg转换为浮点值并返回转换后的值 |
| exp arg    | 计算指数函数（e 的 arg 次方） |
| floor arg  | 计算小于或等于arg的最大整数 |
| fmod x y   | 计算 x 除以 y 的浮点余数。 如果y为0，则返回错误 |
| hypot x y  | 计算直角三角形斜边的长度 sqrt(x*x+y*y) |
| int arg    | 计算arg是否是与机器字宽度相同的整数值，返回arg，否则将arg转换为整数 |
| log arg    | 计算arg的自然对数 |
| log10 arg  | 计算 arg 以 10 为底的对数 |
| pow x y    | 计算 x 的 y 次方值。 如果 x 为负数，则 y 必须为整数值 |
| rand       | 计算 0 到 1 之间的伪随机数 |
| round arg  | 计算 arg 的值，四舍五入到最接近的整数 |
| sin arg    | 计算arg的正弦 |
| sinh arg   | 计算arg的双曲正弦 |
| sqrt arg   | 计算 arg 的平方根。 arg 必须为正数 |
| srand arg  | 计算 0 到 1 之间的伪随机数。arg 必须是整数，用于重置 rand 随机数生成器的种子 |
| tan arg    | 计算arg的正切 |
| tanh arg   | 计算arg的双曲正切 |
| wide arg   | 如果 arg 还不是 1，则为 arg 计算至少 64 位宽的整数值（如果 arg 是 32 位数字，则通过符号扩展） |

下面给出了一些使用数学函数的示例：
```
#!/usr/bin/tclsh

namespace import ::tcl::mathfunc::*
puts [tan 10]
puts [pow 10 2]
puts [ceil 10.34]
puts [hypot 10 20]
puts [srand 45]
puts [log 10]
puts [srand 45]
```
执行上述代码时，会产生以下结果 −
```
0.6483608274590866
100.0
11.0
22.360679774997898
0.0003521866166741525
2.302585092994046
0.0003521866166741525
```

## 系统函数

Tcl 中重要的系统函数包括：
* clock − 秒函数，返回当前时间（以秒为单位）
* clock − format 函数，将秒格式化为日期和时间
* clock − scan 函数，扫描输入字符串并将其转换为秒
* open − 函数，用于打开文件
* exec − 函数，用于执行系统命令
* close − 函数，用于关闭文件

下面列出了上述函数的一些示例：
```
#!/usr/bin/tclsh

#get seconds
set currentTime [clock seconds]
puts $currentTime
#get format
puts "The time is: [clock format $currentTime -format %H:%M:%S]"
puts "The date is: [clock format $currentTime -format %D]"

set date "Jun 15, 2014"
puts [clock scan $date -format {%b %d, %Y}]

puts [exec ls]
puts [exec dir]

set a  [open input.txt]
puts [read $a];
puts $a
close $a
```
执行上述代码时，会产生以下结果：
```
1402819756
The time is: 03:09:16
The date is: 06/15/2014
1402808400
input.txt
main.tcl
input.txt  main.tcl
This is the file you can use to provide input to your program and later on open
   it inside your program to process the input.

file3
```

下表提供了可用于格式化日期和时间的列表字符串：

| 格式 | 描述 |
|--|--|
| %a | 日的缩写形式，例如：Sun |
| %A | 日期的完整形式，例如：Sunday |
| %b | 月份的缩写 |
| %B | 完整月份 |
| %d | 一个月中的某一天 |
| %j | 每年的儒略日 |
| %m | 月份数 |
| %y | 两位数年份 |
| %Y | 四位数的年份 |
| %H | 24 小时制的时间 |
| %I | 12 小时制的小时 |
| %M | 分钟 |
| %S | 秒 |
| %p | AM 或 PM |
| %D | 日期数字，mm /dd/yy |
| %r | 12 小时制时间 |
| %R | 时间采用 24 小时制，不带秒 |
| %T | 24 小时制时间，带秒 |
| %Z | 时区名称，例如 GMT、IST、EST 等 |


## info 命令

info 是一个内置命令，提供有关 Tcl 解释器状态的信息。

reference:  [info](https://wiki.tcl-lang.org/page/info)

* `info option ?arg arg ...?`

* `info args procname`

* `info body procname`

* `info class subcommand class …`

* `info cmdcount`

* `info commands ?pattern?`

* `info complete script`

* `info coroutine`

* `info default procname arg varname`

* `info errorstack`

* `info exists varName`

如果名为varName的变量根据名称解析规则存在于当前上下文中，并且已通过给定值进行定义，
则返回1 ，否则返回0。对于存在但未定义的变量，info contains返回0 。

demo:
```
info exists a
# -> 0
set a 1
# -> 1
info exists a
# -> 1
info exists b
# -> 0
set b(2) 2
# -> 2
info exists b
# -> 1
info exists b(1)
# -> 0
info exists b(2)
# -> 1
info exists $a
# -> 0
```

* `info frame ?number?`

* `info functions pattern`

* `info globals ?pattern?`

* `info hostname`

* `info level ?number?`

* `info library`

* `info loaded ?interp?`

* `info locals ?pattern?`

* `info nameofexecutable`

* `info object subcommand object …`

* `info patchlevel`

* `info procs ?pattern?`

* `info script ?filename?`

* `info sharedlibextension`

* `info tclversion`

* `info vars ?pattern?`


# 正则表达式

"regexp"命令用于匹配 Tcl 中的正则表达式。 正则表达式是包含搜索模式的字符序列。
它由多个规则组成，下表解释了这些规则及其相应的用途。

| 规则 | 说明 |
|--|--|
| x                | 完全匹配 |
| [a-z]            | a-z 中的任何小写字母 |
| .                | 任何字符 |
| ^                | 开始字符串应该匹配 |
| $                | 结束字符串应该匹配 |
| \^               | 用于匹配特殊字符 ^ 的反斜杠序列。类似地，您可以用于其他字符 |
| ()               | 将上述序列添加到括号内以形成正则表达式 |
| x*               | 应匹配 0 次或多次出现的前面的 x |
| x+               | 应匹配前面的 x 的 1 次或多次出现 |
| [a-z]?           | 应匹配前面的 x 的 0 或 1 次出现 |
| {digit}          | 精确匹配先前正则表达式中出现的数字。 包含0-9的数字 |
| {digit,}         | 匹配先前正则表达式中出现的 3 个或更多数字。 包含0-9的数字 |
| {digit1,digit2}  | 出现次数与先前正则表达式的数字 1 和数字 2 出现次数之间的范围相匹配 |

## 语法

正则表达式的语法如下所示：
```
regexp optionalSwitches patterns searchString fullMatch subMatch1 ... subMatchn
```
这里，regex 是命令。 稍后我们将看到可选开关。 模式就是前面提到的规则。 搜索字符串
是执行正则表达式的实际字符串。 完全匹配是保存匹配正则表达式结果的任何变量。
Submatch1 到 SubMatchn 是可选的 subMatch 变量，用于保存子匹配模式的结果。

在深入研究复杂的示例之前，让我们先看一些简单的示例。 带有任意字母的字符串的简单
示例。 当正则表达式遇到任何其他字符时，搜索将停止并返回。
```
#!/usr/bin/tclsh

regexp {([A-Za-z]*)} "Tcl Tutorial" a b
puts "Full Match: $a"
puts "Sub Match1: $b"
```
执行上述代码时，会产生以下结果：
```
Full Match: Tcl
Sub Match1: Tcl
```

## 多种模式

以下示例演示如何搜索多个模式。 这是任何字母表后跟任何字符后跟任何字母表的示例模式。
```
#!/usr/bin/tclsh

regexp {([A-Za-z]*).([A-Za-z]*)} "Tcl Tutorial" a b c
puts "Full Match: $a"
puts "Sub Match1: $b"
puts "Sub Match2: $c"
```
执行上述代码时，会产生以下结果：
```
Full Match: Tcl Tutorial
Sub Match1: Tcl
Sub Match2: Tutorial
```
上述代码的修改版本显示子模式可以包含多个模式，如下所示：
```
#!/usr/bin/tclsh

regexp {([A-Za-z]*.([A-Za-z]*))} "Tcl Tutorial" a b c
puts "Full Match: $a"
puts "Sub Match1: $b"
puts "Sub Match2: $c"
```
执行上述代码时，会产生以下结果：
```
Full Match: Tcl Tutorial
Sub Match1: Tcl Tutorial
Sub Match2: Tutorial
```

## 正则表达式命令开关

Tcl 中可用的开关列表如下：
* nocase − 用于忽略大小写 |
* indices − 存储匹配子模式的位置而不是匹配字符 |
* line − 新行敏感匹配。 忽略换行符后的字符 |
* start index − 设置搜索模式开始的偏移量 |
* 标记开关结束

在上面的例子中，我特意对所有字母使用了`[A-Z, a-z]`，你可以轻松地使用 -nocase 而
不是如下所示：
```
#!/usr/bin/tclsh

regexp -nocase {([A-Z]*.([A-Z]*))} "Tcl Tutorial" a b c
puts "Full Match: $a"
puts "Sub Match1: $b"
puts "Sub Match2: $c"
```
执行上述代码时，会产生以下结果：
```
Full Match: Tcl Tutorial
Sub Match1: Tcl Tutorial
Sub Match2: Tutorial
```
使用开关的另一个示例如下所示：
```
#!/usr/bin/tclsh

regexp -nocase -line -- {([A-Z]*.([A-Z]*))} "Tcl \nTutorial" a b
puts "Full Match: $a"
puts "Sub Match1: $b"
regexp -nocase -start 4 -line -- {([A-Z]*.([A-Z]*))} "Tcl \nTutorial" a b
puts "Full Match: $a"
puts "Sub Match1: $b"
```
执行上述代码时，会产生以下结果：
```
Full Match: Tcl
Sub Match1: Tcl
Full Match: Tutorial
Sub Match1: Tutorial
```
