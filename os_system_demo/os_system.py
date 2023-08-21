"""
 #!/usr/bin/env python
 # -*- coding:utf-8 -*-
 @Author: Little Seven
 @FileName: os_system.py
 @DateTime: 2023/8/21 15:49
 @SoftWare: PyCharm
"""
import os,subprocess,shlex
from shlex import quote

# os.system('ping 127.0.0.1 -n 20 > nul',)
print('test')
# command = ['cmd','d:','dir',]
# res = subprocess.run(command, shell=False,text=True)
# print(res.stdout,res.returncode)

filename = 'ping 127.0.0.1 -n 20 > nul' # 定义一个非常奇怪的文件名
command = 'ls -l {}'.format(quote(filename))
print(command,end='\n')  # executed by a shell: boom!
filename_list = shlex.split(filename)
print(filename_list)
res = subprocess.Popen(filename_list,text=True,shell=True)
# command = 'ls -l {}'.format(quote(filename_list))  # 使用shlex.quote对文件名进行正确的转义
print(command)

# ls -l 'somefile; rm -rf ~'
# subprocess.run(command, shell=True)

