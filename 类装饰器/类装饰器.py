#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
-----------------------------------------------------------
    @FileName  :类装饰器.py
    @Time      :2023/7/16 13:33
    @Author    :LittleSeven
    @Address   ：https://github.com/LittleSeven86
    @微信公众号  ：小柒测试笔记
-----------------------------------------------------------
'''
class DecoratorClass:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("开始类装饰器")
        result = self.func(*args, **kwargs)
        print("开始类装饰器")
        return result

@DecoratorClass
def my_function():
    print("具体操作。。。")

# my_function()
class ExceptionHandler:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        try:
            return self.func(*args, **kwargs)
        except Exception as e:
            print(f"异常捕获: {type(e).__name__} - {str(e)}")

@ExceptionHandler
def divide(a, b):
    return a / b

# divide(10, 0)
import time

class TimerDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        result = self.func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"函数 '{self.func.__name__}' 执行了 {execution_time:.4f} 秒")
        return result

@TimerDecorator
def compute(n):
    total = 0
    for i in range(n):
        total += i
    return total

# compute(10000)

class CallCounter:
    def __init__(self, func):
        self.func = func
        self.call_count = 0

    def __call__(self, *args, **kwargs):
        self.call_count += 1
        return self.func(*args, **kwargs)

@CallCounter
def my_function():
    print("执行函数")

my_function()  # 输出: "执行函数"
my_function()  # 输出: "执行函数"
print(my_function.call_count)  # 输出: 2

class TransactionManager:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        # 模拟开始事务
        print("开始交易")

        try:
            # 执行函数
            result = self.func(*args, **kwargs)

            # 提交事务
            print("提交事务")
            return result
        except Exception as e:
            # 回滚事务
            print(f"事务回滚: {str(e)}")
            raise

@TransactionManager
def transfer_money(from_account, to_account, amount):
    # 模拟业务操作
    print(f"转账： {amount} 从 {from_account} 账户到 {to_account}")

    # 模拟抛出异常
    raise ValueError("账户余额不足")

# 调用函数，触发事务管理
try:
    transfer_money("A123", "B456", 1000)
except Exception as e:
    print(f"异常捕获: {str(e)}")


class DataEncryptor:
    def __init__(self, func):
        self.func = func

    def encrypt(self, data):
        # 实现数据加密逻辑
        encrypted_data = "加密数据_" + data
        return encrypted_data

    def decrypt(self, encrypted_data):
        # 实现数据解密逻辑
        decrypted_data = encrypted_data.replace("加密数据_", "")
        return decrypted_data

    def __call__(self, *args, **kwargs):
        # 对输入参数进行加密
        encrypted_args = [self.encrypt(str(arg)) for arg in args]
        encrypted_kwargs = {k: self.encrypt(str(v)) for k, v in kwargs.items()}

        # 调用原始函数并获取结果
        result = self.func(*encrypted_args, **encrypted_kwargs)

        # 对结果进行解密
        decrypted_result = self.decrypt(str(result))
        return decrypted_result

@DataEncryptor
def process_data(data):
    return "数据: " + data

encrypted_result = process_data("asdlf3jk2h3d")
print(encrypted_result)  # 输出: asdlf3jk2h3d
