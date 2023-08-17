"""
 #!/usr/bin/env python
 # -*- coding:utf-8 -*-
 @Author: Little Seven
 @FileName: pydantic_demo.py
 @DateTime: 2023/8/17 11:14
 @SoftWare: PyCharm
"""
import json

from pydantic import BaseModel,Field

class  User(BaseModel):
    id:int
    name:str
    isMale:bool = True

jack = User(id = '123',name = 'jack')
# print(jack.id,type(jack.id))
# print(jack.model_dump())
# print(jack.model_fields_set)
# print(jack.model_dump())
# print(jack.model_dump_json(),type(jack.model_dump_json()))
print(jack.model_json_schema(),type(jack.model_json_schema()))
print(json.dumps(jack.model_json_schema()),type(json.dumps(jack.model_json_schema())))
print(jack.schema_json())
print(jack.model_dump_json(),type(jack.model_dump_json()))

# assert isinstance(jack.id,str),'校验失败'

a = 1,
print(type(a))

from Utils.loguru_demo import loggings

loggings.info('test,这是pandic路径')

