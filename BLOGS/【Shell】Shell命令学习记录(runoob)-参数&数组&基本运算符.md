# 【Shell】Shell命令学习记录(runoob)-参数&数组&基本运算符

## Shell 传递参数

我们可以在**执行 Shell 脚本**时，向脚本传递参数，脚本内获取参数的格式为：$n。n 代表一个数字，1 为执行脚本的第一个参数，2 为执行脚本的第二个参数，以此类推……(传递参数：即在命令行执行shell语句后加参数)

#### 实例

- 我们在脚本中传递参数时，$0为执行的文件名（包括文件路径）

```bash
echo "Shell 传递参数实例!"
echo "执行的文件名：$0"
echo "first parameter：$1"
echo "second parameter：$2"
echo "third parameter：$3"
```
###### result:
```bash
$ sh para.sh 名字 空格 三餐 siji
Shell 传递参数实例!
执行的文件名：para.sh
first parameter：名字
second parameter：空格
third parameter：三餐
```

- 当传递的参数少于需要的参数数量时，最后的$3取不到值，即为空
- 当传递的参数数量过多时，没有多余的$4，$5用来取值，不会显示
- 当不传递参数的时候，除了运行文件名$0，其他所有的$都取不到值

其他特殊字符处理，脚本中的入参：

|参数处理|	说明|
|-|-|
|$#		|传递到脚本的参数个数|
|$*		|以一个单字符串显示所有向脚本传递的参数。<br>如"$*"用「"」括起来的情况、以"$1 $2 … $n"的形式输出所有参数。|
|$$		|脚本运行的当前进程ID号|
|$!		|后台运行的最后一个进程的ID号|
|$@		|与$*相同，但是使用时加引号，并在引号中返回每个参数。<br>如"$@"用「"」括起来的情况、以"$1" "$2" … "$n" 的形式输出所有参数。|
|$-		|显示Shell使用的当前选项，与set命令功能相同。|
|$?		|显示最后命令的退出状态。0表示没有错误，其他任何值表明有错误。(即上一个命令执行后的返回结果)|

###### example：
```bash
$ cat ./para.sh
echo "Shell 传递参数实例!"
echo "执行的文件名：$0"
echo "first parameter：$1"
echo "second parameter：$2"
echo "third parameter：$3"

echo "parameter count: $#"
echo "一个字符串，显示所有参数: $*"
echo "脚本当前进程号: $$"
echo "后台运行最后一个进程id: $!"		# 当前$!执行结果好像有问题，这个命令有可能已经不支持了，请谨慎使用
echo "\$@使用示例: $@"
echo "\$@使用示例002: \"$@\""
echo "显示shell使用的当前选项: $-"
echo "显示命令的退出状态，是否正常(正常显示0，否则是其他值): $?"

for var in $@
do
        echo "$var"
done

for var in $*
do
        echo "$var"
done

for var in "$@"
do
        echo "$var"
done

for var in "$*"
do
        echo "$var"
done
```
###### result:
```bash
$ sh para.sh 名字 空格 三餐 siji
Shell 传递参数实例!
执行的文件名：para.sh
first parameter：名字
second parameter：空格
third parameter：三餐
parameter count: 4
一个字符串，显示所有参数: 名字 空格 三餐 siji
脚本当前进程号: 27564
后台运行最后一个进程id:
$@使用示例: 名字 空格 三餐 siji
$@使用示例002: "名字 空格 三餐 siji"
显示shell使用的当前选项: hB
显示命令的退出状态，是否正常(正常显示0，否则是其他值): 0
名字
空格
三餐
siji
名字
空格
三餐
siji
名字
空格
三餐
siji
名字 空格 三餐 siji
```

## Shell 数组

数组中可以存放多个值。Bash Shell 只支持一维数组（不支持多维数组），初始化时不需要定义数组大小。

与大部分编程语言类似，数组元素的下标由0开始。

Shell 数组用括号来表示，元素用"空格"符号分割开，语法格式如下：
```bash
array_name=(value value2 value3 ... valuen)
```

#### 实例

```bash
my_array=(a b "c" d)
```
使用数组下标进行数组定义
```bash
array_name[0]=value0
array_name[1]=value1
array_name[3]=value3
```

#### 读取数组

```bash
${array_name[index]}
```
###### example:
```bash
my_array=(A B "C" D)

echo "第一个元素为: ${my_array[0]}"
echo "第二个元素为: ${my_array[1]}"
echo "第三个元素为: ${my_array[2]}"
echo "第四个元素为: ${my_array[3]}"
```
###### result:
```bash
$ sh ./demo.sh
第一个元素为: A
第二个元素为: B
第三个元素为: C
第四个元素为: D
```

#### 获取数组中的所有元素

使用@ 或 * 可以获取数组中的所有元素，例如：
###### example
```bash
my_array[0]=A
my_array[1]=B
my_array[2]=C
my_array[3]=D

echo "数组的元素为: ${my_array[*]}"
echo "数组的元素为: ${my_array[@]}"
```
###### result:
```bash
$ sh ./demo.sh
数组的元素为: A B C D
数组的元素为: A B C D
```

#### 获取数组的长度

获取数组长度的方法与获取字符串长度的方法相同，例如：
###### example
```bash
$ cat demo.sh
my_array[0]=A
my_array[1]=B
my_array[2]=CCC
my_array[3]=D

echo "数组元素个数为：${#my_array[*]}"
echo "数组元素个数为：${#my_array[@]}"
echo "数组第3个元素的长度为：${#my_array[2]}"
```
###### result:
```bash
$ sh ./demo.sh
数组元素个数为：4
数组元素个数为：4
数组第3个元素的长度为：3
```


## Shell 基本运算符

Shell 和其他编程语言一样，支持多种运算符，包括：

- 算数运算符
- 关系运算符
- 布尔运算符
- 字符串运算符
- 文件测试运算符

原生bash不支持简单的数学运算，但是可以通过其他命令来实现，例如 awk 和 expr，expr 最常用。

expr 是一款表达式计算工具，使用它能完成表达式的求值操作。

例如，两个数相加(注意使用的是反引号 \` 而不是单引号 ')：
###### example
```bash
val=`expr 1 + 21`
echo "两数之和: $val"
```
###### result:
```bash
两数之和: 22
```

两点注意：

- 表达式和运算符之间要有空格，例如 2+2 是不对的，必须写成 2 + 2，这与我们熟悉的大多数编程语言不一样。
- 完整的表达式要被 \` \` 包含，注意这个字符不是常用的单引号，在 Esc 键下边。

#### 算数运算符

|运算符	|说明		|举例|
|-|-|-|
|+		|加法		|\`expr $a + $b\` 结果为 30。|
|-		|减法		|\`expr $a - $b\` 结果为 -10。|
|*		|乘法		|\`expr $a \* $b\` 结果为  200。|
|/		|除法		|\`expr $b / $a\` 结果为 2。|
|%		|取余		|\`expr $b % $a\` 结果为 0。|
|=		|赋值		|a=$b 将把变量 b 的值赋给 a。|
|==		|相等。		|用于比较两个数字，相同则返回 true。	[ $a == $b ] 返回 false。|
|!=		|不相等。		|用于比较两个数字，不相同则返回 true。	[ $a != $b ] 返回 true。|

PS: 条件表达式要放在方括号之间，并且要**有空格**，例如: [$a==$b] 是错误的，必须写成 [ $a == $b ]。

###### example:
```bash
a=10
b=20

val=`expr $a + $b`
echo "a + b : $val"

val=`expr $a - $b`
echo "a - b : $val"

val=`expr $a \* $b`
echo "a * b : $val"

val=`expr $b / $a`
echo "b / a : $val"

val=`expr $b % $a`
echo "b % a : $val"

if [ $a == $b ]
then
   echo "a 等于 b"
fi
if [ $a != $b ]
then
   echo "a 不等于 b"
fi
```
###### result:
```bash
a + b : 30
a - b : -10
a * b : 200
b / a : 2
b % a : 0
a 不等于 b
```

注意：

- 乘号(\*)前边必须加反斜杠(\\)才能实现乘法运算；
- if...then...fi 是条件语句，后续将会讲解。
- 在 MAC 中 shell 的 expr 语法是：$((表达式))，此处表达式中的 "\*" 不需要转义符号 "\" 。


#### 关系运算符

关系运算符只支持数字，不支持字符串，除非字符串的值是数字。

下表列出了常用的关系运算符，假定变量 a 为 10，变量 b 为 20：

|运算符	|说明												|举例|
|-|-|-|
|-eq	|检测两个数是否相等，相等返回 true。					|[ $a -eq $b ] 返回 false。|
|-ne	|检测两个数是否不相等，不相等返回 true。				|[ $a -ne $b ] 返回 true。|
|-gt	|检测左边的数是否大于右边的，如果是，则返回 true。		|[ $a -gt $b ] 返回 false。|
|-lt	|检测左边的数是否小于右边的，如果是，则返回 true。		|[ $a -lt $b ] 返回 true。|
|-ge	|检测左边的数是否大于等于右边的，如果是，则返回 true。	|[ $a -ge $b ] 返回 false。|
|-le	|检测左边的数是否小于等于右边的，如果是，则返回 true。	|[ $a -le $b ] 返回 true。|

###### example
```bash
a=10
b=20

if [ $a -eq $b ]
then
   echo "$a -eq $b : a 等于 b"
else
   echo "$a -eq $b: a 不等于 b"
fi
if [ $a -ne $b ]
then
   echo "$a -ne $b: a 不等于 b"
else
   echo "$a -ne $b : a 等于 b"
fi
if [ $a -gt $b ]
then
   echo "$a -gt $b: a 大于 b"
else
   echo "$a -gt $b: a 不大于 b"
fi
if [ $a -lt $b ]
then
   echo "$a -lt $b: a 小于 b"
else
   echo "$a -lt $b: a 不小于 b"
fi
if [ $a -ge $b ]
then
   echo "$a -ge $b: a 大于或等于 b"
else
   echo "$a -ge $b: a 小于 b"
fi
if [ $a -le $b ]
then
   echo "$a -le $b: a 小于或等于 b"
else
   echo "$a -le $b: a 大于 b"
fi
```
###### result:
```bash
10 -eq 20: a 不等于 b
10 -ne 20: a 不等于 b
10 -gt 20: a 不大于 b
10 -lt 20: a 小于 b
10 -ge 20: a 小于 b
10 -le 20: a 小于或等于 b
```

#### 布尔运算符

下表列出了常用的布尔运算符，假定变量 a 为 10，变量 b 为 20：


|运算符	|说明											|举例|
|-|-|-|
|!		|非运算，表达式为 true 则返回 false，否则返回 true。|	[ ! false ] 返回 true。|
|-o		|或运算，有一个表达式为 true 则返回 true。			|[ $a -lt 20 -o $b -gt 100 ] 返回 true。|
|-a		|与运算，两个表达式都为 true 才返回 true。			|[ $a -lt 20 -a $b -gt 100 ] 返回 false。|

###### example
```bash
a=10
b=20

if [ $a != $b ]
then
   echo "$a != $b : a 不等于 b"
else
   echo "$a == $b: a 等于 b"
fi
if [ $a -lt 100 -a $b -gt 15 ]
then
   echo "$a 小于 100 且 $b 大于 15 : 返回 true"
else
   echo "$a 小于 100 且 $b 大于 15 : 返回 false"
fi
if [ $a -lt 100 -o $b -gt 100 ]
then
   echo "$a 小于 100 或 $b 大于 100 : 返回 true"
else
   echo "$a 小于 100 或 $b 大于 100 : 返回 false"
fi
if [ $a -lt 5 -o $b -gt 100 ]
then
   echo "$a 小于 5 或 $b 大于 100 : 返回 true"
else
   echo "$a 小于 5 或 $b 大于 100 : 返回 false"
fi
```
###### result
```bash
10 != 20 : a 不等于 b
10 小于 100 且 20 大于 15 : 返回 true
10 小于 100 或 20 大于 100 : 返回 true
10 小于 5 或 20 大于 100 : 返回 false
```


#### 逻辑运算符

以下介绍 Shell 的逻辑运算符，假定变量 a 为 10，变量 b 为 20:

|运算符	|说明		|举例|
|-|-|-|
|&&		|逻辑的 AND	|[[ $a -lt 100 && $b -gt 100 ]] 返回 false|
|||		|逻辑的 OR	|[[ $a -lt 100 || $b -gt 100 ]] 返回 true|

###### example
```bash
a=10
b=20

if [[ $a -lt 100 && $b -gt 100 ]]
then
   echo "返回 true"
else
   echo "返回 false"
fi

if [[ $a -lt 100 || $b -gt 100 ]]
then
   echo "返回 true"
else
   echo "返回 false"
fi
```
###### result
```bash
返回 false
返回 true
```

#### 字符串运算符

下表列出了常用的字符串运算符，假定变量a为"abc", 变量b为"efg":
|运算符	|说明										|举例|
|-|-|-|
|=		|检测两个字符串是否相等，相等返回 true。		|[ $a = $b ] 返回 false。|
|!=		|检测两个字符串是否相等，不相等返回 true。		|[ $a != $b ] 返回 true。|
|-z		|检测字符串长度是否为0，为0返回 true。			|[ -z $a ] 返回 false。|
|-n		|检测字符串长度是否不为 0，不为 0 返回 true。	|[ -n "$a" ] 返回 true。|
|$		|检测字符串是否为空，不为空返回 true。			|[ $a ] 返回 true。|

###### example
```bash
a="abc"
b="efg"

if [ $a = $b ]
then
   echo "$a = $b : a 等于 b"
else
   echo "$a = $b: a 不等于 b"
fi
if [ $a != $b ]
then
   echo "$a != $b : a 不等于 b"
else
   echo "$a != $b: a 等于 b"
fi
if [ -z $a ]
then
   echo "-z $a : 字符串长度为 0"
else
   echo "-z $a : 字符串长度不为 0"
fi
if [ -n "$a" ]
then
   echo "-n $a : 字符串长度不为 0"
else
   echo "-n $a : 字符串长度为 0"
fi
if [ $a ]
then
   echo "$a : 字符串不为空"
else
   echo "$a : 字符串为空"
fi
```
###### result
```bash
abc = efg: a 不等于 b
abc != efg : a 不等于 b
-z abc : 字符串长度不为 0
-n abc : 字符串长度不为 0
abc : 字符串不为空
```

#### 文件测试运算符

文件测试运算符用于检测 Unix 文件的各种属性。

属性检测描述如下：

|操作符		|说明																	|举例|
|-|-|-|
|-b file	|检测文件是否是块设备文件，如果是，则返回 true。								|[ -b $file ] 返回 false。|
|-c file	|检测文件是否是字符设备文件，如果是，则返回 true。							|[ -c $file ] 返回 false。|
|-d file	|检测文件是否是目录，如果是，则返回 true。									|[ -d $file ] 返回 false。|
|-f file	|检测文件是否是普通文件（既不是目录，也不是设备文件），如果是，则返回 true。	|[ -f $file ] 返回 true。|
|-g file	|检测文件是否设置了 SGID 位，如果是，则返回 true。							|[ -g $file ] 返回 false。|
|-k file	|检测文件是否设置了粘着位(Sticky Bit)，如果是，则返回 true。					|[ -k $file ] 返回 false。|
|-p file	|检测文件是否是有名管道，如果是，则返回 true。								|[ -p $file ] 返回 false。|
|-u file	|检测文件是否设置了 SUID 位，如果是，则返回 true。							|[ -u $file ] 返回 false。|
|-r file	|检测文件是否可读，如果是，则返回 true。									|[ -r $file ] 返回 true。|
|-w file	|检测文件是否可写，如果是，则返回 true。									|[ -w $file ] 返回 true。|
|-x file	|检测文件是否可执行，如果是，则返回 true。									|[ -x $file ] 返回 true。|
|-s file	|检测文件是否为空（文件大小是否大于0），不为空返回 true。						|[ -s $file ] 返回 true。|
|-e file	|检测文件（包括目录）是否存在，如果是，则返回 true。							|[ -e $file ] 返回 true。|

其他检查符：

- -S: 判断某文件是否 socket。
- -L: 检测文件是否存在并且是一个符号链接。

###### example

变量 file 表示文件 /var/www/runoob/test.sh，它的大小为 100 字节，具有 rwx 权限。下面的代码，将检测该文件的各种属性：
```bash
file="/var/www/runoob/test.sh"
if [ -r $file ]
then
   echo "文件可读"
else
   echo "文件不可读"
fi
if [ -w $file ]
then
   echo "文件可写"
else
   echo "文件不可写"
fi
if [ -x $file ]
then
   echo "文件可执行"
else
   echo "文件不可执行"
fi
if [ -f $file ]
then
   echo "文件为普通文件"
else
   echo "文件为特殊文件"
fi
if [ -d $file ]
then
   echo "文件是个目录"
else
   echo "文件不是个目录"
fi
if [ -s $file ]
then
   echo "文件不为空"
else
   echo "文件为空"
fi
if [ -e $file ]
then
   echo "文件存在"
else
   echo "文件不存在"
fi
```

###### result
```bash
文件可读
文件可写
文件可执行
文件为普通文件
文件不是个目录
文件不为空
文件存在
```
