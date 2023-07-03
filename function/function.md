# 引言

函数在程序代码中，起到**分离代码**的功能，是**模块化程序设计**的基本组成，函数定义完成后，可以反复使用，实现代码解耦，方便后期代码的维护。

## 函数的分类

- 内置函数：Python解释器内置的，可以直接在代码中使用而无需导入任何模块。例如，`print()`、`len()`和`range()`等函数都是内置函数

```python 
# 内置函数在使用时，直接调用即可，无需import
print('hello world')
range(0,3)	>>>0,1,2
```

- 自定义函数：由开发者自己编写的，用于解决特定的问题或执行特定的任务。开发者可以根据自己的需求定义函数名称、参数和函数体，并在需要的时候调用这些函数。

```python
def add_numbers(a, b):
    sum = a + b
    return sum

result = add_numbers(2, 3)
print(result)  # 输出：5
```

- 模块函数：Python社区提供的函数库，通过import导入使用，`requests、pytest、unittest`

## 如何自定义函数

```python 
def function_name(parameters):
    # 函数体
    # 执行任务
    return result

- def ==为关键字用于定义函数，后跟函数的名称,函数名称建议见名知意，例如：check_number、read_sql
- 函数名称应遵循标识符的命名规则，以字母或下划线开头，可以包含字母、数字和下划线。
- 参数是函数接受的输入，可以有零个或多个参数，多个参数用逗号分隔。
- 函数体是函数执行的实际代码块。
- return语句用于返回函数的结果。如果没有指定return语句，函数将默认返回None。
```

## return的作用

`return`语句用于将结果或值从函数中返回给调用者。当函数执行到`return`语句时，它会立即退出函数并返回指定的值

### 返回值

函数可以执行一些操作，并将计算得到的结果作为返回值返回给调用者。返回值可以是任意类型的数据，例如整数、字符串、列表等。通过使用`return`语句，可以将结果传递给调用者，调用者可以继续使用该值或将其赋给变量。

```python 
def add(a, b):
    return a + b

result = add(3, 4)
print(result)  # 输出: 7
```

### 提前退出函数

在函数的执行过程中，如果满足某个条件，可以使用`return`语句提前退出函数，无需继续执行函数的剩余代码。这样可以节省计算资源和提高函数执行效率。

```python
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(is_even(4))  # 输出: True
print(is_even(3))  # 输出: False
```

## print和return的区别

当`return`和`print`同时存在于函数中时，它们有不同的作用和效果。

- `return`语句：`return`用于将结果或值从函数中返回给调用者。它指定了函数的返回值，并且在执行到`return`语句时会立即退出函数。`return`可以返回任意类型的数据，并且可以在函数的任何位置使用。

- `print`语句：`print`用于在控制台或输出流中打印信息。它将指定的值或表达式转换为字符串，并将其输出到标准输出。`print`语句通常用于调试目的或在程序执行过程中显示一些信息，但它并不会影响函数的返回值。

```python
def add_and_print(a, b):
    result = a + b
    print("The sum is:", result)
    return result
	print("The sum is:", result)	#代码并未执行

sum_result = add_and_print(3, 4)
print("Returned value:", sum_result)

>>>
The sum is: 7
Returned value: 7
```

