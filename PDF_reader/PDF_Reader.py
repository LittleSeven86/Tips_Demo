"""
 #!/usr/bin/env python
 # -*- coding:utf-8 -*-
 @Author: Little Seven
 @FileName: PDF_Reader.py
 @DateTime: 2023/6/13 14:14
 @SoftWare: PyCharm
"""
from pypdf import PdfReader

def pdf_reader(file_path:str,page_num):
    reader = PdfReader(file_path)
    extract = reader.pages[page_num]
    return extract.extract_text()

if __name__ == '__main__':
    print(pdf_reader('../Books/pytest测试实战_ocr.pdf',4))
