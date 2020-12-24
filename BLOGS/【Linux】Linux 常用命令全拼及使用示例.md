# Linux 常用命令全拼及示例

## pwd: print work directory 打印当前目录 显示出当前工作目录的绝对路径

	#### 如：
	```bash
	pwd		# 没有参数使用，直接输出当前工作目录的绝对路径
	```


## ps: process status(进程状态，类似于windows的任务管理器)

	#### 语法
	```bash
	ps [options] [--help]
	```

	#### 常用参数
	```bash
	-A 所有的进程均显示出来
	-a 不与terminal有关的所有进程
	-u 有效用户的相关进程
	-e 此参数的效果和指定"A"参数相同。
	-x 一般与a参数一起使用，可列出较完整的信息
	-l 较长，较详细地将PID的信息列出
	```

	#### 如：
	```bash
	ps -u root 	//显示root进程用户信息
	ps -A 显示进程信息
	ps aux # 查看系统所有的进程数据
	ps ax # 查看不与terminal有关的所有进程
	ps -lA # 查看系统所有的进程数据
	ps axjf # 查看连同一部分进程树状态
	```


## kill: Linux kill 命令用于删除执行中的程序或工作。

	程序或工作的编号可利用 ps 指令或 jobs 指令查看。

	#### 语法
	```bash
	kill [-s <信息名称或编号>][程序]　或　kill [-l <信息编号>]
	```

	#### 参数
	```bash
	-l <信息编号> 　若不加<信息编号>选项，则 -l 参数会列出全部的信息名称。
	-s <信息名称或编号> 　指定要送出的信息。
	[程序] 　[程序]可以是程序的PID或是PGID，也可以是工作编号。
	```

	使用 kill -l 命令列出所有可用信号。

	最常用的信号是：

	- 1：SIGHUP，启动被终止的进程，重新加载进程。
	- 2：SIGINT，相当于输入ctrl+c，中断一个程序的进行
	- 9：SIGKILL，强制中断一个进程的进行，杀死一个进程。
	- 15：SIGTERM，以正常的结束进程方式来终止进程，正常停止一个进程。
	- 17：SIGSTOP，相当于输入ctrl+z，暂停一个进程的进行

	#### 如：
	```bash
	杀死进程
	# kill 12345

	强制杀死进程
	# kill -KILL 123456

	发送SIGHUP信号，可以使用一下信号
	# kill -HUP pid

	彻底杀死进程
	# kill -9 123456
	```


## killall: Linux killall 用于杀死一个进程，与 kill 不同的是它会杀死指定名字的所有进程。

	kill 命令杀死指定进程 PID，需要配合 ps 使用，而 killall 直接对进程对名字进行操作，更加方便。

	#### 语法
	```bash
	killall [选项] name
	```

	#### 参数说明
	```bash
	name ： 进程名

	-I | --ignore-case ：忽略大小写
	-i | --interactive ：结束之前询问
	-l | --list ：列出所有的信号名称
	-r | --regexp ：将进程名模式解释为扩展的正则表达式。
	-v | --verbose ：显示详细执行过程
	-V |--version ：显示版本信息
	--help ：显示帮助信息
	```

	#### 如：
	```bash
	killall -9 php-fpm         # 结束所有的 php-fpm 进程
	```


## df: disk free （英文全拼：disk free） 命令用于显示目前在 Linux 系统上的文件系统磁盘使用情况统计。

	#### 语法
	```bash
	df [选项]... [FILE]...
	```

	#### 常用参数
	```bash
	-a 全部文件系统列表
	-h 方便阅读方式显示
	-H 等于“-h”，但是计算式，1K=1000，而不是1K=1024
	-k 区块为1024字节
	-l 只显示本地文件系统
	-T 文件系统类型(显示文件系统类型)
	```

	#### 如
	```bash
	$ df 		# 查看文件系统磁盘使用情况
	$ df -T 	# 查看文件系统磁盘使用情况(并显示各个磁盘的文件类型)
	$ df -h 	# 以易读的方式，M G的方式显示磁盘大小 1M=1024K
	```


## file: Linux file命令用于辨识文件类型

	通过file指令，我们得以辨识文件的类型。

	#### 语法
	```bash
	file [-bcLvz][-f <文件名称>][-m <魔法数字文件>...][文件或目录...]
	```

	#### 参数
	```bash
	-b 　列出辨识结果时，不显示文件名称。
	-c 　详细显示指令执行过程，便于排错或分析程序执行的情形。
	-f<名称文件> 　指定名称文件，其内容有一个或多个文件名称时，让file依序辨识这些文件，格式为每列一个文件名称。
	-L 　直接显示符号连接所指向的文件的类别。
	-m<魔法数字文件> 　指定魔法数字文件。
	-v 　显示版本信息。
	-z 　尝试去解读压缩文件的内容。
	[文件或目录...] 要确定类型的文件列表，多个文件之间使用空格分开，可以使用shell通配符匹配多个文件。
	```

	#### 如：
	```bash
	显示文件类型：

	[root@localhost ~]# file install.log
	install.log: UTF-8 Unicode text

	[root@localhost ~]# file -b install.log      <== 不显示文件名称
	UTF-8 Unicode text

	[root@localhost ~]# file -i install.log      <== 显示MIME类别。
	install.log: text/plain; charset=utf-8

	[root@localhost ~]# file -b -i install.log
	text/plain; charset=utf-8


	显示符号链接的文件类型

	[root@localhost ~]# ls -l /var/mail
	lrwxrwxrwx 1 root root 10 08-13 00:11 /var/mail -> spool/mail

	[root@localhost ~]# file /var/mail
	/var/mail: symbolic link to `spool/mail'

	[root@localhost ~]# file -L /var/mail
	/var/mail: directory

	[root@localhost ~]# file /var/spool/mail
	/var/spool/mail: directory

	[root@localhost ~]# file -L /var/spool/mail
	/var/spool/mail: directory
	```


## tar命令  Linux tar（英文全拼：tape archive ）命令用于备份文件。

	该命令用于对文件进行打包，默认情况并不会压缩，如果指定了相应的参数，它还会调用相应的压缩程序（如gzip和bzip等）进行压缩和解压。

	tar 是用来建立，还原备份文件的工具程序，它可以加入，解开备份文件内的文件。

	#### 语法
	```bash
	tar [参数][目的目录][备份文件]...
	or
	tar --exclude=目录名/* 或者 文件名 -zcvf 备份文件名.tgz 目录名
	```

	#### 参数
	```bash
	它的常用参数如下：
	-c ：新建打包文件
	-t ：查看打包文件的内容含有哪些文件名
	-x ：解打包或解压缩的功能，可以搭配-C（大写）指定解压的目录，注意-c,-t,-x不能同时出现在同一条命令中
	-j ：通过bzip2的支持进行压缩/解压缩
	-z ：通过gzip的支持进行压缩/解压缩
	-v ：在压缩/解压缩过程中，将正在处理的文件名显示出来
	-f filename ：filename为要处理的文件
	-C dir ：指定压缩/解压缩的目录dir
	```
	上面的解说可以已经让你晕过去了，但是通常我们只需要记住下面三条命令即可：
	```bash
	压缩：tar -jcv -f filename.tar.bz2 要被处理的文件或目录名称
	查询：tar -jtv -f filename.tar.bz2
	解压：tar -jxv -f filename.tar.bz2 -C 欲解压缩的目录
	```

	#### 如：
	```bash
	压缩文件 非打包
	# touch a.c       
	# tar -czvf test.tar.gz a.c   //压缩 a.c文件为test.tar.gz
	a.c

	列出压缩文件内容
	# tar -tzvf test.tar.gz 
	-rw-r--r-- root/root     0 2010-05-24 16:51:59 a.c

	解压文件
	# tar -xzvf test.tar.gz 
	a.c


	# 创建一个名为 abc 的目录
	mkdir abc

	# 进入 abc 这个目录
	cd abc

	# 创建两个文件,文件名为1.txt 2.txt
	touch 1.txt 2.txt

	# 切换到 abc 的父目录
	cd ..

	# 将文件 abc 进行压缩时，排除1.txt，压缩后的文件名为 abc.tar
	tar --exclude=abc/1.txt -zcvf abc.tgz abc		# 会将abc目录下的文件2.txt及abc目录一起打包

	# 解压文件
	tar -zxvf abc.tgz 		# 默认名字为abc

	# 删除压缩文件
	rm abc.tgz

	# 删除解压后的文件，并删除文件夹
	rm -rf abc
	```


## cat: cat（英文全拼：concatenate）命令用于连接文件并打印到标准输出设备上。

	#### 语法
	```bash
	cat [-AbeEnstTuv] [--help] [--version] fileName
	```

	#### 常用参数
	```bash
	-n 或 --number：由 1 开始对所有输出的行数编号。
	-b 或 --number-nonblank：和 -n 相似，只不过对于空白行不编号。
	-s 或 --squeeze-blank：当遇到有连续两行以上的空白行，就代换为一行的空白行。
	-v 或 --show-nonprinting：使用 ^ 和 M- 符号，除了 LFD 和 TAB 之外。
	-E 或 --show-ends : 在每行结束处显示 $。
	-T 或 --show-tabs: 将 TAB 字符显示为 ^I。
	-A, --show-all：等价于 -vET。
	-e：等价于"-vE"选项；
	-t：等价于"-vT"选项；
	```

	#### 如：
	```bash
	cat -n textfile1 > textfile2 			# 把 textfile1 的文档内容加上行号后输入 textfile2 这个文档里
	cat -b textfile1 textfile2 >> textfile3 # 把 textfile1 和 textfile2 的文档内容加上行号（空白行不加）之后将内容附加到 textfile3 文档里
	cat /dev/null > /etc/test.txt 			# 清空 /etc/test.txt 文档内容
	cat /dev/fd0 > OUTFILE 					# cat 也可以用来制作镜像文件。例如要制作软盘的镜像文件，将软盘放好后输入
	cat IMG_FILE > /dev/fd0					# 相反的，如果想把 image file 写到软盘，输入
	```

	注：

	- 1. OUTFILE 指输出的镜像文件名。
	- 2. IMG_FILE 指镜像文件。
	- 3. 若从镜像文件写回 device 时，device 容量需与相当。
	- 4. 通常用制作开机磁片。


## su：Swith user(切换用户) Linux su（英文全拼：swith user）命令用于变更为其他使用者的身份，除 root 外，需要键入该使用者的密码。

	#### 如：
	```bash
	# 切换用户
	hnlinux@runoob.com:~$ whoami //显示当前用户
	hnlinux
	hnlinux@runoob.com:~$ pwd //显示当前目录
	/home/hnlinux
	hnlinux@runoob.com:~$ su root //切换到root用户
	密码： 
	root@runoob.com:/home/hnlinux# whoami 
	root
	root@runoob.com:/home/hnlinux# pwd
	/home/hnlinux

	# 切换用户，改变环境变量
	hnlinux@runoob.com:~$ whoami //显示当前用户
	hnlinux
	hnlinux@runoob.com:~$ pwd //显示当前目录
	/home/hnlinux
	hnlinux@runoob.com:~$ su - root //切换到root用户
	密码： 
	root@runoob.com:/home/hnlinux# whoami 
	root
	root@runoob.com:/home/hnlinux# pwd //显示当前目录
	/root
	```


## cd：Change directory

	#### 如：
	```bash
	# 切换当前工作目录
	cd ./demo		# 以当前目录为根目录进行路径查找和切换
	cd ../demo		# 以父项目录为根目录进行路径查找和切换
	```


## ls：List files

	#### 语法
	```bash
	ls [-alrtAFR] [name...]
	```

	#### 常用参数
	```bash
	-1 每个文件一行的形式显示
	-a 显示所有文件及目录 (. 开头的隐藏文件也会列出)
	-l 除文件名称外，亦将文件型态、权限、拥有者、文件大小等资讯详细列出
	-r 将文件以相反次序显示(原定依英文字母次序)
	-t 将文件依建立时间之先后次序列出
	-A 同 -a ，但不列出 "." (目前目录) 及 ".." (父目录)
	-F 在列出的文件名称后加一符号；例如可执行档则加 "*", 目录则加 "/"
	-R 若目录下有文件，则以下之文件亦皆依序列出
	```

	#### 如：
	```bash
	ls -ltr s*		# 列出当前目录下所有名称是s开头的文件
	ls -lR /bin		# 将 /bin 目录以下所有目录及文件详细资料列出
	ls -AF 			列出目前工作目录下所有文件及目录；目录于名称后加 "/", 可执行档于名称后加 "*"
	```


## grep命令  Linux grep 命令用于查找文件里符合条件的字符串。

	该命令常用于分析一行的信息，若当中有我们所需要的信息，就将该行显示出来，该命令通常与管道命令一起使用，用于对一些命令的输出进行筛选加工等等。


	#### 如：
	```bash
	在当前目录中，查找后缀有 file 字样的文件中包含 test 字符串的文件，并打印出该字符串的行。此时，可以使用如下命令：
	grep test *file 

	以递归的方式查找符合条件的文件。例如，查找指定目录/etc/acpi 及其子目录（如果存在子目录的话）下所有文件中包含字符串"update"的文件，
    并打印出该字符串所在行的内容，使用的命令为：
	grep -r update /etc/acpi

	反向查找。前面各个例子是查找并打印出符合条件的行，通过"-v"参数可以打印出不符合条件行的内容。
	查找文件名中包含 test 的文件中不包含test 的行，此时，使用的命令为：
	grep -v test *test*

	场景： 系统报警显示了时间，但是日志文件太大无法直接 cat 查看。(查询含有特定文本的文件，并拿到这些文本所在的行)
	解决：
	grep -n '2019-10-24 00:01:11' *.log
	查看符合条件的日志条目。


	从文件内容查找匹配指定字符串的行：
	$ grep "被查找的字符串" 文件名

	例子：在当前目录里第一级文件夹中寻找包含指定字符串的 .in 文件
	grep "thermcontact" /.in

	从文件内容查找与正则表达式匹配的行：
	$ grep –e "正则表达式" 文件名

	查找时不区分大小写：
	$ grep –i "被查找的字符串" 文件名

	查找匹配的行数：
	$ grep -c "被查找的字符串" 文件名

	从文件内容查找不匹配指定字符串的行：
	$ grep –v "被查找的字符串" 文件名
	```


## find命令  Linux find 命令用来在指定目录下查找文件。

	任何位于参数之前的字符串都将被视为欲查找的目录名。<br>如果使用该命令时，不设置任何参数，则 find 命令将在当前目录下查找子目录与文件。
    并且将查找到的子目录和文件全部进行显示。

	#### 参数
	```bash
	-name name, -iname name : 文件名称符合 name 的文件。iname 会忽略大小写
	-type c : 文件类型是 c 的文件。
	-ctime n : 在过去n天内被修改过的文件
	f: 一般文件
	d: 目录
	-pid n : process id 是 n 的文件
	```

	#### 如：
	```bash
	将当前目录及其子目录下所有文件后缀为 .c 的文件列出来:
	# find . -name "*.c"

	将目前目录其其下子目录中所有一般文件列出
	# find . -type f

	将当前目录及其子目录下所有最近 20 天内更新过的文件列出:
	# find . -ctime -20

	查找 /var/log 目录中更改时间在 7 日以前的普通文件，并在删除之前询问它们：
	# find /var/log -type f -mtime +7 -ok rm {} \;

	查找当前目录中文件属主具有读、写权限，并且文件所属组的用户和其他用户具有读权限的文件：
	# find . -type f -perm 644 -exec ls -l {} \;

	查找系统中所有文件长度为 0 的普通文件，并列出它们的完整路径：
	# find / -type f -size 0 -exec ls -l {} \;
	```


## touch: Linux touch命令用于修改文件或者目录的时间属性，包括存取时间和更改时间。若文件不存在，系统会建立一个新的文件。

	ls -l 可以显示档案的记录时间

	#### 语法
	```bash
	touch [-acfm][-d<日期时间>][-r<参考文件或目录>] [-t<日期时间>][--help][--version][文件或目录…]
	```

	#### 参数
	```bash
	a 改变档案的读取时间记录。
	m 改变档案的修改时间记录。
	c 假如目的档案不存在，不会建立新的档案。与 --no-create 的效果一样。
	f 不使用，是为了与其他 unix 系统的相容性而保留。
	r 使用参考档的时间记录，与 --file 的效果一样。
	d 设定时间与日期，可以使用各种不同的格式。
	t 设定档案的时间记录，格式与 date 指令相同。
	--no-create 不会建立新档案。
	--help 列出指令格式。
	--version 列出版本讯息
	```

	#### 如：
	```bash
	用指令"touch"修改文件"testfile"的时间属性为当前系统时间，输入如下命令：
	$ touch testfile                #修改文件的时间属性 

	首先，使用ls命令查看testfile文件的属性，如下所示：
	$ ls -l testfile                #查看文件的时间属性  
	#原来文件的修改时间为16:09  
	-rw-r--r-- 1 hdd hdd 55 2011-08-22 16:09 testfile  

	执行指令"touch"修改文件属性以后，并再次查看该文件的时间属性，如下所示：
	$ touch testfile                #修改文件时间属性为当前系统时间  
	$ ls -l testfile                #查看文件的时间属性  
	#修改后文件的时间属性为当前系统时间  
	-rw-r--r-- 1 hdd hdd 55 2011-08-22 19:53 testfile  

	使用指令"touch"时，如果指定的文件不存在，则将创建一个新的空白文件。例如，在当前目录下，使用该指令创建一个空白文件"file"，输入如下命令：
	$ touch file            #创建一个名为“file”的新的空白文件 
	```


## mkdir：Make directory  Linux mkdir（英文全拼：make directory）命令用于创建目录。

	#### 语法
	```bash
	mkdir [-p] dirName
	```

	#### 常用参数
	```bash
	-p 确保目录名称存在，不存在的就建一个。
	```

	#### 如：
	```bash
	mkdir demo				# 在当前目录下新建一个demo文件夹
	mkdir -p demo/test		# 在当前目录中的demo文件夹下新建文件夹test，如果demo不存在则新建，如果不加-p则会报错
	```


## mv命令：move file Linux mv（英文全拼：move file）命令用来为文件或目录改名、或将文件或目录移入其它位置。

	#### 语法
	```bash
	mv [options] source dest
	mv [options] source... directory
	```

	#### 参数
	```bash
	-b: 当目标文件或目录存在时，在执行覆盖前，会为其创建一个备份。
	-i: 如果指定移动的源目录或文件与目标的目录或文件同名，则会先询问是否覆盖旧文件，输入 y 表示直接覆盖，输入 n 表示取消该操作。
	-f: 如果指定移动的源目录或文件与目标的目录或文件同名，不会询问，直接覆盖旧文件。
	-n: 不要覆盖任何已存在的文件或目录。
	-u：当源文件比目标文件新或者目标文件不存在时，才执行移动操作。
	```

#### 如：

|命令格式												|运行结果|
|-|-|
|mv source_file(文件) dest_file(文件)					|将源文件名 source_file 改为目标文件名 dest_file|
|mv source_file(文件) dest_directory(目录)			|将文件 source_file 移动到目标目录 dest_directory 中|
|mv source_directory(目录) dest_directory(目录)		|目录名 dest_directory 已存在，将 source_directory 移动到目录名 dest_directory 中；目录名 dest_directory 不存在则 source_directory 改名为目录名 dest_directory|
|mv source_directory(目录) dest_file(文件) 			|出错|

	```bash
	将文件 aaa 改名为 bbb :
	mv aaa bbb

	将 info 目录放入 logs 目录中。注意，如果 logs 目录不存在，则该命令将 info 改名为 logs。
	mv info/ logs 

	再如将 /usr/runoob 下的所有文件和目录移到当前目录下，命令行为：
	$ mv /usr/runoob/*  .

	目标目录与原目录一致，指定了新文件名，效果就是仅仅重命名。
	mv  /home/ffxhd/a.txt   /home/ffxhd/b.txt   

	目标目录与原目录不一致，没有指定新文件名，效果就是仅仅移动。
	mv  /home/ffxhd/a.txt   /home/ffxhd/test/ 
	或者
	mv  /home/ffxhd/a.txt   /home/ffxhd/test 

	目标目录与原目录一致, 指定了新文件名，效果就是：移动 + 重命名。
	mv  /home/ffxhd/a.txt   /home/ffxhd/test/c.txt
	```


## rmdir：Remove directory  Linux rmdir（英文全拼：remove directory）命令删除空的目录。

	#### 语法
	```bash
	rmdir [-p] dirName
	```

	#### 常用参数
	```bash
	-p 是当子目录被删除后使它也成为空目录的话，则顺便一并删除。
	```

	#### 如：
	```bash
	rmdir AAA 			# 将工作目录下，名为 AAA 的子目录删除
	rmdir -p BBB/Test 	# 在工作目录下的 BBB 目录中，删除名为 Test 的子目录。若 Test 删除后，BBB 目录成为空目录，则 BBB 亦予删除。
	```


## uname: Unix namem Linux uname（英文全拼：unix name）命令用于显示系统信息。

	#### 语法
	```bash
	uname [-amnrsv][--help][--version]
	```

	#### 常用参数
	```bash
	-a或--all 　显示全部的信息。
	-m或--machine 　显示电脑类型。
	-n或-nodename 　显示在网络上的主机名称。
	-r或--release 　显示操作系统的发行编号。
	-s或--sysname 　显示操作系统名称。
	-v 　显示操作系统的版本。
	--help 　显示帮助。
	--version 　显示版本信息。
	```

	#### 如：
	```bash
	uname -a 	# 显示系统信息
	uname -m 	# 显示计算机类型
	uname -n 	# 显示计算机名
	uname -r 	# 显示操作系统发行编号
	uname -s 	# 显示操作系统名称
	uname -v 	# 显示系统版本与时间
	```


## rm: Remove file  Linux rm（英文全拼：remove）命令用于删除一个文件或者目录。

	#### 语法
	```bash
	rm [options] name...
	```

	#### 常用参数
	```bash
	-i 删除前逐一询问确认。
	-f 即使原档案属性设为唯读，亦直接删除，无需逐一确认。
	-r 将目录及以下之档案亦逐一删除。（删除文件可以直接使用rm命令，若删除目录则必须配合选项"-r"）
	```

	#### 如：
	```bash
	$ rm -i fun.sh
	rm: remove regular file 'fun.sh'? y
	$ rm demo
	rm: cannot remove 'demo': Is a directory
	$ rm -ir demo2
	rm: remove directory 'demo2'? y

	rm -r *		# 删除当前目录下的所有文件及目录（慎用）
	```

	文件一旦通过rm命令删除，则无法恢复，所以必须格外小心地使用该命令。


## cp: Copy file  Linux cp（英文全拼：copy file）命令主要用于复制文件或目录。

	#### 语法
	```bash
	cp [options] source dest
	或
	cp [options] source... directory
	```

	#### 常用参数
	```bash
	-a：此选项通常在复制目录时使用，它保留链接、文件属性，并复制目录下的所有内容。其作用等于dpR参数组合。
	-d：复制时保留链接。这里所说的链接相当于Windows系统中的快捷方式。
	-f：覆盖已经存在的目标文件而不给出提示。
	-i：与-f选项相反，在覆盖目标文件之前给出提示，要求用户确认是否覆盖，回答"y"时目标文件将被覆盖。
	-p：除复制文件的内容外，还把修改时间和访问权限也复制到新文件中。
	-r：若给出的源文件是一个目录文件，此时将复制该目录下所有的子目录和文件。
	-l：不复制文件，只是生成链接文件。
	```

	#### 如：
	```bash
	cp –r test/ newtest 	# 使用指令 cp 将当前目录 test/ 下的所有文件复制到新目录 newtest 下
	```
	注意：用户使用该指令复制目录时，必须使用参数 -r 或者 -R 。


## ln: Link files Linux ln（英文全拼：link files）命令是一个非常重要命令，它的功能是为某一个文件在另外一个位置建立一个同步的链接。

	当我们需要在不同的目录，用到相同的文件时，我们不需要在每一个需要的目录下都放一个必须相同的文件，我们只要在某个固定的目录，放上该文件，然后在 其它的目录下用ln命令链接（link）它就可以，不必重复的占用磁盘空间。

	#### 语法
	```bash
	ln [参数][源文件或目录][目标文件或目录]
	```

	#### 常用参数
	```bash
	# 必要参数
	-b 删除，覆盖以前建立的链接
	-d 允许超级用户制作目录的硬链接
	-f 强制执行
	-i 交互模式，文件存在则提示用户是否覆盖
	-n 把符号链接视为一般目录
	-s 软链接(符号链接)
	-v 显示详细的处理过程
	# 选择参数
	-S "-S<字尾备份字符串> "或 "--suffix=<字尾备份字符串>"
	-V "-V<备份方式>"或"--version-control=<备份方式>"
	--help 显示帮助信息
	--version 显示版本信息
	```

	命令功能 :
	Linux文件系统中，有所谓的链接(link)，我们可以将其视为档案的别名，而链接又可分为两种 : 硬链接(hard link)与软链接(symbolic link)，硬链接的意思是一个档案可以有多个名称，而软链接的方式则是产生一个特殊的档案，该档案的内容是指向另一个档案的位置。硬链接是存在同一个文件系统中，而软链接却可以跨越不同的文件系统。

	不论是硬链接或软链接都不会将原本的档案复制一份，只会占用非常少量的磁碟空间。


	软链接：

	1.软链接，以路径的形式存在。类似于Windows操作系统中的快捷方式。
	2.软链接可以 跨文件系统 ，硬链接不可以。
	3.软链接可以对一个不存在的文件名进行链接。
	4.软链接可以对目录进行链接。
	硬链接：

	1.硬链接，以文件副本的形式存在。但不占用实际空间。
	2.不允许给目录创建硬链接。
	3.硬链接只有在同一个文件系统中才能创建。

	#### 如：
	```bash
	# 软链接会以新文件名创建文件，之后使用ll查看文件列表时，以->形式显示
	ln -s logs link20201223		# 给文件logs创建软链接links20201223
	ll
	-rw-r--r-- 2 username 1049089 285 12月 22 20:38 link20201223 -> logs
	-rw-r--r-- 2 username 1049089 285 12月 22 20:38 logs
	# 硬链接会创建一个新文件，直接以副本形式。
	ln logs lk20201223
	ll
	-rw-r--r-- 2 username 1049089 285 12月 22 20:38 link20201223 -> logs
	-rw-r--r-- 2 username 1049089 285 12月 22 20:38 logs
	-rw-r--r-- 2 username 1049089 285 12月 22 20:38 lk20201223
	```


## chown: Change owner  Linux chown（英文全拼：change owner）命令用于设置文件所有者和文件关联组的命令。

	#### 如：
	```bash
	把 /var/run/httpd.pid 的所有者设置 root：
	chown root /var/run/httpd.pid

	将文件 file1.txt 的拥有者设为 runoob，群体的使用者 runoobgroup :
	chown runoob:runoobgroup file1.txt

	将当前前目录下的所有文件与子目录的拥有者皆设为 runoob，群体的使用者 runoobgroup:
	chown -R runoob:runoobgroup *

	把 /home/runoob 的关联组设置为 512 （关联组ID），不改变所有者：
	chown :512 /home/runoob
	```

## chgrp: Change group  Linux chgrp（英文全拼：change group）命令用于变更文件或目录的所属群组。


## chmod: Change mode   Linux chmod（英文全拼：change mode）命令是控制用户对文件的权限的命令。

	#### 语法
	```bash
	chmod [-cfvR] [--help] [--version] mode file...
	```

	#### 常用参数
	```bash
	[ugoa...][[+-=][rwxX]...][,...]
	u 表示该文件的拥有者，g 表示与该文件的拥有者属于同一个群体(group)者，o 表示其他以外的人，a 表示这三者皆是。
	+ 表示增加权限、- 表示取消权限、= 表示唯一设定权限。
	r 表示可读取，w 表示可写入，x 表示可执行，X 表示只有当该文件是个子目录或者该文件已经被设定过为可执行。

	-c : 若该文件权限确实已经更改，才显示其更改动作
	-f : 若该文件权限无法被更改也不要显示错误讯息
	-v : 显示权限变更的详细资料
	-R : 对目前目录下的所有文件与子目录进行相同的权限变更(即以递归的方式逐个变更)
	--help : 显示辅助说明
	--version : 显示版本
	```

	#### 如：
	```bash
	chmod ugo+r file1.txt 		# 将文件 file1.txt 设为所有人皆可读取
	chmod a+r file1.txt 		# 将文件 file1.txt 设为所有人皆可读取
	chmod u+x ex1.py 			# 将ex1.py设定为只有该文件的拥有者可以执行
	chmod -R a+r * 				# 将目前目录下的所有文件与子目录皆设为任何人可读取
	chmod 777 file 				# 此外chmod也可以用数字来表示权限

	语法为：

	chmod abc file
	其中a,b,c各为一个数字，分别表示User、Group、及Other的权限。

	r=4，w=2，x=1
	若要 rwx 属性则 4+2+1=7；
	若要 rw- 属性则 4+2=6；
	若要 r-x 属性则 4+1=5。
	```
	```bash
	chmod a=rwx file
	和
	chmod 777 file 
	效果相同
	```
	```bash
	chmod ug=rwx,o=x file
	和
	chmod 771 file
	效果相同
	```


## umount: Unmount  Linux umount（英文全拼：unmount）命令用于卸除文件系统。

	#### 如：
	```bash
	下面两条命令分别通过设备名和挂载点卸载文件系统，同时输出详细信息：
	# umount -v /dev/sda1          通过设备名卸载  
	/dev/sda1 umounted  
	# umount -v /mnt/mymount/      通过挂载点卸载  
	/tmp/diskboot.img umounted 

	如果设备正忙，卸载即告失败。卸载失败的常见原因是，某个打开的shell当前目录为挂载点里的某个目录：
	# umount -v /mnt/mymount/  
	umount: /mnt/mymount: device is busy  
	umount: /mnt/mymount: device is busy 
	```
