# 什么是self

## 引言

在Python初学者来说，在定义类`class`的时候，对于`self`这个参数肯定不陌生，在定义构造方法或者类方法的时候，在参数的第一个位置，总会出现，这期我们详细的说一下`self`的含义和作用

## 什么是`self`

在面向对象编程中，`self`是一个约定俗成的名字，用于表示当前对象自身,通常作为类方法的第一个参数，用于引用调用该方法的对象,**所有实例方法都需要加 self 参数，排在第一个，有且仅有一个**。

```python
class Person:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello, 我的名字是：", self.name)

# 当创建Person对象并调用其方法时，self参数会自动传入，并指向该对象本身        
Jack = Person('jack')
Jack.say_hello()

# 这里的Allen.say_hello()相当于Person.say_hello(Allen)
# 其中self参数就是指向person对象的引用
Allen = Person('Allen')
Allen.say_hello()
```

![IMG](https://img-blog.csdnimg.cn/3337ebe31a164374b7a193f31e02396e.png)

![img](https://img-blog.csdnimg.cn/c27b71a28a7c43659f30b6065a328d0f.png)

当我们创建一个类的实例对象时，实际上是在内存中分配了一块空间，并将该对象的引用赋值给了变量。在调用类的方法时，Python会自动将该对象的引用作为第一个参数（即self）传递给方法。

![img](https://img-blog.csdnimg.cn/41f347331e70415c8236ffcf3c938906.png)

通过self参数，可以直接访问和操作该对象的属性和方法，self参数允许方法在内部引用当前对象，从而可以获取或修改对象的状态。

## `self`是固定格式吗？

我们可以通过`keyword`来查看一下python中有哪些关键字

```python 
import keyword

print(keyword.kwlist)

>>>
False, None, True, and,
as, assert, async, await,
break, class, continue, def,
del, elif, else, except,
finally, for, from, global,
if, import, in, is, lambda,
nonlocal, not, or, pass,
raise, return, try, while,
with, yield
```

可以看到，Python中，`self`并不是一个保留的关键字，我们可以使用任何合法的变量名来代替`self`参数

```python
class Person:
    def __init__(Qi, name):
        Qi.name = name

    def say_hello(Qi):
        print("Hello, my name is", Qi.name)

Jack = Person('jack')
Jack.say_hello()

>>>Hello,我的名字是: jack
```

然而，为了遵循约定和编码规范，强烈建议大家使用self作为实例方法的第一个参数，`self`是一个常见的命名习惯，其他程序员**可以更容易地理解你的代码**

## End

```python 
class Self:
    def __init__(self):
        print(f'构造方法:{self},id是{id(self)}')

demo1 = Self()
demo2 = Self()
```

- 构造方法:`<__main__.Self object at 0x000001D510B5FD90>,id是2014620024208`
- 构造方法:`<__main__.Self object at 0x000001D510B5FD60>,id是2014620024160`

- 通过`self`参数，可以保证每个实例对象的只能调用自己的实例属性和实例方法
- 调用实例方法的时候，不需要手动为第一个参数传值