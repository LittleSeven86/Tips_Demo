## 集合

集合是一种`无序且不重复`的数据集合，以逗号分隔，数据重复只显示1个元素，可以是不同的类型。

### 定义集合

```python
#直接定义---集合名 = {数据1，数据2，数据3}
set01={1,2,3,4,5}

#集合名 = set(迭代对象)
set01 = set(i for i in range(0,5))
print(set01)

# 迭代创建	
print({i for i in range(0,5)})

#说明:集合是以{}括起来的数据集合,以逗号分隔，数据不能重复否则只显示一个元素，可以是不同的数据类型
set04 = {100,100,200,300,200}
print(set04)	#{200, 100, 300}
```

### 访问集合

```python
# 通过下标访问,通过一下案例说明，集合不可通过下标进行访问
set_demo = {1,2,1,1,2,3,4,5,6}
print(set_demo[0])
>>> TypeError: 'set' object is not subscriptable

# 通过集合名访问
print(set01)

# 解包
set05={100,'A',200}
a1,b1,c1= set05

# 迭代访问
print({i for i in set_demo})
>>>{1, 2, 3, 4, 5, 6}
```

### 集合运算

```python
#并集 符号 |，显示两个集合的全部元素
s01 = {100,200,300,400,500}
s02 = {'A','B','C','D','E',100,300,500}
res1 = s01|s02
print(res01)	#{100, 'C', 200, 'B', 300, 400, 'D', 500, 'A', 'E'}

#交集 符号& ， 显示集合共同存在的元素
res2 = s01&s02
print(res2)		#{100, 500, 300}

#差集 符号 - ， 
res3 = s02-s01
print(res3)		#{'E', 'D', 'A', 'C', 'B'}
```

## 集合去重

去重是集合惯用的手法，集合使用hash函数来确定元素的存储位置。hash函数将元素映射到一个唯一的哈希值，这个哈希值决定了元素在集合中的位置。

```python
set_demo = {1,2,1,1,2,3,4,5,6}
print(set_demo)		>>>{1, 2, 3, 4, 5, 6}
```

### set.add()

**功能：**向集合中新增一个元素

```python
s01 = {100,'A',200,'B'}
s01.add(300)
print(s01)		#{100, 'B', 200, 300, 'A'}
```

### set.clear()

**功能：**清空集合元素

```python
set_demo = {1,2,1,1,2,3,4,5,6}
set_demo.clear()
print(set_demo)		>>> set()
```

### set.copy()

**功能：**

- 复制集合元素，这里是浅拷贝

```python
set_demo01 = set_demo.copy()
print(set_demo,set_demo01)
>>> {1, 2, 3, 4, 5, 6} {1, 2, 3, 4, 5, 6}
```

### set.update()

**功能：**将一个集合中的元素更新到另一个集合中

```python
#使用方法：set2.update(set3),set3的元素放到set2中
s02 = {'A','B','C'}
s03 = {'A',100,'B',200,300}
s02.update(s03)
print(s02)		#{100, 200, 'A', 300, 'B', 'C'}
```

### set.remove()

**功能：**删除集合中的某个元素

```python
#使用方法：set.remove()
s04 = {'A',100,'B',200,300}
s04.remove(200)
print(s04)		#{'B', 100, 300, 'A'}
```

### set.difference()

**功能：**返回两个或多个集合的差值作为新集合

```python
set_demo02 = {0,1,2,3}
set_demo03 = {2,3,4,5}
print(set_demo02.difference(set_demo03))	>>> {0, 1}
print(set_demo03.difference(set_demo02))	>>> {4, 5}
```

### set.difference()

**功能：**返回两个或多个集合的差值作为新集合	

```python
set_demo02 = {0,1,2,3}
set_demo03 = {2,3,4,5}
print(set_demo02.difference(set_demo03))	>>> {0, 1}
print(set_demo03.difference(set_demo02))	>>> {4, 5}
```

### set.difference_update()

**功能：**

- 从当前集合中移除与其他指定集合的交集部分，即原地更新当前集合。
- `set1.difference_update(set2, set3, ...)`
  - `set1`是要进行更新操作的集合，
  - `set2`、`set3`等是其他集合作为参数，表示要计算差集的集合。

- `difference_update`方法修改了调用它的集合对象本身，而不返回新的集合。

```python
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6}
set3 = {1, 2}

set1.difference_update(set2, set3)

print(set1)		>>> {3}
```

### set.discard()

**功能：**用于从集合中删除指定的元素。如果元素存在于集合中，则会被删除；如果元素不存在于集合中，`discard`方法不会引发错误，而是静默地执行不做任何操作。

语法：`set.discard(element)`

小技能点：与`discard`方法类似的是`remove`方法，不同之处在于，`remove`方法在元素不存在时会引发`KeyError`异常，而`discard`方法在元素不存在时静默地执行不做任何操作。因此，如果你不确定元素是否存在于集合中，可以使用`discard`方法来避免异常的发生。

```python
my_set = {1, 2, 3, 4, 5}

my_set.discard(3)	
my_set.discard(6)

print(my_set)	>>>{1, 2, 4, 5}
```

### set.intersection()

**功能：**返回当前集合与其他指定集合的交集，即两个或多个集合中共同存在的元素构成的新集合。

语法：`set1.intersection(set2, set3, ...)`

说明：需要注意的是，`intersection`方法返回一个新的集合对象，包含了交集部分的元素，而`原始集合对象不会被修改`。如果只需要判断两个集合是否有交集，可以使用`isdisjoint`方法。如果需要获取多个集合的交集，并对原始集合进行修改，可以使用`intersection_update`方法。

```python
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6}
set3 = {3, 4, 7}

intersection_set = set1.intersection(set2, set3)

print(intersection_set)
```

### set.intersection_update()

**功能**：用于将当前集合更新为与其他指定集合的交集，即原地修改当前集合。

```python
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6}
set3 = {3, 4, 7}

set1.intersection_update(set2, set3)

print(set1)		>>>{4}
```

### set.isdisjoint()

**功能**：用于判断当前集合与其他指定集合是否没有交集，即两个集合是否没有共同的元素。

说明：只接受一个集合作为参数进行比较，不能同时判断多个集合之间是否有交集。如果需要判断多个集合之间是否有交集，可以使用`intersection`方法得到交集结果，并判断结果集合是否为空。

```python
set1 = {1, 2, 3, 4, 5}
set2 = {6, 7, 8}
set3 = {4, 5, 6}

print(set1.isdisjoint(set2))  # True，set1与set2没有共同的元素
print(set1.isdisjoint(set3))  # False，set1与set3有共同的元素
```

### set.issuberset()

**功能**：用于判断当前集合是否是其他指定集合的子集，即当前集合是否包含于指定集合。

```python
set1 = {1, 2}
set2 = {1, 2, 3, 4, 5}
set3 = {6, 7, 8}

print(set1.issubset(set2))  # True，set1是set2的子集
print(set1.issubset(set3))  # False，set1不是set3的子集
```

### set.issuperset()

**功能**：用于判断当前集合是否包含其他指定集合的所有元素，即当前集合是否是指定集合的超集。

说明：需要注意的是，`如果两个集合相等（拥有相同的元素），那么一个集合既是另一个集合的子集，也是超集，此时issubset方法会返回True`

```python
set1 = {1, 2, 3, 4, 5}
set2 = {1, 2}
set3 = {6, 7, 8}

print(set1.issuperset(set2))  # True，set1包含set2的所有元素
print(set1.issuperset(set3))  # False，set1不包含set3的所有元素
```

### set.union()

**功能**：`union`是集合对象的一个方法，用于返回当前集合与其他指定集合的并集，即将两个或多个集合中的所有元素合并成一个新集合。

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = {5, 6, 7}

union_set = set1.union(set2, set3)

print(union_set)	>>>{1, 2, 3, 4, 5, 6, 7}
```

### 