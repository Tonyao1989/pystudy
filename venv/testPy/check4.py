#!/usr/bin/python
# -*- coding: UTF-8 -*-
#二次方程式 ax**2 + bx + c = 0
# a、b、c 用户提供，为实数，a ≠ 0
import cmath
a=int(input('请输入数字'))
b=int(input('请输入数字'))
c=int(input('请输入数字'))
#计算
d=(b**2)-4*a*c
#求根公式
x1=(-b-cmath.sqrt(d))/(2*a)
x2= (-b+cmath.sqrt(d))/(2*a)
print('结果为 {0} 和 {1}'.format(x1,x2))
