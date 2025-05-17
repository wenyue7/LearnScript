references:
[Tcl/Tk教程](https://www.w3ccoo.com/tcl-tk/tcl_operators.html)

# 概述

Tk 指的是 Toolkit，它提供跨平台 GUI 小部件，可以帮助您构建图形用户界面。 它是
由 John Ousterhout 开发的 Tcl 脚本语言的扩展。 Tk 与 Tcl 保持独立开发，版本互不
相同，之前在 v8.0 中与 Tcl 同步。

## Tk 的功能

它是跨平台的，支持 Linux、Mac OS、Unix 和 Microsoft Windows 操作系统。
* 它是开源的。
* 它提供了高水平的可扩展性。
* 它是可定制的。
* 它是可配置的。
* 它提供了大量的小部件。
* 它可以与其他动态语言一起使用，而不仅仅是 Tcl。
* 跨平台的 GUI 看起来相同。

## Tk 中内置的应用程序

大型成功的应用程序已经在 Tcl/Tk 中构建
* 仪表板软用户界面
* 关系数据库的表单 GUI
* 关系数据库专用 GUI
* 软/硬件系统设计
* Xtask - 任务管理
* 日历应用
* Tk 邮件
* Tk 调试器


# 特殊变量

在 Tk 中，我们将一些变量分类为特殊变量，它们具有预定义的用法/功能。 下面列出了
特殊变量的列表。

| 特殊变量 | 描述 |
|--|--|
| tk_library     | 用于设置标准 Tk 库的位置 |
| tk_patchLevel  | 指 Tk 解释器的当前补丁级别 |
| tk_strictMotif | 当非零时，Tk 尝试尽可能遵循 Motif 的外观和感觉 |
| tk_version     | 显示 Tk 版本 |

上述特殊变量对于 Tk 解释器有其特殊含义。

使用 Tk 特殊变量的示例

* TK VERSION
```
#!/usr/bin/wish

puts $tk_version
```
运行该程序时，将得到类似的输出，如下所示。
```
8.5
```

* TK LIBRARY PATH
```
#!/usr/bin/wish

puts $tk_library
```
运行该程序时，将得到类似的输出，如下所示。
```
/Library/Frameworks/Tk.framework/Versions/8.6/Resources/Scripts
```

* TK PATCH LEVEL
```
#!/usr/bin/wish

puts $tk_patchLevel
```
运行该程序时，您将得到类似的输出，如下所示。
```
8.6.1
```

* TK STRICTMOTIF
```
#!/usr/bin/wish

puts $tk_strictMotif
```
运行该程序时，您将得到类似的输出，如下所示。
```
0
```


# 小部件

基于 Tk 的应用程序的基本组件称为小部件。 组件有时也称为窗口，因为在 Tk 中，"窗口"
和"窗口小部件"经常互换使用。 Tk 是一个软件包，它提供了一组丰富的图形组件，用于使用
Tcl 创建图形应用程序。

Tk 提供了一系列小部件，从基本的 GUI 小部件（如按钮和菜单）到数据显示小部件。 这些
小部件可配置，它们具有默认配置，因此易于使用。

Tk 应用程序遵循小部件层次结构，其中任意数量的小部件可以放置在另一个小部件内，并且
这些小部件可以放置在另一个小部件内。 Tk 程序中的主小部件称为根小部件，可以通过创建
TkRoot 类的新实例来创建。

## 概述

### 创建小部件

下面给出了创建小部件的语法。
```
type variableName arguments options
```

这里的类型指的是widget类型，如按钮、标签等。 根据每个小部件的单独语法，参数可以是
可选的。 选项范围从每个组件的大小到格式。

### 小部件命名约定

Widget 使用类似于命名包的结构。 在 Tk 中，根窗口以句点 (.) 和窗口中的一个元素命名，
例如按钮命名为 .myButton1。 变量名称应以小写字母、数字或标点符号（句点除外）开头。
第一个字符之后的其他字符可以是大写或小写字母、数字或标点符号（句点除外）。 建议
使用小写字母来开始标签。

### 颜色命名约定

可以使用红色、绿色等名称来声明颜色。 也可以使用十六进制，用#表示。 十六进制位数
可以是 3、6、9 或 12。

### 尺寸约定

默认单位是像素，当我们没有指定尺寸时使用它。 其他尺寸为 i 代表英寸、m 代表毫米、
c 代表厘米、p 代表点。

### 常用选项

所有小部件都有很多常用选项，下表列出：

| 语法 | 描述 |
|--|--|
| -background color          | 用于设置小部件的背景颜色 |
| -borderwidth width         | 用于在3D效果中绘制边框 |
| -font fontDescriptor       | 用于设置小部件的字体 |
| -foreground color          | 用于设置小部件的前景色 |
| -height number             | 用于设置小部件的高度 |
| -highlightbackground color | 用于设置当小部件没有输入焦点时在小部件周围绘制的颜色矩形 |
| -highlightcolor color      | 用于设置当小部件具有输入焦点时在小部件周围绘制的颜色矩形 |
| -padx number               | 设置小部件的 padx |
| -pady number               | 设置小部件的 pady |
| -relief condition          | 设置此小部件的 3D 浮雕。 状况可以是凸起的、凹陷的、平坦的、脊状的、实心的或凹槽的 |
| -text text                 | 设置小部件的文本 |
| -textvariable varName      | 与小部件关联的变量。 当小部件的文本发生变化时，该变量将被设置为小部件的文本 |
| -width number              | 设置小部件的宽度 |

举例：
```
#!/usr/bin/wish

grid [label .myLabel -background red -text "Hello World" -relief ridge -borderwidth 3]
   -padx 100 -pady 100
```


### 基本小部件

可用小部件列表分类如下

|小部件 | 描述 |
|--|--|
| Label    | 用于显示单行文本的小部件 |
| Button   | 可点击并触发操作的小部件 |
| Entry    | 用于接受单行文本作为输入的小部件 |
| Message  | 用于显示多行文本的小部件 |
| Text     | 用于显示和选择性编辑多行文本的小部件 |
| Toplevel | 具有窗口管理器提供的所有边框和装饰的窗口 |

### 布局小部件

| 小部件 | 描述 |
|--|--|
| Frame | 用于容纳其他小部件的容器小部件 |
| Place | 小部件将其他小部件固定在特定位置，并具有其原点坐标和精确大小 |
| Pack  | 简单的小部件，用于在将小部件放入父小部件之前将它们组织成块 |
| Grid  | 小部件以不同方向嵌套小部件 |

### 选择小部件

| 小部件 | 描述 |
|--|--|
| Radiobutton | 具有一组开/关按钮和标签的小部件，可以选择其中一个 |
| Checkbutton | 具有一组开/关按钮和标签的小部件，其中许多可以选择 |
| Menu        | 充当菜单项支架的小部件 |
| Listbox     | 显示单元格列表的小部件，可以选择其中一个或多个单元格 |

### 大型小部件

| 小部件 | 描述 |
|--|--|
| Dialog      | 用于显示对话框的小部件 |
| Spinbox     | 允许用户选择数字的小部件 |
| Combobox    | 将条目与可供使用的选项列表相结合的小部件 |
| Notebook    | 选项卡式小部件，可帮助使用索引选项卡在多个页面之一之间切换 |
| Progressbar | 小部件为文件上传等长时间操作的进度提供视觉反馈 |
| Treeview    | 用于显示并允许浏览更多以树形式的项目层次结构的小部件 |
| Scrollbar   | 滚动没有文本或画布小部件的小部件 |
| Scale       | 缩放小部件以通过滑块选择数值 |

### 其他小部件

| 小部件 | 描述 |
|--|--|
| Canvas | 用于显示图形和图像的绘图小部件 |


## 基本小部件

基本小部件是几乎所有 Tk 应用程序中都可用的常见小部件。 下面给出了可用的基本小部件
的列表：

|小部件 | 说明 |
|--|--|
| Label    | 用于显示单行文本的小部件 |
| Button   | 可点击并触发操作的小部件 |
| Entry    | 用于接受单行文本作为输入的小部件 |
| Message  | 用于显示多行文本的小部件 |
| Text     | 用于显示和选择性编辑多行文本的小部件 |
| Toplevel | 用于创建一个框架的小部件，该框架是一个新的顶级窗口 |

下面显示了一个使用基本小部件的简单 Tk 示例：
```
#!/usr/bin/wish

grid [label .myLabel -text "Label Widget" -textvariable labelText]
grid [text .myText -width 20 -height 5]
.myText insert 1.0 "Text\nWidget\n"
grid [entry .myEntry -text "Entry Widget"]
grid [message .myMessage -background red -foreground white -text "Message\nWidget"]
grid [button .myButton1  -text "Button" -command "set labelText clicked"]
```

## 布局小部件

布局小部件用于处理 Tk 应用程序的布局。 框架小部件用于对其他小部件进行分组，而放置、
打包和网格是布局管理器，可让您完全控制向窗口的添加。 可用布局小部件列表如下所示：

|小部件 | 说明 |
|--|--|
| Frame | 用于容纳其他小部件的容器小部件 |
| Place | 用于将其他小部件保存在特定位置的小部件，并具有其原点坐标和精确大小 |
| Pack  | 简单的小部件，用于在将小部件放入父小部件之前将它们组织成块 |
| Grid  | 小部件以不同方向嵌套小部件 |

下面显示了布局小部件的简单 Tk 示例：
```
#!/usr/bin/wish

frame .myFrame1 -background red  -relief ridge -borderwidth 8 -padx 10 -pady 10
   -height 100 -width 100
frame .myFrame2 -background blue  -relief ridge -borderwidth 8 -padx 10 -pady 10
   -height 100 -width 50
pack .myFrame1
pack .myFrame2
```

## Selection 选择小部件

选择小部件用于在 Tk 应用程序中选择不同的选项。 可用选择小部件的列表如下所示：

| 小部件 | 说明 |
| Radiobutton | 具有一组开/关按钮和标签的小部件，可以选择其中一个 |
| Checkbutton | 具有一组开/关按钮和标签的小部件，其中许多可以选择 |
| Menu        | 充当菜单项支架的小部件 |
| Listbox     | 显示单元格列表的小部件，可以选择其中一个或多个单元格 |

下面显示了一个使用选择小部件的简单 Tk 示例：
```
#!/usr/bin/wish

grid [frame .gender ]
grid [label .label1  -text "Male" -textvariable myLabel1 ]
grid [radiobutton .gender.maleBtn -text "Male"   -variable gender -value "Male"
   -command "set  myLabel1 Male"] -row 1 -column 2
grid [radiobutton .gender.femaleBtn -text "Female" -variable gender -value "Female"
   -command "set  myLabel1 Female"] -row 1 -column 3
.gender.maleBtn select
grid [label .myLabel2  -text "Range 1 not selected" -textvariable myLabelValue2 ]
grid [checkbutton .chk1 -text "Range 1" -variable occupied1 -command {if {$occupied1 } {
   set myLabelValue2 {Range 1 selected}
} else {
   set myLabelValue2 {Range 1 not selected}
} }]
proc setLabel {text} {
   .label configure -text $text
}
```

## Canvas 画布小部件

Canvas 用于提供绘图区域。 画布小部件的语法如下所示：
```
canvas canvasName options
```

选项

下表列出了画布小部件的可用选项：

| 语法 | 描述 |
|--|--|
| -background color         | 用于设置小部件的背景颜色 |
| -closeenough distance     | 设置鼠标光标与可显示项目的距离。 默认值为 1.0 像素。 该值可以是小数，但必须是正数 |
| -scrollregion boundingBox | 画布总面积的边界框 |
| -height number            | 用于设置小部件的高度 |
| -width number             | 设置小部件的宽度 |
| -xscrollincrement size    | 请求滚动时水平滚动的量 |
| -yscrollincrement size    | 请求滚动时垂直滚动的量 |

下面显示了画布小部件的简单示例：
```
#!/usr/bin/wish

canvas .myCanvas -background red -width 100 -height 100
pack .myCanvas
```


### 用于在画布中绘图的小部件

下面列出了可用于在画布中绘图的小部件的列表：

| 小部件 | 描述 |
|--|--|
| Line      | 绘制一条线 |
| Arc       | 绘制圆弧 |
| Rectangle | 绘制一个矩形 |
| Oval      | 绘制一个椭圆形 |
| Polygon   | 绘制多边形 |
| Text      | 绘制文本 |
| Bitmap    | 绘制位图 |
| Image     | 绘制图像 |

下面显示了使用不同画布小部件的示例：
```
#!/usr/bin/wish

canvas .myCanvas -background red -width 200 -height 200
pack .myCanvas
.myCanvas create arc 10 10 50 50 -fill yellow
.myCanvas create line 10 30 50 50 100 10 -arrow both -fill yellow -smooth true
   -splinesteps 2
.myCanvas create oval 50 50 100 80 -fill yellow
.myCanvas create polygon 50 150 100 80 120 120 100 190 -fill yellow -outline green
.myCanvas create rectangle 150 150 170 170  -fill yellow
.myCanvas create text 170 20 -fill yellow -text "Hello" -font {Helvetica -18 bold}
.myCanvas create bitmap 180 50 -bitmap info
```


## Mega 小部件

Mega 小部件包括许多复杂的小部件，这些小部件在一些大型 Tk 应用程序中通常需要。
可用的大型小部件列表如下所示：

| 小部件 | 描述 |
|--|--|
| Dialog  | 用于显示对话框的小部件 |
| Spinbox | 允许用户选择数字的小部件 |
| Combobox | 将条目与可供使用的选项列表相结合的小部件 |
| Notebook | 选项卡式小部件，可帮助使用索引选项卡在多个页面之一之间切换 |
| Progressbar | 小部件为文件上传等长时间操作的进度提供视觉反馈 |
| Treeview | 用于显示并允许浏览更多以树形式的项目层次结构的小部件 |
| Scrollbar | 滚动没有文本或画布小部件的小部件 |
| Scale | 缩放小部件以通过滑块选择数值 |

下面显示了一个使用一些 mega 小部件的简单 Tk 示例：
```
#!/usr/bin/wish

ttk::treeview .tree -columns "Creator Year" -displaycolumns "Year Creator"
.tree heading Creator -text "Creator" -anchor center
.tree heading Year -text "Year" -anchor center
pack .tree
.tree insert {} end -id Languages -text "Languages"
.tree insert Languages end -text C -values [list "Dennis Ritchie" "1990"]
proc scaleMe {mywidget scaleValue} {
   $mywidget configure -length $scaleValue
}
pack [scale .s2  -from 100.0 -to 200.0 -length 100 -background yellow -borderwidth 5
   -font{Helvetica -18 bold} -foreground red -width 40 -relief ridge -orien horizontal
   -variable a -command "scaleMe .s2" ]
pack [ttk::progressbar .p1 -orient horizontal -length 200 -mode indeterminate -value 90]
pack [ttk::progressbar .p2 -orient horizontal -length 200 -mode determinate -variable a
   -maximum 75 -value 20]
```

## 字体

有许多小部件支持显示文本。 其中大多数都提供字体属性的选项。 创建字体的语法如下所示：
```
font create fontName options
```

下表列出了可用于字体创建的选项：

| 语法 | 描述 |
|--|--|
| -family familyName | 字体系列的名称 |
| -size number       | 字体大小 |
| -weight level      | 字体粗细 |

下面显示了一个简单的字体创建示例：
```
#!/usr/bin/wish

font create myFont -family Helvetica -size 18 -weight bold
pack [label .myLabel -font myFont -text "Hello World"]
```

要获取所有可用的字体，我们可以使用以下命令：
```
#!/usr/bin/wish

puts [font families]
```

## image 图像小部件

图像小部件用于创建和操作图像。 创建图像的语法如下：
```
image create type name options
```
在上面的语法中，类型是照片或位图，名称是图像标识符

下表列出了可用于图像创建的选项：

| 语法 | 描述 |
|--|--|
| -file fileName | 图像文件名的名称 |
| -height number | 用于设置小部件的高度 |
| -width number  | 设置小部件的宽度 |
| -data string   | 采用 Base 64 编码字符串的图像 |

下面显示了图像小部件的简单示例：
```
#!/usr/bin/wish

image create photo imgobj -file "/Users/rajkumar/Desktop/F Drive/pictur/vb/Forests/
   680049.png" -width 400 -height 400
pack [label .myLabel]
.myLabel configure -image imgobj
```

下表列出了图像可用的函数：

| 语法 | 描述 |
| image delete imageName | 从内存和相关小部件中直观地删除图像 |
| image height imageName | 返回图像的高度 |
| image width imageName  | 返回图像的宽度 |
| image type imageName   | 返回图像的类型 |
| image names            | 返回内存中的图像列表 |

下面显示了使用上述图像小部件命令的简单示例：
```
#!/usr/bin/wish

image create photo imgobj -file "/Users/rajkumar/images/680049.png"
   -width 400 -height 400
pack [label .myLabel]
.myLabel configure -image imgobj
puts [image height imgobj]
puts [image width imgobj]
puts [image type imgobj]
puts [image names]
image delete imgobj
```
一旦执行"image delete imgobj"命令，图像将从视觉上从内存中删除。 在控制台中，输出
将类似于以下内容：
```
400
400
photo
imgobj ::tk::icons::information ::tk::icons::error ::tk::icons::
warning ::tk::icons::question
```


## 事件

最简单形式的事件是在命令的帮助下处理的。 事件处理的一个简单示例是使用按钮进行事件
处理，如下所示：
```
#!/usr/bin/wish

proc myEvent { } {
   puts "Event triggered"
}
pack [button .myButton1  -text "Button 1"   -command myEvent]
```

一个显示延迟文本动画事件的简单程序如下所示：
```
#!/usr/bin/wish

proc delay {} {
   for {set j 0} {$j < 100000} {incr j} {}
}

label .myLabel -text "Hello................" -width 25
pack .myLabel
set str "Hello................"
for {set i [string length $str]} {$i > -2} {set i [expr $i-1]} {
   .myLabel configure -text [string range $str 0 $i]
   update
   delay
}
```

### 延迟后的事件

延迟后事件的语法如下所示：
```
after milliseconds number command
```
延迟事件后显示的简单程序如下所示
```
#!/usr/bin/wish

proc addText {} {
   label .myLabel -text "Hello................" -width 25
   pack .myLabel
}
after 1000 addText
```

可以使用 after cancel 命令取消事件，如下所示：
```
#!/usr/bin/wish

proc addText {} {
   label .myLabel -text "Hello................" -width 25
   pack .myLabel
}
after 1000 addText
after cancel addText
```

### 事件绑定

事件绑定的语法如下所示：
```
bind arguments
```

Keyboard Events Example
```
#!/usr/bin/wish

bind .  {puts "Key Pressed: %K "}
```
当我们运行程序并按字母X时，我们将得到以下输出 −
```
Key Pressed: X
```

鼠标事件示例
```
#!/usr/bin/wish

bind .  {puts "Button %b Pressed : %x %y "}
```
当我们运行程序并按下鼠标左键时，我们将得到类似于以下内容的输出：
```
Button 1 Pressed : 89 90
```
将事件与按钮关联示例
```
#!/usr/bin/wish

proc myEvent { } {
   puts "Event triggered"
}
pack [button .myButton1  -text "Button 1"   -command myEvent]
bind .  ".myButton1 invoke"
```
当我们运行程序并按回车键时，我们将得到以下输出：
```
Event triggered
```


## 窗口管理器

窗口管理器用于处理顶层窗口。 它有助于控制窗口的大小、位置和其他属性。 在 Tk 中，
`.`用于指代主窗口。 窗口命令的语法如下所示：
```
wm option window arguments
```

下表显示了 Tk wm 命令可用的选项列表：

| 语法 | 描述 |
|--|--|
| aspect windowName a b c d          | 尝试将宽度/高度的比率保持在 a/b 和 c/d 之间 |
| geometry windowName geometryParams | 用于设置窗口的几何形状 |
| grid windowName w h dx dy          | 设置网格大小 |
| group windowName leaderName        | leaderName 提供一组相关窗口的 leaderName |
| deiconify windowName               | 最小化时使屏幕恢复正常 |
| iconify windowName                 | 最小化窗口 |
| state windowName                   | 返回窗口的当前状态 |
| withdraw windowName                | 取消映射窗口并删除内存中的详细信息 |
| iconbitmap windowName image        | 设置或返回图标位图 |
| iconPhoto windowName image         | 设置或返回图标照片 |
| command windowName commandString   | 在 WM_COMMAND 属性中记录启动命令 |
| protocol windowName arguments      | 注册一个处理协议请求的命令名称，可以是WM_DELETE_WINDOW，WM_SAVE_YOURSELF, WM_TAKE_FOCUS. Eg: wm protocol. WM_DELETE_WINDOW Quit. |
| minsize windowName size            | 确定最小窗口大小 |
| maxsize windowName size            | 确定最大窗口大小 |
| title windowName titleText         | 确定窗口的标题 |
| attributes subOptions              | 有很多可用的属性，如 Alpha、全屏等 |

下面的示例中使用了上面的一些命令：
```
#!/usr/bin/wish

wm maxsize . 800 800
wm minsize . 300 300
wm title . "Hello"
wm attributes . -alpha ".90"
wm geometry . 300x200+100+100
```

alpha 是可用的属性之一。 下面列出了常用的子命令列表：

| 语法 | 描述 |
|--|--|
| -alpha number      | 设置窗口的 Alpha |
| -fullscreen number | 数字可以是0（正常屏幕）或1（全屏） |
| -topmost number    | 设置或返回窗口是否位于最顶层。值可以是 0 或 1 |

### 创建窗口

我们可以使用toplevel命令来创建窗口，示例如下：
```
#!/usr/bin/wish

toplevel .t
```

### 销毁窗口

我们可以使用 destroy 命令来销毁窗口，示例如下：
```
#!/usr/bin/wish

destroy .t
```
上述命令将销毁名为.t的窗口


## geometry 几何管理器

几何管理器用于管理窗口和其他框架的几何形状。 我们可以用它来处理窗口和框架的位置和
大小。 layout 布局小部件就是用于此目的

### 定位和调整大小

定位和调整窗口大小的语法如下所示：
```
wm geometry . wxh+/-x+/-y
```
这里，w指的是宽度，h指的是高度。它后面跟着一个"+"或"-"符号，接下来的数字指的是
屏幕上的 x 位置。同样，下面带有数字的"+"或"-"符号指的是屏幕上的 y 位置

下面是上述语句的一个简单示例：
```
#!/usr/bin/wish

wm geometry . 300x200+100+100
```

### 网格几何

网格几何的语法如下所示：
```
grid gridName -column number -row number -columnspan number -rowspan number
```
列、行、列跨度或行跨度有助于提供网格几何形状

下面是上述语句的一个简单示例：
```
#!/usr/bin/wish

frame .myFrame1 -background red  -height 100 -width 100
frame .myFrame2 -background blue -height 100 -width 50
grid .myFrame1 -columnspan 10 -rowspan 10 -sticky w
grid .myFrame2 -column 10 -row 2
```
