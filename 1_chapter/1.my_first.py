#变量名
message = '这是我学习python的第n次'

message = '这是我学习python的第n次,但这一次我是认真学习的'
print(message)

test_1 = '这是测试'
print(test_1)

#大小写
print('大小写-------------')
name = 'zhangzhennan'
name1 = 'ZhangZhenNan'
name2 = 'ZHANGZHENNAN'
print(name.title())         #首字母大写
print(name1.upper())        #字母大写
print(name2.lower())        #字母小写


#在字符串中使用变量
print('在字符串中使用变量-------------')
first_name = 'zhang'
last_name = 'zhennan'
full_name = f"{first_name} {last_name}"  
full_name1 = f"{first_name}{last_name}"
#full_name = f"{first_name}{last_name}"
print(full_name)

print(f"{'hello,'}{first_name.title()}{last_name}")
print(f"hello,{full_name.title()}!")
print(f"hello,{full_name1.title()}!")
message = f"hello, my name is {full_name.title()}"
print(message)


#制表符-换行符
print('制表符--------')
print('\tpython')
print('\npython')
print('换行符--------')
print('Languages:\nC\npython\njava\nC++')
print('换行符+制表符--------')
print('Languages:\n\tC\n\tpython\n\tjava\n\tC++')


#删除空白
print("删除空白----------")
bl = '这句话后面是空白      '
bl = bl.rstrip()
print(bl)
bl1 = '      这句话前面是空白'
bl1 = bl1.lstrip()
print(bl1)
bl2 = '     这句话两边是空白     '
bl2 = bl2.strip()
print(bl2)



testname = 'ZHANG ZHEN NAN'
nm = testname.lower()
print(nm)

testname1 = 'zhang zhen nan'
nm1 = testname1.upper()
print(nm1)

print('古人云:"别想那么多,do it"')

famous_person = '张镇南'
my = '是最优秀的'
print(famous_person+my)
print(famous_person,my)

mz = ' 张天飞 '
mz1 = ' 张sir'
mz2 = '张镇南 '
my_name = '我的名字是\t'
my_name1 = '你的名字是\n'
my_name2 = '他的名字是\n\t'
mz = mz.strip()
mz1 = mz1.lstrip()
mz2 = mz2.rstrip()
print(my_name+mz)
print(my_name1+mz1)
print(my_name2+mz2)
