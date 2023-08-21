"""
 #!/usr/bin/env python
 # -*- coding:utf-8 -*-
 @Author: Little Seven
 @FileName: pyyaml.py
 @DateTime: 2023/8/21 15:20
 @SoftWare: PyCharm
"""
import os
import yaml.scanner


from Utils.loguru_demo import logger

class GetYamlData:
    """ 获取 yaml 文件中的数据 """
    def __init__(self, file_dir:str):
        self.file_dir = str(file_dir)
    @logger.catch
    def get_yaml_data(self) -> dict:
        """
        获取 yaml 中的数据
        :param: fileDir:
        :return:
        """
        # 判断文件是否存在
        if os.path.exists(self.file_dir):
            data = open(self.file_dir, 'r', encoding='utf-8')
            res = yaml.load(data, Loader=yaml.FullLoader)
            logger.info(f'测试用例参数：{res}')
        else:
            # raise FileNotFoundError(f"文件路径{self.file_dir}不存在")
            raise FileNotFoundError(f"文件路径{self.file_dir}不存在")
        return res
    @logger.catch
    def write_yaml_data(self, key: str, value) -> int:
        """
        更改 yaml 文件中的值, 并且保留注释内容
        :param key: 字典的key
        :param value: 写入的值
        :return:
        """
        with open(self.file_dir, 'r', encoding='utf-8') as file:
            # 创建了一个空列表，里面没有元素
            lines = []
            for line in file.readlines():
                if line != '\n':
                    lines.append(line)
            file.close()

        with open(self.file_dir, 'w', encoding='utf-8') as file:
            flag = 0
            for line in lines:
                left_str = line.split(":")[0]
                if key == left_str and '#' not in line:
                    newline = f"{left_str}: {value}"
                    line = newline
                    file.write(f'{line}\n')
                    flag = 1
                else:
                    file.write(f'{line}')
            file.close()
            return flag


class GetCaseData(GetYamlData):
    """ 获取测试用例中的数据 """

    def get_different_formats_yaml_data(self) -> list:
        """
        获取兼容不同格式的yaml数据
        :return:
        """
        res_list = []
        for i in self.get_yaml_data():
            res_list.append(i)
        return res_list

    def get_yaml_case_data(self):
        """
        获取测试用例数据, 转换成指定数据格式
        :return:
        """
        # TODO
        pass

case_data = GetCaseData('demo_11.yml')
res= case_data.get_yaml_data()
print(res)