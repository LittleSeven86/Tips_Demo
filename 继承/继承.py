"""
 #!/usr/bin/env python
 # -*- coding:utf-8 -*-
 @Author: Little Seven
 @FileName: 继承.py
 @DateTime: 2023/7/28 15:32
 @SoftWare: PyCharm
"""
class Animal:
    def make_sound(self):
        print("这是动物的叫声")


class Dog(Animal):
    def make_sound(self):
        print("汪汪汪~狗再叫！")


animal = Animal()
animal.make_sound()  # 输出: 这是动物的叫声

dog = Dog()
dog.make_sound()  # 输出: 汪汪汪~狗再叫！


