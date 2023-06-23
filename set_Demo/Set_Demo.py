#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
-----------------------------------------------------------
    @FileName  :Set_Demo.py
    @Time      :2023/6/18 20:39
    @Author    :LittleSeven
    @Address   ：https://gitee.com/linguchong/Django_Project_Demo.git
-----------------------------------------------------------
'''
set_demo = {1,2,1,1,2,3,4,5,6}
print(set_demo)
# print(set_demo[0])

print({i for i in set_demo})

set_demo01 = set_demo.copy()
print(set_demo,set_demo01)

set_demo02 = {0,1,2,3}
set_demo03 = {2,3,4,5}
# print(set_demo02.difference(set_demo03))
print(set_demo03.difference_update(set_demo02))

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6}
set3 = {1, 2}

set1.difference_update(set2, set3)

print(set1)

