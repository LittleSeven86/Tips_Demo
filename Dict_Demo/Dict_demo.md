# 字典类型

字典是Python中一个"非常重要"的数据类型,字典是无序、可变的序列之一，以"键值对"方式存储的,和列表最大的不同时：字典是无序的，在字典中通过"键"来访问元素 ，字典中key是唯一的，`不可能存在两个相同的 key`。

## 定义字典的方式

- 使用花括号内以逗号分隔 `键: 值` 对的方式: `{'jack': 4098, 'sjoerd': 4127}` or `{4098: 'jack', 4127: 'sjoerd'}`
- 使用类型构造器: `dict()`, `dict([('foo', 100), ('bar', 200)])`, `dict(foo=100, bar=200)`
- 字典名 = `dict(key=value,key2=value2)`

## 访问字典的方式

- 字典名访问

```python
#字典名访问 
print(dict01) print(dict02)
```

- 字典名+键进行访问

```python
#通过字典名+键进行访问	 
print(dict01['id'])			#101 
dict03 = {'编号':101,'姓名':'杰克','年龄':34} 
print(dict03['姓名'])		#使用字典名['键']来访问：杰克
```

- 解包

```python
#解包 
id, name, age = dict02 		#只可以取键不可以取值
```

### 删除字典

- 删除字典中某个元素，使用方法：`del dict['key']`，根据键来删除

```python
dict04 = {'a':100,'b':200,'c':300}
del dict04['b']
print(dict04)	#{'a': 100, 'c': 300}
```

### 增加元素和修改元素

字典中增加元素使用`dict['键'] = 值`

- 若没有该键，即添加元素
- 若健存在，就修改该键的值

```python
#字典增加元素，语法格式：dict['键'] = 值
dict05 = {'a':101, 'age':30,'address':'北京'}
dict05['name'] = 'lucy'
print(dict05) 			#{'a': 101, 'age': 30, 'address': '北京', 'name': 'lucy'}
```

## 字典内置函数

### update

功能：添加新的字典，如果新的字典中有和原字典相同的 key ，则该 key 的 value 会被新字典的 value 所覆盖。

用法：`dict.update(new_dict) `，该函数无返回值； new_dict 为新的字典

```python
user = {'name': 'Neo', 'age': 18, 'birthday': '2000-01-01'}
user_jack = {'name': 'Jack', 'age': 17, 'birthday': '2001-12-12', 'sex': 'man'}
user.update(user_jack)

print(user)

# 执行结果如下：
# >>> {'name': 'Jack', 'age': 17, 'birthday': '2001-12-12', 'sex': 'man'}
```

### setdefault

功能：获取key 的value，若 key 不存在字典中，会添加 key 并将 value 设为默认值,只设置key，不设置value默认值，输出为None

用法:`dict.setdefault(key, value)`,

- 简单来说就是：如果setdefault的key在字典中，已经有value值，只能获取value值，无法设置默认值，key不存在，则value存入key中

```python
info = {'name':"jack","age":18}
# 给info添加一个默认值school为BQ
info.setdefault('school','BQ')
print(info)

>>> {'name': 'jack', 'age': 18, 'school': 'BQ'}

info.setdefault('school',)
>>> {'name': 'jack', 'age': 18, 'school': None}
```

### len

功能：获取字典的元素个数

```python
#使用方法：len(变量名)
dict01 = {'id':101,'name':'toms','age':30}
print(len(dict01))	#展示字典下全部元素个数:3
```

### keys

功能:获取字典中所有的键

```python
#使用方法：dict.keys()
dict02 = {'a':100,'b':200,'c':300}
print(dict02.keys())	#dict_keys(['a', 'b', 'c'])
```

### values

功能：获取字典中所有的值

```python
#使用方法：dict.values()
dict03 = {'a':100,'b':200,'c':300}
print(dict03.values())	#dict_values([100, 200, 300])
```

### get

功能：获取键对应的值

```python
#使用方法：dict.get('键')
dict04 = dict(id=101,name='jack',score=90.5)
values1 = dict04.get('name')	#获取name对应的值
print(values1)	#jack
```

### items

功能：以键值的形式获取字典中的元素

```python
#使用方法：dict.items()
dict04 = dict(id=101,name='jack',score=90.5)
print(dict04.items())	#dict_items([('id', 101), ('name', 'jack'), ('score', 90.5)])
```

### pop

功能：根据字典中的键，删除删除对应元素，并返回删除元素的值

```python
#使用方法：dict.pop()
dict06 = {'id':101,'name':'toms','age':30}
print(dict06.pop('name'))	#toms
```

### 字典中的 value 可以是任何 Python 中的内置数据类型的对象和自定义对象。

**功能：**

```python
films_dict = {
    'warfare': ['父辈的旗帜', '风语者', '红男爵', '拯救大兵瑞恩'],
    'love': ['罗马假日', '怦然心动', '时空恋旅人', '天使爱美丽', '天使之城', '倒霉爱神'],
    'science_fiction': ['流浪地球', '宇宙追缉令', '时间管理局', '命运管理局']
}
film_fiction = {'fantasy':['指环王', '哈利波特', '黑夜传说', '加勒比海盗']}

films_dict.update(film_fiction)     #使用内置update函数对films_dict函数进行补充
print(films_dict)

warfare = films_dict['warfare']		#对value进行实例化
love = films_dict['love']
science_fiction = films_dict['science_fiction']
fantasy = films_dict['fantasy']
count_films = len(warfare)+len(love)+len(science_fiction)+len(fantasy)	#使用len函数计算出有多少元素
print(f'一共有{count_films}部电影')
```

## 