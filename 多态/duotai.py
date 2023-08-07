"""
 #!/usr/bin/env python
 # -*- coding:utf-8 -*-
 @Author: Little Seven
 @FileName: duotai.py
 @DateTime: 2023/8/4 17:11
 @SoftWare: PyCharm
"""
class Model:
    def get(self):
        pass

    def save(self):
        pass
    def update(self):
        pass

class ProjectModels(Model):
    def get(self):
        print('获取到了项目信息')
    def save(self):
        print('保存项目基本信息')
    def update(self):
        print('更新项目基本信息')

class TestCase(Model):
    def get(self):
        print('获取用例基本信息')

    def save(self):
        print('保存用例基本信息')

    def update(self):
        print('更新用例基本信息')

def get_info(obj):
    obj.get()


project1 = ProjectModels()
project1.get()

case1 = TestCase()
case1.get()
get_info(case1)
get_info(project1)

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius


def print_area(shape):
    print("The area is:", shape.calculate_area())


# 创建不同类型的形状对象
rectangle = Rectangle(5, 3)
circle = Circle(4)

# 使用统一的接口打印面积
print_area(rectangle)  # 输出：The area is: 15
print_area(circle)  # 输出：The area is: 50.24
