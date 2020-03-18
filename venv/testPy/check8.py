#!/usr/bin/python
# -*- coding: UTF-8 -*-
## 以下实例通过用户输入两个变量，并相互交换：
a = input('请输入a：')
b = input('请输入b: ')
#创建临时变量交换
temp=a
a=b
b=temp
print('交换后的a:{}'.format(a))
print('交换后的b:{}'.format(b))