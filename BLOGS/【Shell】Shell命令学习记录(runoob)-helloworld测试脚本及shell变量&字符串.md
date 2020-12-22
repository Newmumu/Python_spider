# 【Shell】Shell命令学习记录(runoob)-helloworld测试脚本及shell变量&字符串

## 第一个shell脚本

#### shell脚本示例01

Shell 编程跟 JavaScript、php 编程一样，只要有一个能编写代码的文本编辑器和一个能解释执行的脚本解释器就可以了。

Linux 的 Shell 种类众多，常见的有：

- Bourne Shell（/usr/bin/sh或/bin/sh）
- Bourne Again Shell（/bin/bash）
- C Shell（/usr/bin/csh）
- K Shell（/usr/bin/ksh）
- Shell for Root（/sbin/sh）

```bash
#! /bin/bash
echo "hello world!"
```

**#!** 是一个约定的标记，它告诉系统这个脚本需要什么解释器来执行，即使用哪一种 Shell。

#### 执行shell脚本示例01

1. 作为可执行程序执行
```bash
chmod +x ./test.sh 		# 使脚本具有执行权限
./test.sh 	# 执行脚本
```

2. 作为解释器参数执行
```bash
/bin/sh test.sh
or 
bin/php test.php
```
这种方式运行的脚本，不需要在第一行指定解释器信息，写了也没用。


## Shell变量

#### 定义规则

- 变量名不加美元符号 $
如：
```bash
name="runoob.com"
```
- 命名只能使用英文字母，数字和下划线，首个字符不能以数字开头。
- 中间不能有空格，可以使用下划线（_）。
- 不能使用标点符号。
- 不能使用bash里的关键字（可用help命令查看保留关键字）。

#### 使用变量

- 使用一个定义过的变量，只要在变量名前面加美元符号即可;
```bash
name="weilin"
echo $name
```
- 变量名外面的花括号是可选的，加不加都行，加花括号是为了帮助解释器识别变量的边界;
```bash
for skill in Ada Coffe Action Java; do
    echo "I am good at ${skill}Script"
done
```
- 已定义的变量可以被重新定义
```bash
name="tom"
echo $nam
name="Lisa"
echo $name
```

#### 只读变量

- 使用 **readonly** 命令可以将变量定义为只读变量，只读变量的值不能被改变。
错误示例：
```bash
#! /bin/bash
Url="https://www.baidu.com"
readonly Url
Url="https://pypi.douban.com/simple"
```
运行脚本，结果如下：
```bash
/bin/sh: NAME: This variable is read only.
```

#### 删除变量

- 使用 **unset** 命令可以删除变量。
```bash
unset variable_name
```
- 变量删除后就不能再被使用。unset不能删除只读变量。
```bash
Url="https://www.baidu.com"
unset Url
echo Url
```
以上程序没有输出。

#### 变量类型

运行shell时，会同时存在三种变量：

- 1) 局部变量 局部变量在脚本或命令中定义，仅在当前shell实例中有效，其他shell启动的程序不能访问局部变量。
- 2) 环境变量 所有的程序，包括shell启动的程序，都能访问环境变量，有些程序需要环境变量来保证其正常运行。必要的时候shell脚本也可以定义环境变量。
- 3) shell变量 shell变量是由shell程序设置的特殊变量。shell变量中有一部分是环境变量，有一部分是局部变量，这些变量保证了shell的正常运行。

## Shell 字符串

字符串是shell编程中最常用最有用的数据类型（除了数字和字符串，也没啥其它类型好用了），字符串可以用单引号，也可以用双引号，也可以不用引号。

#### 单引号
```bash
name = 'this is someone name'
```
单引号字符串的限制：

- 单引号里的任何字符都会原样输出，单引号字符串中的变量是无效的；
- 单引号字串中不能出现单独一个的单引号（对单引号使用转义符后也不行），但可成对出现，作为字符串拼接使用。

#### 双引号
```bash
name='runoob'
str="Hello, I know you are \"$name\"! \n"
echo -e $str
```
输出结果为：
```bash
Hello, I know you are "runoob"! 
```
双引号的优点：

- 双引号里可以有变量
- 双引号里可以出现转义字符

#### 拼接字符串
```bash
your_name="runoob"
# 使用双引号拼接
greeting="hello, "$your_name" !"
greeting_1="hello, ${your_name} !"
echo $greeting  $greeting_1
# 使用单引号拼接
greeting_2='hello, '$your_name' !'
greeting_3='hello, ${your_name} !'
echo $greeting_2  $greeting_3
```
结果为：
```bash
hello, runoob ! hello, runoob !
hello, runoob ! hello, ${your_name} !
```

#### 获取字符串长度
```bash
string="abcd"
echo ${#string} #输出 4
```

#### 提取子字符串
以下实例从字符串第 2 个字符开始截取 4 个字符：
```bash
string="runoob is a great site"
echo ${string:1:4} # 输出 unoo
```
注意：第一个字符的索引值为 0。

#### 查找子字符串
查找字符 i 或 o 的位置(哪个字母先出现就计算哪个)：
```bash
string="runoob is a great site"
echo `expr index "$string" io`  # 输出 4
```
注意： 以上脚本中 \` 是反引号，而不是单引号 '，不要看错了哦。

#### expr命令的其他使用场景

expr命令是一个手工命令行计数器，用于在UNIX/LINUX下求表达式变量的值，一般用于整数值，也可用于字符串。

###### 语法

```bash
expr 表达式
```

###### 表达式说明:

- 用空格隔开每个项；
- 用反斜杠 \ 放在 shell 特定的字符前面；
- 对包含空格和其他特殊字符的字符串要用引号括起来

###### 实例

1、计算字串长度
```bash
expr length “this is a test”
14
```
2、抓取字串
```bash
expr substr “this is a test” 3 5
is is
```
3、抓取第一个字符数字串出现的位置
```bash
expr index "sarasara"  a
2
```
4、整数运算
```bash
expr 14 % 9
5
expr 10 + 10
20
expr 1000 + 900
1900
expr 30 / 3 / 2
5
expr 30 \* 3 (使用乘号时，必须用反斜线屏蔽其特定含义。因为shell可能会误解显示星号的意义)
90
expr 30 * 3
expr: Syntax error
```


## Shell 数组

bash支持一维数组（不支持多维数组），并且没有限定数组的大小。

类似于 C 语言，数组元素的下标由 0 开始编号。获取数组中的元素要利用下标，下标可以是整数或算术表达式，其值应大于或等于 0。

#### 定义数组
在 Shell 中，用**括号**来表示数组，数组元素用**"空格"**符号分割开。定义数组的一般形式为：

数组名=(值1 值2 ... 值n)
例如：
```bash
array_name=(value0 value1 value2 value3)
或者

array_name=(
value0
value1
value2
value3
)
还可以单独定义数组的各个分量：

array_name[0]=value0
array_name[1]=value1
array_name[n]=valuen
可以不使用连续的下标，而且下标的范围没有限制。
```

#### 读取数组

读取数组元素值的一般格式是：
```bash
${数组名[下标]}
```
如：
```bash
value=${array_name[n]}
```
使用**@**符号可以获取数组中的所有元素，如：
```bash
echo ${array_name[@]}
```

#### 获取数组长度

获取数组长度的方法和获取字符串长度的方法相同，如：
```bash
# 取得数组元素的个数
length=${#array_name[@]}
# 或者
length=${#array_name[*]}
# 取得数组单个元素的长度(第n+1个元素的长度)
lengthn=${#array_name[n]}
```

## Shell 注释

以 # 开头的行就是注释，会被解释器忽略。

通过每一行加一个 # 号设置多行注释，像这样：
```bash
#--------------------------------------------
# 这是一个注释
# author：菜鸟教程
# site：www.runoob.com
# slogan：学的不仅是技术，更是梦想！
#--------------------------------------------
##### 用户配置区 开始 #####
#
#
# 这里可以添加脚本描述信息
# 
#
##### 用户配置区 结束  #####
```

ps:
如果在开发过程中，遇到大段的代码需要临时注释起来，过一会儿又取消注释，怎么办呢？

每一行加个#符号太费力了，可以把这一段要注释的代码用一对花括号括起来，定义成一个函数，没有地方调用这个函数，这块代码就不会执行，达到了和注释一样的效果。

多行注释
多行注释还可以使用以下格式：
```bash
:<<EOF
注释内容...
注释内容...
注释内容...
EOF
EOF 也可以使用其他符号:

:<<'
注释内容...
注释内容...
注释内容...
'

:<<!
注释内容...
注释内容...
注释内容...
!
```

#### 测试实例
```bash
array_name=(value0 value1 value2 value3 value4)

array_name2=(
value222
value111
)

array_name3[0]=vlaue001
array_name3[2]=value003

# 输出array_name数组第0个元素内容
echo ${array_name[0]}
# 输出array_name数组第0个元素的长度
echo ${#array_name[0]}
# 输出array_name2数组的元素数量
echo ${#array_name2[@]}

# 提取子字符串
string='runoob is a great site.'
echo ${string:1:4}

# 查找子字符串
string="runoob is a great site"
echo `expr index "$string" io`  # 输出 4, expr 命令执行index进行下标统计时，字符串下标从1开始

# 测试多行注释
:<<zhishi
你好我好大家好
是的测试发送大声道f阿斯蒂芬as
阿斯蒂芬asdfa
zhishi

:<<1
kkskfdkdsfa
adsfsakdf
asdfkasdf
1

{
echo "good"
echo "nice"
}
```

result:
```bash
value0
6
2
unoo
4
good
nice
```
