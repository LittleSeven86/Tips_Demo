"""
 #!/usr/bin/env python
 # -*- coding:utf-8 -*-
 @Author: Little Seven
 @FileName: magic_method.py
 @DateTime: 2023/8/14 15:15
 @SoftWare: PyCharm
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Alice", 25)
print(id(person1))      # 2181853216720
print(person1.name)   # 输出：Alice
print(person1.age)    # 输出：25

person2 = Person("Bob", 30)
print(id(person2))      # 2181853216528
print(person2.name)   # 输出：Bob
print(person2.age)    # 输出：30

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

person = Person("Alice", 25)
print(person)   # 输出：Person(name=Alice, age=25)

class MyCallable:
    def __call__(self, *args):
        print("当前类的参数是:", args)

# 创建可调用对象的实例
my_callable = MyCallable()

# 调用实例对象，触发 __call__ 方法
my_callable(1, 2, 3)

import logging

import time
class Logger:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        stime = time.time()
        print(f"开始执行程序: {self.func.__name__}")
        result = self.func(*args, **kwargs)
        # time.sleep(2)
        print(f"结束执行程序: {self.func.__name__},持续时长为：{time.time()-stime:.2f}s")
        return result


@Logger
def add_numbers(a, b):
    return a + b


result = add_numbers(2, 3)
print("Result:", result)

class Demo_Singleton:
    def __new__(cls, *args, **kwargs):
        print('__new__()方法先被调用')
        # return super().__new__(cls)

    def __init__(self):
        print('__init__()方法先被调用')

d = Demo_Singleton()
print(id(d))        # 1408506017392
e = Demo_Singleton()
print(id(e))        # 1408506017152
f = Demo_Singleton()
print(id(f))        # 1408506015616


class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


# 创建对象实例
obj1 = Singleton()
obj2 = Singleton()

print(obj1 is obj2)  # 输出: True，obj1和obj2是同一个对象实例
print(id(obj1),id(obj2))


class SingletonMeta(type):
    instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.instances:
            cls.instances[cls] = super().__call__(*args, **kwargs)
        return cls.instances[cls]


class Singleton(metaclass=SingletonMeta):
    def __init__(self):
        print(id(self))

# 使用 Singleton 类
a = Singleton()
b = Singleton()