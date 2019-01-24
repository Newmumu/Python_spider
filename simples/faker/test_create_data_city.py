from faker import Faker

faker = Faker(locale='zh_CN')

# address
print ('Address'.center(20, '-'))
print (faker.address())
