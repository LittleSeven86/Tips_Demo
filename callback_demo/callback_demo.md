# callback_function

## 什么是回调函数

回调函数是指将一个函数作为参数传递给另一个函数，并在需要时被调用的函数。为了降低函数之间调用的耦合性，从而实现解耦，通常回调函数用于异步操作或事件处理中，以便在某个事件发生或异步操作完成时执行特定的操作

## 回调函数的特点

- 通过函数地址调用函数，如果函数的指针（地址）作为参数传递给另外一个函数
- 函数的入参为函数类型
- 在特定的事件或者条件发生时由另外一方调用，用于对该事件或者条件进行响应
- 在参数位置，**使用函数进行传参时，尾部不添加()**

## 示例demo

```python 
def save_base_info(info_list, callback_func):
    """
    对信息进行校验，小于70分的进行过滤，不提交，剩下的进行提交，保存基本信息，提交至审批流
    :param info_list: 信息列表
    :param callback_func: 回调函数
    :return: 回调函数的返回值
    """
    end_list = list(filter(lambda x: x >= 70, info_list))
    return callback_func(end_list)

def callback_func(score_list):
    print(f'调用了回调函数 {callback_func.__name__}'.center(20, '*'))
    convert_json = {}
    for k, v in enumerate(score_list):
        convert_json[k] = v
    return convert_json

if __name__ == '__main__':
    res = save_base_info([70, 80, 90], callback_func)
    print(res)
    
>>>
调用了回调函数 callback_func
{0: 70, 1: 80, 2: 90}
```

## 常见的使用场景

Python 回调函数是一种常见的编程模式，用于将一个函数作为参数传递给另一个函数，并在某个特定事件发生时被调用。下面是几个使用回调函数的常见场景：

### 事件处理：

在事件驱动的程序中，回调函数经常用于处理特定的事件；比如进行错误处理，对异常结果进行记录，发送警报或者执行数据恢复工作

```python 
# 比如记录错误日志、发送警报、执行恢复操作等。
def auto_task(callback):
    try:
        # 执行自动化任务的代码
        # ...
        # 如果出现错误，抛出异常
        print(1/0)
    except Exception as e:
        # 调用错误处理的回调函数
        callback(e)


def error_callback(error):
    print(f'开始执行错误数据处理:{error}')
    
auto_task(error_callback)    
```

### 异步编程：

在异步编程中，回调函数通常用于处理长时间运行的任务的结果。当任务完成时，会调用预定义的回调函数来处理返回的结果。这在处理网络请求、数据库查询等异步操作时非常常见。

```python 
# 模拟一个长时间运行的异步任务
async def long_running_task():
    # 模拟等待一段时间
    await asyncio.sleep(5)
    return "Task result"

# 定义回调函数来处理任务结果
def callback(result):
    print("任务结果是:", result)
    # 在这里执行进一步的操作，如数据处理、更新UI等

# 执行异步任务
async def run_task():
    result = await long_running_task()
    # 任务完成后调用回调函数处理结果
    callback(result)

asyncio.run(run_task())

>>>
任务结果是: Task result
```

### 迭代器和生成器

回调函数可以用于实现自定义的迭代器和生成器。例如，在读取大型文件时，可以定义一个回调函数，在每次读取到一行文本时被调用。这种方式可以有效地处理大量数据，而不需要一次性将整个文件加载到内存中。

```python 
锄禾日当午
汗滴禾下土
谁知盘中餐
粒粒皆辛苦

def read_large_file(file_path, callback):
    with open(file_path, 'r') as file:
        for line in file:
            # 调用回调函数处理每一行文本
            callback(line)

# 定义回调函数来处理每一行文本
def process_line(line):
    print("Processing line:", line.strip())
 
# 使用迭代器按行读取大型文件
# 未对数据进行处理
with open('静夜思.txt','r',encoding='utf-8') as f:
  for i in f:
    print(i)
    
>>>
锄禾日当午

汗滴禾下土

谁知盘中餐

粒粒皆辛苦
    
# 使用回调函数对数据进行处理       
read_large_file('静夜思.txt',process_line)

>>>
Processing line: 锄禾日当午
Processing line: 汗滴禾下土
Processing line: 谁知盘中餐
Processing line: 粒粒皆辛苦
```

### 定时器和事件循环：

回调函数可以用于定时器和事件循环的编程。您可以设置一个定时器，在指定的时间间隔后调用回调函数。这对于周期性任务、定时任务和事件循环非常有用。

```python
import time

def timer_callback(i):
    print(f'定时器启动,执行了第{i}次'.center(20,'*'))

def set_time(timer,callback):
    i = 0
    while True:
        time.sleep(timer)
        i +=1
        # 使用回调函数对定时器进行处理
        callback(i)
    
set_time(5,timer_callback)
>>>
****定时器启动,执行了第1次****
****定时器启动,执行了第2次****
****定时器启动,执行了第3次****
```

### 钩子函数：

回调函数也可以用作钩子函数，用于在特定的代码点执行自定义的操作。

- 允许开发人员在代码的特定位置注入自己的逻辑，以便在关键时刻执行自定义操作。提供了一种灵活的扩展机制，使应用程序可以通过插件或扩展点来自定义行为，而无需修改核心代码。
- 可以定义一个回调函数，用于在启动时加载配置。这样，当框架或库初始化时，回调函数会被触发，并且您可以在其中加载和应用定义好的自定义配置。
- 在case执行完毕后，需要关闭或终止时清理资源。可以定义回调函数在应用程序关闭之前执行一些必要的清理操作，如释放内存、关闭文件、断开数据库连接等。

这些只是回调函数的一些常见使用场景，实际上，回调函数可以在许多不同的情况下用于实现更灵活的编程模式。通过将函数作为参数传递并在需要时进行调用，回调函数提供了一种松耦合和动态的编程方式，使代码更加模块化和可扩展。