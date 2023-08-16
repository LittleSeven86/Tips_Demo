"""
 #!/usr/bin/env python
 # -*- coding:utf-8 -*-
 @Author: Little Seven
 @FileName: open_demo.py
 @DateTime: 2023/8/15 10:18
 @SoftWare: PyCharm
"""
import time
import types

res = open('demo.txt','a+',encoding='utf-8')
# res.write('这是添加的数据')
res.close()


# import os
#
# with open('demo.txt', "r+b") as file:
#     file.seek(0, os.SEEK_END)
#     file_size = file.tell()
#     pos = file_size - 1
#     while pos > 0 and file.read(1) != b"\n":
#         pos -= 1
#         file.seek(pos, os.SEEK_SET)
#     if pos > 0:
#         file.seek(pos, os.SEEK_SET)
#         file.truncate()
from tqdm import tqdm

# a = []
# for i in tqdm(range(10000000)):
#     temp = ['你好'] * 2000
#     a.append(temp)
#
# for ele in a:
#     continue

def test():
    for i in tqdm(range(10000000)):
        temp = ['你好'] * 2000
        yield temp

# a = test()
# for ele in a:
#     continue

def create_num():
    for i in range(10000):
        yield i


print(isinstance(create_num(),types.GeneratorType))

# a = create_num()

import time

def time_total(func):
    def inner_func(*args, **kwargs):
        stime = time.time()
        func(*args, **kwargs)
        print(f'当前持续了 {time.time() - stime:.2f}s')
    return inner_func

@time_total
def print_numbers():
    gen = create_num()
    for i in gen:
        print(next(gen))


# print_numbers()
# import types
# demo_numbers = (x for x in range(10) if x % 2 == 0)
#
# # 通过迭代生成器表达式逐个获取生成的值
# for num in demo_numbers:
#     print(num)
#
# print(isinstance(demo_numbers, types.GeneratorType))
# print(type(demo_numbers))

# my_list = [1, 2, 3, 4, 5]
# my_iter = iter(my_list)
#
# print(my_iter)
# # print(next(my_iter))  # 输出: 3
# num = (x for x in range(3))
# print(num.__next__())
# print(num.__next__())
# print(num.__next__())
# print(num.__next__())
# print(num.__next__())

from tqdm import tqdm
import time

my_list = range(10)
#
# for i in tqdm(my_list, desc="Processing"):
#     # 模拟耗时操作
#     time.sleep(0.5)


class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

demo_str = 'hello,world'
iter_demo_str = iter(demo_str)


class MyIterator:
    def __init__(self, collection):
        self.collection = collection
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.collection):
            raise StopIteration

        result = self.collection[self.index]
        self.index += 1
        return result


my_list = [1, 2]  # 创建一个列表
import types
iter_list = iter(my_list)
print(next(iter_list))


a = ['321312','22222']
b = ['000','1111']
print(zip(a,b))


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class InOrderIterator:
    def __init__(self, root):
        self.root = root
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def __iter__(self):
        return self

    def __next__(self):
        if not self.stack:
            raise StopIteration()
        node = self.stack[-1]
        if node.right:
            x = node.right
            while x:
                self.stack.append(x)
                x = x.left
        else:
            x = self.stack.pop()
            while self.stack and self.stack[-1].right == x:
                x = self.stack.pop()
        return node.value

# 创建一个二叉树
root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)

# 使用迭代器进行中序遍历
iterator = InOrderIterator(root)
for value in iterator:
    print(value)  # 输出：1 2 3 4 5
