#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
-----------------------------------------------------------
    @FileName  :List_Demo.py
    @Time      :2023/6/18 14:30
    @Author    :LittleSeven
    @Address   ：https://gitee.com/linguchong/Django_Project_Demo.git
-----------------------------------------------------------
'''
list01 = [1,2,3,4,5]
list01.append('abc')
print(list01)	#[1, 2, 3, 4, 5, 'abc']

a = [1, 2, 3]
b = [4, 5, 6]
a.append(b)
print(a)		#[1, 2, 3, [4, 5, 6]]	a.append(b) 会将整个列表当做一个元素添加进去

list1 = []
for i in range(1,10):
    str1 = f"这是数字：{i}"
    list1.append(str1)
print(list1)	#['这是数字：1', '这是数字：2', '这是数字：3', '这是数字：4', '这是数字：5', '这是数字：6', '这是数字：7', '这是数字：8', '这是数字：9']

