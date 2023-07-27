"""
 #!/usr/bin/env python
 # -*- coding:utf-8 -*-
 @Author: Little Seven
 @FileName: 私有属性.py
 @DateTime: 2023/7/27 14:13
 @SoftWare: PyCharm
"""
class Demo:
    def __init__(self):
        # 定义私有方法
        self.__age = 20
    @property
    def age(self):
       return self.__age

    @age.setter
    def age(self,value):
        self.__age = value

    @age.deleter
    def age(self):
        del self.__age

# print(Demo().__)

class MyClass:
    def __init__(self):
        self.__age = 40
    def __private_method(self):
        return "这是私有方法"

    def open_method(self):
        print("这是公共方法")
        result = self.__private_method()
        print(result)

    def get_private(self):
        print(self.__private_method())
        print(self.__age)
#
# print(MyClass()._MyClass__age)
# print(MyClass()._MyClass__private_method())


class Parent:
    def __init__(self):
        self.__private_var = "父类私有属性"

    def __private_method(self):
        return "父类私有方法"

    def public_method(self):
        print("父类公共方法")
        print(self.__private_var)
        print(self.__private_method())


class Child(Parent):
    def __init__(self):
        super().__init__()  # 调用父类的构造函数

        # 子类中定义一个与父类同名的私有属性和私有方法
        self.__private_var = "子类私有属性"

    def __private_method(self):
        return "子类私有方法"

    def get_args(self):
        print("这是类公共方法")
        print(self.__private_var)
        print(self.__private_method())
        self.public_method()  # 调用父类的公有方法

#
# child_obj = Child()
# # child_obj.public_method()
# child_obj.get_args()

class UserManager:
    def __init__(self):
        self.__users = {}  # 私有属性，用于存储用户数据

    def add_user(self, username, email):
        # 检查用户名和邮箱是否已存在等逻辑
        if username not in self.__users and email not in [user['email'] for user in self.__users.values()]:
            self.__users[username] = {'email': email}
            print(f"用户：{username} 被添加")
        else:
            print("用户名或者邮箱已存在")

    def remove_user(self, username):
        if username in self.__users:
            del self.__users[username]
            print(f"用户：{username} 被删除")
        else:
            print("未查询到用户")

    def get_user_email(self, username):
        if username in self.__users:
            return self.__users[username]['email']
        else:
            return "未查询到用户"

    def __private(self):
        pass


# 使用UserManager类的示例
User = UserManager()

User.add_user("小柒", "xiaoqi@qq.com")
User.add_user("小捌", "xiaoba@qq.com")

# 尝试直接访问私有属性
print(User.__users)  # 错误！不能直接访问私有属性

# 尝试直接调用私有方法
User.__private()  # 错误！不能直接调用私有方法

# 使用公共方法访问私有属性和私有方法
print(User.get_user_email("小柒"))  # 输出：xiaoqi@qq.com
User.remove_user("小捌")  # 输出：用户：小捌 被删除
