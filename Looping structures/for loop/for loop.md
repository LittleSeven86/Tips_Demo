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

### 搭配for循环使用实例

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

## 嵌套for循环

顾名思义，嵌套for循环的意思就是for循环中还有for循环

```python
list_demo = [
    ['jack',18],
    ['tom',19],
    ['hellen',20]
]

for args in list_demo:
    print(f'外层循环的参数是：{args}')
    for inside_args in args:
        print(f'内层循环的参数是：{inside_args}')
        
>>>
外层循环的参数是：['jack', 18]
内层循环的参数是：jack
内层循环的参数是：18
外层循环的参数是：['tom', 19]
内层循环的参数是：tom
内层循环的参数是：19
外层循环的参数是：['hellen', 20]
内层循环的参数是：hellen
内层循环的参数是：20
```

## 每日算法一题

```python 
# 给你一个字符串 s，由若干单词组成，单词前后用一些空格字符隔开。返回字符串中 最后一个 单词的长度。
# 单词 是指仅由字母组成、不包含任何空格字符的最大子字符串。
'''
输入：s = "Hello World"
输出：5
解释：最后一个单词是“World”，长度为5。
'''


def length_of_lastworld(str: str) -> int:
    '''
    函数接收一个输入字符串 str，表示给定的字符串，返回的是整数类型
    :param str:
    :return: int
    '''
    # 这一行代码去除输入字符串末尾的空格，确保字符串末尾没有额外的空格。
    str = str.rstrip()
    # 循环从字符串的最后一个字符开始往前遍历，生成一个倒序的索引序列
    for i in range(len(str) - 1, -1, -1):
        # 在遍历过程中，如果遇到空格字符，则说明已经找到了最后一个单词的末尾
        if str[i] == " ":
            # 返回从字符串末尾到找到的空格字符的长度，即为最后一个单词的长度
            return len(str) - i - 1
    # 如果在遍历过程中没有找到空格字符（即没有遇到分隔单词的空格），则说明整个字符串就是一个单词。此时函数会直接返回整个字符串的长度作为最后一个单词的长度
    return len(str)

  
# 优化后代码：

def length_of_last_word(s: str) -> int:
    s = s.rstrip()  # 去除字符串末尾的空格
    last_space_index = s.rfind(' ')  # 查找最后一个空格字符的索引
    return len(s) - last_space_index - 1 if last_space_index != -1 else len(s)
```

