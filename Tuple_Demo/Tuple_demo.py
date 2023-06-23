#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
-----------------------------------------------------------
    @FileName  :Tuple_demo.py
    @Time      :2023/6/18 16:29
    @Author    :LittleSeven
    @Address   ：https://gitee.com/linguchong/Django_Project_Demo.git
-----------------------------------------------------------
'''
import copy

tuple_int = (12,20,30,40,'a')
# print(min(tuple_int))
print(tuple_int.count(12))
print(tuple_int.index('a'))
# iter(tuple_int)

iter_tuple = ( i for i in tuple_int)
print(next(iter_tuple),iter_tuple.__next__())

list = list(tuple_int)
list[0] = 'change'
tuple01 = tuple(list)
print(type(tuple01),tuple01)

