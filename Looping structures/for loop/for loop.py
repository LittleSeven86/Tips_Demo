#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
-----------------------------------------------------------
    @FileName  :for loop.py
    @Time      :2023/7/1 16:05
    @Author    :LittleSeven
    @Address   ：https://gitee.com/linguchong/Django_Project_Demo.git
-----------------------------------------------------------
'''
# 遍历字符串
str_demo = 'hello'
for i in str_demo:
    print(i)

# 遍历列表
list_demo = ['jack','tom','andy']
for i in list_demo:
    print(i)

# 遍历字典--遍历字典的键
dict_demo = {'name':'xiaoqi',"age":17,"height":180}
for k in dict_demo.keys():
    print(k)

# 遍历字典--遍历字典的值
for v in dict_demo.values():
    print(v)

# 遍历字典--遍历字典的键值对
for k,v in dict_demo.items():
    print(k,v)

for i in range(1,6):
  print(i)

for i in range(2, 8, 2):
    print(i)

# 给你一个字符串 s，由若干单词组成，单词前后用一些空格字符隔开。返回字符串中 最后一个 单词的长度。
# 单词 是指仅由字母组成、不包含任何空格字符的最大子字符串。
'''
输入：s = "Hello World"
输出：5
解释：最后一个单词是“World”，长度为5。
'''

def length_of_lastworld(str:str) -> int:
    '''
    :param str:
    :return: int
    '''
    str = str.rstrip()
    for i in range(len(str)-1,-1,-1):
        if str[i] == " ":
            return len(str) -i -1
    return len(str)

res  = length_of_lastworld('Hello World')
print(res)
