method:
	# 查找目录下所有测试用例进行测试
	pytest -v

method2:
	# 执行某个脚本、某个脚本中的类、某个脚本中的函数的测试用例
	pytest -v test_sample.py
	pytest -v test_class.py::TestDomo
	pytest -v test_class.py::TestDomo::test_demo1
	pytest -v test_sample.py::test_03

method3:
	# 通过一个单独的脚本，执行pytest，同样可以指定测试用例和参数
	# 也可以默认执行所有用例
	python run.py
