"""
 #!/usr/bin/env python
 # -*- coding:utf-8 -*-
 @Author: Little Seven
 @FileName: VerifyCode.py
 @DateTime: 2023/5/24 16:58
 @SoftWare: PyCharm
"""
from ddddocr import DdddOcr

def recognize():
    ocr = DdddOcr()
    with open('verifycode_image/img_1.png','rb') as f:
        img_bytes = f.read()
        res = ocr.classification(img_bytes)
    print(res)

if __name__ == '__main__':
    recognize()
