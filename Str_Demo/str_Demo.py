#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
-----------------------------------------------------------
    @FileName  :str_Demo.py
    @Time      :2023/6/13 21:06
    @Author    :LittleSeven
    @Address   ：https://gitee.com/linguchong/Django_Project_Demo.git
-----------------------------------------------------------
'''
# 字符串的定义
import os
import sys

str1 = '人生苦短，我用python'
str2 = "人生苦短，我用python"
str3 = """人生苦短，我用python"""
print(str1, str2, str3)     # 人生苦短，我用python 人生苦短，我用python 人生苦短，我用python

# 字符串的拼接
str4 = str1+str2
print(str4)     # 人生苦短，我用python人生苦短，我用python

# 字符串的复制
str5 = str1*3
print(str5)     # 人生苦短，我用python人生苦短，我用python人生苦短，我用python

# 字符串转义字符--\n   换行符
print('锄禾日当午\n汗滴禾下土\n谁知盘中餐\n粒粒皆辛苦')
'''
锄禾日当午
汗滴禾下土
谁知盘中餐
粒粒皆辛苦
'''

# 字符串转义字符--\t   制表符--作用为常见的tab键
print("人之初\t性本善\t性相近\t习相远")     # 人之初	性本善	性相近	习相远

# 字符串转义字符--\r   等同于回车，注意的时会将光标移动到当前行的开头，并且覆盖当前行已经存在的内容
print("""好好\r学习""")

# 字符串转义字符--\\   输出反斜杠\ ，常在路径当中使用
print('C:\\demo\\demo')     # C:\demo\demo

# 字符串转义字符--\' \"   输出字符串引号' "
print('这是双引号\"，',"这是单引号\'")     # 这是双引号"， 这是单引号'

# 格式化输出并保留小数位
str5 = '%s是%d班的学生，学号是%d,平均成绩是%.2f'%('小明',1,20,89.0000)
print(str5)     # 小明是1班的学生，学号是20,平均成绩是89.00

# format 格式化方法 --默认排序
str6 = '{}是{}班的学生，{}是他的学号，数学成绩是{}'.format('小明',3,20,89.00)  #小明是3班的学生，20是他的学号，数学成绩是89.0
print(str6)

# format 格式化方法 --指定排序
str7 = '{3}是{0}班的学生，{1}是他的学号，数学成绩是{2:.2f}'.format(3,20,89.00000,'小明') # 小明是3班的学生，20是他的学号，数学成绩是89.0
print(str7)

# format 格式化方法 --指定关键字
str7 = '{name}是{num}班的学生，{id}是他的学号，数学成绩是{score:.2f}'.format(num=3,id=20,score=89.00000,name='小明')
# 小明是3班的学生，20是他的学号，数学成绩是89.0
print(str7)

# 使用f''字符串格式化
name = 'json'
age = 18
print(f'{name}今年{age}周岁了')  # json今年18周岁了


# 字符串切片 str[开始位置:结束位置:步长]
str8 = 'ABCDEFG'
print(str8[2])      #  [下标位置]--取下标为下标为2的元素--C

print(str8[0:2])    #  [start:end]--取开始位置至结束位置的元素（不包括结束位置）--AB

print(str8[3:])     #   [start:]--取开始位置到结束结束位置全部到元素--DEFG

print(str8[:7])     #   [:end]--默认从下标位置0到结束位置--ABCDEFG

print(str8[:])      #   [:]--默认输出全部位置--ABCDEFG

print(str8[-4])     #   [-1]--字符串从后向前取值--D

print(str8[3:0:-1]) #   当step<0时，从右向左取字符--DCB

print(str8[::-1])   #   反向输出全部--GFEDCBA

print(str8[::-3])   #   反向输出，步长为3--GDA

print(str8[4::-1])  #   从开始位置4逆向切片--EDCBA



