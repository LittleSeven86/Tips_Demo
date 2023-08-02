"""
 #!/usr/bin/env python
 # -*- coding:utf-8 -*-
 @Author: Little Seven
 @FileName: super_demo.py
 @DateTime: 2023/8/2 13:56
 @SoftWare: PyCharm
"""
class Person:
    def __init__(self, name):
        self.name = name
        print('初始化了Person类的属性')

class Employee(Person):
    def __init__(self, name, employee_id):
        super().__init__(name)
        self.employee_id = employee_id
        print('初始化了Employee类的属性')

    def get_info(self):
        print(f"姓名是: {self.name}, 工号是: {self.employee_id}")

employee = Employee("John", 12345)
employee.get_info()


class A:
    def __init__(self,name):
        self.name = name

class B(A):
    def __init__(self,name,age):
        super().__init__(name)
        self.age = age

b = B('jack',17)
print(b.name)

class Demo_A:
    def __init__(self):
        self.num = 100

    def add(self,args):
        print(f'当前DemoA中的【self】内存地址是：{id(self)}，参数self.n是：{self.num}')
        self.num+=args
        print(f'当前self.num的参数是：{self.num}')

class Demo_B(Demo_A):
    def __init__(self):
        self.num = 10

    def add(self,args):
        print(f'当前DemoB中的【self】内存地址是：{id(self)}，参数self.n是：{self.num}')
        super().add(args)
        self.num+=args

demob = Demo_B()
demob.add(5)
print(demob.num)

class A:
    def __init__(self):
        self.n = 2

    def add(self, m):
        # 第四步
        # 来自 D.add 中的 super
        # self == d, self.n == d.n == 5
        print('self is {0} @AAA.add'.format(self))
        self.n += m
        # d.n == 7


class C(A):
    def __init__(self):
        self.n = 4

    def add(self, m):
        # 第三步
        # 来自 B.add 中的 super
        # self == d, self.n == d.n == 5
        print('self is {0} @CCC.add'.format(self))
        # 等价于 suepr(C, self).add(m)
        # self 的 MRO 是 [D, B, C, A, object]
        # 从 C 之后的 [A, object] 中查找 add 方法
        super().add(m)

        # 第五步
        # d.n = 7
        self.n += 4
        # d.n = 11


class B(A):
    def __init__(self):
        self.n = 3

    def add(self, m):
        # 第二步
        # 来自 D.add 中的 super
        # self == d, self.n == d.n == 5
        print('self is {0} @BBB.add'.format(self))
        # self 的 MRO 是 [D, B, C, A, object]
        # 从 B 之后的 [C, A, object] 中查找 add 方法
        # 从 C 找 add 方法
        super().add(m)

        # 第六步
        # d.n = 11
        self.n += 3
        # d.n = 14


class D(B, C):
    def __init__(self):
        self.n = 5

    def add(self, m):
        # 第一步
        print('self is {0} @DDD.add'.format(self))
        # self 的 MRO 是 [D, B, C, A, object]
        # 从 D 之后的 [B, C, A, object] 中查找 add 方法
        # 从 B 找 add 方法
        super().add(m)

        # 第七步
        # d.n = 14
        self.n += 5
        # self.n = 19


d = D()
d.add(2)
print(d.n)


class Sum_Args_A(object):
    def __init__(self):
        self.args = 5

    def add(self, num):
        print(f'当前self的对象是：{self}')
        self.args += num

class Sum_Args_B(Sum_Args_A):
    def __init__(self):
        super().__init__()
        self.args = 4

    def add(self, num):
        print(f'当前self的对象是：{self}')
        super().add(num)
        self.args += num

class Sum_Args_C(Sum_Args_A):
    def __init__(self):
        super().__init__()
        self.args = 3

    def add(self, num):
        print(f'当前self的对象是：{self}')
        super().add(num)
        self.args += num

class Sum_Args_D(Sum_Args_B, Sum_Args_C):
    def __init__(self):
        super().__init__()
        self.args = 2

    def add(self, num):
        print(f'当前self的对象是：{self}')
        super().add(num)
        self.args += num

d = Sum_Args_D()
d.add(5)
print(d.args)

