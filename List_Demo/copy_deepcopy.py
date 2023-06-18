#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
-----------------------------------------------------------
    @FileName  :copy_deepcopy.py
    @Time      :2023/6/18 15:06
    @Author    :LittleSeven
    @Address   ：https://gitee.com/linguchong/Django_Project_Demo.git
-----------------------------------------------------------
'''
import copy

list01 = [1,2,3,4,5,[6,7]]
list02 = list01
# list03 = list01.copy()
# print(id(list01),list01)
# print(id(list02),list02)
# print(id(list03),list03)
#
# list02[3] = '1'
# print(list01,list02)
#
#
# list01[5][0]=1
# print(id(list01),list01)
# print(id(list03),list03)
#
# list01[4] = '1'
# print(id(list01),list01)
# print(id(list03),list03)

list04 = copy.deepcopy(list01)
print(id(list01),list01)
print(id(list04),list04)

list01[5][0] = 'a'
print(id(list01),list01)
print(id(list04),list04)


str01 = 'abcd'
float01 = 23.0333
tuple01 = (1,2,34)
set01= {1,2,3,'44'}
print(id(str01),str01)
print(id(float01),float01)
print(id(tuple01),tuple01)
print(id(set01),set01)


str01 = 'cdef'
float01 = 24.098
tuple01 = (1,2,'aa')
set01= {1,2,3,}
print(id(str01),str01)
print(id(float01),float01)
print(id(tuple01),tuple01)
print(id(set01),set01)


list02 = [1,2,3,'11']
dict01 = {'name':'jack','age':16}

print(id(list04),list04)
print(id(dict01),dict01)

list02.pop(2)
del dict01['name']
print(id(list04),list04)
print(id(dict01),dict01)


