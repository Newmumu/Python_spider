# encoding=utf-8

# 获取输入的数值
age = int(input('please enter your age:'))

if age >= 18:
	print 'adult'
elif age > 6:
	print 'teenager'
else:
	print 'kid'
