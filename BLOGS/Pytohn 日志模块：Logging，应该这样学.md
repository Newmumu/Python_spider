### Pytohn 日志模块：Logging，应该这样学

### 前言

Python 中的logging模块用于记录日志，用户可以根据程序实现需要自定义日志输出位置、日志级别以及日志格式。

#### 直接在terminal页面输出日志内容

一个简单的logging模块使用样例，直接打印显示日志内容到屏幕。

##### example
```python
# 默认在屏幕输出的日志级别为 warning及以上级别告警
import logging

logging.critical("critial log")  # 致命缺陷级别日志
logging.error("error log")
logging.warning("warning log")
logging.info("info log")
logging.debug("debug log")
```

##### result
```python
CRITICAL:root:critical log
ERROR:root:error log
WARNING:root:warning log
```

PS：默认情况下python的logging模块将日志打印到标准输出，并且只显示大于等于warning级别的日志（critical > error > warning > info > debug）。

#### 将日志文件输出到文件

将日志事件记录到文件是一种非常常见的情况，方便出现问题时快速定位问题。在logging模块默认配置条件下，记录日志内容，代码如下：

##### example
```python
import logging

logging.basicConfig(filename='example.log',level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
```

##### result
同级目录下新增一个日志文件 example.log，
内容为：
```python
DEBUG:root:This message should go to the log file.
INFO:root:so should this
WARNING:root:and this, too
```

#### 定制日志内容（日志级别、日志格式）

根据程序运行对日志记录的要求，通常需要自定义日志显示格式、输出位置以及日志显示级别。可以通过logging.basicConfig()定制满足自己要求的日志输出格式。

##### example
```python
import logging

logging.basicConfig(format='[%(asctime)s %(filename)s line:%(lineno)d] %(levelname)s: %(message)s', level=logging.DEBUG, filename='log.txt', filemode='a')
logging.debug("This message should appear on the console")
logging.info("and this message should appear on the console, too")
logging.warning("and this,too")
```

##### result
同级目录下新增一个日志文件 log.txt，
内容为：
```python
[2020-12-10 17:37:34,635 loggingDemo.py line:10] DEBUG: This message should appear on the console
[2020-12-10 17:37:34,635 loggingDemo.py line:11] INFO: and this message should appear on the console, too
[2020-12-10 17:37:34,635 loggingDemo.py line:12] WARNING: and this,too
```

```python
PS
通过修改logging.basicConfig()函数中参数取值来定制日志显示。函数参数定义及含义如下：

filename 指定日志写入文件名。
filemode 文件打开方式，默认值为"a"
format 设置日志显示格式
dateft 设置日期时间格式
level 设置显示日志级别
stream 指定stream创建StreamHandler。可以指定输出到sys.stderr，sys.stdout或者文件。默认为sys.stderr。
format参数用到的格式化字符串如下：
%(asctime)s 字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
%(filename)s 调用日志输出函数的模块的文件名
%(levelname)s 文本形式的日志级别
%(funcName)s 调用日志输出函数的函数名
%(lineno)d 调用日志输出函数的语句所在的代码行
%(message)s 用户输出的消息
%(module)s 调用日志输出函数的模块名
```

#### 多模块记录日志

如果开发的程序包含多个模块，考虑日之间的记录方式，

##### example(main.py)

```python
# 将文件和logging测试文件放在同一级目录下
# filename: mylib.py

import time
import logging


def do_something():
    logging.warning("warning log in mylib")
    logging.info("mylib sleep 5 秒")
    time.sleep(5)
    logging.info("mylib finished")
```

```python
import logging
import mylib  # 本地创建的一个文件

def main():
	logging.basicConfig(format='[%(asctime)s %(filename)s line:%(lineno)d] %(levlename)s: %(message)s',
                        level=logging.DEBUG, filename='log2.txt', filemode='a')
    logging.info("Started")
    mylib.do_something()
    logging.info("Finished")
if __name__ == '__main__':
	main()
```

##### result
同级目录下新增一个日志文件 log2.txt，
内容为：
```python
[2020-12-10 17:49:50,857 loggingDemo.py line:14] INFO: Started
[2020-12-10 17:49:50,858 mylib.py line:12] WARNING: warning log in mylib
[2020-12-10 17:49:50,858 mylib.py line:13] INFO: mylib sleep 5 秒
[2020-12-10 17:49:55,860 mylib.py line:15] INFO: mylib finished
[2020-12-10 17:49:55,860 loggingDemo.py line:16] INFO: Finished
```

#### 日志同时输出terminal和输入文件

截止目前，我们实现的日志文件只能输出到屏幕或输入文件中，不能同时输出；

logging模块可以通过FileHander和StreamHandler分别制定向文件和屏幕(控制台)输出。

##### example
```python
import logging

logger = logging.getLogger()  # 不加名称 设置为root logger
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s: - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')

# 使用FileHandler输出到文件
fh = logging.FileHandler('log3.txt')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)

# 使用StreamHandler输出到屏幕(控制台)
sh = logging.StreamHandler()
sh.setLevel(logging.DEBUG)
sh.setFormatter(formatter)

# 添加两个Handler句柄到logger实例中
logger.addHandler(fh)
logger.addHandler(sh)

logger.info("This is info message.")
logger.warning("This is warning message.")
```

##### result
```python
console
2020-12-10 18:00:07 - root - INFO: - This is info message.
2020-12-10 18:00:07 - root - WARNING: - This is warning message.
```

```python
同级目录下新增一个日志文件 log3.txt，
内容为：
2020-12-10 18:00:07 - root - INFO: - This is info message.
2020-12-10 18:00:07 - root - WARNING: - This is warning message.
```

#### 如果修改logger定义语句为：

##### result

```python
console 页面
2020-12-10 19:19:49 - weilinlin - INFO: - This is info message.
2020-12-10 19:19:49 - weilinlin - WARNING: - This is warning message.
```

```python
日志文件中追加输出内容为：
2020-12-10 19:19:49 - weilinlin - INFO: - This is info message.
2020-12-10 19:19:49 - weilinlin - WARNING: - This is warning message.
```
