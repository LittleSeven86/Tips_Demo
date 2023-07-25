"""
 #!/usr/bin/env python
 # -*- coding:utf-8 -*-
 @Author: Little Seven
 @FileName: Python类.py
 @DateTime: 2023/7/25 14:15
 @SoftWare: PyCharm
"""


class Circle:
    # 类属性
    pi = 3.14159

    def __init__(self, radius):
        self.radius = radius

    # 实例方法
    def area(self):
        return self.pi * self.radius ** 2


# 访问类属性
print(Circle.pi)  # 输出：3.14159

# 创建类的实例并调用方法
circle = Circle(5)
print(circle.area())  # 输出：78.53975
print(circle.pi)  # 输出：3.14159


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f'{self.name}今年{self.age}')


XiaoMing = Student('xiaoming', 18)
print(XiaoMing.name)    # xiaoming
XiaoMing.introduce()  # xiaoming今年18

Jack = Student('jack', 20)
print(Jack.age)     # 20
Jack.introduce()  # jack今年20

print(XiaoMing)
print(id(XiaoMing)) # 1231016492528
print(id(Jack))     # 1231016492432