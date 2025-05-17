reference:  
[超详细的 pytest 教程【入门篇】](https://zhuanlan.zhihu.com/p/511774800)  
[pytest系列](https://blog.csdn.net/u010454117/category_11174856.html)

# 介绍

* python常用测试框架有Unittest、Doctest、Nose及Pytest
* unittest大部分人都非常清楚，都用来做自动化，无论是UI还是接口自动化
* Nose是对unittest的扩展，使得python的测试更加简单。nose自动发现测试代码并执行，
  nose提供了大量的插件，但是很多插件不支持python3
* doctest是python自带的一个模块，你可以把它叫做“文档测试”（doctest）模块，使用
  起来不太方面，被大家放弃使用
* pytest是基于unittest开发的另一款更高级更好用的单元测试框架，提供了丰富的插件
  且容易使用，二次开发也比较简单

# 安装pytest

pytest需要：Python 3.8+ 或 PyPy3。

在命令行中运行以下命令：
```shell
pip install -U pytest
```
检查您是否安装了正确的版本：
```shell
$ pytest --version
pytest 7.4.2
```

# 用例编写

## 默认的用例识别的规则

* 文件名用 `test_*.py` 文件和`*_test.py`
* 以 test_ 开头的函数
* 以 Test 开头的类，不能包含 `__init__` 方法
* 以 test_ 开头的类里面的方法
* 所有的包 pakege 必须要有`__init__.py` 文件

```
注意：上述默认的用例查找规则，可在 pytest 的配置文件进行修改。另外 pytest 兼容
unittest，以 unittest 的用例编写规范写的用例，pytest 都能够识别出来
```

## 断言的使用

测试用例的预期结果是用例不可缺少的一部分，那么断言就是自动化测试不可缺少的一步，
一个没有断言的用例，自动化测试的就没有意义了。Pytest里面使用关键字assert，断言
为一个表达式，只要表达式的最终结果为True，那么断言通过，用例执行成功，否则用例
执行失败。（不会根据函数返回值判断用例是否执行成功）

### 常规断言方式 Assert

pytest里面断言实际上就是python里面的assert断言方法，常用的有以下几种
* assert xx 判断xx为真
* assert not xx 判断xx不为真
* assert a in b 判断b包含a
* assert a == b 判断a等于b
* assert a != b 判断a不等于b

```Python
import pytest

def func(a):
    if a > 2:
        return True
    else:
        return False

def test_01():
    """断言xx为真"""
    a = 3
    b = 1
    assert func(a)

def test_02():
    """断言 b 包含 a"""
    a = "king"
    b = "hello king"
    assert a in b

def test_03():
    """断言相等"""
    a = "king"
    b = "king"
    assert a == b

def test_04():
    """断言不等于"""
    a = 1
    b = 2
    assert a != b
```

### 异常断言Excepiton

除了支持对代码正常运行的结果断言之外，Pytest也能够对 Exception 和 Warnning 进行
断言，这里不做介绍。

```python
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0
```


### 优化断言提示信息

可以直接在断言语句后加上说明信息，例如：
```python
def test_assert_fail():
    a = 2
    b = 3
    assert a == b, "判断 a 和 b 是否相等 a:{} b: {}".format(a, b)
```



## 函数形式编写用例

查看demo

## 以类的形式编写用例

查看demo

# 执行测试

 pytest 执行测试有两种方式：
 1. 命令行通过 pytest 这个命令执行，将查找目录下所有测试用例进行测试，目录为当前
    目录，也可以人为指定
 2. 另外在代码中也可以通过 pytest.main() 这个方法来执行测试

## 执行参数

```
-v: 显示测试的详细参数信息
-s: 显示测试执行的输出信息
```

1. 某个目录下所有的用例 cmd命令行输入：pytest

2. 执行某一个 py 文件下用例 pytest <脚本名称>.py

3. 运行模块里面的某个函数，或者某个类，某个类里面的方法
```
pytest test_01.py::TestClass::test_one
pytest test_01.py::TestClass
pytest test_01.py::test_answer
```

4. -m 标记表达式（后面详细讲解）
```
pytest -m smoke
```

5. -q 简单打印，只打印测试用例的执行结果

6. -v 详细打印

7. -s 打印print 调式相关信息

8. -x 遇到错误时停止测试

9. —maxfail=num，当用例错误个数达到指定数量时，停止测试
```
pytest test_01.py --maxfail=1
```

10. -k 匹配用例名称、根据用例名称排除某些用例、同时匹配不同的用例名称
```
pytest -s -k xkw test_01.py
pytest -s -k “not xkw” test_01.py
pytest -s -k “test_answer or test_two” test_01.py
```


## pytest.main 执行的参数传递

可以在代码中添加pytest.main来传递执行参数

例如：
```python
import pytest

if __name__ == '__main__':
        pytest.main(["-s", "-v", "-x"])
```

main() 命令行参数详情
* -s: 显示程序中的print/logging输出
* -v: 丰富信息模式, 输出更详细的用例执行信息
* -q: 安静模式, 不输出环境信息
* -x: 出现一条测试用例失败就退出测试。调试阶段非常有用
* -k：可以使用and、not、or等逻辑运算符，区分：匹配范围（文件名、类名、函数名）



运行当前目录和子目录下所有（`test_*.py`和`*_test.py`）的用例
```python
if __name__ == '__main__':
    pytest.main(["./"])
    # pytest.main() 默认也可以
```
运行指定目录下用例，例如：运行eclass目录下的case
```python
pytest.main(["./eclass", '-v'])
```
运行指定模块，例如：运行test_summary.py
```python
pytest.main(["./test_summary.py", '-v'])
```
运行模块中的指定用例，例如：运行test_summary.py里面的TestSummary
```python
pytest.main(["./test_summary.py::TestSummary", '-v'])
```
运行类中的指定用例，例如：运行test_summary.py里面的TestSummary类的test_01
```python
pytest.main(["./test_summary.py::TestSummary::test_01", '-v'])
```
匹配包含king的用例(匹配目录名、模块名、类名、用例名)
```python
pytest.main(['-k','king', '-v'])
```
匹配test_summary.py模块下包含king的用例
```python
pytest.main(['-k','king',"./test_summary.py", '-v'])
```

## 添加自定义命令行参数

动态带参数需要用到：
* pytest_addoption 注册参数
* config.getoption 获取命令行参数

parser.addoption() 常用参数说明：
* name：自定义命令行参数的名字，就配置为："–foo"格式；
* action：默认action=“store”，只存储参数的值，可以存储任何类型的值，命令行参数
  多次使用也只能生效一个，最后一个值覆盖之前的值；
* default：默认值。
* choices：可以指定几个值，自定义参数必须在这几个值中选择一个，否则会报错；
* help：对参数作用的简要说明；

待完善用例

## 配置文件pytest.ini

如果熟悉其他框架可以知道，每个框架都有它自己的配置文件，只需要做简单的配置就可以
实现一些常用的功能，减少编程时间。

pytest 配置文件可以改变 pytest 的运行方式，它是一个固定的文件 pytest.ini文件，
读取配置信息，按指定的方式去运行框架的功能。

用法：在项目根目录创建一个 pytest.ini 的文件，名字固定不能改为其他的。

首先怎么知道配置文件，可以配置哪些功能呢？这需要看帮助文档，一般都是--help会出来
可以操作的功能说明，可以在命令行窗口输入： pytest --help 或者 pytest -h，查看结果

常用的参数使用分类：
* 更改命令行选项
* 自定义标记注册
* 用例搜索规则
* 日志配置参数
* 常用插件参数

### 更改命令行选项

通常我们在执行的时候添加上常用命令行参数，如pytest -v -s -x --maxfail=1，把这些
命令行参数放到pytest.ini 中:
```
[pytest]
addopts = -v -s --maxfail=1
```

### 自定义标记注册

这个在自定义标记文章讲解，可以参考[Pytest 自定义mark标记筛选用例实战](https://ceshizhilu.blog.csdn.net/article/details/118500633)，
主要解决自定义标记的warnings提示信息。

示例：
```
[pytest]
markers=
    web: web 测试用例
    app: app测试用例
```

### 用例搜索规则

指定测试用例目录搜索规则`testpaths = testcase/`
排除掉一些目录规则`norecursedirs = evn reports/`
指定测试类搜索规则`python_classes = Test* *Test`
指定测试文件搜索规则`python_files = test_*.py *_test.py`
指定测试函数搜索规则`python_functions = test* *test`

pytest.ini文件里面：
```
testpaths = testcase/
norecursedirs = evn reports/
python_classes = King* *King
python_files = king_*.py *_king.py
python_functions = king* *king
```

### 日志配置参数

说明：正常来说自动化测试项目都需要日志，在编写代码时需要调式日志，执行时需要执行
日志输出到日志文件。

pytest.ini 文件日志配置
```
"""
 命令行窗口日志输出配置
 log_cli 可以输入0, False 代码不输出日志， 1、True 代表开启日志输出
 log_cli_level 代表日志输出级别
 log_cli_date_format 日期格式
 log_cli_format 日志模板格式
"""
log_cli=1
log_cli_level=info
log_cli_date_format=%Y-%m-%d-%H-%M-%S
log_cli_format=%(asctime)s-%(filename)s-%(module)s-%(funcName)s-%(lineno)d-%(levelname)s-%(message)s

"""
 日志输出到文件配置
 log_file 日志文件
 log_file_level 代表日志输出级别
 log_file_date_format 日期格式
 log_file_format 日志模板格式
"""
log_file=outputs/logs/test.log
log_file_level=INFO
log_file_date_format=%Y-%m-%d %H:%M:%S
log_file_format=%(asctime)s %(filename)s %(module)s %(funcName)s %(lineno)d %(levelname)s: %(message)s
```

### 常用插件参数

说明：像我们经常需要将失败重试、生成HTML报告等需要每次都生成，为了方便，就会将这些命令加到配置文件

pytest.ini示例：
```
addopts = --reruns=1 --reruns-delay=5 --html=reports.html --self-contained-html
```

### 完整的一个配置

pytest.ini 文件：
```
[pytest]
addopts = -v -s --reruns=1 --reruns-delay=5 --html=reports.html --self-contained-html


markers=
    web: web 测试用例
    app: app 测试用例

testpaths = testcase/
norecursedirs = evn reports/
python_classes = King* *King
python_files = king_*.py *_king.py
python_functions = king* *king


log_cli=1
log_cli_level=info
log_cli_date_format=%Y-%m-%d-%H-%M-%S
log_cli_format=%(asctime)s-%(filename)s-%(module)s-%(funcName)s-%(lineno)d-%(levelname)s-%(message)s


log_file=test.log
log_file_level=INFO
log_file_date_format=%Y-%m-%d %H:%M:%S
log_file_format=%(asctime)s %(filename)s %(module)s %(funcName)s %(lineno)d %(levelname)s: %(message)s
```
