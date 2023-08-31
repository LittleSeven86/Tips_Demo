#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
-----------------------------------------------------------
    @FileName  :DataUtils.py
    @Time      :2023/8/31 10:08
    @Author    :LittleSeven
    @Address   ：https://github.com/LittleSeven86
    @微信公众号  ：小柒测试笔记
-----------------------------------------------------------
'''
import oracledb,cx_Oracle
# import oracledb

oracledb.init_oracle_client(lib_dir="/Users/z.m/oracle/instantclient_19_8")



connection = oracledb.connect(user="U_TEST_PMPD", password='PMPDtest123',
                                  host="10.0.27.5", port=1521, service_name="pomp")
cursor = connection.cursor()
res = cursor.execute("select count(1) from project_base_info where project_code = 'R-221125002'")
print(res.fetchall())
# import cx_Oracle
# import platform
#
# print(platform.processor())
#
# cx_Oracle.init_oracle_client(lib_dir="/Users/z.m/oracle/instantclient_19_8")
# tns = 'U_TEST_PMPD/PMPDtest123@I10.0.27.5:1521/pomp'
# connection = cx_Oracle.connect(user="U_TEST_PMPD", password="PMPDtest123",
#                                dsn="10.0.27.5/pomp",
#                                encoding="UTF-8")
# # db1 = cx_Oracle.connect(tns)
# cursor = connection.cursor()
# res = cursor.execute("select * from project_base_info where project_code = 'R-221125002'")
# print(res.fetchall())
