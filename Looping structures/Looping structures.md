## 循环结构

根据条件或者指定的次数,反复执行循环体语句,循环分为2类，

- while循环
- for循环

### while 循环

```python
语法：while循环三要素：
	循环变量初值：
    	循环条件：当条件为真是，执行循环体
    		循环体	循环变量增值：
案例05：
i = 1					//循环变量初值
while i <= 5:			//循环条件
    print('Hello')
    i += 1    			//循环变量增值

#编写一个捐款程序，捐款10000元，计算捐款金额。  
donate = 0
while donate <= 10000:
    money = int(input('请输入捐款金额：'))
    print(f'感谢您捐款{money}元,已募捐金额{money+donate}元')
    donate = donate + money
print('当前捐款总金额%d元'%donate)

#练习01：使用while循环，输出列表中rose元素出现的位置
list01 = [101,'rose',21,'女',89.5,'北京',True]
i = 0
while i <= len(list01)-1:
    if list01[i] == 'rose':
        print(f'rose的下标是{i}')
    i +=1
```

### for循环

for循环通过遍历可迭代对象，来控制循环的执行，每次循环，循环变量都会得到遍历对象中的一个值，在执行循环体语句，当遍历(循环)对象值全部取完时，循环结束,遍历(循环)对象，遍历对象一般是字符串、列表、字典、元祖

```python
'''
for 循环变量 in 遍历对象：
    循环体
'''

#使用for循环，实现1-9的平方
list02 = [1,2,3,4,5,6,7,8,9]
for i in list02:
    print(i*i,end=' ')   

#案例：使用for循环，输出字典中的元素
dict01 = {'id':101,'name':'张三','age':25}
for k,v in dict01.items()://输出循环键值对
    print(k,v,end=' ')

for k in dict01.keys()://键
    print(k)

for v in dict.values()://值
    print(v)

#使用for循环，循环输出测试用例数据
cases = [				
    ['login_02','admin','123456',True],
    ['login_03','root','abc123',False],
    ['login_04','root','',False]
]
for data in cases:
    title,username,password,result = data	//对循环结果进行解包
    print(title,username,password,result)

#案例：输出99乘法表
for zuo in range(1,10):
    for you in range(1,zuo+1):
        print(f'{zuo}*{you}={zuo*you}',end=' ')
    print()

zuo = 1
while zuo < 10:
    you = 1
    while you <= zuo:
        print(f'{zuo}*{you}={zuo*you}',end=' ')
        you += 1
    zuo +=1
    print()

#使用双重for循环，输出直角三角形
for i in range(1,9):
    for k in range(1,i+1):
        print('*',end='')
    print()

#练习6、使用列表实现简单的用户登录功能,创建2个列表分别存储用户名(uname)和密码(passwd),使用for循环,循环输入数据,并进行验证
例如:
uname = ['root','admin','rose']
passwd =['123','456','789']
#说明:当用户键盘输入root和密码123时,提示登录成功,否则失败,用户名和密码是对应关系
while True:
    #如果键盘输入的用户名（username）包含在uname列表中
    username = input('请输入您的用户名：')
    password = input('请输入您的密码：')
    if username in uname:
        #获取键盘输入的用户名（username），在uname列表中出现的位置（下标）
        index = uname.index(username)
        #键盘输入的密码password和passwd列表中的密码是否相等
        #键盘是和键盘输入用户名对应的密码
        if password == passwd[index]:
            print('登录成功')
        else:
            print('密码错误')
    #如果键盘输入的用户名（username）不包含在uname列表中
    print('用户名错误')
```

#### range

语法格式：`for i in range(开始，结束，步长)`

- 开始数值：表示从那个书开始，默认为0，可以省略
- 结束数值：表示到哪里结束，不可以取到结束数值，不可以省略
- 步长：每次循环增加的值，可以省略，默认值为1

```python
#案例：使用for循环，循环输出1-9的数字, 使用方法：range(初始数据，结束数据，步长)
for i in range(1,10):
    print(i)
    
#案例：输出*组成的三角形
for i in range(1,6):
    print(' '*(6-i)+'*'*(2*i-1))
#(6-i)*' '	输出空格
#(2*i-1)*'*'	输出*

#练习：将列表中的字符串，首字母大写， 其余字母小写并输出
list01 = ['zhangsan','lisi','WangWu','zhaoliu','TianQI']
list02 = []
for i in list01:
    w = i[0].upper()+i[1:].lower()
    list02.append(w)
print(list02)
```

## break 退出循环

一般将break语句添加在if条件中，作用是退出循环

```python
while 条件：
    循环体
    if 条件：
        break
for 循环变量 in 迭代对象：
    循环体
    if 条件：
        break
#案例：使用while循环，循环到7停止
i = 1
while i < 11:
    i+=1
    if i == 7:
        print(i)
        break
```

## continue	

一般将continue语句放在if中，作用是结束当前循环，返回到循环开始的地方，继续开始下一次循环

```python
#案例：吃到第99个包子，有虫子，不吃了。
i = 1
while i <= 101:
    i+=1
    if i ==99:
        print('有一半虫子')
        continue
    print(f'壮士吃第{i}个包子')
```
