《Redis实战》
## 一、Redis 五种数据类型
#### 1.Redis 中的字符串
- set key value  # 创建字符串键值对
	```bash
	set hello world
	```
- get key # 根据键 获取值
	```bash
	get hello
	```
- del key # 删除redis中的值
	```bash
	del hello
	```

#### 2. Redis 列表
- lpush rpush 分别从左右侧推元素进入列表
	```bash
	lpush list-key item
	lpush list-key item item2 item3
	```
- lpop rpop 分别从左右侧 从列表中 弹出元素
	```bash
	lpop list-key
	rpop list-key
	```
- lindex 命令用于获取列表中给定位置的一个元素
    ```bash
	lindex 1
	```
- lrange 命令用于获取列表在给定范围上的所有元素、
    ```bash
	lrange list-key 0 -1
	```

#### 3. Redis 集合
##### PS：集合中不能插入重复的元素
- sadd 添加元素到集合中
	```bash
	sadd set-key item
	sadd set-key item2
	```
- smembers 返回集合中所有元素
    ```bash
	smembers set-key
	```
- sismember 判断给定元素是否在集合中
    ```bash
	sismentber set-key item3
	```
- srem 如果集合中存在给定元素，则从集合中删除
    ```bash
	srem set-key item2
	```

#### 4. Redis 散列
- hset 在散列中关联起给定的键值对
	```bash
	hset hash-key sub-key1 value1  # 定义
	hset hash-key sub-key2 value2 
	```
- hget 获取指定的散列键的值
	```bash
	hget hash-key sub-key2
	```
- hgetall 获取散列包含的所有键值对
	```bash
	hgetall hash-key
	```
- hdel 如果给定的键存在于散列中，那么移除这个键
	```bash
	hdel hash-key sub-key1
	hdel hash-key sub-key2
	```

#### 5. Redis 的有序集合
CMD 格式操作
- zadd 将一个带有给定分值的成员添加到有序集合中
	```bash
	zadd zset-key 728 member0
	zadd zset-key 545 member1
	```
- zrange 根据元素在有序排列中所处的位置，从有序集合中获取多个元素
	```bash
	zrange zset-key 0 -1
	zrange zset-key 0 -1 withscores
	```
- zrangebyscores 获取有序集合在给定分支范围内的所有元素

- 如果给定的成员存在于有序集合，那么移除这个成员


Python环境下
from redis import Redis
client = Redis(host='127.0.0.1', port=6379)
client.zdd('key', {'column': score})
