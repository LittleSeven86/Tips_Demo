# random

提供了生成随机数和进行随机选择的功能,实现了各种分布的伪随机数生成器

## 引言

在使用之前需要先导包

```python 
import random
```

## 常见方法

### random.random()

**功能**：返回一个0-1之间的随机浮点数

```python 
print(random.random())

>>>
0.4471742228565089
```

### random.uniform()

**语法**：`random.uniform(start,end)`

**功能**：在区间`(start，end)`区间取一个随机的浮点数

```python 
print(random.uniform(0,4))

>>>
2.860126114882176
```

### random.randint():

**语法：**`random.randint(start,end)`

**功能：**在区间`(start，end)`区间取一个随机的整数

```python 
print(random.randint(1,6))

>>>
5
```

### random.choice()

**功能：**返回序列中随机的一个元素

```python
list_choice = [1, 'tom', 0.123, True, None, {'name': 'jack'}]
res = random.choice(list_choice)
print(res)

>>>
None
```

### random.sample()

**语法：**

```python 
random.sample(sequence, k)

- sequence : 序列参数
- k: 不重复的数量
```

**功能：**随机返回对象中指定数量的元素

```python 
print(random.sample(list_choice,2))

>>>
[1, {'name': 'jack'}]
```

### random.randrange()

**功能：**返回区间内随机一个整数

**语法：**

```python
random.ranrange(start,end,step)

- start:起始位置
- end: 结束位置
- step: 步长
```

```python 
print(random.randrange(1,30,4))

>>>
25
```

