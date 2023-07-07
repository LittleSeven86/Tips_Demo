"""
 #!/usr/bin/env python
 # -*- coding:utf-8 -*-
 @Author: Little Seven
 @FileName: callback_demo.py
 @DateTime: 2023/7/7 14:31
 @SoftWare: PyCharm
"""
from functools import reduce

def save_base_info(info_list, callback_func):
    """
    对信息进行校验，小于70分的进行过滤，不提交，剩下的进行提交，保存基本信息，提交至审批流
    :param info_list: 信息列表
    :param callback_func: 回调函数
    :return: 回调函数的返回值
    """
    end_list = list(filter(lambda x: x >= 70, info_list))
    return callback_func(end_list)

def callback_func(score_list):
    print(f'调用了回调函数 {callback_func.__name__}'.center(20, '*'))
    convert_json = {}
    for k, v in enumerate(score_list):
        convert_json[k] = v
    return convert_json

if __name__ == '__main__':
    res = save_base_info([70, 80, 90], callback_func)
    print(res)



