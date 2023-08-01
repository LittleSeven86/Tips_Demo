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

Son().name()
# print(dir(object))

class Demo:
    def __init__(self, age):
        self.age = age
    
    def __getattr__(self, item):
        print(f'获取到了属性：{item}')
        return self.item

    def __setattr__(self, key, value):
        print(f"设置属性: {key} 为 {value}")
        super().__setattr__(key, value)

    def __delattr__(self, item):
        print(f'删除属性：{item}')
        super().__delattr__(item)

    # def __getattribute__(self, item):
    #     print(f'获取到了属性{item}')
    #     return self.age


demo = Demo(20)
# demo.age  # 输出: 获取到了属性age
print(demo.name)