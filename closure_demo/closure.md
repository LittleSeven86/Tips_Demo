# closure

## 什么是闭包：

我们前面已经学过了如何定义函数，知道当函数调用完，函数内定义的变量都销毁了，但是我们有时候需要保存函数内的这个变量，每次在这个变量的基础上完成一些列的操作，比如: 每次在这个变量的基础上和其它数字进行求和计算，那怎么办呢?

这时候就可以使用闭包解决我们遇到的问题，**闭包**是一种特殊的函数，由外部函数和内部函数嵌套组成，外部函数的返回值是内部函数的引用

## 闭包的关键特性

- 内部函数引用外部函数的变量：闭包函数中的内部函数可以引用外部函数中定义的变量
- 变量和函数组成一个整体，方便多次调用，局部变量会常驻在内存中、可以避免使用全局变量，防止全局变量污染；如果**使用不当会造成内存泄漏**（因为变量一直被占用，没有被释放）
- 由于闭包函数可以访问外部函数的变量，因此这些变量的状态在多次调用闭包函数之间得以保留，**一般在函数结束时，局部变量就会被Python的垃圾回收机制从内存中清除掉**，但在闭包中，由于外函数的临时变量在内函数中用到，此时外函数会把临时变量与内函数绑定到一起，这样虽然外函数结束了，但调用内函数时依旧能够使用临时变量，即闭包外层的参数可以在内存中进行保留

## 语法格式

```python
def outer_func(x):		# 变量x会一直保存在内存中
    def inner_func(y):
        sum = x + y
        return sum
    return inner_func

sum = outer_func(5)

print(sum(10))
print(sum(20))

>>> 
15
25
```

## 处理内外层变量的冲突

因为作用域的不同，内部函数能够读取到外部函数所有的变量，如果**内外部的变量名称冲突**了咋办呢？这时候就学到一个新的关键字**nonlocal**

nonlocal**用于在嵌套函数中声明并修改外部嵌套作用域中的变量**，它允许内部函数对位于其外部函数中的变量进行赋值，而不是创建一个新的同名局部变量。

```python
# 计数器demo
def outerfunc():
    x = 0
    def innerfunc():
        nonlocal x	
        x+=1
        return x
    return innerfunc

# 创建计数器
count = outerfunc()
print(count())
print(count())
print(count())
print(count())
```

**注意点：**

`nonlocal` 关键字只能用于嵌套函数中，用于声明和修改位于嵌套作用域中的变量。对于全局变量，应使用 `global` 关键字来声明并修改。

## 使用场景：

### **保留状态**

闭包函数可以用于保留状态，比如实现计数器的功能

```python 
def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

# 创建计数器
c = counter()

# 每次调用计数器时，状态会被保留
print(c())  # 输出: 1
print(c())  # 输出: 2
print(c())  # 输出: 3
```

### 回调函数

闭包函数可以用作回调函数，处理异步编程或者事件驱动的场景

```python 
from functools import reduce

def outer_function(callback):
    data = 'Hello'

    def inner_function():
        return [60, 70, 80]

    # 调用回调函数
    result = callback(*inner_function())
    return result

# 回调函数
def callback(*args):
    end_list = list(filter(lambda x: x >= 70, args))
    return end_list

end = outer_function(callback)
print(end)
```

### 创建事务控制器

当涉及事务处理时，闭包可以用于创建具有状态的事务处理器

```python 
def create_transaction_processor(initial_balance):
    balance = initial_balance

    def deposit(amount):
        """
        存钱
        """
        nonlocal balance
        balance += amount
        print(f"存款 {amount} 钱. 现在账户余额: {balance} 块钱.")

    def withdraw(amount):
        """
        取钱
        """
        nonlocal balance
        if amount <= balance:
            balance -= amount
            print(f"取出 {amount} 元钱. 现在账户余额: {balance} 块钱.")
        else:
            print("账户余额不足")

    def get_balance():
        return balance

    return deposit, withdraw, get_balance

# 创建事务处理器,内部函数共享了外部函数的balance变量
deposit_func, withdraw_func, get_balance_func = create_transaction_processor(100)

# 执行事务操作
deposit_func(50)
withdraw_func(30)

# 获取当前余额
balance = get_balance_func()
print(f"Current balance: {balance} units.")
```

