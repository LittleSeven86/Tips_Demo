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
import threading

class ConcurrencyControl:
    def __init__(self, max_instances=1):
        self.max_instances = max_instances
        self.lock = threading.Semaphore(max_instances)

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            with self.lock:
                return func(*args, **kwargs)
        return wrapper

@ConcurrencyControl(max_instances=3)
def my_function():
    time.sleep(1)
    print("Executing my_function")

threads = []
for _ in range(5):
    thread = threading.Thread(target=my_function)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

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
    return "Welcome to the Home page"

@router("/about")
def about():
    return "About us"

@router("/contact")
def contact():
    return "Contact us"

# 调用路由处理函数
print(router.routes["/home"]())  # 输出: "Welcome to the Home page"
print(router.routes["/about"]())  # 输出: "About us"
print(router.routes["/contact"]())  # 输出: "Contact us"