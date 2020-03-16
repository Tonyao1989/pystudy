#!/usr/bin/python
# -*- coding: UTF-8 -*-
#以下实例为通过用户输入三角形三边长度，并计算三角形的面积：
import math
a=float(input('请输入长度a：'))
b=float(input('请输入长度b：'))
c=float(input('请输入长度b：'))
p=float(a+b+c)/2
s=math.sqrt(p*(p-a)*(p-b)*(p-c))
print('三角形面积是：{0:0.2f}'.format(s))