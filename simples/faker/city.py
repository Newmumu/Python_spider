# encoding=utf-8
from faker import Faker

faker = Faker(locale='zh_CN')

# # address
print ('Address'.center(20, '-'))
print (faker.address())  # 广东省梧州市门头沟银川路o座 745407
print (faker.street_address())  # 佛山街M座
print (faker.street_name())  # 合肥街
print (faker.city_name())  # 贵阳
print (faker.city())  # 海门县
print (faker.province())  # 安徽省

# company
print ('company'.center(20, '-'))

# 	print faker.company()
print (faker.company())
print (faker.company_suffix())
print (faker.company_prefix())

# 个人信息类
print("info-person".center(20, "-"))

# 东浩
print(faker.name())

# {'username': 'leihan', 'name': '武帅', 'sex': 'F', 'address': '吉林省淮安市双滦家街C座 210434', 'mail': 'lishao@hotmail.com', 'birthdate': '1988-11-12'}
print(faker.simple_profile())

print(faker.user_name())  # ajiang zI2QbHy02p
print(faker.password(special_chars=False))


# 文章类
print("artical".center(20, "-"))

print(faker.word())  # 当前

# 随机生成中文词语
print(faker.words(10))  # ['欢迎', '支持', '图片']

# 输出获取的单词
for i in range(10):
    print faker.words(10)[i],

print ''

# 随机生成一条语句
print(faker.sentence(3))  # 精华有关一些.

# 输出一条段落
# 大家电话空间一起操作图片要求.上海发展到了之间用户也是的人.必须记者关系介绍注册.用户时候投资发布.
print(faker.paragraph())