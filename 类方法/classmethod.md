# classmethod

## 引言

在前面我们学会了如何定义类，在类当中定义的方法默认都是实例方法，当我们调用一个对象的方法时，self参数会被自动传入，并指向该对象本身。而**类方法**是一个特殊的方法，**与类本身相关联，而不是与实例相关联**

## 实例方法

实例对象调用类的方法时，Python会自动将该对象的引用作为第一个参数（即self）传递给方法，至少会有一个`self`参数

```python 
class Person:
    def __init__(self,name):
        self.name = name

    def demo(self):
        print(f'实例方法，通过对象调用，名字是：{self.name}')

Jack = Person('jack')
Jack.demo()

>>>
实例方法，通过对象调用，名字是：jack
```

### 通过类名调用实例方法

Python中支持直接使用类名调用实例方法，但是要手动传递实例对象的引用，不然会报错

```python 
class Person:
    def __init__(self,name):
        self.name = name

    def demo(self):
        print(f'实例方法，通过对象调用，名字是：{self.name}')

Jack = Person('jack')
# 手动传递实例对象
Person.demo(Jack)
>>> 实例方法，通过对象调用，名字是：jack

# 不传递实例对象
Person.demo()
>>> TypeError: Person.demo() missing 1 required positional argument: 'self'
```

## classmethod

### 源码解析

```python 
class classmethod(object):
    def __get__(self, *args, **kwargs): # real signature unknown
       '''
       返回实例的属性，该属性属于拥有者的类
       '''
        pass

    def __init__(self, function): 
        '''
        接受一个函数作为参数，并将其转换为类方法
        '''
        pass
```

### 定义类方法

在定义类方法时，需要添加装饰器`@classmethod`，和实例方法至少要一个`self`参数一样，至少要包含一个`cls`参数,通常命名为` cls`,用于引用类本身。

```python 
class ClassMethod:
    
    @classmethod
    def demo(cls,name):
        print(f'名字是:{name}')
    
    @classmethod
    def check_id(cls):
        print(f'当前对象的id是：{id(cls)}')

ClassMethod.demo('jack')
ClassMethod.check_id()
ClassMethod.check_id()

>>>
名字是:jack
# 证明cls是同一对象
当前对象的id是：2174753542320
当前对象的id是：2174753542320
```

## 类方法的特点

### 类方法可以访问类的属性和其他类方法

```python 
class ClassMethod:
    
    height = 180.55
    def __init__(self,age):
        self.age = age
        
    @classmethod
    def other_classmethod(cls):
        pass
    
    @classmethod
    def demo(cls,name):
        # 通过cls参数，调用类方法
        cls.other_classmethod()
        print(f'名字是:{name}')
        # 通过cls参数，调用访问类属性
        print(cls.height)

ClassMethod.demo('jack')
>>>
名字是:jack
180.55
```

### 类方法无法访问实例的属性

因为类方法不与特定的实例相关联，如果需要访问实例属性，会抛出异常

```python 
class ClassMethod:
    
    @classmethod
    def demo(cls,name):
        cls.testdemo()

    def testdemo(self):
        pass

ClassMethod.testdemo()

>>>
TypeError: ClassMethod.testdemo() missing 1 required positional argument: 'self'
```

### 类方法可以用作工厂方法，用于创建类的实例

通常情况下，需要先实例化一个类对象才能调用该类的方法或属性，但是**类方法提供了不实例化类的情况下直接创建对象的方式**，可以封装实例化的过程，并提供更方便的接口给用户，可以直接通过类名调用类方法，而无需先创建类的实例

```python 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def create_person(cls, name, age):
        return cls(name, age)

person = Person.create_person("Alice", 25)
print(person.name)  # 输出：Alice
print(person.age)   # 输出：25
```

## 常见场景

