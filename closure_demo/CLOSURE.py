"""
 #!/usr/bin/env python
 # -*- coding:utf-8 -*-
 @Author: Little Seven
 @FileName: CLOSURE.py
 @DateTime: 2023/7/6 10:27
 @SoftWare: PyCharm
"""
from functools import reduce

# def outer_func(x):
#     def inner_func(y):
#         sum = x + y
#         return sum
#     return inner_func
#
# sum = outer_func(5)
#
# print(sum(10))
# print(sum(20))
#
# def outerfunc():
#     x = 0
#     def innerfunc():
#         nonlocal x
#         x+=1
#         return x
#     return innerfunc
#
# count = outerfunc()
# print(count())
# print(count())
# print(count())
# print(count())
def create_transaction_processor(initial_balance):
    balance = initial_balance

    def deposit(amount):
        nonlocal balance
        balance += amount
        print(f"存款 {amount} 钱. 现在账户余额: {balance} 块钱.")

    def withdraw(amount):
        nonlocal balance
        if amount <= balance:
            balance -= amount
            print(f"取出 {amount} 元钱. 现在账户余额: {balance} 块钱.")
        else:
            print("账户余额不足")

    def get_balance():
        return balance

    return deposit, withdraw, get_balance

# 创建事务处理器
deposit_func, withdraw_func, get_balance_func = create_transaction_processor(100)

# 执行事务操作
deposit_func(50)
withdraw_func(30)

# 获取当前余额
balance = get_balance_func()
print(f"Current balance: {balance} units.")



def perform_operation(func):
    print("Performing operation...")
    result = 100
    func(result)

def handle_result(result):
    print("Received result:", result)

# 调用函数，并传递闭包函数作为回调
perform_operation(handle_result)



from functools import reduce

def outer_function(callback):
    data = 'Hello'

    def inner_function():
        return [60, 70, 80]

    # 调用回调函数
    result = callback(*inner_function())
    return result

# 回调函数
def callback(*args):
    end_list = list(filter(lambda x: x >= 70, args))
    return end_list

end = outer_function(callback)
print(end)


def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print("在调用函数之前执行装饰逻辑")
        result = original_function(*args, **kwargs)
        print("在调用函数之后执行装饰逻辑")
        return result
    return wrapper_function

@decorator_function
def greeting(name):
    print("你好，{}！".format(name))

greeting("Alice")



