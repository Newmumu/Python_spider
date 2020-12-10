### 随机数据生成器，光靠random是远远不够的，来玩下Faker模块

### 一个好玩的第3方库：伪装者：Faker

### 安装
### 国内源：
### 基本使用
### 常用方法

1. 地理信息类
1. 基础信息类
1. 邮箱信息类
1. 网络基础信息类
1. 浏览器信息类
1. 数字信息
1. 文本加密类
1. 时间信息类


在软件需求、开发、测试过程中，有时候需要使用一些测试数据，针对这种情况，我们一般要么使用已有的系统数据，要么需要手动制造一些数据。

在手动制造数据的过程中，可能需要花费大量精力和工作量，现在好了，有一个Python包能够协助你完成这方面的工作。

### 什么是Faker
	Faker是一个Python包，开源的GITHUB项目，主要用来创建伪数据，使用Faker包，无需再手动生成或者手写随机数来生成数据，只需要调用Faker提供的方法，即可完成数据的生成。
	
	项目地址：https://github.com/joke2k/faker

#### 安装
```python
pip install Faker
```

如果下载速度比较慢的话，可以使用国内镜像源来下载

国内源：
例如：pip3 install -i https://pypi.doubanio.com/simple/ faker

清华：https://pypi.tuna.tsinghua.edu.cn/simple
阿里云：http://mirrors.aliyun.com/pypi/simple/
中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
华中理工大学：http://pypi.hustunique.com/
山东理工大学：http://pypi.sdutlinux.org/
豆瓣：http://pypi.douban.com/simple/

#### 基本使用
```python
from faker import Faker
#创建对象，默认生成的数据为为英文，使用zh_CN指定为中文
fake = Faker('zh_CN')
print(fake.name())#随机生成姓名
print(fake.address())#随机生成地址
print(fake.phone_number())#随机生成电话号码
print(fake.pystr())#随机生成字符串
print(fake.email())#随机生成邮箱地址
for i in range(10):
	print(fake.name())#随机生成10个姓名
```
```python
输出：
徐博
云南省玉市璧山梧州路p座 523028
13039830591
RPHadhNxNMISoBTbQbQn
yili@taogang.net
张淑英
叶燕
陈琳
王俊
胡秀荣
阮淑英
徐娟
黄冬梅
梁丽华
袁琴
```

#### 常用方法

##### 地理信息类
```python
city_suffix()：市，县
country()：国家
country_code()：国家编码
district()：区
geo_coordinate()：地理坐标
latitude()：地理坐标(纬度)
longitude()：地理坐标(经度)
postcode()：邮编
province()：省份
address()：详细地址
street_address()：街道地址
street_name()：街道名
street_suffix()：街、路
```

##### 基础信息类
```python
ssn()：生成身份证号
bs()：随机公司服务名
company()：随机公司名（长）
company_prefix()：随机公司名（短）
company_suffix()：公司性质，如‘信息有限公司’
fake.credit_card_expire(start=‘now’, end=’+10y’, date_format=’%m/%y’)：- - 随机信用卡到期日如’03/30’
credit_card_full()：生成完整信用卡信息
credit_card_number()：信用卡号
credit_card_provider()：信用卡类型
credit_card_security_code()：信用卡安全码
job()：随机职位
first_name_female()：女性名
first_name_male()：男性名
name()：随机生成全名
name_female()：男性全名
name_male()：女性全名
phone_number()：随机生成手机号
phonenumber_prefix()：随机生成手机号段，如139
```

#### 邮箱信息类
```python
ascii_company_email()：随机ASCII公司邮箱名
ascii_email()：随机ASCII邮箱：
company_email()：
email()：
safe_email()：安全邮箱
```

#### 网络基础信息类
```python
domain_name()：生成域名
domain_word()：域词(即，不包含后缀)
ipv4()：随机IP4地址
ipv6()：随机IP6地址
mac_address()：随机MAC地址
tld()：网址域名后缀(.com,.net.cn,等等，不包括.)
uri()：随机URI地址
uri_extension()：网址文件后缀
uri_page()：网址文件（不包含后缀）
uri_path()：网址文件路径（不包含文件名）
url()：随机URL地址
user_name()：随机用户名
image_url()：随机URL地址
````

####浏览器信息类
```python
chrome()：随机生成Chrome的浏览器user_agent信息
firefox()：随机生成FireFox的浏览器user_agent信息
internet_explorer()：随机生成IE的浏览器- user_agent信息
opera()：随机生成Opera的浏览器user_agent信息
safari()：随机生成Safari的浏览器user_agent信息
linux_platform_token()：随机Linux信息
user_agent()：随机user_agent信息
```

#### 数字信息
```python
numerify()：三位随机数字
random_digit()：0~9随机数
random_digit_not_null()：1~9的随机数
random_int()：随机数字，默认0~9999，可以通过设置min,max来设置
random_number()：随机数字，参数digits设置生成的数字位数
pyfloat()：left_digits=5 #生成的整数位数, right_digits=2 #生成的小数位数, - - positive=True #是否只有正数
pyint()：随机Int数字（参考random_int()参数）
pydecimal()：随机Decimal数字（参考pyfloat参数）
```

#### 文本加密类
```python
pystr()：随机字符串
random_element()：随机字母
random_letter()：随机字母
paragraph()：随机生成一个段落
paragraphs()：随机生成多个段落
sentence()：随机生成一句话
sentences()：随机生成多句话，与段落类似
text()：随机生成一篇文章
word()：随机生成词语
words()：随机生成多个词语，用法与段落，句子，类似
binary()：随机生成二进制编码
boolean()：True/False
language_code()：随机生成两位语言编码
locale()：随机生成语言/国际 信息
md5()：随机生成MD5
null_boolean()：NULL/True/False
password()：随机生成密码,可选参数：length：密码长度；special_chars：是否能使用特殊字符；digits：是否包含数字；upper_case：是否包含大写字母；lower_case：是否包含小写字母
sha1()：随机SHA1
sha256()：随机SHA256
uuid4()：随机UUID
```

#### 时间信息类
```python
date()：随机日期
date_between()：随机生成指定范围内日期，参数：start_date，end_date
date_between_dates()：随机生成指定范围内日期，用法同上
date_object()：随机生产从1970-1-1到指定日期的随机日期。
date_time()：随机生成指定时间（1970年1月1日至今）
date_time_ad()：生成公元1年到现在的随机时间
date_time_between()：用法同dates
future_date()：未来日期
future_datetime()：未来时间
month()：随机月份
month_name()：随机月份（英文）
past_date()：随机生成已经过去的日期
past_datetime()：随机生成已经过去的时间
time()：随机24小时时间
timedelta()：随机获取时间差
time_object()：随机24小时时间，time对象
time_series()：随机TimeSeries对象
timezone()：随机时区
unix_time()：随机Unix时间
year()：随机年份
```


#### dir(faker) 的结果
```python
>>> dir(faker)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_factories', '_factory_map', '_locales', '_map_provider_method', '_select_factory', '_unique_proxy', '_weights', 'add_provider', 'address', 'am_pm', 'android_platform_token', 'ascii_company_email', 'ascii_email', 'ascii_free_email', 'ascii_safe_email', 'bank_country', 'bban', 'binary', 'boolean', 'bothify', 'bs', 'building_number', 'cache_pattern', 'catch_phrase', 'century', 'chrome', 'city', 'city_name', 'city_suffix', 'color', 'color_name', 'company', 'company_email', 'company_prefix', 'company_suffix', 'coordinate', 'country', 'country_calling_code', 'country_code', 'credit_card_expire', 'credit_card_full', 'credit_card_number', 'credit_card_provider', 'credit_card_security_code', 'cryptocurrency', 'cryptocurrency_code', 'cryptocurrency_name', 'csv', 'currency', 'currency_code', 'currency_name', 'currency_symbol', 'date', 'date_between', 'date_between_dates', 'date_object', 'date_of_birth', 'date_this_century', 'date_this_decade', 'date_this_month', 'date_this_year', 'date_time', 'date_time_ad', 'date_time_between', 'date_time_between_dates', 'date_time_this_century', 'date_time_this_decade', 'date_time_this_month', 'date_time_this_year', 'day_of_month', 'day_of_week', 'del_arguments', 'dga', 'district', 'domain_name', 'domain_word', 'dsv', 'ean', 'ean13', 'ean8', 'email', 'factories', 'file_extension', 'file_name', 'file_path', 'firefox', 'first_name', 'first_name_female', 'first_name_male', 'first_name_nonbinary', 'first_romanized_name', 'fixed_width', 'format', 'free_email', 'free_email_domain', 'future_date', 'future_datetime', 'generator_attrs', 'get_arguments', 'get_formatter', 'get_providers', 'hex_color', 'hexify', 'hostname', 'http_method', 'iban', 'image_url', 'internet_explorer', 'ios_platform_token', 'ipv4', 'ipv4_network_class', 'ipv4_private', 'ipv4_public', 'ipv6', 'isbn10', 'isbn13', 'iso8601', 'items', 'job', 'json', 'language_code', 'language_name', 'last_name', 'last_name_female', 'last_name_male', 'last_name_nonbinary', 'last_romanized_name', 'latitude', 'latlng', 'lexify', 'license_plate', 'linux_platform_token', 'linux_processor', 'local_latlng', 'locale', 'locales', 'localized_ean', 'localized_ean13', 'localized_ean8', 'location_on_land', 'longitude', 'mac_address', 'mac_platform_token', 'mac_processor', 'md5', 'mime_type', 'month', 'month_name', 'msisdn', 'name', 'name_female', 'name_male', 'name_nonbinary', 'null_boolean', 'numerify', 'opera', 'paragraph', 'paragraphs', 'parse', 'password', 'past_date', 'past_datetime', 'phone_number', 'phonenumber_prefix', 'port_number', 'postcode', 'prefix', 'prefix_female', 'prefix_male', 'prefix_nonbinary', 'profile', 'provider', 'providers', 'province', 'psv', 'pybool', 'pydecimal', 'pydict', 'pyfloat', 'pyint', 'pyiterable', 'pylist', 'pyset', 'pystr', 'pystr_format', 'pystruct', 'pytimezone', 'pytuple', 'random', 'random_choices', 'random_digit', 'random_digit_not_null', 'random_digit_not_null_or_empty', 'random_digit_or_empty', 'random_element', 'random_elements', 'random_int', 'random_letter', 'random_letters', 'random_lowercase_letter', 'random_number', 'random_sample', 'random_uppercase_letter', 'randomize_nb_elements', 'rgb_color', 'rgb_css_color', 'romanized_name', 'safari', 'safe_color_name', 'safe_domain_name', 'safe_email', 'safe_hex_color', 'seed', 'seed_instance', 'seed_locale', 'sentence', 'sentences', 'set_arguments', 'set_formatter', 'sha1', 'sha256', 'simple_profile', 'slug', 'ssn', 'street_address', 'street_name', 'street_suffix', 'suffix', 'suffix_female', 'suffix_male', 'suffix_nonbinary', 'swift', 'swift11', 'swift8', 'tar', 'text', 'texts', 'time', 'time_delta', 'time_object', 'time_series', 'timezone', 'tld', 'tsv', 'unique', 'unix_device', 'unix_partition', 'unix_time', 'upc_a', 'upc_e', 'uri', 'uri_extension', 'uri_page', 'uri_path', 'url', 'user_agent', 'user_name', 'uuid4', 'weights', 'windows_platform_token', 'word', 'words', 'year', 'zip']
```
