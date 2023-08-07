"""
 #!/usr/bin/env python
 # -*- coding:utf-8 -*-
 @Author: Little Seven
 @FileName: abc_method.py
 @DateTime: 2023/8/7 10:17
 @SoftWare: PyCharm
"""
from abc import ABC,abstractmethod

class Models(ABC):
    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def update(self):
        pass

class ProjectBaseModel(Models):
    def get(self):
        print('获取到项目基本信息')
    def update(self):
        print('更新项目基本信息')
# # a = Models()

project1 = ProjectBaseModel()
project1.get()
models = Models()
models.get()
