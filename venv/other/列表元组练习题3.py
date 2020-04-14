#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random
n = int(input('请输入一个整数：'))
n_list = []
for i in range(n):
    num = random.randint()
    n_list.append(num)
print(n_list)

length = int(input('请输入一个整数：'))
my_list1 = []
my_list1 = [random.random() for i in range(length)]
print(my_list1)
