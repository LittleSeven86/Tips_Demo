"""
 #!/usr/bin/env python
 # -*- coding:utf-8 -*-
 @Author: Little Seven
 @FileName: pathlib_demo.py
 @DateTime: 2023/8/21 10:12
 @SoftWare: PyCharm
"""
from pathlib import *
import os
"""
对比os库和Path库常见的使用指南
"""
# 对比os和path的使用区别
print(os.getcwd())
print(Path.cwd())

print(Path.home())

# 查询父级目录
# print(os.path.dirname(os.path.dirname(os.getcwd())))
# print(Path.cwd().parent.parent)
dir_list = []
for i in Path.cwd().parents:
    dir_list.append(i)
# print(dir_list)

# 路径处理
path = Path.absolute(Path.cwd()).joinpath('demo-2.txt')
# 返回文件名+文件后缀
print(path.name)
# 返回文件名
print(path.stem)
# 返回文件后缀
print(path.suffix)
# 返回文件后缀列表
print(path.suffixes)
print(path.root)
# 返回一个包含路径各个部分的元组
print(path.parts)
#
#
# # 分割路径 类似os.path.split(), 不过返回元组
# path = Path.cwd()
# print(path.parts)
#
# # 查询当前项目的根路径
# base_dir = 'D:\Python\Tips_Demo'
# path = Path.cwd()
# print(path.root)
# print(path.resolve())
# for iterm in path.iterdir():
#     print(iterm)
#
# # path = Path('demo.txt')
# # path.rename('demo-1.txt')
#
# paths = ["demo-1.txt","demo-2.txt"]
# Path.cwd().parent.joinpath(*paths)

# 路径拼接
path = Path.cwd()
# 方式一：使用joinpath进行添加
print(path.joinpath('demo-1.txt'))
# 方式二：拼接
print(path/'demo-1.txt')

# 路径判断
