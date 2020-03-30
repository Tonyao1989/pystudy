#!/usr/bin/python
# -*- coding: UTF-8 -*-
#一整数的阶乘（英语：factorial）是所有小于及等于该数的正整数的积，0的阶乘为1。即：n!=1×2×3×...×n。
a=int(input('输入一个数a:'))
factorial = 1
if a<0:
    print('数据%a没有阶乘'%a)
elif a==0:
    print('%a的阶乘为0'%a)
else:
    for i in range(1,a+1):
        factorial=factorial*i
    print('%a的阶乘为%d'%(a,factorial))