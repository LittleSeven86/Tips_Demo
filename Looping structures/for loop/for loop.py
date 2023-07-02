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
list_demo = ['jack', 'tom', 'andy']
for i in list_demo:
    print(i)

# 遍历字典--遍历字典的键
dict_demo = {'name': 'xiaoqi', "age": 17, "height": 180}
for k in dict_demo.keys():
    print(k)

# 遍历字典--遍历字典的值
for v in dict_demo.values():
    print(v)

# 遍历字典--遍历字典的键值对
for k, v in dict_demo.items():
    print(k, v)

for i in range(1, 6):
    print(i)

for i in range(2, 8, 2):
    print(i)

for i in range(11, -1, -1):
    print(i)

# 给你一个字符串 s，由若干单词组成，单词前后用一些空格字符隔开。返回字符串中 最后一个 单词的长度。
# 单词 是指仅由字母组成、不包含任何空格字符的最大子字符串。
'''
输入：s = "Hello World"
输出：5
解释：最后一个单词是“World”，长度为5。
'''


def length_of_lastworld(str: str) -> int:
    '''
    函数接收一个输入字符串 str，表示给定的字符串，返回的是整数类型
    :param str:
    :return: int
    '''
    # 这一行代码去除输入字符串末尾的空格，确保字符串末尾没有额外的空格。
    str = str.rstrip()
    # 循环从字符串的最后一个字符开始往前遍历，生成一个倒序的索引序列
    for i in range(len(str) - 1, -1, -1):
        # 在遍历过程中，如果遇到空格字符，则说明已经找到了最后一个单词的末尾
        if str[i] == " ":
            # 返回从字符串末尾到找到的空格字符的长度，即为最后一个单词的长度
            return len(str) - i - 1
    # 如果在遍历过程中没有找到空格字符（即没有遇到分隔单词的空格），则说明整个字符串就是一个单词。此时函数会直接返回整个字符串的长度作为最后一个单词的长度
    return len(str)

def length_of_last_word_1(s: str) -> int:
    s = s.rstrip()  # 去除字符串末尾的空格
    last_space_index = s.rfind(' ')  # 查找最后一个空格字符的索引
    return len(s) - last_space_index - 1 if last_space_index != -1 else len(s)

res = length_of_last_word_1('Hello World')
print('结果是：'+ str(res))


list_demo = [
    ['jack', 18],
    ['tom', 19],
    ['hellen', 20]
]

for args in list_demo:
    print(f'外层循环的参数是：{args}')
    for inside_args in args:
        print(f'内层循环的参数是：{inside_args}')

for zuo in range(1,10):
    for you in range(1,zuo+1):
        print(f'{zuo}*{you}={zuo*you}',end=' ')
    print()