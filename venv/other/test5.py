#!/usr/bin/python
# -*- coding: UTF-8 -*-
#字典创建
#生成N个随机数的大写字符存入列表
num = 10
import random
#创建空列表 chr(random.randint(65,91))
result = [ chr(random.randint(65,90)) for i  in range (num)]
print(result)