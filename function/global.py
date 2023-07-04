"""
 #!/usr/bin/env python
 # -*- coding:utf-8 -*-
 @Author: Little Seven
 @FileName: global.py
 @DateTime: 2023/7/4 14:33
 @SoftWare: PyCharm
"""
global_variable = 10
del global_variable
print(global_variable)


def update_global_varibale():
    global global_variable
    global_variable = 15
    print(global_variable)  # 函数内部访问全局变量

update_global_varibale()



