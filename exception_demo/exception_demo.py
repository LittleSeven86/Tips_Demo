"""
 #!/usr/bin/env python
 # -*- coding:utf-8 -*-
 @Author: Little Seven
 @FileName: exception_demo.py
 @DateTime: 2023/7/18 14:14
 @SoftWare: PyCharm
"""
try:
    print(10/1)
except ZeroDivisionError as e:
    print(e)
else:
    print(1/1)
finally:
    print('执行结束了')

#
# try:
#     file = open("example.txt", "r")
#     # 执行文件操作
#     # ...
# except FileNotFoundError as e:
#     print(f'异常为：{e}')
# except PermissionError as e :
#     print(f'异常为：{e}')
# else:
#     print("文件操作成功")
# finally:
#     file.close()  # 确保文件关闭

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


import sqlite3

# 初始化数据库连接
conn = sqlite3.connect("bank.db")
cursor = conn.cursor()


def create_table():
    # 创建账户表
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS accounts (
            id INTEGER PRIMARY KEY,
            account_number TEXT UNIQUE,
            balance REAL
        )
    """)
    conn.commit()


def deposit(account_number, amount):
    try:
        # 开启数据库事务
        conn.execute("BEGIN TRANSACTION")

        # 查询账户余额
        cursor.execute("SELECT balance FROM accounts WHERE account_number = ?", (account_number,))
        balance = cursor.fetchone()

        # 更新账户余额
        new_balance = balance[0] + amount
        cursor.execute("UPDATE accounts SET balance = ? WHERE account_number = ?", (new_balance, account_number))

        # 提交事务
        conn.commit()
        print(f"存款成功，账户余额：{account_number}: {new_balance}")
    except Exception as e:
        # 回滚操作
        conn.rollback()
        print(f"交易失败: {e}")


def withdraw(account_number, amount):
    try:
        # 开启数据库事务
        conn.execute("BEGIN TRANSACTION")

        # 查询账户余额
        cursor.execute("SELECT balance FROM accounts WHERE account_number = ?", (account_number,))
        balance = cursor.fetchone()

        if balance[0] >= amount:
            # 更新账户余额
            new_balance = balance[0] - amount
            cursor.execute("UPDATE accounts SET balance = ? WHERE account_number = ?", (new_balance, account_number))

            # 提交事务
            conn.commit()
            print(f"取款成功，账户余额 {account_number}: {new_balance}")
        else:
            print("账户余额不足，取款失败")
    except Exception as e:
        # 回滚操作
        conn.rollback()
        print(f"取款失败: {e}")


def main():
    create_table()

    # 添加示例账户
    cursor.execute("INSERT OR IGNORE INTO accounts (account_number, balance) VALUES (?, ?)", ("jack", 1000.0))
    conn.commit()

    # 进行存款和取款操作
    deposit("jack", 500.0)
    withdraw("jack", 2000.0)
    withdraw("jack", 800.0)  # 取款失败，余额不足

    conn.close()


if __name__ == "__main__":
    main()
