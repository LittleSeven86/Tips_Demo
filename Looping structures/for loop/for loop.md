# for loop

在python中，`for`循环用于遍历可迭代对象（如列表、元组、字符串等）中的元素。下面是使用`for`循环的一般语法结构：

```python
for 变量 in 可迭代对象:
    # 执行循环体代码
    
- 变量：每次迭代时从可迭代对象中获取到的元素
- 可迭代对象：是一个序列或者集合，可以包含多个元素
- 循环替代码：每次循环迭代时，执行的代码语句
```

## 遍历字符串

```python
str_demo = 'hello'
for i in str_demo:
    print(i)
    
>>>
h
e
l
l
o
```

## 遍历列表

```python
list_demo = ['jack','tom','andy']
for i in list_demo:
    print(i)

>>> 
jack
tom
andy
```

## 遍历字典

```python
# 遍历字典--遍历字典的键
dict_demo = {'name':'xiaoqi',"age":17,"height":180}
for k in dict_demo.keys():
    print(k)
    
# 遍历字典--遍历字典的值
for v in dict_demo.values():
    print(v)
    
# 遍历字典--遍历字典的键值对
for k,v in dict_demo.items():
    print(k,v)
```

## range()

`range()`一个内置函数，用于生成一个整数序列。它常用于`for`循环中，控制循环的迭代次数

语法格式如下：

```python
range(start,end,step)

- start（可选）：序列的起始值，默认为0。
- stop：序列的结束值，生成的序列不包含该值。
- step（可选）：序列中相邻两个数之间的步长，默认为1。
```

## 搭配for循环使用实例

```python
# 生成一个从1-5的整数序列
for i in range(1,6):
  print(i)
  
>>>
1
2
3
4
5

# 生成一个从2-8(不包含8)的整数序列，步长为2
for i in range(2, 8, 2):
    print(i)
    
>>>
2
4
6
```

