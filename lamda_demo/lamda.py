"""
 #!/usr/bin/env python
 # -*- coding:utf-8 -*-
 @Author: Little Seven
 @FileName: lamda.py
 @DateTime: 2023/7/5 14:11
 @SoftWare: PyCharm
"""
from functools import reduce

people_list = ['jack', 'tom', 'lusy']
filter_people = list(filter(lambda x: x == 'jack', people_list))
print(filter_people)

numer_list = [1, 2, 3, 4, 5, 6]
filter_num = list(filter(lambda x: x % 2 == 0, numer_list))
print(filter_num)

score_dict = {'jack': 70, 'tom': 40, 'lusy': 90}
filter_score = dict(filter(lambda score: score[1] > 60, score_dict.items()))
print(filter_score)

original_list = [1, 2, 3, 4, 5]
map_list = list(map(lambda x: x ** 2, original_list))
print(map_list)

original_str  = ['jack','tom','lusy','helen']
map_str = list(map(lambda x:'学生姓名：'+x,original_str))
print(map_str)

original_dict = {'jack': 30, 'tom': 40}
map_dict = dict(map(lambda item: (item[0], '成绩是：' + str(item[1])), original_dict.items()))
print(map_dict)

original_list = [1, 3, 4, 6]
reduce_list = reduce(lambda x, y: x + y, original_list)
print(reduce_list)

reduce_list = reduce(lambda x,y:x+y,range(0,101))
print(reduce_list)

names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]

for i in zip(names,ages):
    print(i)


zip_list = list(zip(names,ages))
print(zip_list)

numbers = ['1', '2', '3']
letters = ['a', 'b', 'c']
result = list(map(lambda x: x[0] + x[1], zip(numbers, letters)))
print(result)  # 输出：['1a', '2b', '3c']

print(list(zip(['小明','晓红','小青'],range(0,6))))
