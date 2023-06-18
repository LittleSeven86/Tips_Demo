#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
-----------------------------------------------------------
    @FileName  :Flow control.py
    @Time      :2023/6/18 20:44
    @Author    :LittleSeven
    @Address   ：https://gitee.com/linguchong/Django_Project_Demo.git
-----------------------------------------------------------
'''
# print('<-欢迎使用简易计算器->'.center(20,'*'))
# n1 = float(input('请输入第一个数：'))
# n2 = float(input('请输入第二个数：'))
# result = n1 + n2
# print(f'{n1}+{n2}={result}')
# print('计算完成，byebye'.center(20,'+'))

#案例05：获取键盘输入的数据（正整数、负整数），求该数的绝对值
# num1 = int(input('请输入第一个数：'))
# # if num1 <0:
# #     num1 = -num1
#
# num1 = -num1 if num1< 0 else num1
# print(f'num1绝对值是:{num1}')

donate = 0
while donate<=1000:
    money = float(input("请输入捐款金额"))
    donate += money
print('当前捐款总金额%d元'%donate)