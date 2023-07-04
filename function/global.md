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

### 示例：全局访问函数局部变量

```python
global_variable = 10

def update_global_varibale():
    local_variable = 30    	# 局部变量
    print(local_variable)   # 在函数内部访问局部变量

update_global_varibale()
print(local_variable)   #在函数外部访问局部变量，引发 NameError  
```

![image-20230704151237783](C:\Users\mengzhang32\AppData\Roaming\Typora\typora-user-images\image-20230704151237783.png)

**注意点：未声明全局变量，函数内修改全局变量的值，会抛出异常**

```python
def update_global_varibale():
    print(global_variable)  # 函数内部访问全局变量
    global_variable = 20    # 未声明全局变量在函数内部修改全局变量
    print(global_variable)

update_global_varibale()
```

![image-20230704150701965](C:\Users\mengzhang32\AppData\Roaming\Typora\typora-user-images\image-20230704150701965.png)

