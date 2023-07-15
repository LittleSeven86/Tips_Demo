#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
-----------------------------------------------------------
    @FileName  :带参数装饰器.md.py
    @Time      :2023/7/15 14:51
    @Author    :LittleSeven
    @Address   ：https://github.com/LittleSeven86
    @微信公众号  ：小柒测试笔记
-----------------------------------------------------------
'''

def args_decorator(n):
    def decorator(func):
        def wrapper(*args,**kwargs):
            for _ in range(n):
                res  = func(*args,**kwargs)
            return res
        return wrapper
    return decorator

@args_decorator(n=3)
def greet(name):
    print(f'Hello,{name}')


def log_decorator(log_file):
    def decorator(func):
        def warpper(*args,**kwargs):
            with open(log_file,'a',) as file:
                file.write(f"接口名称：'{func.__name__}'\t参数：{args}\tKwargs: {kwargs}\n")
            res = func(*args,**kwargs)
            return res
        return warpper
    return decorator

@log_decorator('log.log')
def add(a, b):
    return a + b

import time

def performance_timer(max_executions):
    def decorator(func):
        def wrapper(*args, **kwargs):
            total_execution_time = 0

            for _ in range(max_executions):
                start_time = time.time()
                result = func(*args, **kwargs)
                end_time = time.time()

                execution_time = end_time - start_time
                total_execution_time += execution_time

            average_execution_time = total_execution_time / max_executions
            print(f"Function '{func.__name__}' executed {max_executions} times.")
            print(f"Average execution time: {average_execution_time:.4f} seconds")

            return result
        return wrapper
    return decorator

@performance_timer(max_executions=5)
def calculate_sum(n):
    time.sleep(n)


import time,pymysql

def retry_decorator(max_attempts, delay=0):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    print(f"Attempt {attempts + 1} failed: {str(e)}")
                    attempts += 1
                    time.sleep(delay)
            raise Exception(f"Function '{func.__name__}' failed after {max_attempts} attempts")
        return wrapper
    return decorator

@retry_decorator(max_attempts=3, delay=1)
def connect_to_server():
    # 模拟连接服务器的逻辑
    # 如果连接失败会抛出异常
    pymysql.connect(host='106.52.213.128',user='root',passwd='Admin1231@qwe',db='mysql')
    print('数据库链接成功')


# connect_to_server()

def event_trigger(event_func):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            event_func(result)  # 在函数执行完成后触发事件函数
            return result
        return wrapper
    return decorator

def event_handler(result):
    print(f"Event handler triggered with result: {result}")

@event_trigger(event_func=event_handler)
def calculate_sum(a, b):
    result = a + b
    return result

result = calculate_sum(2, 3)





# result = calculate_sum(0.5)



add(2, 3)
greet('jack')


