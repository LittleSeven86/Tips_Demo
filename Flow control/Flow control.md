# 流程控制语句

在程序执行过程中,各条语句执行顺序会影响程序的结果，"流程控制语句就是控制语句的执行顺序",可以实现，用户需要的结果，

基本结构有三种：

- 顺序结构
- 选择(分支、条件)结构
- 循环结构

## 顺序结构

顺序结构就是按照代码出现出现的位置执行的`自上而下`

```python
#研发一款简易计算器
print('<-欢迎使用简易计算器->'.center(20,'*'))
n1 = float(input('请输入第一个数：'))
n2 = float(input('请输入第二个数：'))
result = n1 + n2
print(f'{n1}+{n2}={result}')
print('计算完成，byebye'.center(20,'+'))
```

## 选择结构

根据"条件"是否成功，选择相应的"选择"分支

Python中有3种选择结构：

- 单分支选择结构
- 双分支选择结构
- 多分支选择结构
- 嵌套

### 单分支选择结构

**语法格式：**

```python
if True:
    print(True)
    
#案例03:获取键盘输入的2个整数，输出较大的数
num1 = int(input('输入第一个数：'))
num2 = int(input('请输入第二个数：'))
max_num = num1
if max_num < num2:
    max_num = num2
print('较大的数是：%d'%max_num)

#案例05：获取键盘输入的数据（正整数、负整数），求该数的绝对值
num1 = int(input('请输入第一个数：'))
if num1 <0:
    num1 = -num1
print(f'num1绝对值是:{num1}')

>> num1 = -num1 if num1< 0 else num1
```

### 双分支选择结构

**当条件为真时,执行语句段1,当条件为假时,执行语句段2**

```python
if 条件：
    语句段1
else：
    语句段2
#案例02：获取键盘输入的整数年龄age，判断是都可以上网（18），给出提示信息，
age = int(input('请输入您的年龄：'))
if age >= 18:
    print('可以上网')
else:
    print('不能上网')
```

### 多分支结构

```python
语法格式：
if 条件：
    语句段1
elif 条件2：
    语句段2
elif 条件3：
    语句段3
......
else:
语句段n
#案例01：根据每月工资sal，选择不同的交通工具上班
sal = float(input('请输入您的月工资：'))
if sal < 1000:
    print(f'{sal},你走路上班吧')
elif 1000 <= sal <= 3000:
    print(f'{sal}块钱，你做公交上班吧。')
elif 3001 <= sal <= 5000:
    print(f'{sal}块钱，你做高铁上班吧。')
elif 5001 <= sal <= 8000:
    print(f'{sal}块钱，你做飞机上班吧。')        
```

### 选择结构嵌套使用

```python
使用方式：
if 条件1：
    语句段1
    if 条件2：
        语句段2
    elif 条件3：
        语句段3
#案例：获取键盘输入的三角形三遍的长度，判断能否组成三角形
n1 = int(input('请输入第一条边长度：'))
n2 = int(input('请输入第二条边长度：'))
n3 = int(input('请输入第三条边长度：'))
if n1 >0 and n2 > 0 and n3 >0:
    if n1+n2 > n3 and n1+n2 > n2 and n2+n3 > n1:
        print('可以组成普通三角形')
        if n1 == n2 or n2 == n3 or n3 == n1:
            print('等腰三角形')
        elif n1 == n2 == n3:
            print('等边三角形')
        elif n1*n1 + n2*n2 == n3*n3 or n2*n2 + n3*n3 == n1*n1 or n1*n1 + n3*n3 == n2*n2 :
            print('直角三角形')
    else:
        print('两边之和要大于第三边')
else:
    print('请输入正确的数据')   
```






```