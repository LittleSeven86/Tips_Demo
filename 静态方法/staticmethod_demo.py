"""
 #!/usr/bin/env python
 # -*- coding:utf-8 -*-
 @Author: Little Seven
 @FileName: staticmethod_demo.py
 @DateTime: 2023/7/27 10:07
 @SoftWare: PyCharm
"""
class MyClass:
    @staticmethod
    def my_static_method():
        # 静态方法的实现代码
        pass

MyClass.my_static_method()

class StringUtils:
    @staticmethod
    def reverse_string(string):
        return string[::-1]

    @staticmethod
    def count_vowels(string):
        vowels = ['a', 'e', 'i', 'o', 'u']
        count = 0

        for char in string.lower():
            if char in vowels:
                count += 1
        return count


text = "Hello, World!"

reversed_text = StringUtils.reverse_string(text)
print(reversed_text)  # 输出: "!dlroW ,olleH"

vowel_count = StringUtils.count_vowels(text)
print(vowel_count)  # 输出: 3
class FileHandler:
    @staticmethod
    def read_file(file_path):
        with open(file_path, 'r') as file:
            content = file.read()
        return content

    @staticmethod
    def write_file(file_path, content):
        with open(file_path, 'w') as file:
            file.write(content)


file_path = "demo.txt"

# 读取文件内容
file_content = FileHandler.read_file(file_path)
print(file_content)

# 写入新内容到文件中
new_content = "床前明月光"
FileHandler.write_file(file_path, new_content)
print(file_content)

class StringUtils:
    @staticmethod
    def is_palindrome(string):
        cleaned_string = string.lower().replace(" ", "")
        return cleaned_string == cleaned_string[::-1]

    @staticmethod
    def capitalize_words(sentence):
        words = sentence.split()
        capitalized_words = [word.capitalize() for word in words]
        return " ".join(capitalized_words)


text1 = "madam"
is_palindrome = StringUtils.is_palindrome(text1)
print(is_palindrome)  # 输出: True

text2 = "hello world"
capitalized_text = StringUtils.capitalize_words(text2)
print(capitalized_text)  # 输出: "Hello World"

import requests

class WeatherAPI:
    API_URL = "https://api.weather.com"

    @staticmethod
    def get_weather(city):
        endpoint = "/weather"
        params = {
            "city": city,
            "key": "<your-api-key>"
        }

        response = requests.get(WeatherAPI.API_URL + endpoint, params=params)
        data = response.json()

        # 解析并返回天气数据
        temperature = data["temperature"]
        description = data["description"]
        return f"The weather in {city} is {description} with a temperature of {temperature}°C."

res = WeatherAPI.get_weather('nanjing')
pr
