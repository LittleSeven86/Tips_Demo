"""
 #!/usr/bin/env python
 # -*- coding:utf-8 -*-
 @Author: Little Seven
 @FileName: os_demo.py
 @DateTime: 2023/7/10 10:06
 @SoftWare: PyCharm
"""
import os
import time

print(os.listdir())
print(os.getcwd())  # D:\Python\Tips_Demo\os_demo
# print(os.chdir('../List_Demo'))
print(os.getcwd())  # D:\Python\Tips_Demo\os_demo

# print(os.mkdir('test_add_dir'))
# print(os.makedirs('test_-p_dir/1/2'))
# print(os.rmdir('test_-p_dir/1/2'))


# print(os.getpid())
# print(os.listdir('1'))
# os.remove('1/test.txt')
# print(os.listdir('1'))


import os

directory_path = "../os_demo"

for root, directories, files in os.walk(directory_path):
    for file in files:
        file_path = os.path.join(root, file)
        print(file_path)

print(os.path.exists('../os_demo'))

directory = "../os_demo"
filename = "静夜思.txt"

file_path = os.path.join(directory, filename)
print(file_path)


dir,filename = os.path.split('test_add_dir/静夜思')
print(dir,filename)

dir,filename = os.path.split('test_add_dir')
print(dir,filename)
print(os.path.dirname('../os_demo/test_add_dir'))
print(os.path.dirname('../os_demo/os_demo.py'))

print(os.path.isfile('../os_demo/os_demo.py'))
print(os.path.isfile('../os_demo/test_add_dir'))


res = os.system('echo Hello World!')
os.system('dir')
print(res)
print(os.getpid())
# time.sleep(10)
print(os.path.getsize('os.md'))