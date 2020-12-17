### Python 中的lambda表达式执行多个函数或者多条命令

Python中的lambda表达式限制只能执行一条命令，所以如果我们想要使用lambda表达式执行多条命令或者函数，就需要使用元祖或者列表进行包装。

为了可读性，尽量避免采用这种方式。

##### 使用lambda函数执行多个函数
```python
# 定义供lambda调用的函数
def printHello():
    print("hello world")


def printHello2(name):
    print("hello {}".format(name))


# 定义函数，方便后续调用
fun = lambda: (
    print(1),
    print(2),
    printHello(),	# 可以通过函数名()的方式执行函数
    printHello2(name="weilinlin")
)
```

##### 执行函数，并输出函数的返回值，

```python
# 定义供lambda调用的函数
def printHello():
    print("hello world")


def printHello2(name):
    print("hello {}".format(name))


# 定义函数，方便后续调用
fun = lambda: (
    print(1),
    print(2),
    printHello(),	# 可以通过函数名()的方式执行函数
    printHello2(name="weilinlin")
)

# 还可以通过print(fun())的形式返回lambda表达式执行的返回值
print(fun())

# 执行结果结果
"""
1
2
hello world
hello weilinlin
(None, None, None, None)
"""
```
