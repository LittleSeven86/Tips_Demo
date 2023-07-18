# property

## 什么是property

`property`是一种内置的装饰器，用于将一个方法转换为对象的属性，从而实现属性访问的控制和定制

## 语法示例

示例中的属性使用了单下划线前缀，这是一种命名约定，用于**表示这些属性是受保护的**，不应直接访问。

```python
class MyClass:
    def __init__(self):
        self._x = 0  # Use a different name for the attribute

    # getter method
    @property
    def x(self):
        return self._x

    # setter method
    @x.setter
    def x(self, value):
        self._x = value

    # deleter method
    @x.deleter
    def x(self):
        del self._x

obj = MyClass()
print(obj.x)  # 输出：0

obj.x = 10   # 设置属性x为10
print(obj.x)  # 输出：10

del obj.x   # 删除属性x
print(obj.x)  # 输出：AttributeError: 'MyClass' object has no attribute '_x'
```

## 场景应用

### 数据验证和保护

可以在setter方法中添加数据验证逻辑，确保对象属性的值符合特定条件

```python
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise ValueError("年龄必须是一个整数.")
        if value < 0:
            raise ValueError("年龄必须是一个正整数")
        self._age = value


# 使用property进行数据验证和保护
person1 = Person("Alice", 30)

try:
    person1.age = "twenty"  # 尝试设置一个非整数的年龄
except ValueError as e:
    print("Error:", e)  # 输出：Error：必须是一个整数

try:
    person1.age = -5  # 尝试设置一个负数的年龄
except ValueError as e:
    print("Error:", e)  # 输出：Error:年龄必须是一个正整数

# 年龄设置合法，修改年龄为40
person1.age = 40

print(person1.age)  # 输出：40
```

### 隐藏实现细节

 可以将一些复杂的计算或数据转换封装在属性的getter方法中，对外部用户来说，只需访问属性即可，而不用关心底层的实现逻辑

```python
class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self._balance = balance

    @property
    def account_number(self):
        return self._account_number

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            print("Insufficient funds")

# 创建BankAccount对象
account = BankAccount("123456789", 1000)

# 访问账户信息
print("账号:", account.account_number)  # 输出: 账户: 123456789
print("余额:", account.balance)  # 输出:余额: 1000

# 存款
account.deposit(500)

# 取款
account.withdraw(200)

# 访问更新后的余额
print("账户余额:", account.balance)  # 输出: 账户余额: 1300
```

1. 简化接口：通过隐藏实现细节，外部用户只需要直接访问属性即可获取所需的结果，而不需要了解底层的算法或计算过程。这提供了一个简洁、易于使用的接口，降低了使用复杂性。
2. 提高可维护性：隐藏实现细节可以将底层逻辑与外部代码隔离开来，使代码更具模块化和可维护性。如果需要修改底层逻辑或算法，只需修改属性的getter方法，而不会影响到外部代码的使用。
3. 提供封装和保护：通过隐藏实现细节，可以将一些敏感或私有的数据保护起来，只暴露需要对外部可见的部分。这样可以有效地控制对数据的访问和修改，提高代码的安全性。

### 惰性计算

在首次访问`result`属性时，会执行复杂计算，并将结果缓存起来，后续的访问则直接返回缓存的结果，避免重复计算。这样可以显著提高性能，尤其当计算过程非常耗时时

```python
class ExpensiveComputation:
    def __init__(self, data):
        self._data = data
        self._result = None

    @property
    def data(self):
        return self._data

    @property
    def result(self):
        if self._result is None:
            print("加载中....")
            self._result = self._perform_expensive_computation()
        return self._result

    def _perform_expensive_computation(self):
        # 进行复杂的计算
        # 这里只是一个示例，假设计算结果是数据中大于10的元素个数
        return len([x for x in self._data if x > 10])

# 创建ExpensiveComputation对象
data = [5, 8, 12, 3, 9, 15]
computation = ExpensiveComputation(data)

# 访问数据
print("Data:", computation.data)  # 输出: Data: [5, 8, 12, 3, 9, 15]

# 访问结果，首次访问会触发计算
print("Result:", computation.result)  # 输出: 加载中... \n Result: 3

# 再次访问结果，不会触发计算，直接返回缓存的结果
print("Result:", computation.result)  # 输出: Result: 3
```

### 动态属性

使用`property`可以实现动态属性，可以实现根据对象的状态或其他条件动态计算或返回属性的值，提供了一种灵活的方式来处理动态属性的需求

```python
class DynamicProperty:
    def __init__(self):
        self._status = "initial"

    @property
    def status(self):
        if self._status == "initial":
            return "初始化状态"
        elif self._status == "running":
            return "启动中"
        elif self._status == "completed":
            return "已关闭"

    def start(self):
        self._status = "running"

    def complete(self):
        self._status = "completed"

# 创建DynamicProperty对象
property_obj = DynamicProperty()

# 访问初始状态属性
print(property_obj.status)  # 输出: 初始化状态

# 开始任务，属性状态动态改变
property_obj.start()

# 访问运行中的状态属性
print(property_obj.status)  # 输出: 启动中

# 完成任务，属性状态再次动态改变
property_obj.complete()

# 访问完成状态属性
print(property_obj.status)  # 输出: 已关闭
```