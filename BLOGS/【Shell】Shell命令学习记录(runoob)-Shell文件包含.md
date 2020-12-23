# 【Shell】Shell命令学习记录(runoob)-Shell文件包含

## Shell 文件包含

和其他语言一样，Shell 也可以包含外部脚本。这样可以很方便的封装一些公用的代码作为一个独立的文件。

文件包含，即文件引用，类似于python中的库文件引用！

Shell 文件包含的语法格式如下：

```bash
. filename   # 注意点号(.)和文件名中间有一空格

或

source filename
```

#### 实例

创建两个shell脚本文件

test1.sh代码如下：
```bash
#! /bin/bash
# author: weilinlin
# url: localhost:5000

url="https://www.baidu.com"
```

test2.sh代码如下：
```bash
#! /bin/bash
# author: weilinlin
# url: localhost:5000

# 使用 . 号引用test1.sh文件
. ./test1.sh

# 或使用以下方式引用test1.sh文件
# source ./test1.sh

echo "baidu官方地址: $url"
```

```
# 查看test1.sh文件内容
$ cat test1.sh
url="https://www.baidu.com"

# 查看test2.sh文件内容
$ cat test2.sh
. ./test1.sh

echo "baidu官方地址为: $url"

# 执行test2.sh
$ sh ./test2.sh
baidu官方地址为: https://www.baidu.com
```

**注意：** 被包含的文件 test1.sh 不需要可执行权限。
