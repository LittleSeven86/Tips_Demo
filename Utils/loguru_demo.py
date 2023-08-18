"""
 #!/usr/bin/env python
 # -*- coding:utf-8 -*-
 @Author: Little Seven
 @FileName: loguru_demo.py
 @DateTime: 2023/8/17 16:36
 @SoftWare: PyCharm
"""
import time
from loguru import logger
from pathlib import Path
import sys

project_path = Path.cwd().parent
log_path = Path(project_path, "log")
t = time.strftime("%Y_%m_%d")


class Loggings:
    __instance = None

    def __init__(self):
        logger.remove()
        logger.add(
            f"{log_path}/interface_log_{t}.log",
            backtrace=True,
            diagnose=True,
            rotation="500MB",
            encoding="utf-8",
            enqueue=True,
            retention="10 days",
            format="{time:YYYY-MM-DD HH:mm:ss.SSS} | {level} | 进程号： {process} | 线程号：{thread} | 模块名：{file} | 方法：{function}| 行号：{line} - | msg：{message}"
        )
        logger.add(
            sys.stdout,
            colorize=True,
            backtrace=True,
            diagnose=True,
            # format="<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green>  <level> | {level} | </level> <cyan>模块名：{file}</cyan> | <cyan>方法：{function}</cyan> | <cyan>行号：{line}</cyan> - | <level> msg：{message}</level>")
            format="<level>{time:YYYY-MM-DD HH:mm:ss.SSS} | {level} | 进程号： {process} | 线程号：{thread} | 模块名：{file} | 方法：{function} | 行号：{line} - | msg：{message}</level>")



    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(Loggings, cls).__new__(cls, *args, **kwargs)

        return cls.__instance

    def info(self, msg):
        return logger.info(msg)

    def debug(self, msg):
        return logger.debug(msg)

    def warning(self, msg):
        return logger.warning(msg)

    def error(self, msg):
        return logger.error(msg)

    def critical(self,msg):
        return logger.critical(msg)

    def notify(self):
        '''
        结合提醒Loguru 可以轻松地与强大的库（必须单独安装）结合使用notifiers，以便在程序意外失败时接收电子邮件或发送许多其他类型的通知。
        :return:
        '''
        pass
        #TODO

loggings = Loggings()


if __name__ == '__main__':
    logger.info('test')
    # print(1/0)



    pass
    # @logger.catch
    # def my_function(x, y, z):
    #     # An error? It's caught anyway!
    #     return 1 / (x + y + z)
    #
    # my_function(0,0,0)
