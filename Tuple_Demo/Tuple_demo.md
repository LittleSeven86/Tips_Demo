# 元祖

元组是"有序"、"不可变"的序列之一,一旦创建，没有任何方法可以修改元祖中的元素，可以把元祖看成"常量列表"，

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

