"""
 #!/usr/bin/env python
 # -*- coding:utf-8 -*-
 @Author: Little Seven
 @FileName: callback_demo.py
 @DateTime: 2023/7/7 14:31
 @SoftWare: PyCharm
"""
from functools import reduce

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


import asyncio

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

def read_large_file(file_path, callback):
    with open(file_path, 'r') as file:
        for line in file:
            # 调用回调函数处理每一行文本
            callback(line)

# 定义回调函数来处理每一行文本
def process_line(line):
    print("Processing line:", line.strip())

# 使用迭代器按行读取大型文件
# read_large_file('large_file.txt', callback=process_line)

import time

def timer_callback(i):
    print(f'定时器启动,执行了第{i}次'.center(20,'*'))

def set_time(timer,callback):
    i = 0
    while True:
        time.sleep(timer)
        i +=1
        callback(i)


if __name__ == '__main__':
    res = save_base_info([70, 80, 90], callback_func)
    print(res)

    auto_task(error_callback)

    # asyncio.run(run_task())
    # 未对数据进行处理
    with open('静夜思.txt','r',encoding='utf-8') as f:
        for i in f:
            print(i)
     # 使用回调函数对数据进行处理
    read_large_file('静夜思.txt',process_line)

    set_time(5,timer_callback)




