"""
 #!/usr/bin/env python
 # -*- coding:utf-8 -*-
 @Author: Little Seven
 @FileName: deepcopy_demo.py
 @DateTime: 2023/6/2 16:53
 @SoftWare: PyCharm
"""
import copy

list_a = [1,2,3,'a','b','c']
list_b = list_a
list_b.append([1])

ls

print(list_a,id(list_a))
print(list_b,id(list_b))
