# 数据类型—字符串

## 定义字符串

在Python中，字符串是一个有序的集合,主要作用是存储和表示文本,由单引号、双引号、三个单引号、三个双引号括起来的一串字符

```python
str1 = '人生苦短，我用python'
str2 = "人生苦短，我用python"
str3 = """人生苦短，我用python"""
print(str1, str2, str3)     # 人生苦短，我用python 人生苦短，我用python 人生苦短，我用python
```

## 字符串索引

字符串切片就是,通过字符串中的下标，获取字符串中的某个或者某部分字符(字符串中每一个字符都有一个对应的下标，下标(索引、编号)从0开始)一般格式：`str[start:end:step]`，下标从0开始，可以为负数，负数时，从-1开始

注意：

- 总体索引切片的原则是：左闭右开
- 起始位置可以被省略，表示默认从0开始
- 终止为止可以被省略，表示默认取到最后一个位置
- 当步长大于0的时候，从左往右取字符；当步长小于0的时候，从右往左取字符。

```python 
str8 = 'ABCDEFG'
print(str8[2])      #  	[下标位置]--取下标为下标为2的元素--C
print(str8[0:2])    #  	[start:end]--取开始位置至结束位置的元素（不包括结束位置）--AB
print(str8[3:])     #   [start:]--取开始位置到结束结束位置全部到元素--DEFG
print(str8[:7])     #   [:end]--默认从下标位置0到结束位置--ABCDEFG
print(str8[:])      #   [:]--默认输出全部位置--ABCDEFG
print(str8[-4])     #   [-1]--字符串从后向前取值--D
print(str8[3:0:-1]) #   当step<0时，从右向左取字符--DCB
print(str8[::-1])   #   反向输出全部--GFEDCBA
print(str8[::-3])   #   反向输出，步长为3--GDA
print(str8[4::-1])  #   从开始位置4逆向切片--EDCBA
```

![img:png](../IMG/字符串下标详解.png)

## 字符串操作

```python
str1,str2 = 'Hello','Python'
```

| 操作符 | 描述                                         | 示例                        |
| ------ | -------------------------------------------- |---------------------------|
| +      | 字符串连接（字符串拼接）                     | `str1+str2 = 'HelloPython'` |
| *      | 字符串复制                                   | `str1*2 = 'HelloHello'`     |
| in     | 判断给定的字符串在目标字符串中，返回布尔值   | `str1 in str2==>False `     |
| not in | 判断给定的字符串不在目标字符串中，返回布尔值 | `str1  not in str2==>True ` |

##  转义字符

在字符串中使用转义字符是为了表示一些特殊的字符，这些字符在字符串的常规表示中具有特殊含义或无法直接表示。转义字符由`反斜杠（\）`后面紧跟着特定的字符组成。

下面是一些常见的转义字符及其含义

| 转义字符 | 含义                               |
| -------- | ---------------------------------- |
| `\n`     | 换行符，将光标位置移到下一行开头。 |
| `\t`     | 制表符--作用为常见的tab键          |
| `\\`     | 输出反斜杠\ ，常在路径当中使用     |

## 格式化输出

### 使用百分号进行格式化

是一种传统的格式化方法，在字符串中使用百分号作为占位符，并使用相应的格式化字符来表示要插入的变量类型。

| 字符 | 字符含义                                          |
| ---- | ------------------------------------------------- |
| %d   | 十进制整数，int                                   |
| %f   | 浮点数类型，float，可以通过`%.nf`选择保留几位小树 |
| %s   | 字符串类型，str                                   |
| %%   | 输出为%号                                         |

```python
str5 = '%s是%d班的学生，学号是%d,平均成绩是%.2f'%('小明',1,20,89.0000)
print(str5)     # 小明是1班的学生，学号是20,平均成绩是89.00
```

### 使用format()方法

`format()`方法允许在字符串中使用花括号`{}`作为占位符，并使用`format()`方法传入变量。

- 可以通过索引来制定位置传递参数
- 通过变量名进行传递参数,当指定了关键字，又只写了` {}` 时，传入带有关键字必须写在后面

```python
# format 格式化方法 --指定排序
str7 = '{3}是{0}班的学生，{1}是他的学号，数学成绩是{2:.2f}'.format(3,20,89.00000,'小明') # 小明是3班的学生，20是他的学号，数学成绩是89.0
print(str7)

# format 格式化方法 --指定关键字
str7 = '{name}是{num}班的学生，{id}是他的学号，数学成绩是{score:.2f}'.format(num=3,id=20,score=89.00000,name='小明')	# 小明是3班的学生，20是他的学号，数学成绩是89.0
```

### 使用f-string

f-strings是在Python 3.6及更高版本引入的一种方便的格式化方法。它使用以字母`f`开头的字符串，可以在其中使用花括号`{}`来插入变量。

```python
name = 'json'
age = 18
print(f'{name}今年{age}周岁了')  # json今年18周岁了
```

## 字符串方法

### `str.capitalize()`

作用：返回原字符串的副本，其首个字符大写，其余为小写。

```python
str9,str10 = 'hello World', 'hello'
print(str9.capitalize())	# >>> Hello world
```

### `str.upper()`

作用：其中所有区分大小写的字符均转换为大写

```python
print(str10.upper())	# >>> HELLO
```

### `str.lower()`

作用：其所有区分大小写的字符均转换为小写。

```python
print(str9.lower())		# >>> HELLO
```

### `str.casefold()`

作用：消除大小写的字符串可用于忽略大小写的匹配。

消除大小写类似于转为小写，但是更加彻底一些，因为它会移除字符串中的所有大小写变化形式。 例如，德语小写字母 `'ß'` 相当于 `"ss"`。 由于它已经是小写了，`lower()` 不会对 `'ß'` 做任何改变；而 `casefold()` 则会将其转换为 `"ss"`。

```python
print(str11.casefold())		# >>> ssabcd123wd
```

### `str.startwith()`

作用：判断字符串是否以`prefix:str`开头，`start:int`为开始位置下标，`end:int`为结束位置，返回布尔值

语法：`S.startswith(prefix[, start[, end]]) -> bool`

```python
str9,str10 = 'Hello World', 'hello'
print(str9.startswith('H',1,6))		# >>> False
```

### `str.endwith()`

作用：判断字符串是否以`suffix:str`结尾,可以是一个字符串或由多个后缀组成的元组，`start:int`为开始位置下标，`end:int`为结束位置，返回布尔值

语法：`S.endwith(prefix[, start[, end]]) -> bool`

```python
text = "Hello, world!"

result1 = text.endswith("world!")  # 检查是否以 "world!" 结尾，返回 True
result2 = text.endswith(("Hello", "World"))  # 检查是否以 "Hello" 或 "World" 结尾，返回 True
```

### `str.center()`

作用：返回一个长度为 `width` 的字符串，原字符串位于中间，并使用指定的 `fillchar` 来填充两侧的空白。不指定`fillchar`则默认使用空格

语法：`str.center(width[, fillchar]) -> str`

```python
text = "Hello"

result1 = text.center(10)  #   HELLO   
result2 = text.center(10, "*")  # **HELLO***
```

### `str.find()`

作用：返回子字符串 *sub* 在 `s[start:end]` 切片内被找到的最小索引。 可选参数 *start* 与 *end* 会被解读为切片表示法。 如果 *sub* 未被找到则返回 `-1`

语法：`S.find(sub[, start[, end]]) -> int`

```python
str11 = 'e'
str12 = 'hello world'
res = str12.find(str11)		>>>0
res = str12.find(str11,2,)		>>>-1
```

### `str.index()`

作用：类似于 `find()`，但在找不到子字符串时会引发 `ValueError`。

语法：`S.index(sub[, start[, end]]) -> int`

```python
str11 = 'e'
str12 = 'hello world'
res1= str12.index(str11,2,6)		>>> ValueError: substring not found
res1= str12.index(str11)				>>> 1
print(res1)
```

### `str.isalpha()`

作用：如果字符串中的所有字符都是字母，并且至少有一个字符，返回 `True` ，否则返回 `False`

```python
str12 = 'hello world'
print(str12[0].isalpha())		>>>True
```

### `str.isdigit()`

作用：如果字符串中的所有字符都是数字，并且至少有一个字符，返回 `True` ，否则返回 `False` 。

```python
str13 = '2314as'
print(str13.isdigit())	>>>False
print(str13[2].isdigit())	>>>True
```

### `str.count()`

作用：返回字符串中某一个元素出现的次数 。

语法：`S.count(sub[, start[, end]]) -> int`

```python
str14 = 'asdfaafsdaa'
print(str14.count('a'))		>>>5
```

### `str.join()`

作用：将可迭代对象(`List、Set、Touple、Dict`)中的字符串，使用新的目标分隔符进行链接，并返回一个新的字符串

语法：`'连接符'.join(目标字符串)--> str`

```python
touple1 = ('1','2','3')
str_touple = ''.join(touple1)
print(str_touple)

list1 = ['hello','world','我','爱','python']
_ = ','.join(list1)
print(_)

set1 = {'人生苦短','我用python'}
__ = ','.join(touple1)
print(__)

dict1 = {'hello':'1','python':'2'}
___ = ','.join(dict1.keys())
____ = ','.join(dict1.values())
print(___)
print(____)
```

### `str.split()`

作用：返回一个由字符串内单词组成的列表，使用 *sep* 作为分隔字符串。 如果给出了 *maxsplit*，则最多进行 *maxsplit* 次拆分（因此，列表最多会有 `maxsplit+1` 个元素）。 如果 *maxsplit* 未指定或为 `-1`，则不限制拆分次数（进行所有可能的拆分）。

语法：`S.split(sep=target:str, maxsplit=num:int) -> list`

```python
str15 = 'hello,python,人生苦短,我用python'
str15_list = str15.split(',',maxsplit=1)
print(str15_list)		>>>['hello', 'python,人生苦短,我用python']
```

**进阶玩法**

需求：将一个字符串分割为多个字段，但是分隔符 (还有周围的空格) 并不是固定的。

```python
_ = 'asdf fjdk; afed, fjek,asdf, foo'
```

解决方案：string 对象的 split() 方法只适应于非常简单的字符串分割情形，它并不允许有多个分隔符或者是分隔符周围不确定的空格。当你需要更加灵活的切割字符串的时候， 最好使用 re.split() 方法

```python
import re

_ = 'asdf fjdk; afed, fjek,asdf, foo'
__ = re.split(r'[;,\s]\s*',_)
print(__)		>>>['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

__ = re.split(r'(;|,|\s)\s*',_)
print(__)		>>>['asdf', ' ', 'fjdk', ';', 'afed', ',', 'fjek', ',', 'asdf', ',', 'foo']
```



### `str.strip()`

作用：返回原字符串的副本，移除其中的前导和末尾字符。 *chars* 参数为指定要移除字符的字符串。 如果省略或为 `None`，则 *chars* 参数默认移除空白符。 实际上 *chars* 参数并非指定单个前缀或后缀；而是会移除参数值的所有组合 。

```python
_ = '   spacious   '.strip()
print(_)

__ = 'www.example.com'.strip('cmowz.')
print(__)
```

### `str.replace()`

作用：返回字符串的副本，其中出现的所有子字符串 *old* 都将被替换为 *new*。 如果给出了可选参数 *count*，则只替换前 *count* 次出现，

语法：``str.replace(old_str, new_str,count)`

```python
_ = 'hello,neo,my boy neo'
print(_.replace('neo','jack',1))	>>> 替换指定次数
print(_.replace('neo','jack',2))
print(_.replace('neo','jack'))		>>> 不给定次数，默认全部替换
print(_.replace('neo','jack',-1))	>>> -1 表示全部替换
```

### eval()

作用：返回传入字符串的表达式的结果。就是说：将字符串当成有效的表达式 来求值 并 返回计算结果。去掉字符串的引号

```python
# 1.eval无参实现字符串转化
s = '1+2+3*5-2'
print(eval(s))  # 16

# 2.字符串中有变量也可以
x = 1
print(eval('x+2'))  # 3

# 3.字符串转字典
print(eval("{'name':'linux','age':18}"))
# 输出结果：{'name':'linux','age':18}

# 4.eval传递全局变量参数,注意字典里的:age中的age没有带引号，说明它是个变量，而不是字符串。
# 这里两个参数都是全局的
print(eval("{'name':'linux','age':age}", {"age": 1822}))
# 输出结果：{'name': 'linux', 'age': 1822}
print(eval("{'name':'linux','age':age}", {"age": 1822}, {"age": 1823}))
# 输出结果：{'name': 'linux', 'age': 1823}
```

### 

