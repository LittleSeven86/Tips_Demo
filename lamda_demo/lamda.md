# Lambda

匿名函数（Anonymous functions），也被称为Lambda函数，在编程中用于**快速定义简单函数**的方式，即用即删除，非常轻量化，适用于小型、简单的函数。对于更复杂的函数，应该使用`def`语句来定义它们。

**语法结构：**

```python 
lambda arguments: expression

- 输入是传入到参数列表argument_list的值
- 输出是根据表达式expression计算得到的值
```

```python 
# 使用匿名函数求平方
square = lambda x: x**2

print(square(5))  # 输出：25
```

## 常见使用场景

匿名函数常常搭配一些内置函数进行使用，内置函数提供了一种简洁的方式来定义一次性的、简单的功能，而无需显式地定义命名函数，使用起来爱不释手

### filter

**功能：**用于对可迭代对象进行筛选，返回满足特定条件的元素组成的迭代器，匿名函数定义筛选条件

**语法：**

```python
filter(function，iterable)

- funtion：表示用于筛选的函数，可以使lambda函数或者其他可调用对象
- iterable：要筛选的可迭代对象
```

**示例**

```python 
# 筛选字符串
people_list = ['jack', 'tom', 'lusy']
filter_people = list(filter(lambda x: x == 'jack',people_list))

print(filter_people)
>>> ['jack']

# 筛选奇数
numer_list = [1, 2, 3, 4, 5, 6]
filter_num = list(filter(lambda x: x % 2 == 0, numer_list))
print(filter_num)
>>>[2, 4, 6]

# 筛选字典
score_dict={'jack':70,'tom':40,'lusy':90}
filter_score = dict(filter(lambda score:score[1]>60,score_dict.items()))
print(filter_score)
>>> {'jack': 70, 'lusy': 90}
```

### map

**功能：**用于对可迭代对象中的每个元素执行特定的转换或操作。

**语法：**

```python 
 map(func, *iterables)
    
- funtion：表示用于筛选的函数，可以使lambda函数或者其他可调用对象
- iterable：要筛选的可迭代对象
```

**示例**

```python 
# 求每个数的平方
original_list = [1, 2, 3, 4, 5]
map_list = list(map(lambda x: x ** 2, original_list))
print(map_list)

>>>[1, 4, 9, 16, 25]

# 对每个元素添加前缀
original_str  = ['jack','tom','lusy','helen']
map_str = list(map(lambda x:'学生姓名：'+x,original_str))
print(map_str)

>>> ['学生姓名：jack', '学生姓名：tom', '学生姓名：lusy', '学生姓名：helen']

# 对每个value添加前缀
original_dict = {'jack': 30, 'tom': 40}
map_dict = dict(map(lambda item: (item[0], '成绩是：' + str(item[1])), original_dict.items()))
print(map_dict)

>>>{'jack': '成绩是：30', 'tom': '成绩是：40'}
```

### reduce

**功能：**对可迭代对象中的元素进行累积操作，从而将可迭代对象缩减为单个值，进行累积操作，常用于计算总和、求积等场景，自从 Python 3.9 开始，`reduce()` 函数已不再是内置函数，而是被移动到 `functools` 模块中。因此，在**使用前需要先导入该模块。**

**语法：**

```python 
from functools import reduce

reduce(function, iterable[, initial])
```

**示例**

```python 
# 求和
original_list = [1, 3, 4, 6]
reduce_list = reduce(lambda x, y: x + y, original_list)
print(reduce_list)

>>> 14

# 一行代码求0-100的和
reduce_list = reduce(lambda x,y:x+y,range(0,101))
print(reduce_list)

>>> 5050
```

### zip

**功能：**将多个可迭代对象（列表、元组等）中对应位置的元素打包成一个元组，并**返回一个由元组组成的迭代器**。可以用于同时遍历多个可迭代对象，并将对应位置的元素组合在一起，如果可迭代对象的长度不同，则zip函数将在最短的可迭代对象用完后停止迭代。

**语法：**

```python 
zip(*iterables, strict=False) --> Yield tuples until an input is exhausted.

>>> list(zip('abcdefg', range(3), range(4)))
   [('a', 0, 0), ('b', 1, 1), ('c', 2, 2)]
```

**示例**

```python 
# 使用for循环迭代
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]

for i in zip(names,ages):
    print(i)

>>>
('Alice', 25)
('Bob', 30)
('Charlie', 35)

# 配合lambda一起使用
numbers = ['1', '2', '3']
letters = ['a', 'b', 'c']
result = list(map(lambda x: x[0] + x[1], zip(numbers, letters)))
print(result)  # 输出：['1a', '2b', '3c']

# 迭代对象长度不同
print(list(zip(['小明','晓红','小青'],range(0,6))))
>>> [('小明', 0), ('晓红', 1), ('小青', 2)]
```

