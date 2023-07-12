# 装饰器

## 引言

装饰器本质上是一个Python函数(其实就是闭包)，可以让指定函数在不需要做任何代码变动的前提下增加额外功能，装饰器的返回值也是一个函数对象。

装饰器用于有以下场景，比如:插入日志、性能测试、事务处理、缓存、权限校验等场景。

## 执行逻辑

```python 
def decorator_function(func):
    def wrapper_function(*args, **kwargs):
        # 在调用原始函数之前执行的代码
        # ...
        result = func(*args, **kwargs)
        # 在调用原始函数之后执行的代码
        # ...
        return result
    return wrapper_function
```

在这个示例中，`decorator_function `是一个装饰器函数，它接受一个函数作为参数 `func`，并返回一个新的函数 `wrapper_function`。`wrapper_function` 执行装饰器中定义的代码，然后调用原始函数`func  `

要将装饰器应用到函数上，只需在函数定义之前使用装饰器名称：

```python
@decorator_function
def func():
    # 函数体
    # ...
    pass
```

## 无参装饰器常见使用场景

### 记录日志

可以用于记录函数的调用信息，例如函数名、参数和返回值等

```python
def add_func(func):
    def wrapper_function(*args, **kwargs):
        print(f"调用函数 {func.__name__}")
        print(f"参数：args={args} kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"返回值：{result}")
        return result
    return wrapper_function

@add_func
def add_numbers(a, b):
    return a + b
  
add_numbers(3, 5)

>>>
调用函数 add_numbers
参数：args=(3, 5) kwargs={}
返回值：8
```

### 缓存结果

可以缓存函数的计算结果或外部数据，提高函数的执行效率。

```python
def cache_data(func):
    cached_data = {}

    def wrapper_function(*args):
        if args in cached_data:
            return cached_data[args]
        result = func(*args)
        cached_data[args] = result
        return result

    return wrapper_function

@cache_data
def get_data(key):
    # 模拟获取数据的过程，这里只是简单返回一个字符串
    print("正在获取外部数据...")
    return f"外部数据: {key}"

  
print(get_data("A"))  # 第一次调用，会获取外部数据，并进行缓存
print(get_data("A"))  # 第二次调用，直接从缓存中获取数据
print(get_data("B"))  # 第一次调用，会获取外部数据，并进行缓存
print(get_data("B"))  # 第二次调用，直接从缓存中获取数据  

>>>>
正在获取外部数据...
外部数据: A
外部数据: A
正在获取外部数据...
外部数据: B
外部数据: B
```

### 异常处理

可以捕获函数执行过程中的异常，并进行适当的处理，例如记录错误日志或返回特定的默认值

```python
def handle_exceptions(func):
    def wrapper_function(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            # 处理异常的逻辑，例如记录日志或返回默认值
            print(f"捕获到异常: {e}")
            result = None  # 返回默认值
        return result
    return wrapper_function

@handle_exceptions
def divide(a, b):
    return a / b
  
print(divide(10, 2))  # 正常调用，输出 5.0
print(divide(10, 0))  # 除零异常被捕获，输出捕获到的异常信息和返回的默认值 None  

>>>
5.0
捕获到异常: division by zero
None
```

### 授权验证

验证用户的身份和权限，确保只有经过授权的用户才能访问受限资源或执行敏感操作

```python
def authenticate(original_function):
    def wrapper_function(*args, **kwargs):
        # 假设这里是进行身份验证的逻辑
        user_authenticated = True

        if user_authenticated:
            result = original_function(*args, **kwargs)
            return result
        else:
            raise PermissionError("用户未经授权")

    return wrapper_function

@authenticate
def access_sensitive_data():
    return "敏感数据"
  
print(access_sensitive_data())  # 用户经过授权，输出 "敏感数据"

# 未经授权的用户调用
try:
  access_sensitive_data()
except PermissionError as e:
  print(e)  # 输出 "用户未经授权"

>>>
敏感数据
用户未经授权
```

