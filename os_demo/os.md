# os

![img:png](https://img-blog.csdnimg.cn/ded0076e90b64ad995e09f06a6a9d78f.png)

## 引言

os模块提供了一种**与操作系统进行交互**的方式，允许执行各种与操作系统相关的任务，如文件和目录操作、进程管理、环境变量访问等，适用于Windows、MacOS、Linux等环境下

## 使用方式

### 导入os模块

在使用之前需要导入os模块

```python 
import os
```

### os.getcwd()

作用：返回当前路径

- Windows的`echo %cd%`
- Linux下的`pwd`

```python
# 获取当前工作目录
print(os.getcwd())  
>>> D:\Python\Tips_Demo\os_demo
```

### os.chdir()

作用：改变当前工作目录

```python
print(os.getcwd())  
>>> D:\Python\Tips_Demo\os_demo

print(os.chdir('../List_Demo'))
print(os.getcwd())  
>>>D:\Python\Tips_Demo\os_demo
```

### os.listdir()

作用：指定返回有文件和目录组成的列表

- Windows: `dir`
- Linux: `ls`

```python 
print(os.listdir())	
>>> ['1', 'os.md', 'os_demo.py', '__init__.py']
```

### os.walk()

作用：用于遍历目录中的所有文件和子目录。它返回一个生成器对象，通过迭代器的方式依次返回每个目录下的文件和子目录

```python 
# 展示如何使用os.walk来遍历目录并打印所有文件的路径
directory_path = "../os_demo"

for root, directories, files in os.walk(directory_path):
    for file in files:
        file_path = os.path.join(root, file)
        print(file_path)
        
>>>
../os_demo\os.md
../os_demo\os_demo.py
../os_demo\__init__.py
../os_demo\1\test.txt
```

### os.path.exists()

作用：判断当前路径是否存在，返回`bool`类型

```python 
print(os.path.exists('../os_demo'))

>>>
True
```

### os.mkdir()

作用：创建目录

```python
print(os.listdir())
>>> ['1', 'os.md', 'os_demo.py', '__init__.py']

print(os.mkdir('test_add_dir'))
print(os.listdir())
>>> ['1', 'os.md', 'os_demo.py', 'test_add_dir', '__init__.py']
```

### os.mkdirs()

作用：递归生成目录，功能与Linux中的`mkdir -p`一致

```python 
print(os.makedirs('test_-p_dir/1/2'))
```

### os.rmdir()

作用：删除对应路径下目录

```python 
print(os.rmdir('test_-p_dir/1/2'))
```

### os.remove()

作用：删除对应路径下的文件

```python
print(os.listdir('1'))
>>> ['test.txt']

os.remove('1/test.txt')
print(os.listdir('1'))
>>> []
```

### os.path.join()

作用：用于拼接路径，会**自动根据操作系统的规范添加正确的路径分隔符**（反斜杠 `\` 在 Windows 上，正斜杠 `/` 在类 Unix 系统上）

```python 
directory = "../os_demo"
filename = "静夜思.txt"

file_path = os.path.join(directory, filename)
print(file_path)

>>>
../os_demo\静夜思.txt
```

### os.path.split()

作用：用于将路径分割为目录部分和文件部分，返回一个包含目录和文件的元组。

基本语法：

```python 
directory, filename = os.path.split(path)

- path是要分割的路径
- path 是文件路径，则 directory 是该文件所在的目录路径，而 filename 将是该文件的名称
- path 是一个目录路径，则 directory 是该目录的父目录路径，而 filename 将是空字符串。
```

```python
# path 是文件路径
dir,filename = os.path.split('test_add_dir/静夜思')
print(dir,filename)

# path是目录路径
dir,filename = os.path.split('test_add_dir')
print(dir,filename)
```

### os.dirname()

作用：用于获取给定路径的目录部分

```python
directory = os.path.dirname(path)
```

```python 
# 目录路径
print(os.path.dirname('../os_demo/test_add_dir'))
>>>
../os_demo
```

### os.path.isdir()

作用：判断当前路径下是否为目录

```python 
print(os.path.isdir('../os_demo/os_demo.py'))
print(os.path.isdir('../os_demo/test_add_dir'))

>>>
False
True
```

### os.path.isfile()

作用：判断当前路径是否为目录

```python 
print(os.path.isfile('../os_demo/os_demo.py'))
print(os.path.isfile('../os_demo/test_add_dir'))

>>>
True
False
```

### os.system()

作用：用于在操作系统中执行命令，接受一个字符串参数，表示要执行的命令，然后在操作系统的命令行中运行该命令,并返回命令的退出码,退出码用于指示命令是否成功执行，通常为 0 表示成功，非零值表示错误或异常。

```python
import os

command = "echo Hello, World!"

exit_code = os.system(command)
print("命令退出码：", exit_code)

>>>
Hello, World!
0
```

### os.getpid()

作用：用于获取当前进程的进程 ID（Process ID）。

```python
pid = os.getpid()
print("进程 ID：", pid)

time.sleep(10)

>>>
9520  # 可在任务管理器中查看pid对应进程信息
```

### os.path.getsize()

作用：获取指定路径下文件的大小（以字节为单位）

```python 
print(os.path.getsize('os.md'))

>>>3765
```

