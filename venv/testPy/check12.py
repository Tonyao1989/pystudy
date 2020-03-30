#!/usr/bin/python
# -*- coding: UTF-8 -*-
#以下实例用于判断用户输入的年份是否为闰年：公历年份是4的倍数的，且不是100的倍数
def Leap_year(a):
    if ( a%4==0 ):
        if (a%100==0 ):
            print('%a 不是闰年' %a)
            return a
        else:
            print('%a 是闰年' %a)
            return a
    else:
        print('%a 不是闰年' %a)
        return a

print(Leap_year(2400))