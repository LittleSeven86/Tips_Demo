"""
 #!/usr/bin/env python
 # -*- coding:utf-8 -*-
 @Author: Little Seven
 @FileName: self_demo.py
 @DateTime: 2023/7/26 14:13
 @SoftWare: PyCharm
"""
class Person:
    def __init__(Qi, name):
        Qi.name = name

    def say_hello(Qi):
        print("Hello,我的名字是:", Qi.name)

Jack = Person('jack')
Jack.say_hello()

Allen = Person('Allen')
Allen.say_hello()

class Self:
    def __init__(self):
        print(f'构造方法:{self},id是{id(self)}')

demo1 = Self()
demo2 = Self()

