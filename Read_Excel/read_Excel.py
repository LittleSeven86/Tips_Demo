#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
-----------------------------------------------------------
    @FileName  :read_Excel.py
    @Time      :2023/6/18 21:19
    @Author    :LittleSeven
    @Address   ：https://gitee.com/linguchong/Django_Project_Demo.git
-----------------------------------------------------------
'''
import openpyxl


def read_Excel(file_path,sheet_name):
    work_book = openpyxl.load_workbook(file_path)

    sheet = work_book[sheet_name]
    testcases = []
    for row in sheet.iter_rows(min_row=2,values_only=True):
        testcase = {
            'test_id': row[0],
            'description': row[1],
            'input_data': row[2],
            'expected_output': row[3]
        }
        testcases.append(testcase)
    # 关闭Excel文件
    work_book.close()

    return testcases

if __name__ == '__main__':
    result = read_Excel('工作簿1.xlsx','sheet')
    print(result)