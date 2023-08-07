# abstractmethod

## 引言

前文中，我们留下来了一个小悬念**abstractmethod**，**abstractmethod**是**Python**中的一个装饰器，用于定义抽象方法，可以规范类的接口和行为，实现代码复用和扩展、接口隔离和解耦以及支持多态和多重继承

## 什么是抽象

首先我们理解一下，什么是抽象？

- 抽象梗：鸡你太美、全体起立
- 抽象画

从概念上来说：抽象是哲学的根本特点，抽象不能脱离具体而独自存在，将几个有区别的物体的共同性质或特性，形象地抽取出来

![img](https://img-blog.csdnimg.cn/17e9d5293d414a53b5a1a441d672fdc2.png)

在面向对象编程中，抽象是一种将问题行为模型化的过程，目的是隐藏细节、提取共性，并定义出一组规范供其他类遵循，可以分为两个层面

- 抽象类`（Abstract Class）`：不能被实例化的类，其中包含了一个或多个抽象方法，抽象方法只有方法的签名，没有具体的实现。抽象类定义了一种规范，要求其子类必须实现这些抽象方法。抽象类可以包含非抽象的方法和属性，主要用于作为一种通用的基类，定义一些通用的行为和属性，而留下具体实现给子类去完成。
- 接口`（Interface）`：接口是一种纯粹的抽象机制，只包含抽象方法和常量的定义，没有任何具体实现。接口定义了一系列方法的约定，要求实现该接口的类必须提供这些方法的具体实现，接口常用于定义类之间的协议，用于实现多态和解耦。

## abstractmethod

用于声明抽象方法，抽象方法需要借助`abc`模块`（Abstract Base Classes）`来定义，`abc`模块提供了`ABC``（Abstract Base Class）`和`abstractmethod`装饰器来支持抽象方法的定义和使用

### 源码解析

```python 
def abstractmethod(funcobj):
    """A decorator indicating abstract methods.

    Requires that the metaclass is ABCMeta or derived from it.  A
    class that has a metaclass derived from ABCMeta cannot be
    instantiated unless all of its abstract methods are overridden.
    The abstract methods can be called using any of the normal
    'super' call mechanisms.  abstractmethod() may be used to declare
    abstract methods for properties and descriptors.

    Usage:

        class C(metaclass=ABCMeta):
            @abstractmethod
            def my_abstract_method(self, ...):
                ...
    """
    funcobj.__isabstractmethod__ = True
    return funcobj
```

- 定义名为`abstractmethod`的函数装饰器，接受一个函数对象作为参数
- 要求元类`（metaclass）`必须是`ABCMeta`或其派生类，元类是用于创建类的类，`ABCMeta`是一个特殊的元类，用于定义抽象基类。
- 抽象方法可以使用任何正常的`'super'`调用机制进行调用，即通过super()函数在子类中调用父类的方法。
- 最后，`funcobj.__isabstractmethod__ = True`将被装饰函数对象的`__isabstractmethod__`属性设置为True，表示该函数是一个抽象方法。最后，返回被装饰的函数对象`funcobj`

### 定义示例

```python 
# 使用前需要导入abstractmethod
from abc import ABC,abstractmethod

class Models(ABC):
    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def update(self):
        pass

class ProjectBaseModel(Models):
    
    def get(self):
        print('获取到项目基本信息')
        
    def update(self):
        print('更新项目基本信息')

project1 = ProjectBaseModel()
project1.get()
```

### 注意事项

- **抽象类不能被实例化**，只能作为其他类的父类来使用,实例化会抛出异常

```python 
models = Models()
models.get()

>>>
Traceback (most recent call last):
    models = Models()
TypeError: Can't instantiate abstract class Models with abstract methods get, update
```

- 子类的元类派生自`ABCMeta`，**除非所有的抽象方法都被子类覆盖实现，否则该类不能被实例化**，不然会抛出异常

```python 
from abc import ABC,abstractmethod

class Models(ABC):
    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def update(self):
        pass

class ProjectBaseModel(Models):
    
    def get(self):
        print('获取到项目基本信息')

project1 = ProjectBaseModel()
project1.get()

>>>
Traceback (most recent call last):
    project1 = ProjectBaseModel()
TypeError: Can't instantiate abstract class ProjectBaseModel with abstract method update
```

## 使用场景

### 设计接口

在后续的开发框架学习过程中，可能会创建一个抽象基类并定义一些必须由任何子类实现的抽象方法，这就像是创建了一个蓝图，确保所有的子类都遵循相同的设计和行为模式。

```python 
from abc import ABC, abstractmethod

class Document(ABC):
    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def close(self):
        pass

class WordDocument(Document):
    def open(self):
        return "打开文件"

    def save(self):
        return "保存文件"

    def close(self):
        return "关闭文件"
```



