#!/usr/bin/python
# -*- coding: UTF-8 -*-
#圆的面积公式为 ：
#公式中 r 为圆的半径
# 定义一个方法来计算圆的面积
#定义函数
def area(r):
    PI=3.14
    return PI*(r*r)

#调用函数
print("圆面积是：%.3f" % area(4))