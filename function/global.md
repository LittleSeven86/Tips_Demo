# global

在学会了如何定义函数，以及常见的函数参数的传递后，我们就要学习一下变量的作用域：一般分为**全局变量**和**局部变量**

- 全局变量是可以在整个代码中访问和使用的变量。可以在程序的任何地方被访问，包括函数内部和函数之间
- 局部变量是在特定作用域内定义的变量，通常是在函数内部或代码块内部声明的变量。可见性被限制在声明的代码块、函数或类中，无法在其外部进行访问。

## 变量的生命周期管理

- 全局变量：全局变量的生命周期从变量被定义时开始，整个程序执行过程中持续存在，直到程序结束或全局变量被显式删除。
- 局部变量：局部变量是在函数内部或代码块内部定义的变量。函数执行结束或代码块执行结束时。

## 定义全局变量

### 在函数外部或模块的顶层定义变量

```python
global_varibale = 30
...
```

### 在函数内部使用关键字定义

```python
def update_global_varibale():
    global local_variable	# 使用global关键字定义
    local_variable = 40 

update_global_varibale()
print(local_variable)
```

## 访问全局变量

### 函数内部访问全局变量

函数内部可以访问全局变量，无需使用`global`关键字。但是，**如果函数内存在与全局变量同名的局部变量**，**函数会优先使用局部变量**而不是全局变量

```python
global_variable = 10

def update_global_varibale():
    print(global_variable)  # 函数内部访问全局变量

update_global_varibale()

>>>  10 

global_variable = 10

def update_global_varibale():
    global_variable = 15
    print(global_variable)  # 函数内部访问全局变量

update_global_varibale() 
```

## 修改全局变量

### 函数外部修改

```python
global_variable = 10
global_variable = 50
print(global_variable)

>>> 50
```

### 函数内部修改

如果要在函数内部修改全局变量的值，需要使用`global`关键字在函数内部声明变量为全局变量。

```python
global_variable = 10

def update_global_varibale():
    global global_variable	# 使用global关键字声明全局变量
    global_variable = 15
    print(global_variable)  

update_global_varibale()

>>> 15
```

## 生命周期结束

全局变量的生命周期在整个程序执行过程中持续存在，直到程序结束或使用`del`关键字显示删除

```python
global_variable = 10

del global_variable
print(global_variable)

>>> NameError: name 'global_variable' is not defined
```

**Tips：**

全局变量在某些情况下可以方便地共享数据和状态，并在程序的各个部分之间传递信息。然而，过多地使用全局变量可能会导致代码难以维护和理解，因此应该谨慎使用，并优先考虑使用局部变量和函数参数来封装和传递数据。

# 局部变量

局部变量的生命周期是指变量在其作用域内存在的时间段。在Python中，局部变量的生命周期从变量被创建时开始，直到其作用域结束或变量被销毁

## 创建局部变量

局部变量是在函数内部或代码块内部定义的变量。

```python
def create_local_variable():
    local_variable = 30		# 定义局部变量
    print(local_variable)

create_local_variable()
>>> 30
```

## 访问局部变量

### 作用域内访问

在函数作用域内，可以直接访问局部变量

```python
def some_function():
    local_variable = 10
    print(local_variable)  # 访问局部变量
```

![image-20230705101839728](C:\Users\mengzhang32\AppData\Roaming\Typora\typora-user-images\image-20230705101839728.png)

### 作用域外访问

```python 
def some_function():
    local_variable = 10
    print(local_variable)  # 访问局部变量

print(local_variable)		# 作用域外访问局部变量

>>> NameError: name 'local_variable' is not defined
```

![image-20230705102151576](C:\Users\mengzhang32\AppData\Roaming\Typora\typora-user-images\image-20230705102151576.png)

## 生命周期结束

局部变量的生命周期在其作用域结束时终止，即函数执行结束或代码块执行结束时。

```python
def create_local_variable():
    local_variable = 30
    return local_variable	# 局部变量生命周期结束
    print(local_variable)

res = create_local_variable()
print(res)

>>> 30
```

## 作用域嵌套：

在Python中，可以在**作用域内嵌套其他作用域**，这包括函数、类和模块。作用域嵌套允许内部作用域访问外部作用域中定义的变量、函数和类，这部分内容会在后续的**闭包**当中去讲解，我们先写一个简单的demo感受一下

```python
def outer_function():
    x = 10

    def inner_function():
        y = 20
        result = x + y
        return result

    return inner_function()

print(outer_function())  # 输出：30
```

在上面的示例中，内部函数`inner_function`嵌套在外部函数`outer_function`中。内部函数可以访问外部函数中定义的变量`x`，并进行计算。

 



**注意点：未声明全局变量，函数内修改全局变量的值，会抛出异常**

```python
def update_global_varibale():
    print(global_variable)  # 函数内部访问全局变量
    global_variable = 20    # 未声明全局变量在函数内部修改全局变量
    print(global_variable)

update_global_varibale()
```

![image-20230704150701965](C:\Users\mengzhang32\AppData\Roaming\Typora\typora-user-images\image-20230704150701965.png)

