"""
 #!/usr/bin/env python
 # -*- coding:utf-8 -*-
 @Author: Little Seven
 @FileName: Typing_demo.py
 @DateTime: 2023/8/16 15:38
 @SoftWare: PyCharm
"""
from typing import List,Dict,Set,Tuple,Union,Optional
name:str = 'jack'
print(name,type(name))

# 整数类型
age:int = 18
# 列表类型数据，未注释列表内元素数据类型
book:list = ['鲁滨逊漂流记','三国演义']
# 字典类型，未注释字典内键和值和类型
info:dict = {'school':'primary school'}
# 布尔类型，=
isboy:bool = True

print(f'{name}在{info["school"]}上学，今年{age}岁了')

# 列表类型：并注解为整数类型的列表
book_list:List[int]=[1,2,3,4,5]
# 字典类型：注解为键为字符串、值为字符串的字典
info_dict:Dict[str,str] = {'name':"jack"}
# 集合类型：注解为整数类型的集合
age_demo:Set[int] = {1,2,3,4,1}
# 元祖类型：注解为浮点数类型的元祖
point: Tuple[float] = (3.14, 2.71)
# 可能类型：表示extra_info可能为整数型列表，也可能是键为字符串、值为整数的字典，或者为None
extra_info:Union[List[int],Dict[str,int],None]='json'
# print(extra_info)

def add_numbers(num1:int,num2:int)->int:
    return num1+num2

print(add_numbers(0,0))

def check_list(target:List[int])->List[int]:
    return list(filter(lambda x:x%2!=0,target))
res = check_list([1,2,3,4,5])
print(res)

student_info:Dict[str,str] ={"name":'jack',"address":"安徽"}

info_type = Dict[str,str]
student_info:info_type ={"name":'jack',"address":"安徽"}

print(student_info)

from typing import NewType

UserID = NewType('UserID', int)
username = NewType('username', str)

def get_user_id(user_id: UserID) -> None:
    print(f"User ID: {user_id}")

def get_username(name: username) -> None:
    print(f"Username: {name}")

id_value = UserID(1234)
name_value = username('jason')

get_user_id(id_value)
get_username(name_value)

def print_name(name: str):
    print(name)

from typing import Callable

def add_numbers(a: int, b: int) -> int:
    return a + b

def subtract_numbers(a: int, b: int) -> int:
    return a - b

def perform_operation(operation: Callable[[int, int], int], a: int, b: int) -> int:
    return operation(a, b)

result = perform_operation(add_numbers, 5, 3)
print(result)  # 输出 8

result = perform_operation(subtract_numbers, 10, 4)
print(result)  # 输出 6

from typing import Callable,TypeVar,Any

def greet(name: str) -> None:
    print(f"Hello, {name}!")

def calculate_sum(a: int, b: int) -> int:
    return a + b

# 可调用对象接受一个字符串参数并返回空值（None）
func1: Callable[[str], None] = greet

# 可调用对象接受两个整数参数并返回一个整数结果
func2: Callable[[int, int], int] = calculate_sum

# 使用 func1 和 func2 进行函数调用
func1("Alice")
result = func2(5, 3)
print(result)



Optional[str]
Optional[List[str]]
Optional[Dict[str, Any]]

# 错误
Optional[str, int]
Optional[Union[str, int, float]]

