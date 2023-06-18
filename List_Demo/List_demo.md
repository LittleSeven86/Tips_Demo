# 什么是列表

列表(list)是Python中使用最频繁的数据类型,列表是"有序"、"可变"的序列之一,同一个列表中，元素的数据可以不同，可以存放任何数据类型的数据

## 构建方式

- 使用一对方括号来表示空列表: `[]`
- 使用方括号，其中的项以逗号分隔: `[a]`, `[a, b, c]`
- 使用列表推导式: `[x for x in iterable]`
- 使用类型的构造器: `list()` 或 `list(iterable)`

构造器将构造一个列表，其中的元素与 *iterable* 中的元素具有相同的的值与顺序。 *iterable* 可以是序列、支持迭代的容器或其它可迭代对象。 如果 *iterable* 已经是一个列表，将创建并返回其副本，类似于 `iterable[:]`。 例如，`list('abc')` 返回 `['a', 'b', 'c']` 而 `list( (1, 2, 3) )` 返回 `[1, 2, 3]`。 如果没有给出参数，构造器将创建一个空列表 `[]`。

## 访问列表

#### 通过列表名访问

```python
list01 = [1,2,3,4,5,6,7]
list02 = [1001,'rose',90.5,'北京市',False]
print(list01) 			#通过列表名访问 [1, 2, 3, 4, 5, 6, 7]
print(list02) 			#通过列表名访问 [1001, 'rose', 90.5, '北京市', False]
```

#### 通过列表名+下标方式访问

```python
list04 = [
    ['login_01','admin',123456,True],
    ['login_02','root',123456,False],
    ['login_03','cedar',123456,True]
]
    print(list01[2]) 				# 3
    print(list01[2:5])				# [3, 4, 5] 列表切片 
    print(list04[2]) 				# ['login_03', 'cedar', 123456, True]
    print(list04[2][1]) 			# cedar
    print(list02[1],list02[-1]) 	#rose False
```

#### 对列表切片进行访问

```python
print(list01[2:5])		# [3, 4, 5] 列表切片
print(list04[1][0:2])	# ['login_02', 'root']
```

#### 对列表进行解包

```python
a1, b1, c1, d1, e1 = list02
print(f'a1是:{a1}\nb1是:{b1}\nc1是:{c1}\nd1是:{d1}\ne1是:{e1}')
case01, case02, case03 = list04
print(case03)	#['login_03', 'cedar', 123456, True]
```

## 删除列表

```python
#删除列表 使用方式：del 变量名
list03 = ['奔驰','BMW','QQ',123,99.9]
del list03
print(list03)   #NameError: name 'list03' is not defined

#删除列表中的元素 使用方式：del 变量名[下标]
del list03[3]		# ['奔驰','BMW','QQ',99.9]
```

## 列表运算

可以通过+号将两个列表进行链接，使用*号进行复制

```python
list04 = [1,2,3,4,5]
list05 = ['a','b','c',True,[1,2,3]]
#列表支持+(连接)运算
res01 = list04 + list05
print(res01)	#[1, 2, 3, 4, 5, 'a', 'b', 'c', True, [1, 2, 3]]
#列表支持*(复制)运算
res02 = list04 *3
print(res02)	#[1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
```

## 列表转字符串

`' '.join(list)`

## 字符串转列表

`str.split('',)`

## 判断元素是否在列表中

### in / not in 

- in ：判断某个成员（元素）是否在该数据结构中，返回结果为布尔值。
- not in ：判断某个成员（元素）是否不在该数据结构中，返回结果为布尔值。

```python
names = ['Neo', 'Lily', 'Jack']
print(bool('Adam' in names))
print(bool('Adam' not in names))

# 执行结果如下：
# >>> False
# >>> True
```

## 列表函数

### `list.append()`

作用：向列表尾部追加元素

```python 
list01 = [1,2,3,4,5]
list01.append('abc')
print(list01)	#[1, 2, 3, 4, 5, 'abc']
```

### `list.insert()`

语法：`list.insert(index, new_item)`

作用：index为新的元素放在的新的位置(数字，下标位)，new_item为填的新成员(元素)

```python 
ist02 = [1,2,3,4,5]
list02.insert(1,'a')	#表示在下标为1的位置，插入a
print(list02) 	#[1, 'a', 2, 3, 4, 5]
```

#### `len()`

作用：计算出当前列表有多少元素

```python
list03 = ['a','b','c',123]
len= len(list03)
print(len)		# 4  表示列表list01中有4个元素
```

#### `list.pop()`

作用：删除指定下标位置的元素

语法：list.pop(下标)

```python
list04 = [123,'a','b','c',123]
list04.pop(4)		#4 表示下标，删除指定位置的下标
print(list04)		# [123, 'a', 'b', 'c']
```

#### `list.remove()`

作用：删除列表中某一个元素

```python
list1 = ['这是数字：1', '这是数字：2', '这是数字：3', '这是数字：4', '这是数字：5', '这是数字：6', '这是数字：7', '这是数字：8', '这是数字：9']
list1.remove('这是数字：4')
print(list1)	#['这是数字：1', '这是数字：2', '这是数字：3', '这是数字：5', '这是数字：6', '这是数字：7', '这是数字：8', '这是数字：9']
```

#### `list.clear()`

作用：清空列表里面的元素

```python
list05 = [123,'a','b','c',123]
list05.clear()
print(list05)			# []
```

#### `list.count()`

作用：返回列表中指定元素出现的次数

```python
list06 = [123,'a','b','c',123]
print(list06.count(123))	# 2
```

#### `list.index()`

功能：返回指定元素在列表中首次出现的位置

语法：`list.index(查询元素)`

```python
list07 = ['abc',110,'bcd','def','bcd',110]
num = list07.index('bcd')	#在列表list07中，首次出现bcd  b的下标位置
print(num)		# 2
```

#### `list.reverse()` 

作用：对当前列表顺序的反转

语法：`list = list.reverse() `, 无参数传递

```python
books = ['Python', 'Java', 'PHP']
books.reverse()
print(books)

# 执行结果如下：
# >>> ['PHP', 'Java', 'Python']
```

#### `list.sort()`

作用：对当前列表按照一定的规律进行排序

用法：` list = list.sort(cmp=Node, key=Node, reverse=False)`

- cmp —> 可选参数，制定排序方案的函数

- key —> 参数比较

- reverse —> 排序规则，reverse = True (降序)；reverse = False (升序)，升序是默认状态

- 这里的 cmp 和 key涉及到函数的知识点，后续的函数相关章节会详细介绍

- sort() 函数的注意事项：**列表中的元素类型必须相同，否则会报错，无法排序**

```python
books = ['Python', 'C', 'PHP', 'Go', 'C++', 'Java']
books.sort()
print(books)

# 执行结果如下：
# >>> ['C', 'C++', 'Go', 'Java', 'PHP', 'Python']

int_lists = [79, 6, 99, 46, 30]
int_lists.sort(reverse=True)
print(int_lists)

# 执行结果如下：
# >>> [99, 79, 46, 30, 6]

test_list = ['Hello', 666, 3.14, True]
test_list.sort()
print(test_list)

# 执行结果如下：
# >>> TypeError: '<' not supported between instances of 'int' and 'str'
```

## 浅拷贝和深拷贝

先说结论：

- `deepcopy`是真正意义上的复制，深拷贝，被复制对象完全复制一遍作为独立的新个体，新开辟一块空间。

- `浅拷贝`不会产生独立对象，等于赋值，只是对原有数据块打上新标签，其中一个标签改变，数据块就会变化。浅拷贝等于赋值，也可以通过copy实现，copy仅拷贝对象本身，浅拷贝不会对其中的子对象进行拷贝，如果对子对象进行修改，拷贝结果也会随着修改。

首先说明一下浅拷贝，浅拷贝的实现方式：

- 通过变量赋值

```python 
list01 = [1,2,3,4,5,[6,7]]
list02 = list01	

print(id(list01),list01)		#id = 4303226240 [1, 2, 3, 4, 5, [6, 7]]
print(id(list02),list02)		#id = 4303226240 [1, 2, 3, 4, 5, [6, 7]]

list02[3] = '1'
print(list01,list02)				# [1, 2, 3, '1', 5, [6, 7]] [1, 2, 3, '1', 5, [6, 7]]
```

- 通过`copy()`方式

```python
list01 = [1,2,3,4,5,[6,7]]
list03 = list01.copy()

print(id(list01),list01)		# id = 4303226240 [1, 2, 3, 4, 5, [6, 7]]
print(id(list03),list03)		# id = 4310112704 [1, 2, 3, 4, 5, [6, 7]]

list01[5][0]=1
print(id(list01),list01)		# id = 4303226240 [1, 2, 3, 4, 5, [1, 7]]
print(id(list03),list03)		# id = 4302985728 [1, 2, 3, 4, 5, [1, 7]]

list01[4] = '1'
print(id(list01),list01)		# id = 4303226240 [1, 2, 3, 4, '1', [6, 7]]
print(id(list03),list03)		# id = 4344420864 [1, 2, 3, 4, 5, [1, 7]]
```

- 以上说明：
  - **二次赋值的变量与原始变量共享相同的内存地址空间**，均指向一个地址，当改变了list02当中的值时，list01的值也发生改变
  - **对原对象的值的拷贝**，虽然产生了一个新的内存地址，但是指针指向原对象的地址，浅拷贝或者原对象的值发生变化，那原对象和浅拷贝对象的值都会随着被改变。
  - 对于`copy()`得到的值来说，当复杂的对象中无复杂的子对象，就是说列表当中并无嵌套列表，原来值的改变并不会影响浅复制的值，同时浅复制的值改变也并不会影响原来的值。
  - 复制的对象中有复杂子对象 （例如列表中的一个子元素是一个列表）如果改变复杂子对象的值（列表中的值）会影响浅复制的值。

### deepcopy

作用：深拷贝不仅对列表第一层进行了 copy ，对深层的数据也进行了 copy， 原始变量与新变量之间完全不共享数据，这就是深拷贝。

```python 
list01 = [1,2,3,4,5,[6,7]]
list04 = copy.deepcopy(list01)

print(id(list01),list01)		# id = 4340318592 [1, 2, 3, 4, 5, [6, 7]]
print(id(list04),list04)		# id = 4340321920 [1, 2, 3, 4, 5, [6, 7]]

list01[5][0] = 'a'
print(id(list01),list01)		# id = 4340318592 [1, 2, 3, 4, 5, ['a', 7]]
print(id(list04),list04)		# id = 4340321920 [1, 2, 3, 4, 5, [6, 7]]
```

- 深拷贝和浅拷贝都是对原对象的拷贝，都会生成一个看起来相同的对象，本质区别就是拷贝出来的对象的「地址」是否与原对象一样，即就是对原对象的地址的拷贝，还是值的拷贝

## 可变对象与不可变对象

### 不可变对象

包括：`str、int、float、tuple、set`

特点：内容变化需要分配新的内存空间，因为原来的对象内容不可变。一个对象所指向的地址上的值是不能修改的，如果修改了就是它执行的地址就改变了，相当于将这个对象指向的值复制出来一份，然后做了修改后存到另一个地址上了。

```python 
str01 = 'abcd'
float01 = 23.0333
tuple01 = (1,2,34)
print(id(str01),str01)				# id = 4368746480 abcd
print(id(float01),float01)		# id = 4368434416 23.0333
print(id(tuple01),tuple01)		# id = 4369075072 (1, 2, 34)

str01 = 'cdef'
float01 = 24.098
tuple01 = (1,2,'aa')
print(id(str01),str01)				# id = 4369076016 cdef
print(id(float01),float01)		# id = 4368438768 24.098
print(id(tuple01),tuple01)		# id = 4369346752 (1, 2, 'aa')
```

### 可变对象

包括：`list、dict`

特点：一个对象在不改变其所指向的地址前提下，可以修改其所执行的地址中的值

```python
list02 = [1,2,3,'11']
dict01 = {'name':'jack','age':16}

print(id(list04),list04)		# id = 4336143936 [1, 2, 3, 4, 5, [6, 7]]
print(id(dict01),dict01)		# id = 4335096640 {'name': 'jack', 'age': 16}

list02.pop(2)
del dict01['name']
print(id(list04),list04)		# id = 4336143936 [1, 2, 3, 4, 5, [6, 7]]
print(id(dict01),dict01)		# id = 4335096640 {'age': 16}
```

### 两者区别

可变对象修改了值，不会新建一个内存地址的对象，不可变对象如果修改了值，即使复制了一份新的内存地址，原始地址的值不会被改变。