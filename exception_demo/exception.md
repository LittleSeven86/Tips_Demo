# 异常处理

## 引言

正常情况下，代码是自上而下逐行执行的，执行到最后一行才会终止程序运行，出现异常会导致我们的程序停止运行，为了不影响程序的执行，需要对这些异常进行处理， Python 中的异常机制，可以**监控并捕获到异常**。当程序出现错误的时候对异常进行临时的处理，就可以使得程序继续正常的运行，提高程序的健壮性

## 语法

```python
try:
    # 可能会引发异常的代码块
    # ...
except ExceptionType1:
    # 处理 ExceptionType1 异常的代码块
    # ...
else:
    # 如果没有发生任何异常，执行的代码块
    # ...
finally:
    # 无论是否发生异常，都会执行的代码块
    # ...
```

- **try**：包含可能会引发异常的代码块。
- **excep**t：用于捕获和处理特定类型的异常。
- **ExceptionType**：指定要捕获的异常类型，可以使用多个except语句来处理不同类型的异常。
- **else**：在try块中没有发生任何异常时执行的代码块。
- **finally**：无论是否发生异常，都会执行的代码块。 

## 常见使用场景

### 文件操作

在处理文件时，可能会遇到文件不存在或无法访问的情况，使用异常处理可以捕获这些错误并采取适当的措施

```python 
try:
    file = open("example.txt", "r")
    # 执行文件操作
    # ...
except FileNotFoundError as e:
    print(f'异常为：{e}')
except PermissionError as e :
    print(f'异常为：{e}')
else:
    print("文件操作成功")
finally:
    file.close()  # 确保文件关闭
    
>>>
异常为：[Errno 2] No such file or directory: 'example.txt'
```

### 数据库操作

在接口自动化，进行对数据库数据进行治理，需要执行我们既定的SQL，如果连接失败、超时等情况，可以使用异常处理进行记录

```python
import sqlite3

try:
    conn = sqlite3.connect("sqllite3.db")
    cursor = conn.cursor()
    cursor.execute("select * from args")
    # 执行数据库操作
    # ...
except sqlite3.Error as e:
    print("数据库错误:", str(e))
else:
    print("数据库操作成功")
finally:
    cursor.close()
    conn.close()
```

### 重试机制

```python
import requests
import time

MAX_RETRY = 3  # 最大重试次数

def make_request(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # 检查请求是否成功
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")
        return None

def fetch_data_with_retry(url):
    retry_count = 0
    while retry_count < MAX_RETRY:
        data = make_request(url)
        if data is not None:
            return data
        retry_count += 1
        print(f"请求： {retry_count}/{MAX_RETRY}...")
        time.sleep(1)  # 延迟一秒后再重试
    return None

def main():
    url = "https://www.baidu.com1/"  # 假设这是我们的请求地址
    data = fetch_data_with_retry(url)
    if data:
        print(f"数据为: {data}")
    else:
        print("重试次数过多，查询数据失败.")

if __name__ == "__main__":
    main()
    
>>>
请求失败: HTTPSConnectionPool(host='www.baidu.com1', port=443): Max retries exceeded with url: / (Caused by SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:997)')))
请求： 1/3...
请求失败: HTTPSConnectionPool(host='www.baidu.com1', port=443): Max retries exceeded with url: / (Caused by SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:997)')))
请求： 2/3...
请求失败: HTTPSConnectionPool(host='www.baidu.com1', port=443): Max retries exceeded with url: / (Caused by SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:997)')))
请求： 3/3...
重试次数过多，查询数据失败.
```