#!/usr/bin/python
# -*- coding: UTF-8 -*-
#平方根，又叫二次方根，表示为〔√￣〕，如：数学语言为：√￣16=4。语言描述为：根号下16=4。
#以下实例为通过用户输入一个数字，并计算这个数字的平方根：
import cmath
num1=int(input('请输入一个数字：'))
sqrtqnum=cmath.sqrt(num1)
print('数字{0}的平方根是{1:0.3f}+{2:0.3f}j'.format(num1,sqrtqnum.real,sqrtqnum.imag))
