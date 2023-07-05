"""
 #!/usr/bin/env python
 # -*- coding:utf-8 -*-
 @Author: Little Seven
 @FileName: global.py
 @DateTime: 2023/7/4 14:33
 @SoftWare: PyCharm
"""
# global_variable = 10
# del global_variable
# print(global_variable)
#
#
# def update_global_varibale():
#     global global_variable
#     global_variable = 15
#     print(global_variable)  # 函数内部访问全局变量
#
# update_global_varibale()


def create_local_variable():
    local_variable = 30
    return local_variable
    print(local_variable,id(local_variable))

res = create_local_variable()
print(res)