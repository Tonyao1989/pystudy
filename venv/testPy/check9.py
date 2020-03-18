#!/usr/bin/python
# -*- coding: UTF-8 -*-
#以下实例通过使用 if...elif...else 语句判断数字是正数、负数或零：
a = float(input('请输入一个数字a：'))
if ( a>0 ):
    print("%a 是正数"%a)
elif ( a<0 ):
    print("%a 是负数"%a)
else:
    print("输入数字是0")
