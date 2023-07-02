# 引言

`break` 是一个控制流语句，用于在循环中提前终止循环，即使循环条件仍然为 `True`。当 `break` 语句被执行时，循环会立即停止，并且程序会继续执行循环之后的代码。

在 Python 中，`break` 主要用于 `while` 循环和 `for` 循环中，其用法和效果有所不同。

## 在while循环中使用break

```python 
while condition:
    # 循环体代码块
    if some_condition:
        break
    # 其他代码
    
- condition 是 while 循环的条件表达式，只要该条件为 True，循环将一直执行。
- 在循环体内，我们可以使用 if 条件语句来检查某些条件 some_condition。
- 如果满足 some_condition，我们使用 break 语句来立即终止整个 while 循环，无论 condition 是否为 True。    
```

**代码实例**

```python
# 当i循环到5时，停止当前循环
i = 0
while i <10:
    i += 1
    print(i)
    if i == 5:
        break
        
>>>
1
2
3
4
5
```

## 在for循环中使用break

```python 
for element in iterable:
    # 循环体代码块
    if some_condition:
        break
    # 其他代码
    
- iterable 是一个可迭代对象，for 循环会遍历该对象的元素。
- 在循环体内，我们同样可以使用 if 条件语句来检查某些条件 some_condition。
- 如果满足 some_condition，我们使用 break 语句来立即终止整个 for 循环，即使可迭代对象中还有未遍历的元素。
```

**代码实例**

```python
numbers = [2, 4, 6, 8, 10, 12]
target = 8

for num in numbers:
    if num == target:
        print("Target found!")
        break
    print("Checking:", num)

print("Loop ended.")

>>>
Checking: 2
Checking: 4
Checking: 6
Target found!
Loop ended.
```

# continue

`continue` 是另一个控制流语句，它用于跳过当前循环的剩余部分，继续执行下一次循环。当程序执行到 `continue` 语句时，它会立即停止当前循环的执行，并回到循环的起始位置，检查循环条件，然后决定是否继续执行下一次循环。

## 在while中使用continue

```python 
while condition:
    # 循环体代码块
    if some_condition:
        continue
    # 其他代码
    
- condition 是 while 循环的条件表达式，只要该条件为 True，循环将一直执行。
- 在循环体内，我们可以使用 if 条件语句来检查某些条件 some_condition。
- 如果满足 some_condition，我们使用 continue 语句来跳过当前循环的剩余代码，立即执行下一次循环，而不会执行 continue 之后的代码。    
```

**代码实例**

```python 
i = 0
while i <=5:
    i+=1
    if i == 3:
        continue
    print(i)
    
>>>
1
2
4
5
6
```

## 在for循环中使用continue

```python 
for element in iterable:
    # 循环体代码块
    if some_condition:
        continue
    # 其他代码
    
- iterable 是一个可迭代对象，for 循环会遍历该对象的元素。
- 在循环体内，我们同样可以使用 if 条件语句来检查某些条件 some_condition。
- 如果满足 some_condition，我们使用 continue 语句来跳过当前循环的剩余代码，立即执行下一次循环，而不会执行 continue 之后的代码。    
```

**代码实例**

```python 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    if num % 2 == 0:
        continue
    print("Current number:", num)

print("Loop ended.")

>>>
Current number: 1
Current number: 3
Current number: 5
Current number: 7
Current number: 9
Loop ended.
```

# break和continue的区别

## 功能不同

- `break`: 当执行到 `break` 语句时，循环会立即终止，不管循环条件是否满足。程序会跳出整个循环，继续执行循环后的代码。
- `continue`: 当执行到 `continue` 语句时，循环会跳过当前迭代的剩余部分，并直接进入下一次迭代。循环会继续执行，不会提前终止循环。

## 循环的范围不同

- `break`: `break` 语句影响到包含它的最近的 `while` 循环或 `for` 循环，使得整个循环终止。
- `continue`: `continue` 语句影响到包含它的最近的 `while` 循环或 `for` 循环，使得当前迭代被跳过，立即开始下一次迭代

## 使用的场景不同

- `break`: 适用于当满足某个条件时，立即终止整个循环的情况。例如，在查找特定元素时，找到目标后就可以停止循环，不需要继续遍历剩余元素。
- `continue`: 适用于当满足某个条件时，跳过当前迭代，继续进行下一次迭代的情况。例如，在处理一个列表时，某些元素满足条件不需要进行处理，可以跳过它们，继续处理其他元素。

