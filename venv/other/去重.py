#!/usr/bin/python
# -*- coding: UTF-8 -*-
#去重
#创建新列表
import  random
scr_list = [random.randint(20,30) for i in range(15)]
print(scr_list)

#用新列表搜集
taget_lis=[]
for newlist in scr_list:
    if newlist not in taget_lis:
        taget_lis.append(newlist)
print(taget_lis)


#set方法
import  random
scr_list1 = [random.randint(20,30) for i in range(15)]
print(scr_list1)
scr_list2=list(set(scr_list1))
print(scr_list2)

#itertools 模块 groupby函数
import  itertools
import  random
scr_list3 = [random.randint(20,30) for i in range(15)]
print(scr_list3)
it_list=itertools.groupby(scr_list3)
for k,g in it_list:
    print(k,end =" ")