"""
 #!/usr/bin/env python
 # -*- coding:utf-8 -*-
 @Author: Little Seven
 @FileName: function.py
 @DateTime: 2023/7/3 10:38
 @SoftWare: PyCharm
"""


def add_numbers(a, b):
    sum = a + b
    return sum

result = add_numbers(2, 3)
print(result)  # 输出：5

def add_and_print(a, b):
    result = a + b
    print("The sum is:", result)
    return result
    print("The sum is:", a)

sum_result = add_and_print(3, 4)
print("Returned value:", sum_result)