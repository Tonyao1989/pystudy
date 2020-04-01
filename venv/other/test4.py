#!/usr/bin/python
# -*- coding: UTF-8 -*-
#字典创建
#生成N个随机数的大写字符存入列表
num = 4
import random
#创建空列表
result = []
#循环存入列表
for i  in range (num):
    n = random.randint(23,56)
    result.append(chr(n))
print(result)