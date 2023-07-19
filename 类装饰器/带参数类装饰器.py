#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
-----------------------------------------------------------
    @FileName  :带参数类装饰器.py
    @Time      :2023/7/16 14:49
    @Author    :LittleSeven
    @Address   ：https://github.com/LittleSeven86
    @微信公众号  ：小柒测试笔记
-----------------------------------------------------------
'''
import threading, time


class ConcurrencyControl:
    # 用于指定允许同时执行的函数实例数量
    def __init__(self, max_instances=1):
        self.max_instances = max_instances
        self.lock = threading.Semaphore(max_instances)

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            # 可以确保在并发环境中只有指定数量的函数实例能够同时执行
            with self.lock:
                return func(*args, **kwargs)

        return wrapper


@ConcurrencyControl(max_instances=3)
def my_function():
    time.sleep(1)
    print("执行函数")


# threads = []
# for _ in range(5):
#     thread = threading.Thread(target=my_function)
#     thread.start()
#     threads.append(thread)
#
# for thread in threads:
#     thread.join()


class APIRouter:
    def __init__(self):
        self.routes = {}

    def __call__(self, path):
        def decorator(func):
            self.routes[path] = func
            return func

        return decorator


router = APIRouter()


@router("/home")
def home():
    return "欢迎来到首页"


@router("/about")
def about():
    return "关于我们"


@router("/contact")
def contact():
    return "联系我们"


# 调用路由处理函数
print(router.routes["/home"]())  # 输出: "欢迎来到首页"
print(router.routes["/about"]())  # 输出: "关于我们"
print(router.routes["/contact"]())  # 输出: "联系我们"


class CustomDecorator:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print(f"参数: arg1={self.arg1}, arg2={self.arg2}")
            return func(*args, **kwargs)

        return wrapper


@CustomDecorator("value1", "value2")
def my_function():
    print("执行函数")


# my_function()

import time

class RequestLimiter:
    def __init__(self, max_requests=10, interval=60):
        self.max_requests = max_requests
        self.interval = interval
        # 记录请求时间，并在每次请求前清理过期的请求记录。
        self.last_request_times = []

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            current_time = time.time()
            # 清理过期的请求记录
            self.last_request_times[:] = [t for t in self.last_request_times if current_time - t <= self.interval]

            if len(self.last_request_times) >= self.max_requests:
                print("Too many requests. Please try again later.")
                return None

            # 记录当前请求时间
            self.last_request_times.append(current_time)
            return func(*args, **kwargs)

        return wrapper


@RequestLimiter(max_requests=5, interval=10)
def make_api_request():
    print("发起API请求")

# for _ in range(10):
#     make_api_request()
#     time.sleep(1)

import sqlite3

class Transactional:
    def __init__(self, database):
        self.database = database

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            # 连接到数据库
            conn = sqlite3.connect(self.database)
            cursor = conn.cursor()
            try:
                # 执行函数内部的数据库操作
                result = func(cursor, *args, **kwargs)
                # 提交事务
                conn.commit()
                return result
            except Exception as e:
                # 回滚事务
                conn.rollback()
                raise e
            finally:
                # 关闭数据库连接
                conn.close()

        return wrapper


@Transactional(database="mydb.db")
def update_records(cursor):
    cursor.execute("UPDATE users SET name = 'lusy' WHERE id = 5")
    cursor.execute("INSERT INTO users (id, name,age) VALUES (3, 'tom',19)")

update_records()




