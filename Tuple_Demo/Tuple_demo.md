# 元祖

元组是`有序、不可变`的序列之一,可以把元祖看成"常量列表"，元组是不可变的数据结构，这意味着一旦创建，就无法直接修改其元素的值

- 优点："访问和处理数据的速度快、代码更安全"

## 构建元祖的方式

- 使用一对圆括号来表示空元组: `()`
- 使用一个后缀的逗号来表示单元组: `a,` 或 `(a,)`
- 使用以逗号分隔的多个项: `a, b, c` or `(a, b, c)`
- 使用内置的 `tuple()`: `tuple()` 或 `tuple(iterable)`

## 元祖在数据库中的实际应用

```python
sql_data = ('username','root') #元组类型
print("seLect * from user where %s=%s" % sql_data)	#seLect * from user where username=root
```

## 访问元祖

#### 通过元组名访问

```python
tuple01 = (1,2,3,4,5)
print(tuple01)	#(1,2,3,4,5)
```

#### 通过下标访问

```python
print(tuple01[2])	#3
```

#### 解包

```python
a1,b1,c1,d1,e1 = tuple01
print(a1,b1,c1,d1,e1)	#1 2 3 4 5
```

#### 切片

```python
print(tuple01[2:])	#(3, 4, 5)
```

### 删除元祖

元祖只可以进行查询，不能进行删除某个元素、修改、增加

```python
t5 = (101,'rose','女','北京')
del t5
print(t5)	#NameError: name 't5' is not defined
```

## 修改元祖中的值

可以通过创建一个新的元组来实现间接修改元组元素的值。下面是一个例子：

```python
tuple_int = (12,20,30,40,'a')
list = list(tuple_int)
list[0] = 'change'
tuple01 = tuple(list)
print(type(tuple01),tuple01)

>>>> <class 'tuple'> ('change', 20, 30, 40, 'a')
```



### 元祖运算

```python
#元组支持+ (连接)运算
t6 = (10, 20, 30)
t7 = ('A', 'B', 'C')
res1=t6 + t7
print('连接后结果:' ,res1) #连接后结果: (10, 20, 30, 'A', 'B', 'C')

#元祖支持*（复制）运算
res2=t7*3
print('复制后结果:',res2) #('A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C')
```

## 常见方法

### len()

```python
tuple = (1,2,3,4,'a','b')
print(len(tuple))			>>> 6
```

### tuple.count()

- 功能：统计某元素在当前元祖中出现的次数

```python
tuple_int = (12,20,30,40,'a')
print(tuple_int.count(12))		>>> 1
```

### tuple.index()

- 功能：查询某元素第一次出现的索引下标

```python
tuple_int = (12,20,30,40,'a')
print(tuple_int.index('a'))		>>> 4
```

