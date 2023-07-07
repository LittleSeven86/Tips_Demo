"""
 #!/usr/bin/env python
 # -*- coding:utf-8 -*-
 @Author: Little Seven
 @FileName: 递归.py
 @DateTime: 2023/7/7 10:15
 @SoftWare: PyCharm
"""
def recursion_func(num):
    if num != 0:
        num -=1
        return recursion_func(num)
    else:
        return num

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


import os

def list_files(path):
    if os.path.isfile(path):
        print(path)
    else:
        files = os.listdir(path)
        for file in files:
            list_files(os.path.join(path, file))





if __name__ == '__main__':
    res = recursion_func(6)
    print(res)

    result = factorial(5)
    print(result)  # 输出: 120

    res1 = fibonacci(6)
    print(res1)
    print(factorial(6))

    file_list = list_files('D:\Python\Tips_Demo')
    print(file_list,len(file_list))

    file_list = []
    for current_path,current_dir,dir_list in os.walk('D:\Python\Tips_Demo'):
        for list in dir_list:
            file_list.append(list)
    print(file_list,len(file_list))