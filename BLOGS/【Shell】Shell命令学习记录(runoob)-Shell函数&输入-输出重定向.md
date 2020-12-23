# 【Shell】Shell命令学习记录(runoob)-Shell函数&输入-输出重定向

## Shell 函数

linux shell 可以用户定义函数，然后在shell脚本中可以随便调用。

shell中函数的定义格式如下：

```bash
[ function ] funname [()]
{
    action;
    [return int;]
}
```

说明：

- 1、可以带function fun() 定义，也可以直接fun() 定义,不带任何参数。
- 2、参数返回，可以显示加：return 返回，如果不加，将以最后一条命令运行结果，作为返回值。 return后跟数值n(0-255

下面的例子定义了一个函数并进行调用：
```bash
demoFun(){
    echo "这是我的第一个 shell 函数!"
}
echo "-----函数开始执行-----"
demoFun
echo "-----函数执行完毕-----"
```
输出结果
```
-----函数开始执行-----
这是我的第一个 shell 函数!
-----函数执行完毕-----
```

下面定义一个带有return语句的函数：
```bash
funWithReturn(){
    echo "这个函数会对输入的两个数字进行相加运算..."
    echo "输入第一个数字: "
    read aNum
    echo "输入第二个数字: "
    read anotherNum
    echo "两个数字分别为 $aNum 和 $anotherNum !"
    return $(($aNum+$anotherNum))
}
funWithReturn
echo "输入的两个数字之和为 $? !"		# $? 获取上一条命令执行的返回值
```

输出结果：
```bash
这个函数会对输入的两个数字进行相加运算...
输入第一个数字: 
1
输入第二个数字: 
2
两个数字分别为 1 和 2 !
输入的两个数字之和为 3 !
```

函数返回值在调用该函数后通过 $? 来获得。

注意：所有函数在使用前必须定义。这意味着必须将函数放在脚本开始部分，直至shell解释器首次发现它时，才可以使用。调用函数仅使用其函数名即可。

函数参数
在Shell中，调用函数时可以向其传递参数。在函数体内部，通过 $n 的形式来获取参数的值，例如，$1表示第一个参数，$2表示第二个参数...

带参数的函数示例：
```bash
funWithParam(){
    echo "第一个参数为 $1 !"
    echo "第二个参数为 $2 !"
    echo "第十个参数为 $10 !"
    echo "第十个参数为 ${10} !"
    echo "第十一个参数为 ${11} !"
    echo "参数总数有 $# 个!"
    echo "作为一个字符串输出所有参数 $* !"
}
funWithParam 1 2 3 4 5 6 7 8 9 34 73
```

输出结果：
```bash
第一个参数为 1 !
第二个参数为 2 !
第十个参数为 10 !
第十个参数为 34 !
第十一个参数为 73 !
参数总数有 11 个!
作为一个字符串输出所有参数 1 2 3 4 5 6 7 8 9 34 73 !
```

注意，$10 不能获取第十个参数，获取第十个参数需要${10}。当n>=10时，需要使用${n}来获取参数。

另外，还有几个特殊字符用来处理参数：

|参数处理	|说明|
|-|-|
|$#		|传递到脚本或函数的参数个数|
|$*		|以一个单字符串显示所有向脚本传递的参数|
|$$		|脚本运行的当前进程ID号|
|$!		|后台运行的最后一个进程的ID号|
|$@		|与$*相同，但是使用时加引号，并在引号中返回每个参数。|
|$-		|显示Shell使用的当前选项，与set命令功能相同。|
|$?		|显示最后命令的退出状态。0表示没有错误，其他任何值表明有错误。|

$? 仅对其上一条指令负责，一旦函数返回后其返回值没有立即保存入参数，那么其返回值将不再能通过 $? 获得。




## Shell 输入/输出重定向


大多数 UNIX 系统命令从你的**终端**接受输入并将所产生的输出**发送回​​到您的终端**。<br>
一个命令通常从一个叫标准输入的地方读取输入，默认情况下，这恰好是你的终端。<br>
同样，一个命令通常将其输出写入到标准输出，默认情况下，这也是你的终端。<br>

|命令				|说明|
|-|-|
|command > file	|将输出重定向到 file。|
|command < file	|将输入重定向到 file。|
|command >> file	|将输出以追加的方式重定向到 file。|
|n > file		|将文件描述符为 n 的文件重定向到 file。|
|n >> file		|将文件描述符为 n 的文件以追加的方式重定向到 file。|
|n >& m			|将输出文件 m 和 n 合并。|
|n <& m			|将输入文件 m 和 n 合并。|
|<< tag			|将开始标记 tag 和结束标记 tag 之间的内容作为输入。|

需要注意的是文件描述符 0 通常是标准输入（STDIN），1 是标准输出（STDOUT），2 是标准错误输出（STDERR）。

### 输出重定向

重定向一般通过在命令间插入特定的符号来实现。特别的，这些符号的语法如下所示:

```bash
command1 > file1
```

上面这个命令执行command1然后将输出的内容存入file1。

注意任何file1内的已经存在的内容将被新内容替代。如果要将新内容添加在文件末尾，请使用>>操作符。

example:

执行下面的 who 命令，它将命令的完整的输出重定向在用户文件中(users):
```bash
ps -ef | grep 'bash' > logs		# 覆盖方式进行输出重定向
```

执行后，并没有在终端输出信息，这是因为输出已被从默认的标准输出设备（终端）重定向到指定的文件。

你可以使用 cat 命令查看文件内容：
```
cat logs
wWX75689   22480   31372 pty0     20:10:00 /usr/bin/bash
wWX75689   20804   22480 pty0     20:31:48 /usr/bin/bash
```

如果不希望文件内容被覆盖，可以使用 >> 追加到文件末尾，

```bash
ps -ef | grep 'bash' >> logs		# 追加方式进行输出重定向
```

### 输入重定向

和输出重定向一样，Unix 命令也可以从文件获取输入，语法为：
```bash
command1 < file1
```

example:
```bash
$ wc -l logs
5 logs
```

```bash
$ wc -l < logs
5
```

两者的不同在于：第一个例子会输出文件名；第二个例子不会输出文件名，它仅仅从标准输入中读取内容；

```bash
command1 <infile> outfile
```

同时替换输入和输出，执行command1，从文件infile读取内容，然后将输出写入到outfile中。

```bash
# 将logs文件作为命令行中的脚本输入参数，logs_backup作为输出重定向文件，直接将logs读取的内容写入到logs_backup中，以下命令等同于命令：cp logs logs_backup
cat < logs > logs_backup
```


### 重定向深入讲解

一般情况下，每个 Unix/Linux 命令运行时都会打开三个文件：

标准输入文件(stdin)：stdin的文件描述符为0，Unix程序默认从stdin读取数据。
标准输出文件(stdout)：stdout 的文件描述符为1，Unix程序默认向stdout输出数据。
标准错误文件(stderr)：stderr的文件描述符为2，Unix程序会向stderr流中写入错误信息。
默认情况下，command > file 将 stdout 重定向到 file，command < file 将stdin 重定向到 file。

如果希望 stderr 重定向到 file，可以这样写：
```bash
$ command 2>file
```

如果希望 stderr 追加到 file 文件末尾，可以这样写：
```bash
$ command 2>>file
```

2 表示标准错误文件(stderr)。

如果希望将 stdout 和 stderr 合并后重定向到 file，可以这样写：
```bash
$ command > file 2>&1
```
或者
```bash
$ command >> file 2>&1
```

如果希望对 stdin 和 stdout 都重定向，可以这样写：
```bash
$ command < file1 >file2

example:
cat < logs > logs_backup
```
command 命令将 stdin 重定向到 file1，将 stdout 重定向到 file2。


### Here Document

Here Document 是 Shell 中的一种特殊的重定向方式，用来将输入重定向到一个交互式 Shell 脚本或程序。

它的基本的形式如下：
```bash
command << delimiter
	document
delimiter
```

它的作用是将两个delimiter之间的内容(document)作为输入传递给command。

PS：
- 结尾的delimiter一定要顶格写，前面不能有任何字符，后面也不能拿有任何字符，包括空格和tab缩进。
- 开始的delimiter前后的空格都会被忽略掉。

example：

命令行中使用**wc -l**命令计算Here Document的行数：

```bash
$ wc -l << EOF
  	  欢迎来到
  	  电影网
  	  dililili.com
EOF

result:
3		# 输出结果为3行
$ 
```

我们也可以将 Here Document 用在脚本中，例如：
```bash
cat << EOF
欢迎来到
电影网
dililili.com
EOF
```

执行以上脚本，输出结果：
```bash
欢迎来到
电影网
dililili.com
```


### /dev/null 文件

如果希望执行某个命令，但又不希望在屏幕上显示输出结果，那么可以将输出重定向到 /dev/null：

```bash
$ command > /dev/null
```

/dev/null 是一个特殊的文件，写入到它的内容都会被丢弃；如果尝试从该文件读取内容，那么什么也读不到。但是 /dev/null 文件非常有用，将命令的输出重定向到它，会起到"禁止输出"的效果。

如果希望屏蔽 stdout 和 stderr，可以这样写：
```bash
$ command > /dev/null 2>&1
```

**注意：**0 是标准输入（STDIN），1 是标准输出（STDOUT），2 是标准错误输出（STDERR）。

这里的 2 和 > 之间不可以有空格，2> 是一体的时候才表示错误输出。
