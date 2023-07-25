"""
 #!/usr/bin/env python
 # -*- coding:utf-8 -*-
 @Author: Little Seven
 @FileName: 构造方法.py
 @DateTime: 2023/7/25 15:05
 @SoftWare: PyCharm
"""
# 没有显式定义 __init__() 方法
class MyClass1:
    pass

# 创建类实例
obj1 = MyClass1()

# 显式定义 __init__() 方法
class MyClass2:
    def __init__(self):
        print("显示的定义构造方法")

# 创建类实例
obj2 = MyClass2()

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

#继承自 Animal 类，并重写了父类的构造函数
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return "狗在叫!"

# 创建一个Dog对象并调用speak方法
dog = Dog("Dog")
print(dog.speak(),dog.name)  # 输出：狗在叫! Dog

import configparser
import cx_Oracle

class DatabaseConnector:
    def __init__(self, db_name):
        self.db_name = db_name
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')

    def connect(self):
        db_host = self.config.get(f'{self.db_name}', 'host')
        db_port = int(self.config.get(f'{self.db_name}', 'port'))
        db_user = self.config.get(f'{self.db_name}', 'user')
        db_password = self.config.get(f'{self.db_name}', 'password')
        db_name = self.config.get(f'{self.db_name}', 'db_name')

        dsn = cx_Oracle.makedsn(db_host, db_port, service_name=db_name)
        try:
            connection = cx_Oracle.connect(user=db_user, password=db_password, dsn=dsn)
            print("Database connected successfully.")
            # 在这里可以执行其他与数据库相关的操作


        except cx_Oracle.Error as e:
            print("Failed to connect to the database:", str(e))


# 创建对象并连接数据库
db_name = "Test_Env_DataBase"  # 假设传入的数据库名称是 "Test_Env_DataBase"
db_connector = DatabaseConnector(db_name)
db_connector.connect()

