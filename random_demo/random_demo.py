"""
 #!/usr/bin/env python
 # -*- coding:utf-8 -*-
 @Author: Little Seven
 @FileName: random_demo.py
 @DateTime: 2023/7/10 14:54
 @SoftWare: PyCharm
"""
import random

print(random.random())

print(random.uniform(0,4))
print(random.randint(1,6))


import random

list_choice = [1, 'tom', 0.123, True, None, {'name': 'jack'}]
res = random.choice(list_choice)
print(res)

print(random.sample(list_choice,2))
print(random.randrange(1,30,4))