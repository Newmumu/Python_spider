## 《MongoDB权威指南》

### 第1章 简介

 MongoDB 是 强大、灵活、可扩展的数据存储方式。
#### 1.1 丰富的数据模型

 1. MongoDB 面向文档的数据库，不是关系型数据库；
 	行row - 文档 document
 2. 容易扩展
 3. 丰富的功能（索引 存储javascript 聚合 固定集合 文件存储）（不支持联结和事务）
 4. 不牺牲性能
 5. 简便的管理（除了启动服务器，几乎没有必要的管理操作）

### 第2章 入门

 MongoDB 非常强大，容易上手；  
 文档是MongoDB中数据的基本单元，类似于关系型数据库中的行（row，但是比行row要复杂）  
 集合可以被看做没有模式的表  
 MongoDB的单个实例可以容纳多个独立的数据库，每一个都有自己的集合和权限  
 MongoDB自带简洁但功能强大的JavaScript shell  
 每一个文档都有一个特殊的键_id，它在文档所处的集合中是惟一的  

#### 2.1 文档

 1. 文档是MongoDB的核心概念。多个键及其关联的值有序的放置在一起便是文档。
 	在JavaScript中文档表示为对象：{"greeting": "Hello world!"}  
 	这个文档中只有一个键 greeting 对应的值为 Hello world，大多数情况下，文档经常会包含多个键/值对；
 		{"greeting": "Hello, world!", "foo": 3}
 	文档中的键值对是有序的，
 		{ "foo": 3, "greeting": "Hello, world!"}
 	这个文档和上面的文档完全不同；  
 	
 2. 文档中的值可以是字符串 + 数字等；  
 3. 文档中的键是字符串，除了少数例外情况，键可以使用任意的UTF-8字符；  
 	- 键不能含有\0（空字符）
 	- . 和 $ 有特别的意义，只有特定环境可使用  
 	- 以 _ 开头的键 是保留的  

 4. MongoDB不但区分类型，也区分大小写，鞋面两个文档是不同的
 	{"foo": 3}
 	{"foo": "3"}
 	以下两个也是不同的
 	{"foo": 3}
 	{"Foo": 3}

 5. MongoDB的文档中不能有重复的键：以下文档是非法的
 	{"greeting": "Hello world", "greeting": "Hello, MongoDB"}

#### 2.2 集合

 集合就是一组文档，MongoDB中的文档类似于关系型数据库中的行，集合如同表

##### 2.2.1 无模式

 1. 集合是 无模式 ，意味着一个集合中的文档可能是格式各样的；
 2. 以下两个文档可以存在于同一个集合中
 	{"greeting": "Hello world!"}
 	{"foo": 5}

##### 2.2.2 命名

 1. 集合名需要满足下列条件
 	- 集合名不能是空字符串 ""
 	- 集合名不能含有 \0 字符（空字符）
 	- 集合名不能以 system. 开头
 	- 用户创建的集合名字不能含有保留字符 $ 

 	可以使用子集合组织数据， db.blog.posts 代表 blog.posts

#### 2.3 数据库

 数据库的名字需要满足以下条件
	- 不能是空字符串
	- 不得含有""（空格）、.、$、/、\、和\0（空字符）
	- 应全部小写
	- 最多64字节

#### 2.4 启动MongoDB

 1. 运行mongod文件
	```bash
	linux
	./mongod
	windows
	mongod.exe
	```

#### 2.5 MongoDB shell

 MongoDB自带一个JavaScript shell 可以从命令行和MongoDB实例进行交互。
 1. 运行shell
 	运行mongo 启动shell（启动之前需要先启动mongod）
 2. MongoDB客户端
 	shell其实是一个独立的mongoDB客户端，开启的时候回将数据库连接赋值给全局变量db
 3. shell中的基本操作 CRUD
 	1. 创建（insert）
 		```python
 		# 创建json格式的数据
 		data = {"title": "My Blog Post", "content": "Here's my blog psot", "date": new Date()}
 		# 调用数据库集合进行文档插入
 		db.blog.insert(data)
 		# 查看数据是否被成功插入
 		db.blog.find()
 		```
 	2. 读取（find）
 		```python
 		db.blog.findOne() 只查看一个文档
 		db.blog.find() shell 自动显示最多20个匹配的文档，也可以获取更多
 		```
 	3. 更新（update）
 		更改博客文章 使用update update 至少接受2个参数，第一个需要更新文档的限定条件，第二个是新的文档，假设我们要增加评论。需要增加新的键，对应的值是存放评论的数组。
 		```python
 		data.comments = []
 		```
 		然后执行update操作，用新版本的文档替换标题为 "My Blog Post" 的文章
 		```python
 		db.blog.update({title: "My Blog Post"}, data)
 		```
 		使用如下语句验证
 		```python
 		db.blog.find()
 		```
 	4. 删除（remove）
 		```python
 		db.blog.remove({title: "My Blog Post"})
 		```
 		集合已经被置为空
 4. 使用shell的窍门
 	1. 内置了帮助文档，可以通过help命令查看
 		```python
 		db.help() 查看数据库级别的命令的帮助
 		db.foo.help() 查看集合级别的命令的帮助
 		```
 	2. 了解函数功用的技巧（输入的时候不要输入括号，就会显示函数的JavaScript源代码）
 		```python
 		# 如
 		db.foo.update
 		```
 	3. db.getCollection("集合名称") 避免集合名称也是数据库函数名称的尴尬场景（取不到值）
 	4. x.y 与 x['y'] 等价
 		```javascript
 		var collections = ['posts', 'comments', 'authors'];
 		for (i in collections) {
 			doStuff(db.blog[collections[i]])	
 		}
 		# 而不是下面这种写法 
 		doStuff(db.blog.posts)
 		doStuff(db.blog.comments)
 		doStuff(db.blog.authors)
 		```

#### 2.6 数据类型

 1. 基本数据类型
 	MongoDB的文档类似于JSON
 	JSON的数据类型（null、布尔、数字、字符串、数组、对象）
 	MongoDB支持的数据类型（null、布尔、32/64位整数、64位浮点数、字符串、符号、对象id、日期、正则、代码、二进制数据、最大值、最小值、未定义undefined、数组、内嵌文档）
 2. 数字
 	shell中的数字都被MongoDB当做双精度数，有些64位整数，不能精确的表示为64位浮点数，因此应避免使用shell 进行包含数字的文档的修改和保存；
 3. 日期（使用new Date()）
 	Date对象用作MongoDB的日期类型，创建Date对象通常使用new Date() 而不是 Date()，如果没有new 实际会返回对日期的字符串标识，而不是真正的Date对象
 4. 数组
 	数组是一组值，即可以作为有序对象来操作，也可以作为无序对象来操作；
 	{"things": ['pie', 3.14]}
 5. 内嵌文档（将一个文档作为另外一个文档中键的一个值）
 	如：
 		```json
 		{
 			"name": "John Doe",
 			"address": {
 				"street": "123 Park Street",
 				"city": "Anytown",
 				"state": "NY"
 			}
 		}
 		```
 	上述例子中的 address 的值时另外一个文档，这个文档有自己的 street city state键值；
 6. ```_id和ObjectId```
 	1. ObjectId 
 		MongoDB中存储的文档都必须有个```_id```键，这个键的值可以是任意类型的，默认是一个ObjectId对象。（唯一标识）
 	2. 自动生成_id
 		如果在插入文档的时候没有_id键，系统会自动创建一个。

### 第3章 创建、更新及删除文档

 简介：
 	向集合中添加新文档
 	从集合中删除文档
 	更新现有文档
 	为这些操作选择合适的安全级别和速度
 1. 插入并保存文档
	- 插入是向MongoDB中添加数据的基本方法，使用insert方法插入
	```python
	db.foo.insert({"bar": "baz"})
	这个操作会自动为文档添加一个 _id 键，然后将数保存到MongoDB中。
	```
	1. 批量插入
		避免了多次请求每次都需要处理文档的头部信息的处理
		从外部数据库导入数据，可以使用命令行工具，如：mongoimport
	2. 插入：原理和作用
		转换为BSON格式数据，校验是否包含了_id键，文档不超过4MB，不做其他验证，将数据插入到数据库中；  
		MongoDB在插入数据是不会执行代码，因此不存在注入式攻击的情况；传统的注入式攻击对MongoDB来说是无效的；  
 2. 删除文档

	```python
	db.users.remove()
	```
	删除users集合中的所有文档，但是不会删除集合本身，原有的索引也会保留；  
	
	```python
	db.mailing.list.remove({'opt-out': true})
	```
	删除mailing.list 集合中所有的opt-out为true的人  
	删除数据是永久的，不能撤销，不可恢复  

	删除速度
		```python
		# 创建一百万和虚拟元素
		for i in range(1000000):
			collection.insert({'foo': 'bar', 'baz': i, 'z': 10-i})
		```
		```python
		# 删除刚才创建的所有文档，并记录所花费时间，通过remove
		import time
		
		from pymongo import Connection

		db = Connection().foo
		collection = db.bar

		start = time.time()

		collection.remove()
		collection.find_one()

		total = time.time() - start
		print("%d seconds" % total)
		```
		书中样例消耗 46.08秒

		使用db.drop_collection('bar') 替代 remove 和 find_one 只花费0.01秒（优势：速度快；劣势：不能限制条件，整个集合被删除，所有的索引被删除）  

 3. 更新文档

 update 更新已经存入数据库的文档  
 两个参数一个是查询文档，用来找出要更新的文档，一个是修改器，描述对找到的文档做哪些修改（原子性，两个更新同时发生，先到服务器的先执行，之后执行另外一个）  

 1. 文档替换
 	将原有文档中的几个属性作为一个新的键/文档来存储
 	```python
 	{
 		"_id": ObjectId("**********"),
 		"name": "joe",
 		"friends": 32,
 		"enemies": 2
 	}
 	# 修改为
 	{
 		"_id": ObjectId("**********"),
 		"username": "joe",
 		"relationships": 
 		{
 			"friends": 32,
 			"enemies": 2,
 		}
 	}
 	```
 	可通过一下命令进行文档替换
 	```python
 	> var joe = db.users.findOne({'name': 'joe'});
 	> joe.relationships = {"friends": joe.friends, "enemies": joe.enemies};
 	> joe.username = joe.name;
 	> delete joe.friends;
 	> delete joe.enemies;
 	> delete joe.name;
 	> db.users.update({'name': 'joe'}, joe);
 	```
 	之后通过findOne查看更新后的文档结构即可；

 	如果文档中有多个相同name的文档，我们在使用
 	```python
 	db.users.update({'name': 'joe'}, joe);
 	```
 	就会报错,提示我们的_id键值重复；为避免这种情况，我们需要确保更新总是指向唯一文档，例如通过_id进行匹配；  

 2. 使用修改器
 通常文档只有一部分需要修改，就需要使用原子的更新修改器，可以使这种部分更新极为高效；
 	```python
 	# 网站分析数据，增加访问计数器
 	{
 		"_id": ObjectId("***********"),
 		"url": "www.example.com",
 		"pageviews": 52
 	}
 	每次有人访问，即可通过url找到文档，仅修改pageviews的值即可；
 	> db.analytics.update({'url': 'www.example.com'}, {"$inc": {"pageviews": 1}})
 	# 之后通过find命令查看校验
 	db.analytics.find()
 	```
 	1. "$set" 修改器入门
 		"$set"用来指定一个键的值，如果键不存在，则创建它。（例如给用户添加喜欢的书籍）  
 		```python
 		> db.users.update({'name', 'joe'}, {'$set': {'favorite book':'war and peace'}});
 		# 更新为另外一个本书
 		> db.users.update({'name', 'joe'}, {'$set': {'favorite book':'green eggs and ham'}});
 		# "$set"修改数据类型 字符串到数组
 		> db.users.update({'name', 'joe'}, {'$set': {'favorite book':['green eggs and ham', 'war and peace']}});
 		# 不喜欢读书，删除favorite book 键 "$unset"
 		db.users.update({'name': 'joe'}, {'$unset': {'favorite book': 1}})
 		```
 		在进行增加、修改、删除键的时候，应该使用$ 修改器，避免修改文档中的所有内容；  
 	
 	2. 增加和减少
 		"$inc" 修改器，用来增加已有键的值，或者在键不存在的时候创建一个键，对于分析数据、因果关系、投票或者是其他有变化数值的地方，使用这个比较方便；  
 		"$inc" 修改器的键的值必须为数字，不能使用字符串、数组或其他非数字的值；  

 	3. 数组修改器
 		数组操作，只能用来指为数组的键上，$push $pop 
 		如果键已存在，"$push"会向已有的数组末尾加入一个元素，要是没有就会创建一个新的数组。
 		```python
 		# 给存储博客文章添加评论数组 键：comments
 		db.blog.posts.findOne()
 		#
 		db.blog.posts.update(
 			{'title': 'A blog post'}, 
 			{"$push": {
 				"comments": {
 					"name": "joe",
 					"email": "joe@example.com",
 					"content": "nice post."
 				}
 			}}
 		)
 		```
 		```python
 		# 再添加一条评论
 		> db.blog.posts.update(
 			{'title': 'A blog post'}, 
 			{"$push": {
 				"comments": {
 					"name": "bob",
 					"email": "bob@example.com",
 					"content": "good post."
 				}
 			}}
 		)
 		```
 		```python
 		# 如果一个值不在一个数组中，就把这个值添加到数组中 使用"$ne"来实现
 		db.papers.update(
 			{"authors cited": {"$ne": "Richie"}},
 			{"$push": {"authors cited": "Richie"}}
 		)
 		```
 		```python
 		# 也可以使用 $addToSet 完成（因为有些情况下 $ne 行不通）
 		# 使用addToSet可以避免重复，在一个数组中添加的值不会重复；
 		# 将$addToSet 和 $each 组合起来可以一次向一个数组中添加多个不同的值，但是 $ne + $push 就不行，如一次添加多个邮件地址
 		> db.users.update(
 			{"_id": ObjectId("***********")},
 			{"$addToSet": {
 				{"emails": {
 					"$each": ['joe@php.net', 'joe@example.com', 'joe@python.org']
 				}}
 			}})
 		```
 		```python
 		# 从数组中删除元素的方法  $pop 从任意一端删除元素
 		{"$pop": {key: 1}} 从数组末尾删除一个元素
 		{"$pop": {key: -1}} 从数组头部删除一个元素
 		```
 		```python
 		# 基于特定条件 删除元素，而不仅仅是位置 "$pull"
 		> db.lists.insert({"todo": ['dishes', 'laundry', 'dry cleaning']})
 		想要把 laundry 放到第一位，可以先删除，再插入
 		> db.lists.update({}, {"$pull": {"todo": "laundry"}})
 		# $pull 是根据值，将匹配到的数组中的所有元素，从数组中删除！
 		```

 	4. 数组的定位修改器
 		以包含评论的博客文章为例（多条评论）
 		```python
 		# 增加第一个评论的投票数量
 		> db.blog.update(
 			{"post": post_id},
 			{"$inc": {"comments.0.votes": 1}}
 			)
 		```
 		MongoDB中还有一个定位操作符 $ ，用来定位查询文档中已经匹配的元素，并进行更新，
 		```python
 		> db.blog.update(
 			{'comments.author': 'John'},
 			{"$set": {"comments.$.author": "Jim"}}
 		# 定位符只更新第一个匹配的元素，因此如果John有不止一个评论，那么只有他的第一条评论中的名字会被更改；
 			)
 		```
 	5. 修改器的速度
 		"$inc" 可以就地修改，不需要改变文档大小，只需要修改键的值；
 		数组修改器可能改变了文档大小，如："$set"，速度就会相对慢一些；

 		```python
 		# "$inc" 和 "$push"的区别
 		from pymongo import Connection
 		import time
 		db = Connection().performance_test
 		db.drop_collection("updates")
 		collection = db.updates
 		collection.insert({"x": 1})
 		# make sure the insert is complete before we start timing
 		collection.find_one()
 		start = time.time()
 		for i in range(100000):
 			collection.update({}, {"$inc": {"x": 1}})
 		# make sure the updates are complete before we stop timing
 		collection.find_one()
 		print(time.time() - start)
 		# 书中数据， 7.33秒 平均每秒有13000次更新
 		# 
 		for i in range(100000):
 			collection.update({}, {"$push": {"x": 1}})
 		# 书中数据，共花费 67.58秒，平均每秒不到1500次
 		```
 
 3. upsert
 	upsert 特殊更新，若没有文档符合更新条件，就会以这个条件和更新的文档为基础创建一个新的文档。如果找到了，就正常更新。  
 	```python
 	# 没有upsert 更新文档数据
 	// check if we have entry for this page
 	blog = db.analytics.findOne({url: '/blog'})
 	// if we do,add one to the number of views and save
 	if (blog) {
 		blog.pageviews++;
 		db.analytics.save(blog);
 	}
 	// otherwise,create a new document for this page
 	else {
 		db.analytics.save({url: '/blog', pageviews: 1})
 	}
 	这样的形式需要我们每次在进行数据更新的时候，需要先到数据库中进行查询校验。
 	# 
 	# 使用upsert修改器进行更新
 	update 的第三个参数标识这是个upsert
 	db.analytics.update({"url": '/blog'}, {"$inc": {"visits": 1}}, true)
 	```

 save shell帮助程序
 	save 是一个shell函数，在文文档存在时更新，文档呢不存在是创建，只有一个参数，如果这个文档有_id 键，save会调用upsert，否则调用插入。  
 	```JavaScript
 	var x = db.foo.findOne()
 	x.num = 42
 	db.foo.save(x)
 	db.foo.update({'_id': x._id}, x)
 	```
 4. 更新多个文档
 	update的第4个参数设置为 true 即可（显式指明需要更新多个文档）
 	```python
 	# 给每一个特定日期生日的用户一份生日礼物
 	db.users.update({'birthday': '10/13/1978'}, {"$set": {'gift': "Happy Birthday"}}, false, true)
 	#
 	想要知道多文档更新到底更新了多少文档，可以使用 getLastError命令（getLastOpStatus）
 	> db.count.update({x: 1}, {'$inc': {'x': 1}}, false, true)
 	> db.runCommand({'getLastError': 1})
 	返回的结果中 键值为n对应的值即为更新的文档数量
 	```
 5. 返回已更新的文档
 	getLastError 仅能获取有限信息，不能返回已更新的文档
 	可以通过findAndModify获取

 	```python
 	# 两个例子
 	> ps = db.runCommand(
 		{
 			'findAndModify': 'processes',
 			'query': {'status': 'READY'},
 			'sort': {'priority': -1},
 			'update': {'$set': {'status': "RUNNING"}}
 		}
 	).value
 	> do_something(ps)
 	> db.process.update({"_id": ps._id}, {'$set': {'status': 'DONE'}})
 	```
 	```python
 	findAndModify 中既有update 也有 remove
 	> ps = db.runCommand({'findAndModify': 'processes',
 			'query': {'status': 'READY'},
 			'sort': {'priority': -1},
 			'remove': true
 		}
 	).value
 	```
 	findAndModify 命令中每个键对应的值如下
 	- findAndModify
 	字符串，集合名
 	- query
 	查询文档，用来检索文档的条件
 	- sort
 	排序结果的条件
 	- update
 	修改器文档，对所找到的文档执行的更新
 	- remove
 	布尔类型，标识是否删除文档
 	- new
 	布尔类型，表示返回的是更新前的文档还是更新后的文档。默认是更新前的文档。
 	update 和 remove 必须有一个，也只能有一个，如果匹配不到，会返回一个错误。

 4. 瞬间完成

 1. 安全操作
 	对于日志记录、用户点击或者分析数据什么的，客户端发送数据后可以不用理会是否被服务器接受到，也不接收返回。但是对于电子商务系统等，还是需要花时间确保订单的顺利，执行时检查到了错误，还可以重来。
 	可以通过 getLastError进行错误捕捉，然后根据语言特点进行校验即可；
 
 2. 捕获“常规”错误
 	同一个集合中不能出现两个_id值相同的文档，

 5. 请求和连接
 
 请求和连接
 	数据库为每一个MongoDB数据库连接创建一个队列，存放每个连接的请求。
 	PS：每个连接都有独立的队列，要是打开两个shell 会有两个数据库连接，会存在一个shell中插入数据，而另外一个shell中暂时查询不到的情况。

### 第4章 查询

 - 使用find findOne函数和查询文档对数据执行查询
 - 使用$条件查询实现范围、集合包含、不等式等其他查询
 - 有些查询用查询文档，甚至$条件语句都不能表达。对于这种查询，可以使用$where子句，用强大的JavaScript来表达。
 - 查询将会返回一个数据库游标，游标只有在你需要的时候才会惰性的批量返回文档。
 - 还有很多对游标执行元操作，包括忽略一定数量的结果，限定返回数量，对结果排序。

 1. find简介
 	- MongoDB使用find进行查询，返回集合中文档的子集，子集的范围是从0个文档到整个集合。第一个参数决定了要返回哪些文档，其形式也是一个文档。
 	- 空的查询文档{}会匹配集合全部内容，若不指定，默认就是{}
 	如（返回集合c中的所有内容）：
 		```python
 		db.c.find()
 		```
 	```python
 	# 查找所有age的值为27的文档
 	> db.users.find({'age': 27})
 	# 查找值为joe的username的键
 	> db.users.find({'username': 'joe'})
 	# 可以指定查询的多个条件内容
 	> db.users.find({'username': 'joe', 'age': 27})
 	```
 	1. 返回指定的键
 		通过find的第二个参数指定返回的键
 		```python
 		# 只对用户的username 和 email键感兴趣
 		> db.users.find({}, {'username': 1, 'email': 1})
 		(可以看到即使不指定_id键也会被返回)
 		```
 		通过find的第二个参数剔除掉查询结果中的某个键值对
 		```python
 		# 不希望查询结果中包含 fatal_weakness键
 		> db.users.find({}, {'fatal_weakness': 0})
 		# 也可以用来防止返回"_id"
 		db.users.find({}, {'username': 1, '_id': 0})
 		```
 	2. 限制
 		商品的销售控制，原有库存和存货两个键进行文档查询，可以通过改写文档：添加键initial_stock（初始存货） 和 in_stock 进行改写和判断
 
 2. 查询条件
 	- 复杂条件的查询， 范围、OR子句、取反
 	1. 查询条件
 		$lt $lte $gt $gte 是全部的比较操作符，分别对应< <= > >=
 		```python
 		# 查询18-30岁（含）的用户
 		> db.users.find({'age': {'$gte': 18, '$lte': 30}})
 		```
 		```python
 		这样的范围查询对日期尤为有用，如：查找2007年1月1日前注册的人
 		> start = new Date("01/01/2007")
 		> db.users.find({"registered": {"$lt": start}})
 		```
 		```python
 		# 查询所有名字不为joe的用户
 		> db.users.find({"username": {"$ne": "joe"}})
 		"$ne" 能用于所有类型的数据
 		```
 	2. OR查询
 		"$in" 能查询一个键的多个值，
 		"$or" 更加通用，可以用来完成多个键值的任意给定值。
 		对于单一键有多个值与之匹配的话，需要使用$in加一个条件数组；
 		$in 比较灵活，可以指定不同类型的条件和值，如：在进行用户的id 和 迁移成用户名的过程中，做到两者兼顾的查询：
 		```python
 		> db.users.find({"user_id": {"$in": [12345, 'joe']}})
 		既可以匹配user_id 为 12345的值，也可以匹配user_id 为 joe的信息
 		```
 		与$in相对的条件过滤操作符是 $nin，返回与所有条件都不匹配的文档
 		>
 		$in 能够对单个键进行or查询，但是不能实现如下查询：ticket_no 为 775 或者 winner 为 true的文档，针对以上情况，我们使用$or 包含可能的条件作为数组进行查询；
 		```python
 		> db.raffle.find({'$or': [{"ticket": 775}, {"winner": true}]})
 		```
 		```python
 		$or 中也可嵌套 $in 操作符
 		db.raffle.find({"$or": [{"ticket_no": {"$in": [725, 231, 432]}}, 
 								{"winner": true}]})
 		```
 		and 查询尽可能用最少的条件限定结果的范围，使用or查询，第一个条件尽可能匹配更多的文档。
 	3. $not
 		$not 是元条件句，可以用在任何其他条件之上
 		```python
 		如：
 		$mod 查询结果 除以数组中第一个参数，余数等于第二个参数，则符合要求 - 输出
 		取出id_num为 1 6 11 16等的用户
 		> db.users.find({"id_num": {"$mod": [5, 1]}})
 		取出id_num为 2 3 4 5 7 8 9 12等的用户，需要使用$not
 		> db.users.find({"id_num": {"$not": {"$mod": [5, 1]}}})
 		```
 	4. 条件语句的规则
 		一个键可以有多个条件，但是不能对应多个更新修改器，如文档不能同时含有{"$inc": 1}, "$set": {"age": 40}
 3. 特定于类型的查询
 	1. null
 		mongodb中 null不仅能匹配对应键的值为null的情况，也能匹配键不存在的情况
 		所以在进行键对应值是否为null的查询时，还需要判断键是否存在
 		> db.c.find({"z": {"$in": [null], "exists": true}})
 	2. 正则表达式
 		mongodb 使用的是Perl兼容的正则表达式
 		> db.users.find({"name": /joe/i})  忽略大小写
 		> db.users.find({"name": /joey?/i})  忽略大小写，ie匹配 joe 和 joey
 		可以为前缀型正则表达式（如：/^joey/）查询创建索引
 		mongodb中也可以保存正则表达式，作为键的值
 	3. 查询数组
 		如果一个键对应的值是一个数组，我们可以通过条件罗列的形式进行标识
 		> db.food.insert({"fruit": ["apple", "banana", "peach"]})
 		> db.food.find({"fruit": "banana"})可以成功匹配该文档
 		类似于：
 		> db.food.find({"fruit": "apple", "fruit": "banana", "fruit": "peach"})
 		1. $all 
 		如果需要通过多个元素来匹配数组，需要使用"$all"，可以匹配一组元素。
 			```python
 			> db.food.insert({"_id": 1, "fruit": ["apple", "banana", "peach"]})
 			> db.food.insert({"_id": 2, "fruit": ["apple", "banana", "peach"]})
 			> db.food.insert({"_id": 3, "fruit": ["apple", "banana", "peach"]})
 			```
 			找到既有apple 又有banana的文档，需要使用 all
 			db.food.find({"fruit": {"$all": ["apple", "banana"]}})
 			>
 			如果只有一个元素，是否使用all 没有区别
 			>

 			```python
 			查询指定位置的匹配，通过 key.index 的语法指定下标
 			db.food.find({"fruit.2": "peach"})
 			```
 		2. $size
 		(查询指定长度的数组)
 		db.food.find({"fruit": {"$size": 3}})
 		3. $slice
 		从find中返回数组的子集合
 		```bash
 		假设有一个博客文章的文档，想要返回前10条评论
 		db.blog.posts.findOne(criteria, {"comments": {"$slice": 10}})
 		```
 		也可以接受偏移值和返回的元素数量
 		```bash
 		返回后10条评论
 		db.blog.posts.findOne(criteria, {"comments": {"$slice": -10}})
 		偏移值和返回元素数量
 		db.blog.posts.findOne(criteria, {"comments": {"$slice": [23, 10]}})
 		```
 	4. 查询内嵌文档
 		1. 查询内嵌文档和普通文档完全相同
 			> db.people.find({"name": {"first": "joe", "last": "Schmoe"}})
 			> db.people.find({"name.first": "joe", "name.last": "Schmoe"})
 			第二种可以在 匹配元素增加键值，改变find参数时正常匹配；
 4. $where查询
 	1. 场景-比较文档中的两个键的值是否相等
 		db.food.find({"$where": function () {
 			for (var current in this) {
	 			for (var other in this) {
		 			if (current != other && this[current] == this[other]) {
			 			return true;
			 		}
		 		}
	 		}
	 	}});
	 	>
	 	db.foo.find({"$where": "this.x + this.y == 10"})
	 	>
	 	db.foo.find({"$where": "function() { return this.x + this.y == 10; }"})
	 	>
	 	where 查询比较耗时
 5. 游标
 	1. limit、skip和sort
 		limit(3)只返回3个元素（少于3个返回全部）
 		skip(3) 跳过检索结果中前三个结果
 		sort 以对象为参数，一组键值对，键是文档的键名称，值代表排序方向（1，升序；-1 降序）如果有多个键值对，则按照顺序进行排序；
 		>
 		搜索mp3 每页返回50个结果，按照价格从高到低排序
 		db.stock.find({"desc": "mm3"}).limit(50).sort({"price": -1})
 		如果结果数量较大，会导致性能降低，应该尽量避免
 		>
 		>
 		比较顺序，（sort） 混合类型的键排序
 		从小到大::
 		>>   
 		最小值
 		null
 		数字（整型、长整型、双精度）
 		字符串
 		对象、文档
 		数组
 		二进制数据
 		对象ID
 		布尔型
 		日期型
 		时间戳
 		正则
 		最大值
 		>>   
 	2. 避免使用skip略过大量结果
 		1. 不使用skip进行分页
 		2. 随机选取文档
 			```bash
 			> //do not use
 			> var total = db.foo.count()
 			> var random = Math.floor(Math.random()*total)
 			> db.foo.find().skip(random).limit(1)
 			```
 			```bash
 			好的方法 为每一个文档添加额外的随机键，然后在查询时，生成一个随机值，根据这个值进行查询即可
 			db.people.insert({"name": "joe", "random": Math.random()})
 			db.people.insert({"name": "john", "random": Math.random()})
 			db.people.insert({"name": "jim", "random": Math.random()})
 			>
 			> var random = Math.random()
 			> result = db.foo.findOne({"random": {"$gt": random}})
 			>
 			> 为了避免 恰好所有文档中的随机数都小于查询时生成的随机数的情况
 			> if (result == null) {
 			> 	  result = db.foo.findOne({"random": {"$lt": random}})	
 			> }
 			```
 	3. 高级查询选项
 		查询分为包装和普通的两类，
 		> 普通
 		> var cuisor = db.foo.find({"foo": "bar"})
 		> 包装
 		> var cursor = db.foo.find({"foo": "bar"}).sort({"x": 1})
 		包装查询，实际不是将{"foo": "bar"} 作为查询发送到数据库，而是将查询包装到一个更大的文档中，shell将{"foo": "bar"} 转换为{"$query": {"foo": "bar"}, "$orderby": {"x": 1}}
 	4. 获取一致结果
 		在MongoDB文档存取过程中，如果取出文档，修改后进行存储是，原先的预留空间不足，则会将该文档放在集合的最后，导致文档被移动，后续的查询，会将之前查询的文档再次返回；
 		> 
 		因此我们可以使用$snapshot 快照选项进行处理，这样的话，查询就是针对不变的集合视图运行的；
 	5. 游标内幕
 		分为客户端游标和数据库游标
 		游标在客户端已经不再作用域内了，驱动会向服务器发送专门的消息，让其销毁游标。

### 第5章 索引
 - 索引： 加速查询 类似于课本的目录
 1. 索引简介
 	例子：db.people.find({"username": "mark"})
 	> 当查询中仅适用一个键，可以对键建立索引，提高查询速度，创建索引需要使用ensureIdex方法：
 	> db.people.ensureIndex("username": 1)
 	> 同一集合，同样的索引只需要创建一次，反复创建无用。
 	> 对指定键的索引，只会加速对该键的查询，对其他的查询没有性能提升（即使包含了被索引的键）
 	> 
 	> db.people.find({"date": date1}).sort({"date": 1, "username": 1})
 	> 
 	这时服务器必须“查找整本书”找到想要的日期，这个过程称为：表扫描；尽量要避免服务器进行表扫描。
 	> 
 	```bash
 	上面的查询可以提前建立 date 和 username的索引
 	> db.ensureIndex({"date": 1, "username": 1})
 	传递给ensureIndex的文档形式和传递给sort的文档形式一样，一组值为1或-1的键，标识索引创建的方向。
 	```
 	有个索引{"a": 1, "b": 1, "c": 1, ..., "z": 1} 实际上相当于 {"a": 1}, {"a": , "b": 1}, {"a": 1, "b": 1, "c": 1} ... 等索引，只有使用索引前部的查询才能使用该索引。
 	> 
 	> 缺点：
 	每次进行数据 插入、更新、删除都会产生额外的开销。因为数据库不但需要执行操作，还需要再索引中标记。每个集合默认最大索引数64个。
 	一定不要索引每一个键，会导致插入非常慢，还占用大量空间；
 	如果要返回集合中一半以上的数据，表扫描比每条文档进行索引更快。
 	> 
 	1. 扩展索引
 		建立索引时需要考虑：
 		- 会做什么样的查询，哪些键需要索引？
 		- 每个键的索引方向是怎样的？
 		- 如何应对扩展，有没有中不同的键的排列可以使常用数据更多的保留在内存中？
 	2. 索引内嵌文档中的键
 		和普通的键的索引建立类似
 		db.blog.ensureIndex({"comments.date": -1})
 	3. 




### 第6章 聚合
### 第7章 进阶指南
### 第8章 管理
### 第9章 复制
### 第10章 分片
### 第11章 应用举例
### 附录A 安装MongoDB
### 附录B mongo：MongoDB shell
### 附录C 深入MongoDB内部
