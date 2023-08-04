"""
 #!/usr/bin/env python
 # -*- coding:utf-8 -*-
 @Author: Little Seven
 @FileName: duotai.py
 @DateTime: 2023/8/4 17:11
 @SoftWare: PyCharm
"""
class Model:
    def get(self):
        pass

    def save(self):
        pass
    def update(self):
        pass

class ProjectModels(Model):
    def get(self):
        print('获取到了项目信息')
    def save(self):
        print('保存项目基本信息')
    def update(self):
        print('更新项目基本信息')

class TestCase(Model):
    def get(self):
        print('获取用例基本信息')

    def save(self):
        print('保存用例基本信息')

    def update(self):
        print('更新用例基本信息')


project1 = ProjectModels()
project1.get()

case1 = TestCase()
case1.get()