#!/usr/bin/python
# -*- coding: UTF-8 -*-
#以下实例用于判断一个数字是否为奇数或偶数：
def is_oddeven(a):
    if (a%2==0):
        print('%a是偶数'% a)
        return a
    else:
        print('%a是奇数' % a)
        return a



print(is_oddeven(5))