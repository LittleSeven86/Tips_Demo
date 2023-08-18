"""
 #!/usr/bin/env python
 # -*- coding:utf-8 -*-
 @Author: Little Seven
 @FileName: function.py
 @DateTime: 2023/7/3 10:38
 @SoftWare: PyCharm
"""
import time

from Utils.loguru_demo import logger

# 位置参数
def check_name(name,age):
    return f'是{name}啊，今年他{age}岁'

res = check_name(19,'xiaoqiang')
print(res)

def greet(age,name= '小柒'):
    print("Hello", name, "you are", age, "years old.")

greet(age=25, name="Alice")
greet(age=25)

def stu_info(*args):
    logger.info(f'执行了{stu_info.__name__}')
    logger.warning(f'执行了{stu_info.__name__}')
    logger.debug(f'执行了{stu_info.__name__}')
    logger.critical(f'执行了{stu_info.__name__}')
    logger.error(f'执行了{stu_info.__name__}')
    print(f'{args[0]}同学，这次考试{args[1]}分')

stu_info('小明',90)
@logger.catch
def a ():
    return 1/0

a()
try:
    a()
except BaseException as e:
    logger.exception(e)

def func(a, b):
    return a / b


def nested(c):
    try:
        func(5, c)
    except ZeroDivisionError:
        logger.exception("异常捕获了")


nested(0)

# 通过循环进行入参进行处理
def print_person(**person):
    for key, value in person.items():
        print(key, ":", value)
    logger.info(12345)

print_person(name="Alice", age=25, city="New York")
# 输出:
# name : Alice
# age : 25
# city : New York

def persion_info(**kwargs):
    print(f'名字是：{kwargs["name"]}，今年{kwargs["age"]}岁')

persion_info(name = '小柒',age = 20)

class Demo:
    def __init__(self):
        logger.info('test')
        pass

a = Demo()
