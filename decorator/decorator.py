#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
-----------------------------------------------------------
    @FileName  :decorator.py
    @Time      :2023/7/12 15:17
    @Author    :LittleSeven
    @Address   ：https://github.com/LittleSeven86
    @微信公众号  ：小柒测试笔记
-----------------------------------------------------------
'''



def yellow_car(func):
    car_type= func()
    def inner_func(*args,**kwargs):
        return f'送过来一辆{car_type},现在变成了宝马车'
    return inner_func

@yellow_car
def car():
    return '奔驰'

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










if __name__ == '__main__':
    # res = car()
    # print(res)
    # add_numbers(3, 5)
    print(get_data("A"))  # 第一次调用，会获取外部数据，并进行缓存
    print(get_data("A"))  # 第二次调用，直接从缓存中获取数据
    print(get_data("B"))  # 第一次调用，会获取外部数据，并进行缓存
    print(get_data("B"))  # 第二次调用，直接从缓存中获取数据
    print(divide(10, 2))  # 正常调用，输出 5.0
    print(divide(10, 0))  # 除零异常被捕获，输出捕获到的异常信息和返回的默认值 None

    print(access_sensitive_data())  # 用户经过授权，输出 "敏感数据"

    # 未经授权的用户调用
    try:
        access_sensitive_data()
    except PermissionError as e:
        print(e)  # 输出 "用户未经授权"



