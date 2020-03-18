#!/usr/bin/python
# -*- coding: UTF-8 -*-
#以下实例通过创建自定义函数 is_number() 方法来判断字符串是否为数字：
def is_number(a):
    try:
        float(a)#先判断是否是浮动型
        return True
    except ValueError as e:
        pass
    try:
        import unicodedata
        for i in a:#遍历字符串中的
            unicodedata.numeric(i) #把一个表示数字的字符串转换为浮点数返回的函数
        return  True
    except  ValueError as a:
        print(a)
        pass
    return False


#调用函数
print(is_number('十1234w'))

#遍历
# a='123abc'
# for i in (a):
#     print(i)