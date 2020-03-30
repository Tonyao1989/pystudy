#!/usr/bin/python
# -*- coding: UTF-8 -*-
#一个大于1的自然数，除了1和它本身外，不能被其他自然数（质数）整除（2, 3, 5, 7等），
# 换句话说就是该数除了1和它本身以外不再有其他的因数。
a=int(input('请输入一个数据a：'))
if ( a>1 ):
   # print('数字%a是自然数' % a)
    for i in range (2,a):
        if ( a%i )==0:
            print('数字%a不是质数'%a)
            break
    else:
        print('数字%a是质数'%a)
else:
    print('数字%a不是自然数'%a)