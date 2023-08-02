"""
 #!/usr/bin/env python
 # -*- coding:utf-8 -*-
 @Author: Little Seven
 @FileName: 继承.py
 @DateTime: 2023/7/28 15:32
 @SoftWare: PyCharm
"""

class Father(object):
    def name(self):
        print('这是爸爸~')

class Son(Father):
    def name(self):
        super().name()
        print('这是儿子~')

# Son().name()
# print(dir(object))

class MyClass:
    def __init__(self):
        self.age = 20

    def __getattribute__(self, item):
        print(f"__getattribute__() 获取到： {item}")
        # 返回属性的值，如果属性不存在则引发AttributeError异常
        return object.__getattribute__(self,item)

    # def __getattr__(self, item):
    #     print(f"__getattr__() 获取到： {item}")
    #     # 当属性不存在时返回一个默认值
    #     raise AttributeError(f"属性 '{item}' 不存在")



# my_obj = MyClass()
# print(my_obj.age)
# print(my_obj.name)

# print(my_obj.age)  # 调用__getattribute__()方法，属性存在
# print(my_obj.age1)
# 打印结果：
# __getattribute__() 获取到： age
# 20

# print(my_obj.nonexistent_attribute)  # 调用__getattribute__()和__getattr__()方法，属性不存在

# 打印结果：
# __getattribute__() called for nonexistent_attribute
# __getattr__() called for nonexistent_attribute
# nonexistent_attribute does not exist.

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

# print(D.mro())
print(dir(D))