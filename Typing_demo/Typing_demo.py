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

age:int = 18
book:list = ['鲁滨逊漂流记','三国演义']
info:dict = {'school':'primary school'}
isboy:bool = True

print(f'{name}在{info["school"]}上学，今年{age}岁了')

book_list:List[int]=[1,2,3,4,5]

info_dict:Dict[str,str] = {'name':"jack"}

age_demo:Set[int] = {1,2,3,4,1}

point: Tuple[float] = (3.14, 2.71)

extra_info:Union[List[int],Dict[str,int],None]

