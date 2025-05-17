#!/bin/python3
#########################################################################
# File Name: test_sample.py
# Author: LiHongjin
# mail: 872648180@qq.com
# Created Time: Fri Oct 20 14:48:38 2023
#########################################################################

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

