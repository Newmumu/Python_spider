# 【Shell】Shell命令学习记录(runoob)-echo命令&printf命令&test命令

## Shell echo命令

Shell 的 echo 指令与 PHP 的 echo 指令类似，都是用于字符串的输出。命令格式：
```bash
echo string
```
#### 1.显示普通字符串:

```bash
echo "It is a test"
```
这里的双引号完全可以省略，以下命令与上面实例效果一致：
```bash
echo It is a test
```


#### 2.显示转义字符

```bash
echo "\"It is a test\""
```
结果将是:
```bash
"It is a test"
```
同样，双引号也可以省略


#### 3.显示变量

read 命令从标准输入中读取一行,并把输入行的每个字段的值指定给 shell 变量
```bash
read name 	# 从输入框中接收输入变量
echo "$name It is a test"
```

以上代码保存为 test.sh，name 接收标准输入的变量，结果将是:
```bash
$ sh ./demo.sh
ok,
ok, It is a test
```


#### 4.显示换行
```bash
echo -e "OK! \n" # -e 开启转义
echo "It is a test"
```
输出结果：
```bash
OK!

It is a test
```

```bash
echo "OK! \n" # 没有-e 开启转义时，显示内容为：
echo "It is a test"
```
输出结果：
```bash
OK! \n
It is a test
```


#### 5.显示不换行
```bash
echo -e "OK! \c" # -e 开启转义 \c 不换行
echo "It is a test"
```
输出结果：
```bash
OK! It is a test
```
#### 6.显示结果定向至文件
```bash
echo "It is a test" > myfile
```
查看输出文件
```
$ cat myfile.sh
It is a test.
```


#### 7.原样输出字符串，不进行转义或取变量(用单引号)
```bash
echo '$name\"'
```
输出结果：
```
$name\"
```
#### 8.显示命令执行结果
```bash
echo `date`
```
注意： 这里使用的是反引号 \`, 而不是单引号 '。

结果将显示当前日期
```bash
$ echo `date`
2020年12月22日 15:50:00
```


## Shell printf 命令

printf 命令模仿 C 程序库（library）里的 printf() 程序。<br>
printf 由 POSIX 标准所定义，因此使用 printf 的脚本比使用 echo 移植性好。<br>
printf 使用引用文本或空格分隔的参数，外面可以在 printf 中使用格式化字符串，还可以制定字符串的宽度、左右对齐方式等。默认 printf 不会像 echo 自动添加换行符，我们可以手动添加 \n。<br>

printf 命令的语法：
```bash
printf  format-string  [arguments...]
```

**参数说明**：

- format-string: 为格式控制字符串
- arguments: 为参数列表。

###### example
```bash
$ echo "hello world"
hello world

$ printf "hello world\n"
hello world

```

#### 使用printf格式化输出

```bash
printf "%-10s %-8s %-4s\n" 姓名 性别 体重kg  
printf "%-10s %-8s %-4.2f\n" 郭靖 男 66.1234
printf "%-10s %-8s %-4.2f\n" 杨过 男 48.6543
printf "%-10s %-8s %-4.2f\n" 郭芙 女 47.9876
```
结果
```
$ sh ./demo.sh
姓名     性别   体重kg
郭靖     男      66.12
杨过     男      48.65
郭芙     女      47.99
```

**%s %c %d %f** 都是格式替代符，％s 输出一个字符串，％d 整型输出，％c 输出一个字符，％f 输出实数，以小数形式输出。

**%-10s** 指一个宽度为 10 个字符（- 表示左对齐，没有则表示右对齐），任何字符都会被显示在 10 个字符宽的字符内，如果不足则自动以空格填充，超过也会将内容全部显示出来。

**%-4.2f** 指格式化为小数，其中 .2 指保留2位小数。

example
```bash
# format-string为双引号
printf "%d %s\n" 1 "abc"

# 单引号与双引号效果一样
printf '%d %s\n' 1 "abc"

# 没有引号也可以输出
printf %s abcdef

# 格式只指定了一个参数，但多出的参数仍然会按照该格式输出，format-string 被重用
printf %s abc def

printf "%s\n" abc def

printf "%s %s %s\n" a b c d e f g h i j

# 如果没有 arguments，那么 %s 用NULL代替，%d 用 0 代替
printf "%s and %d \n"
```
result
```bash
1 abc
1 abc
abcdefabcdefabc
def
a b c
d e f
g h i
j  
 and 0
```

#### printf 的转义序列

|序列		|说明|
|-|-|
|\a		|警告字符，通常为ASCII的BEL字符|
|\b		|后退|
|\c		|抑制（不显示）输出结果中任何结尾的换行字符（只在%b格式指示符控制下的参数字符串中有效），而且，任何留在参数里的字符、任何接下来的参数以及任何留在格式字符串中的字符，都被忽略|
|\f		|换页（formfeed）|
|\n		|换行|
|\r		|回车（Carriage return）|
|\t		|水平制表符|
|\v		|垂直制表符|
|\\		|一个字面上的反斜杠字符|
|\ddd	|表示1到3位数八进制值的字符。仅在格式字符串中有效|
|\0ddd	|表示1到3位的八进制值字符|

example【已验证，暂未理解其中的\b 和 \a及\ddd,\0ddd】
```bash
$ printf "a string, no processing:<%s>\n" "A\nB"
a string, no processing:<A\nB>

$ printf "a string, no processing:<%b>\n" "A\nB"
a string, no processing:<A
B>

$ printf "www.runoob.com \a"
www.runoob.com $                  #不换行
```


## Shell test 命令

Shell中的 test 命令用于检查某个条件是否成立，它可以进行数值、字符和文件三个方面的测试。

#### 数值测试
|参数	|说明|
|-|-|
|-eq	|等于则为真|
|-ne	|不等于则为真|
|-gt	|大于则为真|
|-ge	|大于等于则为真|
|-lt	|小于则为真|
|-le	|小于等于则为真|

example
```bash
num1=100
num2=100
if test $[num1] -eq $[num2]
then
    echo '两个数相等！'
else
    echo '两个数不相等！'
fi
```
result
```bash
两个数相等
```

代码中的 [] 执行基本的算数运算，如：

实例
```bash
a=5
b=6

result=$[a+b] # 注意等号两边不能有空格
echo "result 为： $result"
```
result
```bash
result 为： 11
```


#### 字符串测试
|参数			|说明|
|-|-|
|=			|等于则为真|
|!=			|不相等则为真|
|-z 字符串	|字符串的长度为零则为真|
|-n 字符串	|字符串的长度不为零则为真|

```bash
num1="ru1noob"
num2="runoob"
if test $num1 = $num2
then
    echo '两个字符串相等!'
else
    echo '两个字符串不相等!'
fi
```

输出结果：
```
两个字符串不相等!
```



#### 文件测试

|参数			|说明|
|-|-|
|-e 文件名	|如果文件存在则为真|
|-r 文件名	|如果文件存在且可读则为真|
|-w 文件名	|如果文件存在且可写则为真|
|-x 文件名	|如果文件存在且可执行则为真|
|-s 文件名	|如果文件存在且至少有一个字符则为真|
|-d 文件名	|如果文件存在且为目录则为真|
|-f 文件名	|如果文件存在且为普通文件则为真|
|-c 文件名	|如果文件存在且为字符型特殊文件则为真|
|-b 文件名	|如果文件存在且为块特殊文件则为真|

example
```bash
if test -e ./test.sh
then
    echo '文件已存在!'
else
    echo '文件不存在!'
fi
```
result
```bash
文件已存在!
```

另外，Shell 还提供了与( -a )、或( -o )、非( ! )三个逻辑操作符用于将测试条件连接起来，其优先级为： ! 最高， -a 次之， -o 最低。例如：

example
```bash
cd /shDemo	# 切换到当前目录下
ls -1		# 查看当前文件夹中的文件清单
demo.sh
myfile.sh
para.sh
test.sh
```
```bash
if test -e ./test.sh -o -e ./ceshi.sh
then
    echo '至少有一个文件存在!'
else
    echo '两个文件都不存在'
fi
```
result
```bash
至少有一个文件存在!
```
