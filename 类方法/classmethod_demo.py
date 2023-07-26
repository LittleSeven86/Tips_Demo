"""
 #!/usr/bin/env python
 # -*- coding:utf-8 -*-
 @Author: Little Seven
 @FileName: classmethod_demo.py
 @DateTime: 2023/7/26 15:39
 @SoftWare: PyCharm
"""
class Person:
    def __init__(self,name):
        self.name = name

    def demo(self):
        print(f'实例方法，通过对象调用，名字是：{self.name}')

Jack = Person('jack')
Jack.demo()

class ClassMethod:
    height = 180.55
    def __init__(self,age):
        self.age = age

    @classmethod
    def check_id(cls):
        print(f'当前对象的id是：{id(cls)}')
    @classmethod
    def other_classmethod(cls):
        pass
    @classmethod
    def demo(cls,name):
        cls.other_classmethod()
        print(f'名字是:{name}')
        print(cls.height)
        cls.testdemo()

    def testdemo(self):
        pass


# ClassMethod.demo('jack')
#
# ClassMethod.check_id()
# ClassMethod.check_id()
# ClassMethod.testdemo()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def create_person(cls, name, age):
        return cls(name, age)

person = Person.create_person("Alice", 25)
print(person.name)  # 输出：Alice
print(person.age)   # 输出：25
